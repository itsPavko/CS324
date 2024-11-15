import sqlite3
from sqlite3 import Error
import pandas as pd
from datetime import datetime

def create_connection(db_file):
    """ create a database connection to the specified SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_book(conn, book):
    """
    Create a new book into the knjige table
    :param conn:
    :param book:
    :return: book id
    """
    sql = ''' INSERT INTO knjige(katBroj,naslov,izdavac,godinaIzdavanja,izdata)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()
    return cur.lastrowid

def podesiIzdat(conn, katBroj):
    """
    Update status of a book to issued
    :param conn:
    :param katBroj:
    :return: project id
    """
    sql = ''' UPDATE knjige
              SET izdata = True
              WHERE katBroj = ?'''
    cur = conn.cursor()
    cur.execute(sql, (katBroj,))
    conn.commit()

def main():
    database = r"biblioteka.db"

    sql_create_knjige_table = """ CREATE TABLE IF NOT EXISTS knjige (
                                        katBroj integer PRIMARY KEY,
                                        naslov text NOT NULL,
                                        izdavac text,
                                        godinaIzdavanja integer,
                                        izdata boolean NOT NULL DEFAULT False
                                    ); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_knjige_table)
        
        book = (1234, 'Book Title', 'Publisher', 2020, False);
        insert_book(conn, book)
        
        podesiIzdat(conn, 1234)
        
        df = pd.read_sql_query("SELECT * FROM knjige", conn)
        print(df)
        
        savremene_knjige = df[df['godinaIzdavanja'] >= 2000]
        izdate_knjige = df[df['izdata'] == True]
        izdate_knjige.to_csv('izdate_knjige.csv', columns=['naslov', 'izdavac', 'godinaIzdavanja'], index=False)
        
        conn.close()

if __name__ == '__main__':
    main()