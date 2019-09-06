import json
from difflib import get_close_matches
from os import system, name

# Function Definitions
def nearmatch(user_data, keys):
    return get_close_matches(user_data,keys)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def printer_func(data, items):
    print (data + " means:")
    for value in items:
        print (value)

def data_check(user_data, keys, data1):
    if user_data in keys:
        clear()
        item1 = data1[user_data]
        printer_func(user_data, item1)
        return 1
    elif user_data.title() in keys:
        clear()
        item1 = data1[user_data.title()]
        printer_func(user_data.title(), item1)
        return 1
    elif user_data.upper() in keys:
        clear()
        item1 = data1[user_data.upper()]
        printer_func(user_data.upper(), item1)
        return 1
    elif user_data.lower() in keys:
        clear()
        item1 = data1[user_data.lower()]
        printer_func(user_data.lower(), item1)
        return 1
    else:
        return 0

# Main Function
data1 = json.load(open("data.json"))
print("Enter /exit to exit")
user_data = input("Enter the word: ")
keys = data1.keys()
while user_data != '/exit':
    clear()
    if data_check(user_data,keys,data1):
            user_data = "/exit"
    else:
        closematch = nearmatch(user_data,keys)
        clear()
        if len(closematch) > 0:
            print ("Did you mean one of these:")
            for value in closematch:
                print (value)
        else:
            print("Word does not exist in language")
        print("Enter /exit to exit")
        user_data = input("Enter the word: ")
