
def EmployeeInfo ( Name , Age , Salary , City):
    print("Name     :",Name)
    print("Age      :",Age )
    print("Salary   :",Salary)
    print("City     :",City)
    
def main():
    # Positonal
   
    #EmployeeInfo("Rahul",26,2000.50, "PUNE")    #CORRECT
    #EmployeeInfo(26,"Rahul","Pune",2000.50)     #WRONG

    
    print("-"*30)
    print("Keyword")
    EmployeeInfo(Age= 26 , Name= "Rahul" , City= "Pune", Salary="2000.50")     #WRONG

    
if __name__ == "__main__":
    main()