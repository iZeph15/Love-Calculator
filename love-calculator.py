print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is the the other person's name? \n")

combined_string = name1+name2
lowercase = combined_string.lower()

t = lowercase.count("t")
r = lowercase.count("r")
u = lowercase.count("u")
e = lowercase.count("e")

true = t + r + u + e

l = lowercase.count("l")
o = lowercase.count("o")
v = lowercase.count("v")
e = lowercase.count("e")

love = l + o + v + e
love_score = str(true) + str(love)
int_love = int(love_score)

# print(love_score)

if (int_love < 10) or (int_love > 90):
    print(f"Your score is {int_love}, you go together like coke and mentos.")
elif int_love>= 40 and int_love <= 50:
    print(f"Your score is {int_love}, you are alright together.")
else:
    print(f"Your score is {int_love}.")