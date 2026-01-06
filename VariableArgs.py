def Addition(*no):
    print(no)
    print(type(no))     # <class 'Tuple'>
    print(len(no))      # 5
    
def main():
    Addition(11,21,51,101,11)    

if __name__ == "__main__":                                               
    main()