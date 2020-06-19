import pizzapi
import tkinter as tk

'''
Function: Create Customer
'''
def CreateCustomer(firstName, lastName, email, number):
    customer = pizzapi.Customer(firstName.get(), lastName.get(), email.get(), number.get())
    return customer


'''
Function: Create Address
'''
def CreateAddress(street, city, state, zipcode):
    address = pizzapi.Address(street.get(), city.get(), state.get(), zipcode.get())
    return address


'''
Function: CreateCard
'''
def CreateCard(cardNum, expiration, cvv, zipcode):
    card = pizzapi.PaymentObject(cardNum.get(), expiration.get(), cvv.get(), zipcode.get())
    return card


'''
Function: Create Order
'''
def CreateOrder():
    pass


'''
Function: Submit
'''
def SubmitOrder(customer, address, card):
    order = pizzapi.Order(address.closest_store(), customer, address)
    order.pay_with(card)



'''
Function: Get Menu Items
'''
def GetMenuItems(address):
    store = address.closest_store()
    menu = store.getMenu()
    return menu.search(name='Pizza')


'''
Creating the GUI
'''
window = tk.Tk()

# create all the labels for each entry
fNameLabel = tk.Label(text='First Name')
lNameLabel = tk.Label(text='Last Name')
emailLabel = tk.Label(text='Email')
numberLabel = tk.Label(text='Phone Number')
streetLabel = tk.Label(text='Street')
cityLabel = tk.Label(text='City')
stateLabel = tk.Label(text='State')
zipLabel = tk.Label(text='Zip Code')
creditLabel = tk.Label(text='Credit Card Number')
expirationLabel = tk.Label(text='Expiration Date (MMYY)')
cvLabel = tk.Label(text='Security Code')

# create all the entry fields for the information
fNameEntry = tk.Entry()
lNameEntry = tk.Entry()
emailEntry = tk.Entry()
numberEntry = tk.Entry()
streetEntry = tk.Entry()
cityEntry = tk.Entry()
stateEntry = tk.Entry()
zipEntry = tk.Entry()
creditEntry = tk.Entry()
expirationEntry = tk.Entry()
cvEntry = tk.Entry()

# add all the fields to the user interface
fNameLabel.pack()
fNameEntry.pack()
lNameLabel.pack()
lNameEntry.pack()
emailLabel.pack()
emailEntry.pack()
numberLabel.pack()
numberEntry.pack()
streetLabel.pack()
streetEntry.pack()
cityLabel.pack()
cityEntry.pack()
stateLabel.pack()
stateEntry.pack()
zipLabel.pack()
zipEntry.pack()
creditLabel.pack()
creditEntry.pack()
expirationLabel.pack()
expirationEntry.pack()
cvLabel.pack()
cvEntry.pack()

newCustomer = CreateCustomer(fNameEntry, lNameEntry, emailEntry, numberEntry)
newAddress = CreateAddress(streetEntry, cityEntry, stateEntry, zipEntry)
newCard = CreateCard(creditEntry, expirationEntry, cvEntry, zipEntry)


'''
Function: GetMenu
'''
def CreateMenu(address):
    menuWindow = tk.Tk()
    textbox = tk.Text(menuWindow, height='40', width='40')
    textbox.pack()
    textbox.insert(tk.END, GetMenuItems(newAddress))


# add a view menu button
viewMenuButton = tk.Button(text='View Menu')
viewMenuButton.bind("<Button-1>", CreateMenu(newAddress))

# add submit button
submitButton = tk.Button(text='Submit')
submitButton.bind("<Button-1>", SubmitOrder())
submitButton.pack()


window.mainloop()


