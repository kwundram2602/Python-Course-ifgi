class calculator:
    def add(self, number1 : int, number2 : int):
        return number1 + number2
    
    def subtraction(self, number1 : int, number2 : int):
        return number1 - number2
    
    def multiply(self, number1 : int, number2 : int):
        return number1 * number2
    
    def division(self, number1 : int, number2 : int):
        if number2 != 0:
            return number1/number2
        else:
            raise Exception("Man kann nicht durch 0 dividieren")
    