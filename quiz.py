import json
import random

user = [] # Array to hold users in session

# function to play the Quiz
def play():
	print("\n==========WELCOME==========")
	score = 0
	with open("assets/questions.json", 'r+') as f:
		j = json.load(f)
		for i in range(5):
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print("***QUESTION****")
			print(f'\nQ{i+1} {j[ch]["question"]}\n')
			for option in j[ch]["options"]:
				print(option)
			answer = input("\nEnter your answer: ")
			if j[ch]["answer"][0] == answer[0].upper():
				print("***RESULT****")
				print("\nYou are correct")
				print("Difficulty Level "+j[ch]["Level"])
				score+=1
			else:
				print("***RESULT****")
				print("\nYou are incorrect")
				print("Difficulty Level "+j[ch]["Level"])
			del j[ch]

		print(f'\nFINAL SCORE: {score}')


# Function to display the Quiz questions

def quizQuestions():
	if len(user) == 0:
		print("You must first login before adding questions.")
	elif len(user) == 2:
		if user[1] == "Admin":
			print('\n==========ADD QUESTIONS==========\n')
			ques = input("Enter the question that you want to add:\n")
			opt = []
			print("Enter the 4 options with character initials (A, B, C, D)")
			for _ in range(4):
				opt.append(input())
			ans = input("Enter the answer:\n")
			with open("assets/questions.json", 'r+') as f:
				questions = json.load(f)
				dic = {"question": ques, "options": opt, "answer": ans}
				questions.append(dic)
				f.seek(0)
				json.dump(questions, f)
				f.truncate()

				print("Question successfully added.")		
		else:
			print("You don't have access to adding questions. Only Admin are allowed to add questions.")


# Function to create a New Account or Add Users

def createAccount():
	print("\n==========CREATE ACCOUNT==========")
	username = input("Enter your USERNAME: ")
	password = input(" ENTER PASSWORD: ")
	with open('assets/user_accounts.json', 'r+') as user_accounts:
		users = json.load(user_accounts)
		if username in users.keys():
			print("An account of this Username already exists.\nPlease enter the login panel.")
		else:
			users[username] = [password, "USER"]
			user_accounts.seek(0)
			json.dump(users, user_accounts)
			user_accounts.truncate()
			print("Account created successfully!")

def loginAccount():
	print('\n==========LOGIN PANEL==========')
	username = input(" ENTER USERNAME: ")
	password = input(" ENTER PASSWORD: ")
	with open('assets/user_accounts.json', 'r') as user_accounts:
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
	print('''\n==========RULES==========
1. You have 5 to 10 questions in a round.
2. All questions are compulsory.
3. No negative marking
4. You will be awarded 1 mark for each correct answer.
5. There will be no time limit.
	''')

if __name__ == "__main__":
	choice = 1
	while choice != 7:
		print('\n=========WELCOMEF==========')
		print('-----------------------------------------')
		print('1. PLAY QUIZ')
		print('2. ADD QUIZ QUESTIONS')
		print('3. CREATE AN ACCOUNT')
		print('4. LOGIN PANEL')
		print('5. LOGOUT PANEL')
		print('6. INSTRUCTIONS')
		print('7. EXIT')
		choice = int(input('ENTER YOUR CHOICE: (1 to 7) '))
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
		else:
			print('WRONG INPUT. ENTER THE CHOICE AGAIN')
