# basic caluclator to help calculate simple variations
# formula used from: https://www.wikihow.com/Calculate-Variance

# ========== FUNCTIONS ==========
# 1 : Style (1 for bold)
# 31 : Text color (31 for red)
# 40 : Background color (40 for black)

def RedInput(inputInput):
    termTextStart = "\033[1;31m"
    termTextEnd = "\033[0m"

    inputValue = input(termTextStart+ inputInput+ termTextEnd);
    YellowPrint(inputValue)
    return inputValue

def GreenPrint(printInput):
    termTextStart = "\033[1;32m"  # Green color start
    termTextEnd = "\033[0m"  # Reset color 

    print(termTextStart + str(printInput) + termTextEnd)

def OrangePrint(printInput):
    termTextStart = "\033[1;38;5;202m"  # Orange color start
    termTextEnd = "\033[0m"  # Reset color 

    print(termTextStart + printInput + termTextEnd)

def RedPrint(printInput):
    termTextStart = "\033[1;31m"
    termTextEnd = "\033[0m"

    print(termTextStart + printInput + termTextEnd);

def YellowPrint(printInput):
    LogTextStart = "\033[1;33m"  # Yellow color start
    LogTextEnd = "\033[0m"  # Reset color

    print(LogTextStart , printInput , LogTextEnd);




def SquareEachNum(array):
    returnValue = 0
    for x in array:
        returnValue += x**2 
    YellowPrint( "SquareEachNum: " + str(returnValue))
    return returnValue 

def MinusEachBySum(array):
    returnArray = []
    numSum = Sum(array)
    for x in array:
        x -= numSum
        returnArray.append(x)
        YellowPrint("MinusBySum: "+ str(returnArray))
    return returnArray

def MinusEachByMean(array):
    returnArray = []
    mean = Mean(array)
    for x in array:
        x -= mean
        returnArray.append(x)
        YellowPrint("MinusByMean: "+ str(returnArray))
    return returnArray

def SquareEachInArray(array):
    returnArray = []
    for x in array:
        x = x**2
        returnArray.append(x)
    YellowPrint("SquareEachInArray: " + str(returnArray))
    return returnArray

def Sum(array):
    returnValue = 0
    for x in array:
        returnValue += x
    YellowPrint("Sum: " + str(returnValue))
    return returnValue

def Mean(array):
    returnValue = 0
    for x in array:
        returnValue += x
    returnValue = returnValue / len(array)
    YellowPrint("Mean: " + str(returnValue))
    return returnValue


# ========= PROGRAM START ===========

i = 0
numbers = []

while i != 1:
    RedPrint('Hello, welcome to the program, by- vulbyte')

    # get input and convert to a flaot if has a space 
    inputStr = RedInput('enter all values seperated with a space ie: "12 32 3". \n does not need to be in any specific order: \n') 
    inputArray = inputStr.split()
    numbers = [float(num) for num in inputArray]
    print("Numbers:", numbers)

    i = int(input("are these numbers correct? if yes enter 1, to exit type 9, any other number if incorrect "))
    
    if i == '9': 
        exit()        

x = int(RedInput("are you looking for population variance (1), or \n are you looking for simple variance OR sample standard deviation? (9)?"))

i = 0

while i != 1:
    if (x == 1):
        ph = ( SquareEachNum(numbers) - float(len(numbers)) * Mean(numbers)**2 )
        print(ph)

        i = 1
    elif (x == 9):
        ph = 0 #placeholder
        r = 0 
       
        print("steps:") 
        ph = Mean(numbers) 
        print("get mean value (sum/amnt): " + str(ph)) # with example should return 14
        r = MinusEachByMean(numbers)
        print("minus the mean from meach data point: " + str(r))
        r = SquareEachInArray(r)
        print("square each result: " + str( r ))
        r = Sum(r)
        print("sum the squared values: " + str( r ))
        r = r/(len(numbers)-1)
        print("divide by amnt-1: " + str( r ))
        print("Sample Variance: ")
        GreenPrint(r)
        r = r**(1/2)
        print("above is your result \n√ for sample standard deviation: ")
        print("Sample Standard Deciation: " + str( r )) 
        GreenPrint(r)


        i = 1
    else:
        i = RedInput("input invalid, did you mean to exit? 1 for yes, 0 for no")
        if i == 1:
            exit()
        else:
            i = 0
input("enter any key to exit")

##print the fox >:3c
#OrangePrint("    |\__/|   ")
#OrangePrint("   /      \  ")
#print      ("  /_ O  0 _\ <Thank you for using vulbyes variance calculator, have a nice day!")
#OrangePrint("     \ @/    ")
#OrangePrint("")

print("        ┌┐           ┌┐\n        ├┴─┐       ┌─┴┤\n        │  │       │  │\n           xxxxxxx    │\n        xxxxxxxxxx    │\n      xxxxxxxxxxx     └┐\n     xxxxxxxxxx        │\n     xxxxx             │\n     xxx ┌──┐   ┌──┐   │\n ─┬┐ xxx │  ├───┤  │   └─┬┬─\n  └┤ xxx/│  │   │  │ /// ├┘\n   │ xxx └──┘ ▼ └──┘     │    <Thank you for using my variance calculator\n     xxx               ┌─┘     and have a great day     - vulbyte\n     xxx─┐         ┌───┘\n     xxx └─────────┘\n     xx\n     x\n")
