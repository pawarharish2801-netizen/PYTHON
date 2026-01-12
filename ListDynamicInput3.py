def Summation(Arr):
    Sum = 0

    for i in range(len(Arr)):
        Sum = Sum + Arr[i]

    return Sum

def main():
    Size = 0
    Value = 0
    Ret = 0
    
    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())    
        Data.append(Value) 

    Ret = Summation(Data)

    print("Summation is : ",Ret)
    
if __name__ == "__main__":
    main()