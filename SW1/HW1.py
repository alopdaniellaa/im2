def convert(dollar):
    indianRupee = dollar * 88.18
    britishPound = dollar * 0.74
    chineseYuan = dollar * 7.12
    return indianRupee, britishPound, chineseYuan

while True:
    number = (input("Enter dollar($)/(* to exit): "))
    if number == "*":
        print("Bye")
        break
    
    print(f"Dollar($)     Indian Rupee(R)   British(Pound)  Chinese Yuan(Y)")

    num = number.split("@")
    for d in num:
        d = float(d)
        rupee, pound, yuan = convert(d)
        print(f"{d}\t\t{rupee:.2f}\t\t{pound:.2f}\t\t{yuan:.2f}")
        
    

 
        

    

