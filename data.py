import pickle

phones = {'АПАНАСОВ': 7727, 'КОЛЕСНИК': 7058, 'ГУЧКО': 7010, 'МАРКЕВИЧ': 7421,
          'ДОВНАР': 7087, 'КАЗМЕРЧУК_П': 7191, 'ГРИНКЕВИЧ': 7162, 'НОВИКОВА': 7191,
          'ОРЛОВ': 7994, 'КУЗЬМИЧ': 7701, 'ИВАНЫШКИНА': 7121, 'КАЗМЕРЧУК_Д': 7045,
          'КОВАЛЕВСКАЯ': 7168, 'КРИУЛИН': 7237}


def pack_phones():
    dbfile = open('phones.dat', 'wb')
    pickle.dump(phones, dbfile)
    dbfile.close()


pack_phones()
