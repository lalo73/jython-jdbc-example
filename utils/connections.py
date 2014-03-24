import java.lang.Class
from java.sql import DriverManager
from utils.importer import importJar
import os


class ConnectionFactory(object):
    CONNECTORS = {
        'my-sql': {
            'jar-file': 'mysql-connector-java-5.1.29-bin.jar',
            'driver': "com.mysql.jdbc.Driver",
            'url': "jdbc:mysql://localhost/",
        },
        'postgresql': {
            'jar-file': 'postgresql-9.3-1101.jdbc41.jar',
            'driver': "org.postgresql.Driver",
            'url': "jdbc:postgresql://localhost/",
        },
    }

    @classmethod
    def get_mysql_connection(cls, database, user, password):
        return cls.get_connection('my-sql', database, user, password)

    @classmethod
    def get_postgresql_connection(cls, database, user, password):
        return cls.get_connection('postgresql', database, user, password)

    @classmethod
    def get_connection(cls, database_engine, database, user, password):
        options = cls.CONNECTORS[database_engine]
        importJar(cls.get_jar_path(options['jar-file']))
        java.lang.Class.forName(options['driver'])
        url = options['url']
        return DriverManager.getConnection("%s%s?user=%s&password=%s" % (url, database, user, password))

    @classmethod
    def get_jar_path(cls, path):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)


__author__ = 'lalo'
