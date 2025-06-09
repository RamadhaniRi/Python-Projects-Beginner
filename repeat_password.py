password = input("Password:")
while True:
    rpt_password = input("Repeat password:")

    if password == rpt_password:
        break
    else:
        print("They do not match!")
            

print("User account created!")