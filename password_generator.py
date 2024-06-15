''' 
A password generator: is a useful tool that generates strong and
                          random passwords for users. This project aims to create a
                          password generator application using Python, allowing users to
                          specify the length and complexity of the password.

 User Input: Prompt the user to specify the desired length of the
             password and complexity level.

 Generate Password: Use a combination of random characters to
                    generate a password of the specified length.

 Display the Password: Print the generated password on the screen.
 '''

# importing required labraries
import random
import string
import secrets

# creating a function that will generate the password
def password_generator(lenght,complexity,symbol):
    password=None
    if lenght==4:
        password=random.randrange(0000,9999)
    elif complexity == "E":
        if lenght==6:
            password=random.randrange(000000,999999)
        elif lenght == 8:
            password=random.randrange(00000000,99999999)
    if lenght==6:
        if complexity == "M":
            alpha = ''.join(secrets.choice(string.ascii_lowercase )for i in range(3)).capitalize()
            dgts = ''.join(secrets.choice(string.digits )for i in range(3))
            password = alpha+dgts

        if complexity == "S":
            alpha = ''.join(secrets.choice(string.ascii_lowercase )for i in range(3)).capitalize()
            dgts = ''.join(secrets.choice(string.digits )for i in range(2))
            password = alpha+symbol+dgts

            
    if lenght==8:
        if complexity == "M":
            alpha = ''.join(secrets.choice(string.ascii_lowercase )for i in range(4)).capitalize()
            dgts = ''.join(secrets.choice(string.digits )for i in range(4))
            password = alpha+dgts

        if complexity == "S":
            alpha = ''.join(secrets.choice(string.ascii_lowercase )for i in range(4)).capitalize()
            dgts = ''.join(secrets.choice(string.digits )for i in range(3))
            password = alpha+symbol+dgts

    return password




symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','\\',':',';','"','\'','<',',','>','.','?','/']
symbol=None
complexity=None

# fetching inputs from the user and validating the inputs
lenght=int(input("Enter the desired length of the password (eg. 4,6,8):: "))
while lenght != 4 and lenght != 6 and lenght != 8:
    lenght=int(input("The lenght of the password should either be 4,6 or 8:: "))

if lenght == 4:
    pass
else:
    complexity=input("Enter the complexity level.\n E for easy, M for medium and S for strong:: ").upper()
    while complexity != "E" and complexity != "M" and complexity != "S":
        complexity=input("E for easy, M for medium and S for strong:: ").upper()
    if complexity == 'S':
        symbol=input("Enter the special symbol you want to keep in your password:: ")
        while symbol not in symbols:
            symbol=input("Enter the special symbol (eg.'@','#','$','%','^','&','*',etc ):: ")

# print(lenght,complexity,symbol)
password=password_generator(lenght,complexity,symbol)
print(password)

    
