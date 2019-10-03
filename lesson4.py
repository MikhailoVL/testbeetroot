import random

print("Task 1")
print(random.randint(10, 100))

print("Task 2")
a = [1, 2, 3, 4, 5, 6]
random.shuffle(a)
print(random.choice(a))

print("Task 3")
print(random.random())

print("Task 4")
print(random.uniform(0, 25))

spisok=["камень", "ножницы", "бумага"]

def rock_scissors_paper(spi):
	print("это игра \"КАМЕНЬ, НОЖНИЦЫ, бумага")
	print("введите камень, ножницы или бумага")
	pc_choice = random.choice(spi)
	your_choice = input("ваш ход - ")
	print(pc_choice)
	if your_choice == "камень" or your_choice =="ножницы" or your_choice =="бумага":
		if pc_choice == your_choice:
			print("ничья")
		elif your_choice == "камень":
			if pc_choice == "ножницы":
				print("you won")
			else:
				print("you lost")
		elif your_choice == "бумага":
			if pc_choice == "камень":
				print("you won")
			else:
				print("you lost")
		elif your_choice == "ножницы":
			if pc_choice == "бумага":
				print("you won")			
			else:
				print("you lost")			
	else:
		print("неверный ввод")		 

rock_scissors_paper(spisok)
