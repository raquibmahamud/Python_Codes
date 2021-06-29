class User():
    pass
class Address(User):
    pass
class Customar(Address):
   pass

Cu = Customar()
Cu.name = "Raquib Mahamud"
print(f"the name is :{Cu.name}\n")
Us = User()
Us.userID = 163432541
Us.password = 1234
print(f"Id : {Us.userID} \n Password : {Us.password}")
Ad = Address()
Ad.Line1 = "I am a student "
Ad.city = "Dhaka"
Ad.country = "Bangladesh"
print(f"The line is : {Ad.Line1},\n City :{Ad.city}\n Country :{Ad.country}")
class Ipayment:
    payment = int(input("Enter payment: "))
    if payment > 0 :
        print(f"I need to pay:{payment}")
