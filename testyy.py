import secrets
import string
import random
import json






# def random_char():
#     with open("words.txt", "r") as file:
#         allText = file.read()
#         words = list(map(str, allText.split()))
#     return ''.join(random.choice(words) for t in range(2))
#     # print random string
    
# print (random_char()+(secrets.choice(string.digits))*2)

# a={"email":"kaskos1211" , "password":'AvGF$#'}
with open("sample.json", "r") as handler:
    info = json.load(handler)

users = info["users"]
passwords = info["passwords"]
for i in range(10):
    alphabet=string.ascii_letters.lower()
    email="".join(secrets.choice(alphabet)for i in range(14))+"".join(secrets.choice(string.digits)for i in range(3))
    alphabet1=string.ascii_letters +')(*&^%$#@!~=+' +string.digits
    password="".join(secrets.choice(alphabet1)for i in range(20))
    if email not in users and password not in passwords:

        users.append(email)
        passwords.append(password)



# a={"users":users , "passwords":passwords}
# json_object = json.dumps(a, indent = 4)

# # Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)
# print("'{}','{}'".format(users[3], passwords[3]))
