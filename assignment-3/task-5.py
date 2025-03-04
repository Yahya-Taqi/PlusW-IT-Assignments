balance = 0

def Deposit(amount):
    global balance
    if amount < 0:
        print(f"ERROR: Please Enter Valid Amount!")
        return
    
    balance += amount
    print(f"{amount} added to balance")
    
def WithDrawAmount(amount):
    global balance
    if amount > balance:
        print(f"ATTENTION: Not Enough Balance Available!")
    else:
        balance -= amount
        print(f"{amount} withdrawn remaining balance: {balance}")
        
def ShowBalance():
    global balance
    print(f"Current Balance: {balance}")
    
## Setting initial balance
balance = 1000
Deposit(20)
ShowBalance()
WithDrawAmount(100)