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

	# detect non-unique usernames
	usr_list = []
	for user in c.execute("SELECT * FROM Utilisateurs"):
		if user['username'] in usr_list:
			return 1
		usr_list.append(user['username'])

	# detect usernames shorter than 3 chars
	for username in usr_list:
		if len(username) < 3:
			return 1

	# detect usernames containing special caracters
	for username in usr_list:
		if any(not c.isalnum() for c in username): #stackoverflow
			return 1

	# detect passwords shorter than 8 chars
	for user in c.execute("SELECT * FROM Utilisateurs"):
		if len(user['password']) < 8:
			return 1

	# verify passwords
	for user in c.execute("SELECT * FROM Utilisateurs"):
		
		uppercase_not_found = 1
		lowercase_not_found = 1
		special_not_found = 1
		number_not_found = 1

		for char in user['password']:
			if char.isupper() :
				uppercase_not_found = 0
			if char.islower() :
				lowercase_not_found = 0
			if not char.isalnum() :
				special_not_found = 0
			if char.isnumeric() :
				number_not_found = 0
		
		if uppercase_not_found or lowercase_not_found or special_not_found or number_not_found:
			return 1

    # verify that keys are exactly 128 char long
	for user in c.execute("SELECT * FROM Utilisateurs"):
		if len(user['spublickey']) != 128 or len(user['sprivatekey']) != 128 or len(user['epublickey']) != 128 or len(user['eprivatekey']) != 128 :
			return 1

	return 0
