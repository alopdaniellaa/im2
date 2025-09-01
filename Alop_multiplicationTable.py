while True:
    row = int(input("Enter row: "))
    col = int(input("Enter column: "))
    search = int(input("Search: "))
    
    if row <= 0 or col <= 0:
        break
    
    for x in range(1, row + 1):
        for y in range(1, col + 1):
            if x * y == search:
                print(f"[{x*y}]", end = " ")
            else:
                print(f"{x*y}", end = " ")
        print()
            
            