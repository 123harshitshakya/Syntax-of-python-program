# name=input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)

# if age >=18:
# 	print("you are old enough to vote")
# else:
# 	print("Please come back in {0} years".format(18 -age))





# print("Please guess a number between 1 to 10: ")
# guess=int (input())

# if guess !=5:

# 	if guess<5:
# 		print("Please guess higher")
#     else:
#     	print("Please guess lower")
#     guess=int(input())	
#     if guess ==5:
#     	print("Well done, you guessed it")
#     else:
#     	print("Sorry, you not guessed correctly")
# else:
# 	print("You got it first time")    		



# age=int(input("How old are you? "))
# if(age<16) or (age > 65):
# 	print("Enjoy your free time")
# else:
# 	print("Have a good day at work")


# age=int(input("How old are you? "))
# if not(age < 18):
# 	print("You are old enough to vote")
# 	print("Please put an X in the box")
# else:
# 	print("Please come back in {0} years".format(18 - age))




# parrot ="Norwegian Blue"

# letter=input("Enter a character")

# if letter in parrot:
# 	print("Give me an {},Bob".format(letter))
# else:
# 	print("I don't need that letter")



parrot= "Norwegian Blue"

letter=input("Enter a character: ")

if letter not in parrot:
	print("I don't need that letter")
else:
	print("Give me an {}, Bob".format(letter))










