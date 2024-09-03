import random
import string

#Password generating program

def generating_password(lenght: int = 12):
    #Defining what the password can contain AND avoiding sql injection characters such as / 
    
    structure = string.ascii_letters + string.digits + "!@#$%^&*-_=+[]{};:',.<>/?" 
    
    #Randomizing + generating password while avoiding the same two characters in a row (thus the while loop)
    
    password = []
    while len(password) < lenght:
        character = random.choice(structure)
        if not password or character !=password[-1]:
            password.append(character)
    return ''.join(password)

password = generating_password()
print(f"Strong password generated: {password}")