import random

def hello_world()-> str:
    """
    This function returns the string 'Hello World!'

    @return string with 'Hello World!'
    """
    return "Hello World!"

def main()-> None:
    chance = random.random()
    if chance < 0.5:
        print(hello_world())

if __name__ == "__main__":
    main()