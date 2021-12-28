import sqlite3, random, string
import EX2_funcs
import unittest


conn = sqlite3.connect('db_test.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

#python3
def gen_random_str(size):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))

c.execute('DROP TABLE IF EXISTS Utilisateurs')
c.execute('CREATE TABLE Utilisateurs (username VARCHAR(128), password VARCHAR(128), spublickey CHAR(128), sprivatekey CHAR(128), epublickey CHAR(128), eprivatekey CHAR(128))')

class EX2FuncsTestCase(unittest.TestCase):
    
    def test_add(self):
        
        usernames = ['jean32',   'pierre46', 'jacques55', 'thomas15', 'philippe12']
        passwords = ['Ef655fl$', 'e1&24eF2', 'wF846S5_3', '&dWv68V6', '5Bs61r8ev#']
        spub      = []
        spriv     = []
        epub      = []
        epriv     = []
        
        for i in range(len(usernames)):
            spub.append(gen_random_str(128))
            spriv.append(gen_random_str(128))
            epub.append(gen_random_str(128))
            epriv.append(gen_random_str(128))

            EX2_funcs.add(usernames[i], passwords[i], spub[i], spriv[i], epub[i], epriv[i])


        i = 0
        for user in c.execute('SELECT * FROM Utilisateurs'):
            self.assertEqual(user['username'], usernames[i])
            self.assertEqual(user['password'], passwords[i])
            self.assertEqual(user['sprivatekey'], spriv[i])
            self.assertEqual(user['eprivatekey'], epriv[i])
            self.assertEqual(user['spublickey'], spub[i])
            self.assertEqual(user['epublickey'], epub[i])
            i+=1

    def test_login(self):
        self.assertEqual(EX2_funcs.login('jean32', 'Ef655fl$'), True)
        self.assertEqual(EX2_funcs.login('pierre46', 'e1&24eF2'), True)
        self.assertEqual(EX2_funcs.login('jacques55', 'wF846S5_3'), True)
        self.assertEqual(EX2_funcs.login('thomas15', '&dWv68V6'), True)
        self.assertEqual(EX2_funcs.login('philippe12', '5Bs61r8ev#'), True)
        self.assertEqual(EX2_funcs.login('philippe12', 'bonjour'), False)
        self.assertEqual(EX2_funcs.login('jean33', 'Ef655fl$'), False)
        self.assertEqual(EX2_funcs.login('marc64', 'lrkjgm'), False)

    def test_get_spub_key(self):
        for user in c.execute('SELECT * FROM Utilisateurs'):
            self.assertEqual(EX2_funcs.get_spub_key(user['username']), user['spublickey'])
        self.assertEqual(EX2_funcs.get_spub_key(user['username']), user['spublickey'])



    def test_get_epub_key(self):
        for user in c.execute('SELECT * FROM Utilisateurs'):
            self.assertEqual(EX2_funcs.get_epub_key(user['username']), user['epublickey'])
        self.assertEqual(EX2_funcs.get_epub_key("non_existing_user"), None)



    def test_get_spriv_key(self):
        for user in c.execute('SELECT * FROM Utilisateurs'):
            self.assertEqual(EX2_funcs.get_spriv_key(user['username']), user['sprivatekey'])
        self.assertEqual(EX2_funcs.get_spriv_key("non_existing_user"), None)



    def test_get_epriv_key(self):
        for user in c.execute('SELECT * FROM Utilisateurs'):
            self.assertEqual(EX2_funcs.get_epriv_key(user['username']), user['eprivatekey'])
        self.assertEqual(EX2_funcs.get_epriv_key("non_existing_user"), None)


    def test_check(self):
        self.assertEqual(EX2_funcs.check(), 0) # 0 => aucun probleme

        # Rule : username has to be unique
        c.execute("INSERT INTO Utilisateurs (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES('" + 'jean32' + "', '" + 'password_test1' + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "')")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 1) # 1 => probleme
        c.execute("DELETE FROM Utilisateurs WHERE password='password_test1'")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 0)

        # Rule : username has to be at least 3 char long
        c.execute("INSERT INTO Utilisateurs (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES('" + 'ab' + "', '" + 'Ef655fl$' + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "')")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 1)
        c.execute("DELETE FROM Utilisateurs WHERE username='ab'")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 0)

        # Rule : username cant have special caracters
        c.execute("INSERT INTO Utilisateurs (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES('" + 'op&b' + "', '" + 'Ef655fl$' + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "')")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 1)
        c.execute("DELETE FROM Utilisateurs WHERE username='op&b'")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 0)

        # Rule : password has to be at least 8 char long
        c.execute("INSERT INTO Utilisateurs (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES('" + 'passwordtestcase' + "', '" + 'Ef6$' + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "')")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 1)
        c.execute("DELETE FROM Utilisateurs WHERE username='passwordtestcase'")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 0)

        # Rule : password must contain at least one uppercase letter
        c.execute("INSERT INTO Utilisateurs (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES('" + 'passwordtestcase' + "', '" + 'ab#$%/mn54b' + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "')")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 1)
        c.execute("DELETE FROM Utilisateurs WHERE username='passwordtestcase'")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 0)

        # Rule : password must contain at least one special caracter
        c.execute("INSERT INTO Utilisateurs (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES('" + 'passwordtestcase' + "', '" + 'AbCdEf123' + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "')")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 1)
        c.execute("DELETE FROM Utilisateurs WHERE username='passwordtestcase'")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 0)

        # Rule : password must contain at least one number
        c.execute("INSERT INTO Utilisateurs (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES('" + 'passwordtestcase' + "', '" + 'aaBB$%$&mnb' + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "')")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 1)
        c.execute("DELETE FROM Utilisateurs WHERE username='passwordtestcase'")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 0)

        # Rule : password must contain at least one lowercase letter
        c.execute("INSERT INTO Utilisateurs (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES('" + 'passwordtestcase' + "', '" + 'GFH/&(1684JJ' + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "')")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 1)
        c.execute("DELETE FROM Utilisateurs WHERE username='passwordtestcase'")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 0)

        # Rule : spublickey be exactly 128 char long
        c.execute("INSERT INTO Utilisateurs (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES('" + 'passwordtestcase' + "', '" + 'GFH/&(1684jj' + "', '" + gen_random_str(12) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "')")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 1)
        c.execute("DELETE FROM Utilisateurs WHERE username='passwordtestcase'")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 0)

        # Rule : sprivatekey be exactly 128 char long
        c.execute("INSERT INTO Utilisateurs (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES('" + 'passwordtestcase' + "', '" + 'GFH/&(1684jj' + "', '" + gen_random_str(128) + "', '" + gen_random_str(150) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "')")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 1)
        c.execute("DELETE FROM Utilisateurs WHERE username='passwordtestcase'")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 0)

        # Rule : epublickey be exactly 128 char long
        c.execute("INSERT INTO Utilisateurs (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES('" + 'passwordtestcase' + "', '" + 'GFH/&(1684jj' + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(12) + "', '" + gen_random_str(128) + "')")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 1)
        c.execute("DELETE FROM Utilisateurs WHERE username='passwordtestcase'")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 0)

        # Rule : eprivatekey be exactly 128 char long
        c.execute("INSERT INTO Utilisateurs (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES('" + 'passwordtestcase' + "', '" + 'GFH/&(1684jj' + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(128) + "', '" + gen_random_str(150) + "')")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 1)
        c.execute("DELETE FROM Utilisateurs WHERE username='passwordtestcase'")
        conn.commit()
        self.assertEqual(EX2_funcs.check(), 0)





if __name__ == '__main__':
    unittest.main()