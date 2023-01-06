import os
import hashlib
import time
from random import randint
import math

def generate_salt():
    return os.urandom(32)

def hash_password(password, salt):
    salted_password = str(salt)+password
    return hashlib.sha256(salted_password.encode()).hexdigest()

def verify_password(password, salt, hashed_password):
    return hash_password(password, salt) == hashed_password


if __name__ == "__main__":

    salt = generate_salt()
    for i in range(randint(1,12)):
        print("Generating a salt ... ")
        time.sleep(1)
    
    print("\nThe Salt Generated is: " + str(salt))
    
    password = input("\nEnter a password: ")
    hashed_password = hash_password(password,salt)
    for i in range(randint(1,21)):
        print("Hashing the Password ... ")
        time.sleep(1)
    
    print("\nRESULT:")
    
    print("The hashed password is in combination with the salt added is: " + str(hashed_password))

    
