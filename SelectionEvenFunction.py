def CheckEven(No):
    if(No % 2 == 0):
        print("It is Even")
    else:
        print("It is Odd")

def main():
    CheckEven(21)           # Positional
    CheckEven(No = 22)      # Keyword

if __name__ == "__main__":
    main()