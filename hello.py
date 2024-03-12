# Ask user for name
# name = input("What's your name? ")

#Split users name into first name and last name
# first , last = name.split(" ")

# you can chain 2 variables like strip and title to reduce clutter like this message
# Remove whitespace from str

# name = name.strip()

# .Capitalize/.Title users name
# name = name.capitalize()


# Say hello to user putting f in front of sequece can tell the machine to format this sequece differently
# print(f"Hello, {first}")
# def - the ability to create new functions or choose name of fuctions def hello()

def hello(to): 
    print("hello,", to)

name = input("What's your name? ")
hello(name)
#scope 