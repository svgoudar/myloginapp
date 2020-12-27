# mysql://b44f47c62c8d3e:f0c81fd0@us-cdbr-east-02.cleardb.com/heroku_0728eba485451c8?reconnect=true

from flask_mysqldb import MySQL
mysql = MySQL()
# MySQL configurations
from mysql.connector import connection,cursor


def DB_CONF():
    # ssl = {'cert': 'ssl/b44f47c62c8d3e-cert.pem', 'key': 'b44f47c62c8d3e-key.pem'}
    cnx = connection.MySQLConnection(user='b44f47c62c8d3e', password='f0c81fd0',
                                     host='us-cdbr-east-02.cleardb.com',
                                     database='heroku_0728eba485451c8',
                                     ssl_ca=r'ssl/cleardb-ca.pem',
                                     ssl_cert='ssl/b44f47c62c8d3e-cert.pem',
                                     ssl_key='ssl/b44f47c62c8d3e-key.pem')

    # create_db = '''CREATE DATABASE IF NOT EXISTS `ACCOUNT_DB` DEFAULT CHARACTER SET UTF8MB4 COLLATE UTF8MB4_general_ci;'''
    # use_db = '''USE `ACCOUNT_DB`;'''
    create_table = '''CREATE TABLE IF NOT EXISTS `ACCOUNTS` (
                            `USER_ID` int(11) NOT NULL AUTO_INCREMENT,
                            `USERNAME` varchar(50) NOT NULL,
                            `PASSWORD`varchar(255),
                            `EMAIL` varchar(100) NOT NULL unique,
                             PRIMARY KEY (`USER_ID`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=UTF8MB4;
    '''
    # sample_insert = '''INSERT INTO ACCOUNTS(USERNAME,PASSWORD,EMAIL) VALUES ( 'sanjeev', 'sanju123', 'sanju123@gmail.com'); '''
    cur = cnx.cursor()
    # cur.execute(create_db)
    # cur.execute(use_db)
    cur.execute(create_table)
    # cur.execute(sample_insert)
    cur.close()
    cnx.close()
    return "DB CONFIGURED SUCCESSFULLY"

