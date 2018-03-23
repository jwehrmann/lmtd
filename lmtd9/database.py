from __future__ import print_function
import numpy as np
import sqlite3
import os



def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def select(query, ):
    abspath = os.path.dirname(os.path.abspath(__file__))
    dbpath = os.path.join(abspath, 'data', 'database.db')
    # print(dbpath)
    con = sqlite3.connect(dbpath)
    con.row_factory = dict_factory    
    con.text_factory = str

    cur = con.cursor()
    if len(query) == 2:
        a = cur.execute(query[0], [query[1]])
    else:
        a = cur.execute(query)
    r = cur.fetchall()

    return r


def get_split(split='train'):

    splits = ['train', 'valid', 'test']
    split_id = splits.index(split)
    
    rs = select('select * from lmtd9_0 where "set" = {}'.format(split_id))
    
    genres = [x for x in sorted(rs[0].keys()) if x.startswith('is')]

    ids = []
    labels = []

    for row in rs:
        ids.append('{:06d}'.format(row['id']))
        labels.append([row[x] for x in genres])

    return np.asarray(ids), np.asarray(labels), np.asarray(genres)


def get_data_by_trailer_ids(trailer_ids):

    trailer_ids = ', '.join([str(int(x)) for x in trailer_ids])

    
    rs = select('select trailers.id, trailers.path, movies.* ' +\
                'from lmtd9_0 ' +\
                'join trailers using(id)' +\
                'join movies using(imdbID)' +\
                'where id in ({})'.format(trailer_ids))

    result_dict = {}
    for row in rs:
        strkey = '{:06d}'.format(row['id'])
        result_dict[strkey] = row        

    return result_dict

