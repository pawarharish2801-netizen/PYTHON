
def EmployeeInfo ( Name , Age , Salary , City = "Pune"):
    print("Name     :",Name)
    print("Age      :",Age )
    print("Salary   :",Salary)
    print("City     :",City)
    
def main():
    EmployeeInfo(Age= 26 , Name= "Rahul" ,  Salary="2000.50")     #WRONG

    
if __name__ == "__main__":
    main()