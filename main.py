from src import *

if __name__ == '__main__':
    db = get_db('sample.json')
    q = get_query('sample.sql')

    res = read(db, q)
    print(res)