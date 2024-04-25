class Calculator:
    def add(self, number1 : int, number2 : int):
        # return the added number
       return number1 + number2
    
    def subtract(self, number1 : int, number2 : int):
        # return the subtracted number
        return number1 - number2
    
    def multiply(self, number1 : int, number2 : int):
        # return the multiplyed number
        return number1 * number2
    
    def divide(self, number1 : int, number2 : int):
        if number2 != 0:
            # return the divided number if number2 isnt 0
            return number1/number2
        else:
            raise ZeroDivisionError("You cannot devide by zero")
        
 