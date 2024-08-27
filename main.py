from src.properties.const import const    


def test(user_input):
    
    if user_input == "dog":
        print ("woof")
    elif user_input == "cat":
        print("meow")
    else:
        print ("not valid")

if __name__ == "__main__":
    user_input = input("enter text here:")
    a = test(user_input=user_input)
    print(a)
    print("executed")
    
