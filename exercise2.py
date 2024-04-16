def donuts(count):
    text = "Number of Donuts: {}"
    if isinstance(count, int):
        if count < 10:
            return text.format(count)
        else: 
            return text.format("many")         
    else:
        return "The input has to be an integer."
        

def verbing(s):
    if isinstance(s, str):
        if len(s) >= 3:
            if s.endswith("ing"):
                s = s + "ly"
                return s
            else:
                s = s + "ing"
                return s
        else: 
            return s
    else:
        return "The input has to be a string."
    

def main():
    print('donuts')
    print(donuts(4))
    print(donuts(9))
    print(donuts(10))
    print(donuts('twentyone'))
    print('verbing')
    print(verbing('hail'))
    print(verbing('swiming'))
    print(verbing('do'))

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
    