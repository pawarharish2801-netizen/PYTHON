# One function can call another function 

def Fun():
    print("Inside Fun")

def Gun():
    print("Inside Gun")
    Fun()

def main():
    Gun()
     
if __name__ == "__main__":
    main()    
