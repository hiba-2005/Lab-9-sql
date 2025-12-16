import mysql.connector
from mysql.connector import pooling

pool = pooling.MySQLConnectionPool(
    pool_name="app_pool",
    pool_size=5,
    host="localhost",
    user="root",
    password="VotreMdp",
    database="universite",
    autocommit=False
)

def get_conn():
    return pool.get_connection()
