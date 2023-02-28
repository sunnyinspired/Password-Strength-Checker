checkResult = []


def checkLength(pwd):
    if len(pwd) >= 8:
        checkResult.append(True)
    else:
        checkResult.append(False)


def checkDigit(pwd):
    digit = False
    for i in pwd:
        if i.isdigit():
            digit = True

    checkResult.append(digit)


def checkUpper(pwd):
    upperCase = False
    for i in pwd:
        if i.isupper():
            upperCase = True
    checkResult.append(upperCase)


password = input("Enter Password: ")
checkLength(password)
checkDigit(password)
checkUpper(password)

pwd_true = checkResult.count(True)
pwd_strength = round(pwd_true / len(checkResult) * 100)
if pwd_strength >= 90:
    print(f"Password Strength: {pwd_strength}% ... Strong Password")
elif pwd_strength >= 70:
    print(f"Password Strength: {pwd_strength}% ... Fair Password")
elif pwd_strength >= 50:
    print(f"Password Strength: {pwd_strength}% ... Poor Password")
else:
    print(f"Password Strength: {pwd_strength}% ... Weak Password")

