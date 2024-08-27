from src.properties.const import const    


def test():
    user_input = input()
    if user_input == "dog":
        print ("woof")
    else:
        print ("not valid")

if __name__ == "__main__":
    a = test()
    print(a)
    print("executed")
    
