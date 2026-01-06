# One function can call another function 

def Fun():
    print("Inside Fun")

def Gun():
    print("Inside Gun")

def main():
    Fun()
    Gun()
     
if __name__ == "__main__":
    main()    
