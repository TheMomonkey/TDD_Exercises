import sqlite3

conn = sqlite3.connect('db_test.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

def add(username, password, spub, spriv, epub, epriv):
	c.execute("INSERT INTO Utilisateurs (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES('" + username + "', '" + password + "', '" + spub + "', '" + spriv + "', '" + epub + "', '" + epriv + "')")
	conn.commit()

def login(username, password, spub, spriv, epub, epriv):
	return

def getkey(username, password, spub, spriv, epub, epriv):
	return

def check(username, password, spub, spriv, epub, epriv):
	return
