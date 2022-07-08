from tkinter import *
import math


def main_window_appearance_en():
    start_window.destroy()


    def exit_app():
        exit()


    def result_window_en():
        x = textx.get(1.0, 'end-1c').lower()

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        encrypted_message = ''

        shiftx = int(shift_amount.get()) % 26


        for char in x:
            if str(char) in alphabet:
                position = alphabet.index(char)
                new_position = int(position) + shiftx
                encrypted_message += alphabet[new_position]
            else:
                encrypted_message += str(char)

        main_window.destroy()

        resultscreen = Tk()
        width = 545
        height = 335
        screenwidth = resultscreen.winfo_screenwidth()
        screenheight = resultscreen.winfo_screenheight()
        resultscreen.geometry(
            f"{width}x{height}+{math.floor((screenwidth / 2) - (width / 2))}+{math.floor((screenheight / 2) - (height / 2) - 30)}")

        resultscreen.title("Rosetta 2.1")

        icon = PhotoImage(file='data\\icon.png')
        resultscreen.iconphoto(True, icon)

        resultscreen.config(bg='#000000')

        resultscreen.resizable(0, 0)

        result = Frame(resultscreen, bg='#000000', bd=7, relief=GROOVE)
        result.pack(pady=5, padx=5)

        label = Label(result, text='The Encoded Message', font=('Constantia', 18), fg='#00ffff', bg='#000000')
        label.pack(side=TOP)

        text = Text(result, width=42, height=8, font=('MV Boli', 15))
        text.insert(1.0, encrypted_message)
        text.pack(side=BOTTOM)

        buttonss = Frame(resultscreen, bg='#000000')
        buttonss.pack()

        exit = Button(buttonss, text='Exit', font=('Arial', 16), pady=3, padx=6, fg='#00ffff', bg='#000000',
                        activebackground='#00ffff', activeforeground='#000000', bd=5, relief=GROOVE, command=exit_app)
        exit.pack(padx=60, pady=10) #, side=LEFT)

#        tryagain = Button(buttonss, text='Try Again', font=('Arial', 16), pady=3, padx=6, fg='#00ffff',bg='#000000',
#                          activebackground='#00ffff', activeforeground='#000000', bd=5, relief=GROOVE)
#        tryagain.pack(side=RIGHT, padx=60, pady=10)

        resultscreen.mainloop()



    def result_screen_en():
        main_window.after(250, result_window_en())



    main_window = Tk()

    width = 545
    height = 335
    screenwidth = main_window.winfo_screenwidth()
    screenheight = main_window.winfo_screenheight()
    main_window.geometry(f"{width}x{height}+{math.floor((screenwidth / 2) - (width / 2))}+{math.floor((screenheight / 2) - (height / 2) - 30)}")

    main_window.title("Rosetta 2.1")

    icon = PhotoImage(file='data\\icon.png')
    main_window.iconphoto(True, icon)

    main_window.config(bg='#000000')

    main_window.resizable(0,0)

    all = Frame(main_window, bg='#000000', bd=0)
    all.pack(pady=5, padx=5)

    message = Frame(all, bg='#000000', bd=7, relief=GROOVE)
    message.pack(pady=5, padx=5)

    label = Label(message, text='Type Your Message', font=('Constantia', 18), fg='#00ffff', bg='#000000')
    label.pack(side=TOP)

    textx = Text(message, width=42, height=8, font=('MV Boli', 15))
    textx.pack(side=BOTTOM)

    shifting = Frame(all, bg='#000000', bd=7, relief=GROOVE)
    shifting.pack(pady=5, padx=5, side=LEFT)

    label = Label(shifting, text='Shift Number:', font=('Constantia', 15), fg='#00ffff', bg='#000000')
    label.pack(side=LEFT)

    shift_amount = Entry(shifting, font=('Gadugi', 15), width=23)
    shift_amount.pack(side=RIGHT)

    buttons = Frame(all, bg='#000000')
    buttons.pack(side=RIGHT, pady=5, padx=5)

    submit = Button(buttons, text='Encode', font=('Constantia', 15), fg='#00ffff', bg='#000000', padx=9, pady=0,
                    activebackground='#00ffff', activeforeground='#000000', bd=7, relief=GROOVE, command=result_screen_en)
    submit.pack()


def main_window_appearance_de():
    start_window.destroy()

    def exit_app():
        exit()

    def result_window_de():

        x = textxx.get(1.0, 'end-1c').lower()

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        encrypted_message = ''

        shiftx = int(shift_amount.get()) % 26

        shiftx *= -1

        for char in x:
            if str(char) in alphabet:
                position = alphabet.index(char)
                new_position = int(position) + shiftx
                encrypted_message += alphabet[new_position]
            else:
                encrypted_message += str(char)

        main_window.destroy()

        resultscreen = Tk()
        width = 545
        height = 335
        screenwidth = resultscreen.winfo_screenwidth()
        screenheight = resultscreen.winfo_screenheight()
        resultscreen.geometry(
            f"{width}x{height}+{math.floor((screenwidth / 2) - (width / 2))}+{math.floor((screenheight / 2) - (height / 2) - 30)}")

        resultscreen.title("Rosetta 2.1")

        icon = PhotoImage(file='data\\icon.png')
        resultscreen.iconphoto(True, icon)

        resultscreen.config(bg='#000000')

        resultscreen.resizable(0, 0)

        result = Frame(resultscreen, bg='#000000', bd=7, relief=GROOVE)
        result.pack(pady=5, padx=5)

        label = Label(result, text='The Decoded Message', font=('Constantia', 18), fg='#00ffff', bg='#000000')
        label.pack(side=TOP)

        text = Text(result, width=42, height=8, font=('MV Boli', 15))
        text.insert(1.0, encrypted_message)
        text.pack(side=BOTTOM)

        buttonss = Frame(resultscreen, bg='#000000')
        buttonss.pack()

        exit = Button(buttonss, text='Exit', font=('Arial', 16), pady=3, padx=6, fg='#00ffff', bg='#000000',
                      activebackground='#00ffff', activeforeground='#000000', bd=5, relief=GROOVE, command=exit_app)
        exit.pack(side=LEFT, padx=60, pady=10)

#        tryagain = Button(buttonss, text='Try Again', font=('Arial', 16), pady=3, padx=6, fg='#00ffff', bg='#000000',
#                          activebackground='#00ffff', activeforeground='#000000', bd=5, relief=GROOVE)
#        tryagain.pack(side=RIGHT, padx=60, pady=10)

        resultscreen.mainloop()

    def result_screen_de():
        main_window.after(250, result_window_de)

    main_window = Tk()

    width = 545
    height = 335
    screenwidth = main_window.winfo_screenwidth()
    screenheight = main_window.winfo_screenheight()
    main_window.geometry(f"{width}x{height}+{math.floor((screenwidth / 2) - (width / 2))}+{math.floor((screenheight / 2) - (height / 2) - 30)}")

    main_window.title("Rosetta 2.1")

    icon = PhotoImage(file='data\\icon.png')
    main_window.iconphoto(True, icon)

    main_window.config(bg='#000000')

    main_window.resizable(0,0)

    all = Frame(main_window, bg='#000000', bd=0)
    all.pack(pady=5, padx=5)

    message = Frame(all, bg='#000000', bd=7, relief=GROOVE)
    message.pack(pady=5, padx=5)

    label = Label(message, text='Type Your Message', font=('Constantia', 18), fg='#00ffff', bg='#000000')
    label.pack(side=TOP)

    textxx = Text(message, width=42, height=8, font=('MV Boli', 15))
    textxx.pack(side=BOTTOM)

    shifting = Frame(all, bg='#000000', bd=7, relief=GROOVE)
    shifting.pack(pady=5, padx=5, side=LEFT)

    label = Label(shifting, text='Shift Number:', font=('Constantia', 15), fg='#00ffff', bg='#000000')
    label.pack(side=LEFT)

    shift_amount = Entry(shifting, font=('Gadugi', 15), width=23)
    shift_amount.pack(side=RIGHT)

    buttons = Frame(all, bg='#000000')
    buttons.pack(side=RIGHT, pady=5, padx=5)

    submit = Button(buttons, text='Decode', font=('Constantia', 15), fg='#00ffff', bg='#000000', padx=9, pady=0,
                    activebackground='#00ffff', activeforeground='#000000', bd=7, relief=GROOVE, command=result_screen_de)
    submit.pack()


def encodescreen():
    start_window.after(250, main_window_appearance_en)


def decodescreen():
    start_window.after(250, main_window_appearance_de)


start_window = Tk()

width = 545
height = 335
screenwidth = start_window.winfo_screenwidth()
screenheight = start_window.winfo_screenheight()
start_window.geometry(
    f"{width}x{height}+{math.floor((screenwidth / 2) - (width / 2))}+{math.floor((screenheight / 2) - (height / 2) - 30)}")
start_window.title("Rosetta 2.1")
icon = PhotoImage(file='data\\icon.png')
start_window.iconphoto(True, icon)
start_window.config(bg='#484848')

welcomming = Label(start_window, text='Rosetta 2.1\nAn Encryption Tool', font=('Impact', 20), fg='#00ffff',
                   bg='#000000',
                   bd=7, relief=RAISED, padx=70)
welcomming.pack(pady=20)

choose = Label(start_window, text='# Choose What You Want:', font=('Arial', 15), fg='#00ffff', bg='#484848',
               padx=20)
choose.pack(pady=30)

buttons = Frame(start_window, bg='#484848')
buttons.pack()

encode = Button(buttons, text='Encoding', font=('Arial', 16), pady=3, padx=6, fg='#00ffff', bg='#000000',
                activebackground='#00ffff', activeforeground='#000000', bd=5, relief=GROOVE, command=encodescreen)
encode.pack(side=LEFT, padx=40)

decode = Button(buttons, text='Decoding', font=('Arial', 16), pady=3, padx=6, fg='#00ffff', bg='#000000',
                activebackground='#00ffff', activeforeground='#000000', bd=5, relief=GROOVE, command=decodescreen)
decode.pack(side=RIGHT, padx=40)

start_window.resizable(0, 0)

mainloop()





# BETA Version
# Still Under Development
# Coded & Designed By Mohanad Medhat
