"""
Title: customer service
author: braeden dirksen
date: oct 26
"""

listlist = []


def addtolist(a):
    a.append(input("What is the persons name?"))
    return a

def menu():
    print("""
    MENU:
    (1) add someone to a list
    (2) view lists
    (3) create new list
    (4) view a list
    """)
    menu = input()
    return menu

def viewlist():
    print(listlist)
    print(input("what list would you like to view?"))
    
repeat = True
while repeat:
    select = menu()
    if select == "1":
        addtolist(input("what list would you like to add seomeone to?"))
    elif select == "2":
        print(listlist)
    elif select == "3":
        listname = input("choose a name for the list")
        listlist.append(listname)
        listname = []
        listname.append("test1")
    elif select == "4":
        print(input("what list would you like to view"))


