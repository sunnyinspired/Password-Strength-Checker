# list to store the result of the checks
checkResult = {}


# function to check the length of the password
def checkLength(pwd):
    if len(pwd) >= 8:
        checkResult["length"] = True
    else:
        checkResult["length"] = False


# function to check if the password contains a number
def checkDigit(pwd):
    digit = False
    for i in pwd:
        if i.isdigit():
            digit = True

    checkResult["digit"] = digit


# function to check if the password contains an uppercase character
def checkUpper(pwd):
    upperCase = False
    for i in pwd:
        if i.isupper():
            upperCase = True
    checkResult["upper"] = upperCase


# Get the user input
password = input("Enter Password: ")

# call the three functions above to check
checkLength(password)
checkDigit(password)
checkUpper(password)

# Check the list and count the occurrence of TRUE
pwd_true = 0
for value in checkResult.values():
    if value:
        pwd_true += 1

# Calculate the percentage of truth which will be used as the password strength
pwd_strength = round(pwd_true / len(checkResult.values()) * 100)

# Print a message and display the strength based on its value.
print(f"==== Password Analysis ==== \nLength: {len(password)}\n"
      f"Numbers: {checkResult['digit']}\n"
      f"UpperCase: {checkResult['upper']}\n"
      f"Strength: {pwd_strength}%")
if pwd_strength >= 90:
    print("Conclusion: Strong Password")
elif pwd_strength >= 70:
    print("Conclusion: Fair Password")
elif pwd_strength >= 50:
    print("Conclusion: Poor Password")
else:
    print("Conclusion: Weak Password")
