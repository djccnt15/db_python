from src import *

if __name__ == '__main__':
    db = get_db('sample.json')
    q = get_query('sample.sql')

    res = db_read(q, db.host, db.port, db.user, db.pw, db.db)
    print(res)