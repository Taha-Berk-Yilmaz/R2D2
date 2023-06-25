import sqlite3
from getpass import getpass


#con = sqlite3.connect("user.db")
#cursor = con.cursor()
#cursor.execute("""CREATE TABLE users (username TEXT,passwd TEXT, privilage TEXT)""")
#cursor.execute("INSERT INTO users VALUES ('Alkanoid', 'Zümrüt', 'root')")
#con.commit()
#con.close()

"""
passwdd = 'Alkanoid' 
con = sqlite3.connect("user.db")
cursor = con.cursor()
cursor.execute("SELECT * FROM users WHERE username = " + "'{passwdd}'".format(passwdd = passwdd)) 
print(*cursor.fetchone(), sep = ' | ')
con.commit()
con.close()
"""

def update():
	try:
		con = splite3.connect("user.db")
		cursor = con.cursor()
		name = input('Please enter your username: ')
		cursor.execute("""UPDATE users SET privilage = 'root' WHERE  username = '{name}'""".format(name = name))

	except sqlite3.Error as error:
		print('An error appeard while updating the sqlite3 table => ' + str(error))
		
	finally:
		con.commit()
		con.close()

def add_user():
	con = sqlite3.connect("user.db")
	cursor = con.cursor()
	root_username = input("Please enter your username: ")
	root_passwd = str(input("Please enter your password: ")) 
	cursor.execute("SELECT * FROM users WHERE username = " + "'{user_name}'".format(user_name = root_username))
	string = (cursor.fetchone())
	print(string[0] + string[1] + string[2])
	"""
	username_string = str(string.split(',', 2)[0]) #('username'
	passwd_string = str(string.split(',', 2)[1]) #'passwd'
	priv_string = str(string.split(',', 2)[2]) # 'priv')
	"""
	if root_username == string[0] and root_passwd == string[1] and 'root' == string[2]:
		username = input("New users username: ")
		passwd = getpass("New users password: ")
		priv = input("New users privilage: ")
		cursor.execute("INSERT INTO users VALUES ("'{username}'", "'{paswd}'", "'{priv}'")".format(username = username, paswd = passwd, priv = priv))
	elif string[2] == 'user':
		print("Sorry you don't have permission to add a user.")

	con.commit()
	con.close()

def info():
	try:
		username_input = input("Please enter the username: ")
		passwd_input = str(getpass("Please enter the password: "))
		con = sqlite3.connect("user.db")
		cursor = con.cursor()
		cursor.execute("SELECT * FROM users WHERE username = " + "'{user_name}'".format(user_name = username_input))
		string = (cursor.fetchone())

		if username_input == string[0] and passwd_input == string[1]:
			returning = True
		else:
			returning = False

		return (returning)

		#print(username_string.split('(', 1)[1])
		#print(passwd_string.split(')', 1)[0])


		con.commit()
		con.close()

	except KeyboardInterrupt:
		print("See you another time sir.")


"""
con = sqlite3.connect("user.db")
cursor = con.cursor()
name = input("enter")
cursor.execute("SELECT * FROM users WHERE username = " + "'{user_name}'".format(user_name = name))

string = (cursor.fetchone())
print(string[0])



if name == string[0]:
	print("hello")
"""
"""
username_string = str(string.split(',', 2)[0]) #('username'
passwd_string = str(string.split(',', 2)[1]) #'passwd'
priv_string = str(string.split(',', 2)[2]) # 'priv')

print(username_string + passwd_string + priv_string)

"""

"""
print(info('Alkanoid'))
if 'Alkanoid' in info('Alkanoid'): #and info('Alkanoid').rsplit(' | ', 1)[0]:
	print('yes')
"""