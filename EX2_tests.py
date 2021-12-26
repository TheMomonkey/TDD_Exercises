import sqlite3, random, string
import EX2_funcs
import unittest

conn = sqlite3.connect('db_test.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

def gen_random_str(size):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))

c.execute('DROP TABLE IF EXISTS Utilisateurs')
c.execute('CREATE TABLE Utilisateurs (username VARCHAR(128), password VARCHAR(128), spublickey CHAR(128), sprivatekey CHAR(128), epublickey CHAR(128), eprivatekey CHAR(128))')

class EX2FuncsTestCase(unittest.TestCase):
    
    def test_add(self):
        
        usernames = ['jean32', 'pierre46', 'jacques55', 'thomas15', 'philippe12']
        passwords = ['ef655f', 'e1f24ef2', 'wf846s5s3', '2dwv68v6', '5vs61r8ev6']
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

#    def test_login(self):
#        self.assertEqual(_, _)

#    def test_getkey(self):
#        self.assertEqual(_, _)

#    def test_check(self):
#        self.assertEqual(_, _)

if __name__ == '__main__':
    unittest.main()