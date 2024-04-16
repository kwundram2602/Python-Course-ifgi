def donuts(count):
    # Declaring the output string
    text = "Number of Donuts: {}"
    # Check if count is of type integer
    if isinstance(count, int):
        # Check for the length and returning the strings accordingly to the assignment 
        if count < 10:
            return text.format(count)
        else: 
            return text.format("many")       
    # If the input is not of type integer return a hint  
    else:
        return "The input has to be an integer."
        

def verbing(s):
    # Check if the input parameter s is of type string
    if isinstance(s, str):
        # Check for the length and the endings, then change the ending accordingly
        if len(s) >= 3:
            if s.endswith("ing"):
                s = s + "ly"
                return s
            else:
                s = s + "ing"
                return s
        else: 
            return s
    # If the input is not of type string return a hint
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
    