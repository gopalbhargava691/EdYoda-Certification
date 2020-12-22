import json
import random
import getpass

user = []

def play():
	print("\n~MCQ Quiz~")
	score = 0
	with open("data/questions.json", 'r+') as f:
		j = json.load(f)
		for i in range(5):
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1} {j[ch]["question"]}\n')
			for option in j[ch]["options"]:
				print(option)
			answer = input("\nEnter your answer: ")
			if j[ch]["answer"][0] == answer[0].upper():
				print("\nYou are correct")
				score+=1
			else:
				print("\nYou are incorrect")
			del j[ch]
		print(f'\nFINAL SCORE: {score}')

def quizQuestions():
	if len(user) == 0:
		print("You must first login before adding questions.")
	elif len(user) == 2:
		if user[1] == "ADMIN":
			print('\n~ADD MCQ's~\n')
			ques = input("Enter the question that you want to add:\n")
			opt = []
			print("Enter the 4 options with character initials (1, 2, 3, 4)")
			for _ in range(4):
				opt.append(input())
			ans = input("Enter the answer:\n")
			with open("data/questions.json", 'r+') as f:
				questions = json.load(f)
				dic = {"question": ques, "options": opt, "answer": ans}
				questions.append(dic)
				f.seek(0)
				json.dump(questions, f)
				f.truncate()
				print("Question successfully added.")		
		else:
			print("You don't have access to add questions.")


def createAccount():
	print("\n~CREATE ACCOUNT~")
	username = input("Please Enter USERNAME: ")
	password = getpass.getpass(prompt= 'Please Enter PASSWORD: ')
	with open('data/user_accounts.json', 'r+') as user_accounts:
		users = json.load(user_accounts)
		if username in users.keys():
			print("An account of this Username already exists.\nPlease enter the login panel.")
		else:
			users[username] = [password, "PLAYER"]
			user_accounts.seek(0)
			json.dump(users, user_accounts)
			user_accounts.truncate()
			print("Account created successfully!")

def loginAccount():
	print('\n~LOGIN PANEL~')
	username = input("USERNAME: ")
	password = getpass.getpass(prompt= 'PASSWORD: ')
	with open('data/user_accounts.json', 'r') as user_accounts:
		users = json.load(user_accounts)
	if username not in users.keys():
		print("An account of that name doesn't exist.\nPlease create an account first.")
	elif username in users.keys():
		if users[username][0] != password:
			print("Your password is incorrect.\nPlease enter the correct password and try again.")
		elif users[username][0] == password:
			print("You have successfully logged in.\n")
			user.append(username)
			user.append(users[username][1])

def logout():
	global user
	if len(user) == 0:
		print("You are already logged out.")
	else:
		user = []
		print("You have been logged out successfully.")

def rules():
	print('''\n~RULES~
1. MCQ's have 4 options
2. Each MCQ consists of 1 point. 
3. You can create an account from ACCOUNT CREATION panel.
	''')


if __name__ == "__main__":
	choice = 1
	while choice != 7:
		print('\n~Quiz is live Now~')
		print('-----------------------------------------')
		print('1. START QUIZ')
		print('2. ADD MCQ's')
		print('3. ACCOUNT CREATION')
		print('4. LOGIN')
		print('5. LOGOUT')
		print('6. BASIC INFO')
		print('7. EXIT')
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			play()
		elif choice == 2:
			quizQuestions()
		elif choice == 3:
			createAccount()
		elif choice == 4:
			loginAccount()
		elif choice == 5:
			logout()
		elif choice == 6:
			rules()
		elif choice == 7:
			break
		elif choice == 8:
			about()
		else:
			print('WRONG INPUT. ENTER THE CORRECT CHOICE')
