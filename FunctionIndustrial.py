# Procedural

def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():
    Value = 0
    Ret = False

    print("Enter number : ")
    Value = int(input())

    Ret = CheckEven(Value)

    print(Ret)
    
if __name__ == "__main__":
    main()