shoppingitem1 = "underwear"
shoppingitem2 = "tank top"
shoppingitem3 = "jacket"

items = {
    0: shoppingitem1,
    1: shoppingitem2,
    2: shoppingitem3
}

print("Matrix size:", len(items))
print(f"Shopping items1: {shoppingitem1}")
print(f"Shopping items2: {shoppingitem2}")
print(f"Shopping items3: {shoppingitem3}")

while True:
    option = input("\nWhat would you like to do [A]dd, [C]hange, [R]emove, [D]isplay, [S]earch ? ")

    if option == "A" or option == "a":
        keynum = input("Enter key: ")
        val = input("Enter value: ")
        if keynum.isdigit():
            items[int(keynum)] = val
            print("Item added.")
        else:
            print("Invalid key.")

    elif option == "C" or option == "c":
        keynum = input("Enter key: ")
        if keynum.isdigit() and int(keynum) in items:
            new_val = input("Enter new value: ")
            items[int(keynum)] = new_val
            print("Item updated.")
        else:
            print("I'm sorry, not in the items list.")

    elif option == "R" or option == "r":
        remove = input("Enter key or value to remove: ")
        if remove.isdigit():
            remove = int(remove)
            if remove in items:
                removed_val = items.pop(remove)
                print(f"The key {remove} with value '{removed_val}' has been deleted.")
            else:
                print("I'm sorry, not in the items list.")
        else:
            found = False
            for k, v in list(items.items()):
                if v == remove:
                    del items[k]
                    print(f"The key {k} with value '{remove}' has been deleted.")
                    found = True
                    break
            if not found:
                print("I'm sorry, not in the items list.")

    elif option == "D" or option == "d":
        print("\nDisplaying items")
        print("Key\tValue")
        for keynum, val in items.items():
            print(f"{keynum}\t{val}")

    elif option == "S" or option == "s":
        lookfor = input("Enter key or value: ")
        foundit = False  

        for keynum in list(items.keys()):
            if lookfor == items[keynum]:
                foundit = True
                print(f"Found {lookfor} Item.")
            elif lookfor.isdigit() and int(lookfor) == keynum:
                foundit = True
                print(f"Found {items[keynum]} item.")

        if not foundit:
            print(f"I'm sorry, {lookfor} NOT in the items list.")

    elif option == "*":
        print("Bye.")
        break

    else:
        print("Invalid choice. Please try again.")
