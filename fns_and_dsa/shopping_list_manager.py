def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True :
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            added_items = input("What would you like to add: ")
            shopping_list.append(added_items)
        elif choice == "2":
            try:
                shopping_list.remove(input("What would you like to remove: "))
            except:
                print("This item is not in your shopping list.")
        elif choice == "3":
            print(shopping_list)
        elif choice == "4":
            print("Good bye!")
            break
        else:
            print("Please,Enter a number between 1 and 4 .")
if __name__ == "__main__":
    main()