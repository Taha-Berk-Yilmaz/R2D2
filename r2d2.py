from getpass import getpass
from pyqrcode import QRCode
from langdetect import detect 
import wikipedia
import speech_recognition as sr
import random
import pyttsx3
import os
import subprocess as sp 				#There is a error on subprocess. I Couldn't get it??
import requests
import smtplib
import time
import comic
import users 
import pytube
import pyautogui
import sys
import pyqrcode
import png
import sqlite3

paths = {
    'notepad': r"D:\Notepad++\notepad++.exe",
    'tor_browser': r'D:\Tor Browser\Start Tor Browser.lnk',
    'calculator': r"C:\Windows\System32\calc.exe",
    'vmbox': r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Oracle VM VirtualBox\Oracle VM VirtualBox.lnk",
    'CDisplayEx': r"C:\Users\HP\Desktop\CDisplayEx.lnk",
    'FL Studio': r"C:\Users\HP\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Image-Line\FL Studio 20.lnk",
    'Spotify': r"C:\Users\HP\Desktop\Spotify.lnk"
}

commands = ["open camera", "open notepad", "tell me a joke", "open cmd", "open calculater", "add user", "show users", "yt download", "clear", "get access", "vm box", "flip coin", "screenshot", "comic", "detect language", "send mail", "qr code", "commands", "exit"]

def spotify():
	print("------------------------")
	print('Starting Spotify.')
	os.startfile(paths['Spotify'])

def search_on_google():
	print("------------------------")
	print('Searching on google.')
	topic = input('Please enter the topic please: ')
	kit.search(topic)

def play_on_youtube():
	print("------------------------")
	print('Searching on youtube.')
	video = input('Please enter the vide name: ')
	kit.playonyt(video)

def search_wikipedia():
	print("------------------------")
	print('Searching on wiki.')
	topic = input('Please enter the topic here: ')
	results = wikipedia.summary(topic, sentences = 2)
	return (results)

def weather():
	print("------------------------")
	print('Finding weather results.')
	res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=Ankara&appid=a575cb6ed6bb26e10ce4f1b4fc123cd7&units=metric").json()
	weather = res["weather"][0]["main"]
	temperature = res["main"]["temp"]
	feels_like = res["main"]["feels_like"]
	return (weather, f"{temperature}℃", f"{feels_like}℃")

def my_ip():
	print("------------------------")
	print('Getting your ip address.')
	ip_address = requests.get('https://api64.ipify.org?format=json').json()
	return (ip_address["ip"])

def remove():
	print("------------------------")
	directory = input("Please enter the file path: ")
	os.system("rm " + str(directory))

def delete():
	print("------------------------")
	print('Deleteing all evidence...')
	os.system("rmdir R2D2")
	#Don't use this if it doesn't necesseary.

def make_phonk():
	print("------------------------")
	print('Opening FL Studio.')
	os.startfile(paths['FL Studio'])

def restart():
	print("------------------------")
	lowerstr = 'restarting...'
	upperstr = lowerstr.upper()
	for i in range(0,2):
		for letter in range(len(lowerstr)):
			s = '\r' + lowerstr[0:letter] + upperstr[letter] + lowerstr[letter+1:] + '\r'
			sys.stdout.writelines(s)
			sys.stdout.flush()
			qtime.sleep(0.1)
	os.system("^C")
	os.system("python r2d2.py")

def lang_detect():
	print("------------------------")
	text = input("Please enter text here: ")
	detected_lang = detect(text)
	print(detected_lang)

def send_mail():
	print("------------------------")
	conn = smtplib.SMTP('smtp.gmail.com', 587)
	conn.starttls()
	user_mail = input("Please enter you gmail: ")
	user_pass = getpass("Please enter your password: ")
	recive_mail = input("Please enter receivers gmail: ")
	msg = input("Please enter your mesage here: ")
	conn.login(user = user_mail , password = user_pass)
	conn.sendmail(from_addr = user_mail , to_adrrs = recive_mail, msg = msg)
	sonn.close()

def qr_code():
	print("------------------------")
	get_url = input("Please enter your generating link here: ")
	gen_url = pyqrcode.create(get_url)
	gen_url.svg('myqr.svg', scale = 8)
	gen_url.png('myqr.png', scale = 6)
"""
def read_comic():
	print("------------------------")
	print(*comic.comics.keys(), sep = '\n')
	comic_book = str(input("Ok " + name + " Can you tell me the name of comic: "))
	sp.run('cd ', comic.comics[comic_book], shell = True)
	sp.run('dir', shell = True)
	comic_book_2 = str(input("Please enter the chapter: "))
	os.system(paths['CDisplayEx'] + comic_book_2)
"""

def take_screenshot():
	print("------------------------")
	for sec in range(0, 5):
		sys.stdout.write("You have " + str(5 - sec) + " seconds left." + "\n")
		sys.stdout.flush()
		time.sleep(0.9)
	screenshot = pyautogui.screenshot()
	screenshot.save(r"C:\\Users\\HP\\Desktop\\Screenshots\\auto_screenshot.png")

def flip_coin():
	print("------------------------")
	head = input("Please enter your head statement: ")
	tails = input("Please enter your tails statement: ")
	print("I wish you luck " + name)
	result = random.randint(0,1)
	if result == 0:
		print("The coin says " + head)

	elif result == 1:
		print("The coin says " + tails)

def vm_box():
	print("------------------------")
	os.startfile(paths['vmbox'])
	print("VM Box opened.")

def get_random():										
	print("------------------------")
	print("You have guess the right number between 0 to 100.000.")
	first_guess = int(getpass("If you guess the number right you will get a root access and nobody will see your guess.\nIf you want to exit the guessing game try computer lang.\nThis is your first guess: "))
	if first_guess == 69420:
		users.update()
		print("You are root user now.")
	else:
		sayi = random.randint(0,100000)
		while True:
			guess = int(input("Please enter your guess here: "))
			if guess == sayi:
				print("You get that right and you get fake root access idiot.")
				break
			elif guess < sayi:
				print("Come on try higher.")
			elif guess > sayi:
				print("Try lower.")
			elif guess == 1100101111100011010011110100:
				print("You exitted.")
				break
			else:
				print("You entered invalid value.")

def yt_download():
	print("------------------------")
	link = input("Please enter video link here: ")
	yt = pytube.YouTube(link)
	print("Downloading..")
	mp4_file = yt.streams.filter(file_extension = 'mp4')
	mp4_file_resolution = mp4_file.get_by_resolution('720p')
	mp4_file_resolution.download(r'D:\DownloadedVideos')
	print("Downloaded ", link)

def add_user():											
	print("------------------------")
	print("Add a new user is risky.\nAre you sure about that/(BETA)/.")
	permission = input("")
	if permission == 'yes':
		users.add_user()
			
def open_camera():
	print("------------------------")
	sp.run('start microsoft.windows.camera:', shell=True)
	print("Camera opened.")

def open_notepad():
	print("------------------------")
	os.startfile(paths['notepad'])
	print("Notepad++ opened.")
    
def open_cmd():
	print("------------------------")
	os.system('start cmd')
	print("Another cmd window opened.")

def open_calculator():
	print("------------------------")
	sp.Popen(paths['calculator'])
	print("Calculator opened.")

def get_random_joke():
	print("------------------------")
	headers = {
		'Accept': 'application/json'
	}
	res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
	return res["joke"]

if users.info() == True:

	say_my_name = ["sir.", "Mr. Berk.", "My Lord."]
	name = random.choice(say_my_name)
	lowerstr = 'initializing...'
	upperstr = lowerstr.upper()

	try:
		sp.run('cls', shell = True)
		
		for i in range(0,2):
			for letter in range(len(lowerstr)):
				s = '\r' + lowerstr[0:letter] + upperstr[letter] + lowerstr[letter+1:] + '\r'
				sys.stdout.writelines(s)
				sys.stdout.flush()
				time.sleep(0.1)

		dosya = open('commands.txt', 'r+')
		sys.stdout.write("\n")
		listener = sr.Recognizer()
		engine = pyttsx3.init('dummy')
		voices = engine.getProperty('voices')
		engine.setProperty('voices', voices[0].id)
		with sr.Microphone() as source:
			text = input("text or speech: ")

			if 'speech mod please' in text:
				print("How can I help you")
				engine.say("How can I help you")
				engine.runAndWait()
				voice = listener.listen(source)
				command = listener.recognize_google(voice)
				new_command = command.upper()
				print(new_command)

				if 'BD1 ARE YOU ONLINE' in  new_command:
					print("Yes " + name + " I'm ready for your orders.")

					while True:
						with sr.Microphone() as source:
							voice = listener.listen(source)
							command = listener.recognize_google(voice)
							new_command = command.upper()
							print(new_command)

							if 'OPEN CAMERA' in new_command:
								open_camera()

							if 'OPEN NOTEPAD' in new_command:
								open_notepad()

							if 'TELL ME A JOKE' in new_command:
								joke = get_random_joke()
								print(joke)
								engine.say(joke)
								engine.runAndWait()

							if 'OPEN CMD' in new_command:
								open_cmd()

							if 'OPEN CALCULATOR' in new_command:
								open_calculator()	

							if 'ADD USER' in new_command:
								if login_u == 'Alkanoid' and login_p == users.list_0f_users['Alkanoid']:
									add_user()

							if 'SHOW USERS' in new_command:
								print(users.list_0f_users)

							if 'YT DOWNLOAD' in new_command:
								yt_download()

							if 'CLEAR' in new_command:
								sp.run('cls', shell = True)

							if 'GET ACCESS' in new_command:
								get_random()

							if 'VM BOX' in new_command:
								vm_box()

							if 'FLIP COIN' in new_command:
								flip_coin()

							if 'SCREENSHOT' in new_command:
								take_screenshot()
							
							#if 'COMIC' in new_command:
								#read_comic()
							
							if 'DETECT LANGUAGE' in new_command:
								lang_detect()

							if 'SEND MAIL' in new_command:
								send_mail()

							if 'QR CODE' in new_command:
								qr_code()

							if 'COMMANDS' in new_command:
								dosya = open('commands.txt', 'r+')
								print(dosya.readlines())

							if 'RESTART' in new_command:
								restart()

							if 'EXIT' in new_command:
								print("My power system is closing " + name + "\n")
								break

							elif new_command not in dosya.readlines():
								print("It's an invalid command " + name + " Or I was just glitching.")

			elif 'text mod please' in text:

				while True:
					print("------------------------")
					new_command = input("For your orders " + name + ".\\ \n")

					if 'open camera' in new_command:
						open_camera()

					if 'open notepad' in new_command:
						open_notepad()

					if 'tell me a joke' in new_command:
						joke = get_random_joke()
						print(joke)
							
					if 'open cmd' in new_command:
						open_cmd()

					if 'open calculator' in new_command:
						open_calculator()

					if 'add user' in new_command:
						add_user()

					if 'show users' in new_command:
						print(users.list_0f_users)

					if 'yt download' in new_command:
						yt_download()

					if 'clear' in new_command:
						sp.run('cls', shell = True)

					if 'get access' in new_command:
						get_random()

					if 'vm box' in new_command:
						vm_box()

					if 'flip coin' in new_command:
						flip_coin()

					if 'screenshot' in new_command:
						take_screenshot()

					#if 'comic' in new_command:
						#read_comic()

					if 'detect language' in new_command:
						lang_detect()

					if 'send mail' in new_command:
						send_mail()

					if 'qr code' in new_command:
						qr_code()

					if 'commands' in new_command:
						print(dosya.readlines(), sep = '\n')

					if 'restart' in new_command:
						restart()

					if 'exit' in new_command:
						print("My power system is closing " + name + "\n")
						break

					elif new_command not in commands:
						print("It's an invalid command " + name + " Or I was just glitching.")

	except KeyboardInterrupt:
		print("\nMy power system is closing " + name + "\n")

else:
	print("You entered wrong identity.")




