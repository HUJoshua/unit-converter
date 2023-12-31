import customtkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import datetime as dt
from CTkListbox import *

# system settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

# app frame
user = customtkinter.CTk()
user.title("Measurement Converter")
user.geometry('750x500')
user.config(bg="#020a24")

title_label = customtkinter.CTkLabel(user, text="Unit Converter", font=('Arial', 32, 'bold'), text_color="#fff", bg_color="#020a24")
title_label.place(x=290,y=20)

# unit options
unit_options = ["Length", "Mass", "Volume", "Area", "Speed", "Data Storage", "Force", "Pressure", "Heat", "Density"]

length_options = ["meters", "millimeters", "centimeters", "kilometers", "feet", "miles", "yards", "inches"]
mass_options = ["grams", "kilograms", "milligrams", "tons", "pounds", "ounces"]
volume_options = ["liters", "cubic meters", "cubic centimeters", "milliliters", "gallons", "fluid ounces"]
area_options = ["square meters", "square kilometers", "square centimeters", "square millimeters", "acres", "hectares", "square miles", "square feet"]
speed_options = ["meters per second", "kilometers per hour", "miles per hour"]
data_storage_options = ["Bytes", "bits", "kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes"]
force_options = ["Newtons", "Dynes", "Poundal", "Gram Force", "Pound Force", "Ton Force", "Ounce Force", "Sthene", "Kilogram Force"]
pressure_options = ["Pascal", "Bar", "Technical Atmosphere", "Standard Atmosphere", "Torr", "Pounds per sq. Inch"]
heat_options = ["Joules", "Calories", "kilocalories", "BTU"]
density_options = ["kg per cubic meter", "grams per ml", "metric tons per cubic meter", "kg per cubic cm", "pounds per cubic foot", "grams per cubic meter", "ounces per cubic inch", "ounces per cubic foot", "pounds per cubic inch"]

variable1 = StringVar()
variable2 = StringVar()
variable3 = StringVar()
#converted_value = float()

# history

def add_to_history(value, timestamp=True):
    if timestamp:
        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        value = f"{timestamp} - {value}"
    history_listbox.insert(tk.END, value)

file_path = "history.txt" 

def save_history():
    with open(file_path, "w") as file:
        for item in history_listbox.get(0, tk.END):
            file.write(item + "\n")

def load_history():
    try:
        with open(file_path, "r") as file:
            for line in file:
                add_to_history(line.strip(), timestamp=False)
    except FileNotFoundError:
        pass
        #print("History file not found.")

def on_exit():
    response = messagebox.askquestion("Confirm Exit", "Are you sure you want to exit?")
    if response == "yes":
        save_history()
        user.destroy()


# search history
var = StringVar()

def search_history(*args):
    search_term = var.get()
    history_listbox.delete(0, tk.END)
    for item in all_history:
        if search_term.lower() in item.lower():
            history_listbox.insert(tk.END, item)

# copy to clipboard
#def copy_to_clipboard():
    #selected_item = result_label.cget("text")
    #pyperclip.copy(selected_item)

def convert():
    length_factors = {"meters":1.0, "millimeters":0.001, "centimeters":0.01, "kilometers":1000.0, "feet":0.3048, "miles":1609.344, "yards":0.9144, "inches":0.0254}
    mass_factors = {"grams":1.0, "kilograms":1000.0, "milligrams":0.001, "tons":1000000.0, "pounds":453.592, "ounces":28.3495}
    volume_factors = {"liters":1.0, "cubic meters":1000.0, "cubic centimeters":0.001, "milliliters":0.001, "gallons":3.785, "fluid ounces":0.02957}
    area_factors = {"square meters":1.0, "square kilometers":1000000.0, "square centimeters":0.0001, "square millimeters":0.000001, "acres":4046.856, "hectares":10000, "square miles":2590000.0, "square feet":0.0929}
    speed_factors = {"meters per second":1.0, "kilometers per hour":3.6, "miles per hour":0.447}
    data_storage_factors = {"Bytes":1.0, "bits":0.125, "kilobytes":1024.0, "Megabytes":1048576, "Gigabytes":1073741824, "Terabytes":1099511627776, "Petabytes":1125899906842624}
    force_factors = {"Newtons":1.0, "Dynes":0.00001, "Poundal":0.1382, "Gram Force":0.00980665, "Pound Force":4.448222, "Ton Force":9806.65, "Ounce Force":0.278014, "Sthene":1000, "Kilogram Force":9.80665}
    pressure_factors = {"Pascal":1.0, "Bar":100000, "Technical Atmosphere":98066.5, "Standard Atmosphere":101325, "Torr":133.322368, "Pounds per sq. Inch":6894.757}
    heat_factors = {"Joules":1.0, "Calories":4.184, "kilocalories":4184, "BTU":1055.056}
    density_factors = {"kg per cubic meter":1.0, "grams per ml":1000, "metric tons per cubic meter":1000, "kg per cubic cm":1000000, "pounds per cubic foot":16.018463, "grams per cubic meter":0.001, "ounces per cubic inch":1729.994, "ounces per cubic foot":1.001153, "pounds per cubic inch":27679.90471}
    try:
        if variable1.get() == "Length":
            #first convert to meters
            meters = float(input_value_entry.get()) * length_factors[variable2.get()]
            #convert from meters to the desired unit
            converted_value = meters / length_factors[variable3.get()]
        elif variable1.get() == "Mass":
            #first convert to gram
            gram = float(input_value_entry.get()) * mass_factors[variable2.get()]
            #convert from grams to the desired unit
            converted_value = gram / mass_factors[variable3.get()]
        elif variable1.get() == "Volume":
            #first convert to liters
            liters = float(input_value_entry.get()) * volume_factors[variable2.get()]
            #convert from liters to the desired unit
            converted_value = liters / volume_factors[variable3.get()]
        elif variable1.get() == "Area":
            #first convert to square_meter
            square_meter = float(input_value_entry.get()) * area_factors[variable2.get()]
            #convert from square_meter to the desired unit
            converted_value = square_meter / area_factors[variable3.get()]
        elif variable1.get() == "Speed":
            #first convert to m/s
            meters_per_second = float(input_value_entry.get()) * speed_factors[variable2.get()]
            #convert from m/s to the desired unit
            converted_value = meters_per_second / speed_factors[variable3.get()]
        elif variable1.get() == "Data Storage":
            #first convert to bytes
            bytes = float(input_value_entry.get()) * data_storage_factors[variable2.get()]
            #convert from bytes to the desired unit
            converted_value = bytes / data_storage_factors[variable3.get()]
        elif variable1.get() == "Force":
            #first convert to newton
            newton = float(input_value_entry.get()) * force_factors[variable2.get()]
            #convert from newton to the desired unit
            converted_value = newton / force_factors[variable3.get()]
        elif variable1.get() == "Pressure":
            #first convert to pascal
            pascal = float(input_value_entry.get()) * pressure_factors[variable2.get()]
            #convert from pascal to the desired unit
            converted_value = pascal / pressure_factors[variable3.get()]
        elif variable1.get() == "Heat":
            #first convert to joules
            joules = float(input_value_entry.get()) * heat_factors[variable2.get()]
            #convert from joules to the desired unit
            converted_value = joules / heat_factors[variable3.get()] 
        else:
            #first convert to kg/cubic meter
            kg_per_m3 = float(input_value_entry.get()) * density_factors[variable2.get()]
            #convert from kg/cubic meter to the desired unit
            converted_value = kg_per_m3 / density_factors[variable3.get()]
        result = f'{input_value_entry.get()} {variable2.get()} to {variable3.get()}'
        result_label.configure(text=f'{input_value_entry.get()} {variable2.get()} = {converted_value:.6f} {variable3.get()}')
        #pyperclip.copy(result_label)
        # Add the calculation to the history listbox 
        add_to_history(result, timestamp=True)
        save_history()
        update_all_history()
    except:
        messagebox.showerror('Error', 'Please enter a valid value!') 
        #pass

xscrollbar = Scrollbar(user, orient=HORIZONTAL)
yscrollbar = Scrollbar(user, orient=VERTICAL)

history_listbox = tk.Listbox(user, width=40, height=15, yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)

yscrollbar.config(command=history_listbox.yview)
xscrollbar.config(command=history_listbox.xview)

yscrollbar.place(in_=history_listbox, relx=1.0, relheight=1.0, bordermode="outside")
xscrollbar.place(in_=history_listbox, relx=0.0, rely=1.0, relwidth=1.0, bordermode="outside")

#yscrollbar.place(x=210, y=10, height=150)
#xscrollbar.place(x=10, y=160, width=200)

search_entry = tk.Entry(user, width=30, textvariable=var)
search_entry.insert(0, "Search history")

def clear_default_text(event):
    if search_entry.get() == "Search history":
        search_entry.delete(0, tk.END)

search_entry.bind("<FocusIn>", clear_default_text)

def update_all_history():
    all_history.clear()
    for item in history_listbox.get(0, tk.END):
        all_history.append(item)

all_history = []

for item in history_listbox.get(0, tk.END):
    all_history.append(item)

#search_entry.bind("<<KeyRelease>>", search_history)

# Load the history when the program starts   
load_history() 

user.protocol("WM_DELETE_WINDOW", on_exit)

def clear():
    input_value_entry.delete(0, END)
    result_label.configure(text="")
    unit_options.set("")
    input_options.set("")
    output_options.set("")
    
# adding labels

unit_label = customtkinter.CTkLabel(user, text="Units", font=('Arial', 18), text_color="#fff", bg_color="#020a24")
unit_label.place(x=60,y=130)

unit_options = customtkinter.CTkComboBox(user, text_color="#000", state="readonly", fg_color="#fff", dropdown_hover_color="gold", values=unit_options, variable=variable1, width=180)
unit_options.place(x=60,y=160)

input_label = customtkinter.CTkLabel(user, text="From", font=('Arial', 18), text_color="#fff", bg_color="#020a24")
input_label.place(x=60,y=230)

input_options = customtkinter.CTkComboBox(user, text_color="#000", state="readonly", fg_color="#fff", dropdown_hover_color="gold", variable=variable2, width=180)
input_options.place(x=60,y=260)

output_label = customtkinter.CTkLabel(user, text="To", font=('Arial', 18), text_color="#fff", bg_color="#020a24")
output_label.place(x=270,y=230)

output_options = customtkinter.CTkComboBox(user, text_color="#000", state="readonly", fg_color="#fff", dropdown_hover_color="gold", variable=variable3, width=180)
output_options.place(x=270,y=260)

input_value_label = customtkinter.CTkLabel(user, text="Value", font=('Arial', 18), text_color="#fff", bg_color="#020a24")
input_value_label.place(x=270,y=130)

input_value_entry = customtkinter.CTkEntry(user, text_color="#000", fg_color="#fff", width=180)
input_value_entry.place(x=270,y=160)

convert_button = customtkinter.CTkButton(user, text="Convert", font=('Arial', 18), command=convert, text_color="#000", fg_color="#fff", hover_color="gold", bg_color="#020a24", corner_radius=10, width=150)
convert_button.place(x=60,y=330)

result_label = customtkinter.CTkLabel(user, text = "", font=('Arial', 16), text_color="#fff", bg_color="#020a24",)
result_label.place(x=20,y=380)

clear_button = customtkinter.CTkButton(user, text="Clear", font=('Arial', 18), command=clear, text_color="#000", fg_color="#fff", hover_color="gold", bg_color="#020a24", corner_radius=10, width=150)
clear_button.place(x=60,y=430)

def show_history_listbox():
    history_listbox.place(x=480,y=100)
    show_history.configure(text = "Hide History", command=hide_history_listbox)
    search_entry.place(x=520,y=430, height=28)

def hide_history_listbox():
    history_listbox.place_forget()
    show_history.configure(text = "Show History", command=show_history_listbox)
    search_entry.place_forget()
    
show_history = customtkinter.CTkButton(user, text="Show History", font=('Arial', 18), text_color="#000", fg_color="#fff", command=show_history_listbox, hover_color="gold", bg_color="#020a24", corner_radius=10, width=150)
show_history.place(x=290,y=430)

# populate the input and output units boxes
def load_options(*args):
    if variable1.get() == "Length":
        input_options.configure(values=length_options)
        output_options.configure(values=length_options)
        input_options.set("meters")
        output_options.set("centimeters")
    elif variable1.get() == "Mass":
        input_options.configure(values=mass_options)
        output_options.configure(values=mass_options)
        input_options.set("kilograms")
        output_options.set("grams")
    elif variable1.get() == "Volume":
        input_options.configure(values=volume_options)
        output_options.configure(values=volume_options)
        input_options.set("liters")
        output_options.set("milliliters")
    elif variable1.get() == "Area":
        input_options.configure(values=area_options)
        output_options.configure(values=area_options)
        input_options.set("square meters")
        output_options.set("square feet")
    elif variable1.get() == "Speed":
        input_options.configure(values=speed_options)
        output_options.configure(values=speed_options)
        input_options.set("meters per second")
        output_options.set("kilometers per hour")
    elif variable1.get() == "Data Storage":
        input_options.configure(values=data_storage_options)
        output_options.configure(values=data_storage_options)
        input_options.set("Bytes")
        output_options.set("Megabytes")
    elif variable1.get() == "Force":
        input_options.configure(values=force_options)
        output_options.configure(values=force_options)
        input_options.set("Newtons")
        output_options.set("Kilogram Force")
    elif variable1.get() == "Pressure":
        input_options.configure(values=pressure_options)
        output_options.configure(values=pressure_options)
        input_options.set("Pascal")
        output_options.set("Standard Atmosphere")
    elif variable1.get() == "Heat":
        input_options.configure(values=heat_options)
        output_options.configure(values=heat_options)
        input_options.set("Joules")
        output_options.set("Calories")        
    else:
        input_options.configure(values=density_options)
        output_options.configure(values=density_options)
        input_options.set("kg per cubic meter")
        output_options.set("grams per ml")

# load input and output options
variable1.trace("w", load_options)

var.trace("w", search_history)



# memoize function to cache

#def memoize(func):
    #cache = {}

    # inner wrapper function to store the data in the cache
    #def wrapper(*args):
        #if args in cache:
            #return cache[args]
        #else:
            #cache_data = func(*args)
            #cache[args] = cache_data
            #return cache_data
    #return wrapper

# memoized function to get converted value
#@memoize
#def convert_cached():
    #result_label.configure(text=f'{input_value_entry.get()} {variable2.get()} = {converted_value:.4f} {variable3.get()}')
    #result_label.configure(text="")

#start_time = time.time()
#messagebox.ABORT()
#convert()
#print('time taken (normal function):', time.time() - start_time)

#start_time = time.time()
#convert_cached()
#print('time taken (memoized function):', time.time() - start_time)

# run app
user.mainloop()

