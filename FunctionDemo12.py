# Nested Function
def Phoenix():
    print("Inside Phoenix")

    def Zara():
        print("Inside Zara ")

def main():
    Phoenix.Zara()

     
if __name__ == "__main__":
    main()    
