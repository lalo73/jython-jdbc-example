from __future__ import with_statement
import unittest
from utils.connections import ConnectionFactory


class ConnectionTest(unittest.TestCase):

    def setUp(self):
        self.connection = None
        self.prepared_statement = None

    def test_insert(self):

        try:
            self.connection = connection = self.get_connection()
            sql_query= "INSERT INTO Aerolinea (NOMBRE, CODIGO) VALUES (?,?)"
            self.prepared_statement = prepared_statement = connection.prepareStatement(sql_query)
            prepared_statement.setString(1, "UnaAerolinea")
            prepared_statement.setString(2, "UNA")
            prepared_statement.execute()
            self.assertEqual(1, prepared_statement.getUpdateCount(), "It should insert one registry")
        finally:
            if self.prepared_statement:
                self.prepared_statement.close()
            if self.connection:
                self.connection.close()

    def test_select(self):
        try:
            self.connection = connection = self.get_connection()
            sql_query = "SELECT ID,NOMBRE,CODIGO FROM Aerolinea WHERE CODIGO = ?"
            self.prepared_statement = prepared_statement = connection.prepareStatement(sql_query)
            prepared_statement.setString(1, "UNA")
            result_set = prepared_statement.executeQuery()

            while result_set.next():
                id = result_set.getInt("ID")
                nombre = result_set.getString("NOMBRE")
                codigo = result_set.getString("CODIGO")
                print "ID: %i nombre: %s  codigo: %s" % (id, nombre, codigo)

        finally:
            if self.prepared_statement:
                self.prepared_statement.close()
            if self.connection:
                self.connection.close()

    def get_connection(self):
        database, user, password = "Epers_Ej1", "root", "root"
        return ConnectionFactory.get_mysql_connection(database, user, password)

if __name__ == '__main__':
    unittest.main()


__author__ = 'lalo'
