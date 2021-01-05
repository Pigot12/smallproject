# Variables: (name, city, age, lower degree)
# age > 20, city = Athens, lower = yes

variable1 = "Athens"
variable2 = "20"

name = str(input(print("Tell me your name ")))

print("Answer Commited")

city = input(print("Tell me your city "))

print("Answer Commited")

age = int(input(print("Tell me your age ")))

print("Answer Commited")

lower = str(input(print("Tell me if you have a lower degree ")))

print("Answer Commited")

if(name == name):
    print("You pass the 1st level.So your name is " + name + " .")

if(city == "Athens"):
    print("You pass the 2nd level")
else:
    print("You didn't pass this level.The right answer was " + variable1 + " .")

if(age > 20):
    print("You pass the 3nd level.You are year " + str(age) + " old and the requrment age is " + variable2 + " .")
else:
    print("You didn't pass this level.You need to be " + variable2 + " or older.")

if(lower == "Yes" , "yes"):
    print("You pass the last level.Your answer to that question was " + lower + " .So you have one.")
else:
    print("You didn't pass this question.Your answer to that question was " + lower + " .")

