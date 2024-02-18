from  operations import Library

def menu( ):
    print("MENU")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("Q) Quit")

myLoopControl = True
lib = Library() 

while myLoopControl:
    menu()
    itemChosen = input("You can choose : ")

    if itemChosen == "1":
        lib.list_of_books()

    elif itemChosen == "2":
        lib.add_book()

    elif itemChosen == "3":
        lib.remove_book()

    elif itemChosen.upper() == "Q": #girilen karakter büyük hare dönüştürülür
        print("Exit")
        myLoopControl = False
        
    else:
        print("Wrong Choice!") 