print("Hur gammal är du?")
age = input()
age = int(age)

if age <= 14:
    print("Då får du barnbiljett för 16kr")

elif age >= 15 and age <= 20:
    print("Du får ungdomsbiljett för 20kr")

elif age > 20 and age < 65:
    print("Du får ordinariepris för 27kr")

elif age >= 65:
    print("Du får seniorbiljett för 21kr")

