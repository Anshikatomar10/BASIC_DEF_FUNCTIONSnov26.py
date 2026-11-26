#LEVEL 1 (no inputs no returns ) 
#at its simplest ,def just groups lines of code under oone command name , so you dont have to repeat them
def show_menu():
    print("_"*5, "MENU","_"*5)
    print("1. chai -rs15")
    print("2.samosa -rs20")
    print("-"*15)

show_menu()   

# LEVEL 2 def (with parameters(inputs))
#parameters are the variables under the parentheses() that let you pass that let you pass different data into your machine each time you run it .

def greet_customer(customer_name , item):
    print(f"welcome {customer_name} \n your {item} is being prepared . ")
   
greet_customer("arav","chai")
greet_customer("priya","samosa")
greet_customer("rahul","chai")

#LEVEL 3 . def with return( Getting an ans back  ).
#print () only displays textt on your screen - Python immediately forgets the number .
# return hands calculated value back to your code so you can save it a variable and do math with it later .

def calculate_bill(chai_qty,samosa_qty):
    total = (chai_qty*15)+(samosa_qty*20)
    return# sends the number back out of the function .

my_bill = calculate_bill(2,3)
print(f"total billl :{my_bill}")
print(f"with rs 10 tip :{my_bill}+10")

# LEVEL 4 combiniing all the prior functions all together .
 # it helps make the program look more put together .

def show_menu():
    print(f"welcome to python chai stall ")
    print("chai -15|samosa -20 ")

def calculate_bill(chai_qty,samosa_qty):
    return(chai_qty*15)+(samosa_qty*20)

def apply_discount(bill_amountt):
    if bill_amountt >= 100:
        print("you got rs 20 discount")
        return bill_amountt -20
    return bill_amountt

# --------main program --------
show_menu()
chai = int(input("how many chai ??"))
samosa = int(input("how many samosa ??"))

raw_total = calculate_bill(chai,samosa)
final_total = apply_discount(raw_total)
print(f"final total to pay : rs{final_total}")