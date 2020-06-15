import pizzapi
import tkinter as tk

'''
Function: Create Customer
'''
def CreateCustomer():
    pass


'''
Function: Create Address
'''
def CreateAddress():
    pass


'''
Function: CreateCard
'''
def CreateCard():
    pass


'''
Function: Create Order
'''
def CreateOrder():
    pass


'''
Function: Submit
'''
def Submit():
    print("Submitted")


'''
Function: Get Menu Items
'''
def GetMenuItems():
    return 'default'


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
creditLabel.pack()
creditEntry.pack()
expirationLabel.pack()
expirationEntry.pack()
cvLabel.pack()
cvEntry.pack()

# add dropdown menu for the menu items
menuLabel = tk.Label(text='Menu Options')
menuItems = GetMenuItems()
default = 'Empty'
menuDropdown = tk.OptionMenu(window, default, *menuItems)
menuLabel.pack()
menuDropdown.pack()

# add submit button
submitButton = tk.Button(text='Submit')
submitButton.bind("<Button-1>", Submit())
submitButton.pack()


window.mainloop()


