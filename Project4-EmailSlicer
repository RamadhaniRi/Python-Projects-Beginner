#EmailSlicer
# we will slice the string in email like bro@gmail.com to bro and gmail.com

email = input("input your email here!")
index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print(f"your username is {username}, your domain is {domain}")

# or you can use this code

 
def emailslicer(email):
    index = email.index("@")

    username = email[:index]
    domain = email[index + 1:]
    return username, domain

email = input("input your email here!")
username, domain = emailslicer(email)
print(f"your username is {username}, your domain is {domain}")
