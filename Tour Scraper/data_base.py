import sqlite3

db = sqlite3.connect('database.db')


def store(extracted):
    """ Store the new tour into the date base """
    row = extracted.split(',')
    band, city, date = [col.strip() for col in row]
    cur = db.cursor()
    cur.execute(f'INSERT INTO events VALUES(?,?,?)', (band, city, date))
    db.commit()


def read(extracted):
    """ Read the tour row from the date base """
    row = extracted.split(',')
    band, city, date = [col.strip() for col in row]
    cur = db.cursor()
    cur.execute(f'SELECT * FROM events WHERE band=? AND city=? AND date=?', (band, city, date))
    return cur.fetchall()
