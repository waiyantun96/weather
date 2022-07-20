from cgitb import text
# import imp
import tkinter as tk
from tkinter.ttk import Label
import requests
from tkinter import *

window = tk.Tk()
window.geometry('600x600')
# window.resizable(False,False)

window.title("Weather App")
window.grid_columnconfigure(0, weight=1)


    # print(choice)

countries = ['Bahamas','Canada', 'Cuba','United States','New York','Myanmar','Thailand']

welcome_label = tk.Label(window,
                        text='Select Your City Name',
                        font=('Helvetica', 15))
welcome_label.grid(row=0, column=0, sticky='N', padx=20 ,pady=10)


def display_selected():
    variable.get()

variable = StringVar()
variable.set(countries[3])
dropdown = OptionMenu(
    window,
    variable,
    *countries,
    command=display_selected
)
dropdown.grid(row=2,column=0, padx=40, pady=10)

def some_one():
    if variable.get():
        user_input = variable.get()
        params = {
            'access_key': '8782b9c9be74f9e666638bddb580b858',
            'query': user_input
            }
        response = requests.get('http://api.weatherstack.com/current',
                                params)
        text_response = response.json()
    else:
        text_response = "You don't Add city name"
    
    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response['current']['temperature'])
    textwidget.grid(row=4, column=0,padx=10,pady=30)

check_button = tk.Button(text='Check Weather', command=some_one)
check_button.grid(row=3,column=0 , padx=40, pady=10)


if __name__ == "__main__":
    window.mainloop()