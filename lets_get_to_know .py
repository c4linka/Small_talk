print("Let's get to know each other :)")

name = input("What is your name? ")
name = name.capitalize()
print("Hello",(name),":)")
age = int(input("How old are you? "))
print("Oh, you look much younger than",(age),"What is your secret?")
secret = input("Please, tell me what do you do. ")
print("And will I look so good, if I also",(secret.strip("I .")) + "? ")

answer1 = input("Answer yes or no ")
if (answer1 == "yes"):
    print("That's fantastic! I will do that!")
if (answer1 == "no"):
    print("Ok, I will try something good for me...")
if (answer1 != "yes") and (answer1 != "no"):
    print("Whatever...")


answer2 = input("Would you like to know, how old you will be in 10 years? Write yes or no. ")
if (answer2 == "yes"):
    print("In 10 years you will be",(age+10),"years old. Ok, that all for now. Thank you for nice conversation :)")
if (answer2 == "no"):
    print("Ok, then no")
if (answer2 != "yes") and (answer2 != "no"):
    print("Ok, that all for now, Thank you for nice conversation :))")
