import pdb

#Setting booleans to check what temp to convert
c_to_f: bool = False
f_to_c: bool = False
#Making a list for the correct choices for celsius and farenheit
celsius_list = ['c','C','Celsius','celsius']
farenheit_list = ['f','F','farenheit','Farenheit']
choice = input("Pick your tempurature to convert (celsius or farenheit): ")

if choice.isalpha:
    if choice in celsius_list:
        c_to_f = True
    if choice in farenheit_list:
        f_to_c = True
    else:
        print("Wrong choice.")
        #print(f"Tempurature choices are {farenheit_list} or {celsius_list}")
        choice = input("Pick your tempurature to convert (celsius or farenheit): ")
    pdb.set_trace()
elif choice.isnum:
    print("Remember no numbers or spaces.")
    choice = input("Pick your tempurature to convert (celsius or farenheit): ")


if c_to_f:
    celsius = input("Please enter celsius tempurature:")
if f_to_c:
    farenheit = input("Please enter farenheit tempurature to convert")