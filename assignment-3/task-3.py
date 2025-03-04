phoneBook = {}

def AddContact(name, phoneNumber):
    ## if phone number already exists
    if phoneNumber in phoneBook.values():
        print(f"Phone Number Already Exists!")
        return
    else:
        phoneBook[name] = phoneNumber
        print(f"New Contact Added!")
        return

def GetContact(name):
    if name in phoneBook:
        return phoneBook[name]
    else:
        return "Contact Not Found!"
      
AddContact("Joma", "+92-3123456789")
AddContact("JoJoma", "+92-3987654211")

## tried to add new person with same contact
AddContact("JoJo", "+92-3987654211")

print(f"{GetContact("Joma")}")
print(f"{GetContact("Jojo")}")