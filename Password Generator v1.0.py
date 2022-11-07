import random
import time

print ("Welcome to the Password Generator v1.0")
# I can't see this program getting past v1.0, unless i add a GUI? ...hm...

chars="abccdefghijklmnopqrstuvwxyz1234567890[]#./!£$%^&*()_+~@}{?><"
# the characters the generator will consider when generating a password

pwchoices = input("Amount of Passwords to generate: ")  
pwchoices = int(pwchoices)
# asks for user input of an integer, then stores it under 'pwchoices'

length = input("How long would you like your passwords to be?: ")
length = int(length)
# asks for user input of an integer, then stores it under 'length'

print("\nHere are your Passwords:")
for pwd in range(pwchoices):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print (passwords)
# creates a list then adds 'pwchoices' multiplied by 'length' and prints to output


time.sleep(15)
# 15 seconds pause to copy-paste your new password from console

exit()
# i wonder what this does o.O