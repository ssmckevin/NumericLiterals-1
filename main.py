from DecIntDFA import DecIntDFA

def main():
    str = input(">>")
    decDFA = DecIntDFA()
    decAccepts = decDFA.accepts(str)
    octAccepts = False
    hexAccepts = False
    if(decAccepts):
        print("Decimal Integer Accepted")
    elif(octAccepts):
        print("Octal Integer Accepted")
    elif(hexAccepts):
        print("Hexadecimal Integer Accepted")
    else:
        print("Rejected. Not an Integer Literal.")
    

if __name__ == "__main__":
    main()