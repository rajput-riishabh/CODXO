#####################################################   Currency Converter without API  ############################################################################################################################

# # Featching the exchange rate data from exchange_rate.txt file
# with open("exchange_rate.txt") as rates:
#     country_rate= rates.readlines()

# # Create an exchange Rate Dictionary from exchange rate txt file
# exchange_rates = {}
# for rate in country_rate:
#     country_data=rate.split("=")
#     exchange_rates[country_data[0]]=float(country_data[1])
    
# # print(exchange_rates)

# # Create a function that will exchange the currencies 

# def convert_currency(amount, from_currency, to_currency):

#     # Check if the currencies are valid
#     if from_currency not in exchange_rates or to_currency not in exchange_rates:
#         return "Invalid Currency"
    
#     # Convert the amount to INR if from_currency is not INR
#     if from_currency != 'INR':
#         amount_inr = amount / exchange_rates[from_currency]
#     else:
#         amount_inr = amount
    
#     # Convert INR amount to the target currency
#     if to_currency != 'INR':
#         converted_amount = amount_inr * exchange_rates[to_currency]
#     else:
#         converted_amount = amount_inr
    
#     return converted_amount


# # Asking For Input From The User

# amount = float(input("Please Enter the Amount To Be Converted:: "))
# from_currency = input("Enter the currency you want to convert from:: ").upper()
# to_currency = input("Enter the currency you want to convert to:: ").upper()

# # calling the converter function
# converted_amount = convert_currency(amount, from_currency, to_currency)
# #print the conclusion
# print('{0} {1} is equal to {2:.2f} {3}'.format(amount,from_currency,converted_amount,to_currency))


#####################################################   Currency Converter with API  ############################################################################################################################


# import requests  #import the desired library

# # Create a function that will exchange the currencies 
# def convert_currency(amount, from_currency, to_currency):
#     # API link 
#     url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    
#     # Make a GET request to the API
#     response = requests.get(url)
    
#     # Check if the request was successful
#     if response.status_code == 200:
#         data = response.json()
#         exchange_rate = data['rates'][to_currency]
#         converted_amount = amount * exchange_rate
#         return converted_amount
#     else:
#         return None


# amount = float(input("Please Enter the Amount To Be Converted::"))
# from_currency = input("Enter the currency you want to convert from (e.g.INR, USD, EUR)::  ").upper()
# to_currency = input("Enter the currency you want to convert to (e.g.INR, USD, EUR):: ").upper()

# converted_amount = convert_currency(amount, from_currency, to_currency)

# if converted_amount == None:
#     print("Currency conversion failed or Invalid currency.")
# else:
#     print('{0} {1} is equal to {2:.2f} {3}'.format(amount,from_currency,converted_amount,to_currency))



##################################################### Currency Converter with API and GUI  ############################################################################################################################

# importing required libraries
import requests
from tkinter import ttk
from tkinter import*

col1="#808080"

# Create a function that will exchange the currencies 
def convert():
    amount = float(amount_entry.get().upper()) #fetching input values from input fields using .get() method 
    from_currency = home_entry.get().upper()
    to_currency = conversion_entry.get().upper()
    
    # API link
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    # Make a GET request to the API
    response = requests.get(url)
    
    if response.status_code == 200: ## Check if the request was successful
        data = response.json()
        exchange_rate = data['rates'][to_currency]
        converted_amount = amount * exchange_rate
        converted_entry.insert(0,f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        converted_entry.insert(0,"Currency conversion failed or Invalid currencies.")

# defining the clear() function to clear the input fields
def clear():
    amount_entry.delete(0,END)
    home_entry.delete(0,END)
    conversion_entry.delete(0,END)
    converted_entry.delete(0,END)
     

# creating a gui window
window = Tk()
window.geometry("400x600")
window.title("Currency Converter")
window.resizable(height=True,width=True)

  



curr_notebook=ttk.Notebook(window)
curr_notebook.pack(pady=5)

conversion_frame=Frame(curr_notebook,width=480,height=480, bg="#808080") 
curr_notebook.add(conversion_frame, text="CONVERT YOUR CURRENCIES HERE")

home = LabelFrame(conversion_frame, text="FROM CURRENCY")
home.pack(pady=10)

conversion_label=Label(home,text="currency to convert from...")
conversion_label.pack(pady=5)

home_entry=Entry(home, font=("helvetica",24))
home_entry.pack(pady=5,padx=5,)

conversion=LabelFrame(conversion_frame,text="TO CURRENCY")
conversion.pack(pady=10)


conversion_label=Label(conversion,text="currency to convert to...")
conversion_label.pack(pady=5)

conversion_entry=Entry(conversion,font=("helvetica",24))
conversion_entry.pack(pady=5,padx=5)


button_frame=Frame(conversion_frame, bg="#808080")
button_frame.pack(pady=10)

amount_lable=LabelFrame(conversion_frame,text="amount to convert")
amount_lable.pack(pady=10)

amount_entry=Entry(amount_lable,font=("helvetica",24))
amount_entry.pack(pady=5,padx=5)

convert_button=Button(amount_lable,text="convert",command=convert)
convert_button.pack(pady=10)

converted_label=LabelFrame(conversion_frame,text="converted currency")
converted_label.pack(pady=10)

converted_entry=Entry(converted_label,font=("helvetica",24),bd=0,width=20)
converted_entry.pack(pady=5,padx=10)

clear_button=Button(conversion_frame, text="clear",command=clear, width=20)
clear_button.pack(pady=10,padx=10)


window.mainloop()