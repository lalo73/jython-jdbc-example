def importJar(jarFile):
    '''
    import a jar at runtime (needed for JDBC [Class.forName])

    adapted from http://forum.java.sun.com/thread.jspa?threadID=300557
    Author: SG Langer Jan 2007 translated the above Java to Jython
    Author: seansummers@gmail.com simplified and updated for jython-2.5.3b3

    >>> importJar('mysql-connector-java-5.1.29-bin.jar')
    >>> import java.lang.Class
    >>> java.lang.Class.forName('com.mysql.jdbc.Driver')
    <type 'com.mysql.jdbc.Driver'>
    '''
    from java.net import URL, URLClassLoader
    from java.lang import ClassLoader
    from java.io import File
    m = URLClassLoader.getDeclaredMethod("addURL", [URL])
    m.accessible = 1
    m.invoke(ClassLoader.getSystemClassLoader(), [File(jarFile).toURL()])

if __name__ == '__main__':
    import doctest
    doctest.testmod()

__author__ = 'lalo'
