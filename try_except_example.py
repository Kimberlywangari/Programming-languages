sct 211 - 0060 /2022
Njoroge Kimberly

while True:
    try:
        num1 = int(input("First number: "))
        break
    except:
        print("Enter a number: ")

while True:
    try:
        num2 = int(input("Second number: "))
    except:
        print("Enter a number: ")
    
print ("Sum is" , num1 + num2)