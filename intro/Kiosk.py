print("Here we have icecones för 20kr, hotdogs för 15kr, cola för 15kr och candy för 10kr! What do you want?")

icecone = 20
hotdog = 15
juice = 15
candy = 10

price = 0
item = input()


if item == "icecone":
    print("How many icecones do you want?")
    price = icecone

elif item == "hotdog":
    print("How many hotdogs do you want?")
    price = hotdog

elif item == "juice":
     print("How many juices do you want?")
     price = juice

elif item == "candy":
     print("How many candies do you want?")
     price = candy


amount = input()
amount = int(amount)


print(amount*price)

print("is that all?")

yes = input()
print("Thank you for purchasing!")


















