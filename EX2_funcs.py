import sqlite3

conn = sqlite3.connect('db_test.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

def add(username, password, spub, spriv, epub, epriv):
	c.execute("INSERT INTO Utilisateurs (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES('" + username + "', '" + password + "', '" + spub + "', '" + spriv + "', '" + epub + "', '" + epriv + "')")
	conn.commit()

def login(username, password):

	c.execute("SELECT * FROM Utilisateurs WHERE username='" + username + "'")
	user = c.fetchone()

	if user:
		return user['password'] == password
	
	return False

def get_spub_key  (username):

	c.execute("SELECT * FROM Utilisateurs WHERE username='" + username + "'")
	user = c.fetchone()

	if user:
		return user['spublickey']
	#print("Utilisateur " + username + " non trouvé")

def get_spriv_key (username):

	c.execute("SELECT * FROM Utilisateurs WHERE username='" + username + "'")
	user = c.fetchone()

	if user:
		return user['sprivatekey']
	#print("Utilisateur " + username + " non trouvé")

def get_epub_key  (username):

	c.execute("SELECT * FROM Utilisateurs WHERE username='" + username + "'")
	user = c.fetchone()

	if user:
		return user['epublickey']
	#print("Utilisateur " + username + " non trouvé")

def get_epriv_key (username):

	c.execute("SELECT * FROM Utilisateurs WHERE username='" + username + "'")
	user = c.fetchone()

	if user:
		return user['eprivatekey']
	#print("Utilisateur " + username + " non trouvé")

def check():
	return
