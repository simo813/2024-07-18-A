from database.DB_connect import DBConnect
from model.gene import Gene
from model.interaction import Interaction


class DAO():

    @staticmethod
    def get_all_genes():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                    FROM genes"""
            cursor.execute(query)

            for row in cursor:
                result.append(Gene(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_interactions():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                       FROM interactions"""
            cursor.execute(query)

            for row in cursor:
                result.append(Interaction(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_chromosoma():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct (g.Chromosome) as chromosome
                        from genes_small.genes g """
            cursor.execute(query)

            for row in cursor:
                result.append(row["chromosome"])

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getNodes(minChromosome, maxChromosome):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct (g.GeneID), g.`Function` , g.Essential , g.Chromosome 
                        from genes_small.genes g 
                        where g.Chromosome >= %s and g.Chromosome <= %s """
            cursor.execute(query, (minChromosome, maxChromosome))

            for row in cursor:
                result.append(Gene(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getEdges(minChromosome, maxChromosome):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("""
                                select g.GeneID as g1, g.Function as f1, g2.GeneID as g2, g2.Function as f2, i.Expression_Corr as w
                                from genes_small.interactions i, genes_small.genes g, genes_small.classification c, genes_small.genes g2, genes_small.classification c2
                                where       g.Chromosome >= %(minChromosome)s and g.Chromosome <= %(maxChromosome)s
                                        and g2.Chromosome >= %(minChromosome)s and g2.Chromosome <= %(maxChromosome)s
                                        and c.GeneID = g.GeneID
                                        and c2.GeneID = g2.GeneID
                                        and c.Localization = c2.Localization
                                        and i.GeneID1 = g.GeneID
                                        and i.GeneID2 = g2.GeneID
                                        and i.GeneID1 <> i.GeneID2
                            
                                group by g.GeneID, g.Function, g2.GeneID, g2.Function, i.Expression_Corr
                            """,
                           {'minChromosome': minChromosome, 'maxChromosome': maxChromosome})  # Pass params as dict
            for row in cursor:
                result.append((row["g1"], row["f1"], row["g2"], row["f2"], row["w"]))

            cursor.close()
            cnx.close()
        return result