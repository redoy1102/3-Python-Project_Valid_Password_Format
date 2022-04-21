password = input("Enter your password: ")
atTheRet = password.find("@")
hash = password.find("#")
underScore = password.find("_")
star = password.find("*")
lowerCase = upperCase = 0

for x in password:
    if "a" <= x <= "z":
        lowerCase = 1
    if "A" <= x <= "Z":
        upperCase = 1

if atTheRet != -1 and hash != -1 and underScore != -1 and star != -1 and lowerCase == 1 and upperCase == 1:
    print("Valid Password Format.")
else:
    print("Oops! Invalid password format.")
