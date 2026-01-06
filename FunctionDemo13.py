# Nested Function
def Phoenix():
    print("Inside Phoenix")

    def Zara():
        print("Inside Zara ")
        
    Zara()

def main():
    Phoenix()

if __name__ == "__main__":
    main()    
