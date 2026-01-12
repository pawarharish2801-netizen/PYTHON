# Procedural

def CheckEven(No):
    if(No % 2 == 0):
        print("It is Even")
    else:
        print("It is Odd")

def main():
    Value = 0

    print("Enter number : ")
    Value = int(input())

    CheckEven(Value)

if __name__ == "__main__":
    main()