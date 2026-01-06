
def EmployeeInfo ( A):
    print(type(A))
    print("Name     : ",A[0])
    print("Age      :",A[1] )
    print("Salary   : ",A[2])
    print("City     :",A[3])
    
def main():
    EmployeeInfo([11,21,234,233])

    
if __name__ == "__main__":
    main()