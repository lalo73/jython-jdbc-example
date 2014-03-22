import java.lang.Class
from java.sql import DriverManager
from utils.importer import importJar
import os


class ConnectionFactory(object):
    PATH_TO_MYSQL_JAR = 'mysql-connector-java-5.1.29-bin.jar'

    @classmethod
    def get_mysql_connection(cls, database, user, password):

        importJar(cls.get_jar_path(cls.PATH_TO_MYSQL_JAR))
        java.lang.Class.forName("com.mysql.jdbc.Driver")
        url = "jdbc:mysql://localhost/"
        return DriverManager.getConnection("%s%s?user=%s&password=%s" % (url, database, user, password))

    @classmethod
    def get_jar_path(cls, path):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)


__author__ = 'lalo'
