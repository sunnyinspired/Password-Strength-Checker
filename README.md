# Password-Strength-Checker
This is a python command line interface program which checks the strength of a given password and analyses it as well.
Basically, the program checks for the following:
1. Length - must be up to 8 characters
2. Number: must contain a number
3. UpperCase: must contain an uppercase character.

HOW IT WORKS
------------------
The program prompts the user for password input and when the password is supplied, it checks it for the above requirements.
It does the check using the following functions:
- checkLength()
- checkDigit()
- checkUpper()

For each check, a result is recorded in a dictionary called checkResult, length, digit and upper are used as the keys of the dictionary ,
while True or False is used as the corresponding value depending if it passes the check at the repective function or not.

At the end of the check, the values of the dictionary is extracted and same then an iteration over it to check and count the occurrence of True.
The password strength is calculated based on the number of True and the corresponding strength as well as the analysis is printed out.

Example of such analysis is shown below:
Enter Password: Admin12
    ==== Password Analysis ==== 
    Length: 7
    Numbers: True
    UpperCase: True
    Strength: 67%
    Conclusion: Poor Password
