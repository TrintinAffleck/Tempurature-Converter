#Setting booleans to check what temp to convert
game_on = True
while game_on:
    c_to_f: bool = False
    f_to_c: bool = False
    #Making a list for the correct choices for celsius and farenheit
    celsius_list = ['c','C','Celsius','celsius']
    farenheit_list = ['f','F','farenheit','Farenheit']
    def check_int(s: str):
        if s[0] in ('-'):
            return s[1:].isdigit()
        return s.isdigit()

    def play_again():
        again = input("Do you want to restart the program or quit?")
        print("You can type r or q as shorthand")
        if again in ['restart', 'r']:
            game_on = True
        elif again in ['quit','q']:
            game_on = False
            quit()
        else:
            play_again()

    print("\n"*9)
    print("Welcome to my tempurature converter you can use shorthands like f or c for tempurature input.")
    while True:
        choice = input("Pick your tempurature to convert (celsius or farenheit): ")
        if choice.isalpha():
            if choice in celsius_list:
                c_to_f = True
                break
            if choice in farenheit_list:
                f_to_c = True
                break
            else:
                print("Wrong choice.")
                print("Remember no numbers or spaces.")

    if c_to_f:
            celsius = ""
            while True:
                celsius = input("Please enter celsius tempurature:")
                if check_int(celsius):
                    result = (float(celsius) * 9/5) + 32
                    print(round(result,1))
                    play_again()
                    break
                elif not check_int(celsius):
                    print("Please use numbers only!")
                    continue

    if f_to_c:
            while True:
                farenheit = input("Please enter farenheit tempurature:")
                if check_int(farenheit):
                    result =(float(farenheit) - 32 ) / 1.8
                    print(round(result,1))
                    play_again()
                    break
                else:
                    print("Please use numbers only!")
                    continue