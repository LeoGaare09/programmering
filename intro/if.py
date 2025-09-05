print("Hej! Hur gammal är du?")
age = input()
age = int(age)

if age < 18:
    print("Du är ett barn")



elif age >= 18 or age < 60: 
    print("Du är vuxen")

elif age >= 60:
    print("Du är gammal")

else:
    print("Jag vet inte vad du är")




