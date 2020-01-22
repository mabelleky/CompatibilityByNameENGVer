
# Prompt user input for names
firstNameOfPerson1 = input("Enter your first name only: ")
middleNameOfPerson1 = input("Enter your middle name: ")
lastNameOfPerson1 = input("Enter your last name: ")

firstNameOfPerson2 = input("Enter the first name of the person you're matching with: ")
middleNameOfPerson2 = input("Enter the middle name of the person you're matching with: ")
lastNameOfPerson2 = input("Enter the last name of the person you're matching with: ")

# Capitalize all user inputs
p1FirstName = firstNameOfPerson1.upper()
p1MiddleName = middleNameOfPerson1.upper()
p1LastName = lastNameOfPerson1.upper()

p2FirstName = firstNameOfPerson2.upper()
p2MiddleName = middleNameOfPerson2.upper()
p2LastName = lastNameOfPerson2.upper()

# dictionary construct mimicing switch case for checking strokes per letter
switchCase = {
    ' ': 0,
    'A': 3,
    'B': 3,
    'C': 1,
    'D': 2,
    'E': 4,
    'F': 3,
    'G': 2,
    'H': 3,
    'I': 3,
    'J': 2,
    'K': 3,
    'L': 2,
    'M': 4,
    'N': 3,
    'O': 1,
    'P': 2,
    'Q': 2,
    'R': 3,
    'S': 1,
    'T': 2,
    'U': 1,
    'V': 2,
    'W': 4,
    'X': 2,
    'Y': 3,
    'Z': 3
}


def CheckTotalCharStrokes(nameChar):
    return switchCase.get(nameChar, "Invalid character(s) entered")


def GetTotalStrokesForName(name):
    sumOfStrokes = 0

    if len(name) == 0:
        return 0
    else:
        for letter in name:
            charTotalStrokes = CheckTotalCharStrokes(letter)
            if charTotalStrokes == "Invalid character(s) entered":
                return ("Invalid character(s) entered")
                # while (charTotalStrokes == "Invalid character(s) entered"):
            else:
                sumOfStrokes += charTotalStrokes
    return sumOfStrokes


def OnesDigitOfTotalStrokes(pname):
    sumOfStrokes = GetTotalStrokesForName(pname)
    if sumOfStrokes == "Invalid character(s) entered":
        print("Invalid character(s) entered")
        return ("Invalid character(s) entered")
    else:
        strSumOfStrokes = str(sumOfStrokes)
        onesDigitPosition = len(strSumOfStrokes) - 1
        strOnesDigit = strSumOfStrokes[onesDigitPosition]
        return (int(strOnesDigit))


def OnesDigitOfNum(num):
    strNum = str(num)
    onesDigitPosition = len(strNum) - 1
    strOnesDigit = strNum[onesDigitPosition]
    return (int(strOnesDigit))


def AddTwoNums(num1, num2):
    if (num1 == "Invalid character(s) entered") or (num2 == "Invalid character(s) entered"):
        return ("Invalid character(s) entered")
    else:
        totalNum = num1 + num2
        return OnesDigitOfNum(totalNum)


'''
Calculate compatibility score by taking and storing the ones digit into an array from the sum of index 0 & index 1, 
index 1 & index 2, index 2 & index 3, index 3 & index 4, index 4 & index 5.
Keep taking and storing the ones digit from the sum of the indexes like pattern above (add index 0 & 1, 1 & 2, etc) 
until your array is left with 2 numbers; the two numbers left is the compatibility score represented in percentage.
'''

position0 = OnesDigitOfTotalStrokes(p1FirstName)
position1 = OnesDigitOfTotalStrokes(p2FirstName)
position2 = OnesDigitOfTotalStrokes(p1MiddleName)
position3 = OnesDigitOfTotalStrokes(p2MiddleName)
position4 = OnesDigitOfTotalStrokes(p1LastName)
position5 = OnesDigitOfTotalStrokes(p2LastName)

listOfStrokes = [position0, position1, position2, position3, position4, position5]
counter = 4

while (counter > 0):
    for position in range(len(listOfStrokes) - 1):
        newOnesDigit = AddTwoNums(listOfStrokes[position], listOfStrokes[position + 1])
        listOfStrokes[position] = newOnesDigit

    listOfStrokes.pop()
    counter = counter - 1

print("\n Your compatibility score is: ", listOfStrokes[0], listOfStrokes[1], "%")
