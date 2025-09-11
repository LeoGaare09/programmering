print("say two numbers")
number_1 = input()
number_1 = int(number_1)
number_2 = input()
number_2 = int(number_2)


def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplikation(x, y):
    return x * y

def division(x, y):
    return x / y 


print("What method?")
print("1 för addition")
print("2 för subtraction")
print("3 för multiplication")
print("4 för division")

choice = input()
if choice == "1":
    result = addition(number_1, number_2)
    print(result)
    
elif choice == "2":
    result_2 = subtraction(number_1, number_2)
    print(result_2)
   
elif choice == "3":
    result_3 = multiplikation(number_1, number_2)
    print(result_3)
    
elif choice == "4":
    result_4 = division(number_1, number_2)
    print(result_4)














    





