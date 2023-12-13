sct211 - 0060 /2022
Njoroge Kimberly

class Addition:
    def add(self, *args):
        result = 0
        if len(args) > 1:
            for num in args:    
                result = result + num
        else:
            print("Please enter two numbers or more numbers")
            exit()
        return result
class Subtraction:
    def minus(self, *args):
        result = 0

        if len(args) > 1:
            for num in args:    
                result = result - num
        else:
            print("Please enter two numbers or more numbers")
            exit()
        return (result + args[0] + args[0])
class Multiplication:
    def product(self, *args):
        result = 1

        if len(args) > 1:
            for num in args:    
                result = result * num
        else:
            print("Please enter two numbers or more numbers")
            exit()
        return result
class Division:
    def divide(self, *args):
        result = 0
        FirstNumber= True
        if len(args) > 1:
            for num in args:
                if FirstNumber == True:
                    result = num
                    FirstNumber = False
                    continue
                if num == 0:
                    print("Number not divisible by 0")
                    exit()
                else:
                    result = result / num
        else:
            print("Please enter two numbers or more numbers")
            exit()         
        return result

class Calculator:
    def __init__(self, addition, subtraction, division, multiplication):
        self.Addition = addition
        self.Subtraction = subtraction
        self.Division = division
        self.Multiplication = multiplication
        
    def add(self, *args):
        return self.Addition.add(*args)
        
    def minus(self, *args):
        return self.Subtraction.minus(*args)
    
    def divide(self, *args):
        return self.Division.divide(*args)
        
    def product(self, *args):
        return self.Multiplication.product(*args)


#Instantiate "Calculator" object
calculate = Calculator(Addition(), Subtraction(), Division(), Multiplication())

# print(calculate.divide(values))
print("Values. ")
tempvalues = list()
n = 0
while True:
    temp = input('Enter a number(Enter q to stop entry): ')
    if temp == 'Q' or temp == 'q':
        break
    try:
        tempvalues.append(float(temp))
        print(tempvalues[n])
        n += 1
    except:
        print('Please enter number only!')
    
values = tuple(tempvalues)
print(values)
print("Operator.\nEnter Operator: ")
while True:
    op = input('Sum, Minus, Quotient or Product: ')
    if op == 'Sum' or op == 'sum':
        print('Result is: ', calculate.add(*values))
        quit()
    elif op == 'Product' or op == 'product':
        print('Result is: ', calculate.product(*values))
        quit()
    elif op == 'Quotient' or op == 'quotient':
        print('Result is: ', calculate.divide(*values))
        quit()
    elif op == 'Minus' or op == 'minus':
        print('Result is: ', calculate.minus(*values))
        quit()
    else:
        print('Enter a accepted operator! ')
