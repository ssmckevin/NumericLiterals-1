from DecIntDFA import DecIntDFA
# from OctIntDFA import OctIntDFA
# from HexIntDFA import HexIntDFA
from FloatingPointDFA import FloatingPointDFA as FPDFA

def main():
    print("Please enter Numeric literal to test validity.")
    str = input(">>")
    decDFA = DecIntDFA()
    # octDFA = OctIntDFA()
    # hexDFA = HexIntDFA()
    fpDFA = FPDFA()
    decAccepts = decDFA.accepts(str)
    # octAccepts = octDFA.accepts(str)
    # hexAccepts = hexDFA.accepts(str)
    floatingAccepts = fpDFA.accepts(str)
    if(decAccepts):
        print("Decimal Integer Accepted")
    # elif(octAccepts):
    #     print("Octal Integer Accepted")
    # elif(hexAccepts):
    #     print("Hexadecimal Integer Accepted")
    elif(floatingAccepts):
        print("Floating Point Accepted")
    else:
        print("Rejected.")
    

if __name__ == "__main__":
    main()