import tkinter as tk
from tkinter import font
from tkinter.ttk import Style
from encryptDecrypt import machine

encDecTxt = ''
    
def Encode(mail, result, cnvs):
    global encDecTxt
    encDecTxt = machine(mail.get(0.0, 100000000000.0).rstrip("\n"), 'E')
    result.delete(0.0, 100000000000000.0)
    result.insert(0.0, encDecTxt)

def Decode(mail, result, cnvs):
    global encDecTxt
    encDecTxt = machine(mail.get(0.0, 100000000000.0).rstrip("\n"), 'D')
    result.delete(0.0, 100000000000000.0)
    result.insert(0.0, encDecTxt)

def GUI():
    top = tk.Tk()
    top.title("Encrypt-Decrypt")
    top.resizable(0,0)

    cnvs = tk.Canvas(top, highlightthickness = 2, highlightbackground = "black", bg = "#ffff99", height = 720, width = 1080)

    cnvs.create_rectangle(100, 30, 980, 700, width=1.5)
    cnvs.create_rectangle(150 , 10, 930, 50, width=1.5, fill = "#33cc33")

    headFont = font.Font(family = 'Orator Std', weight = "bold", size = 23)
    cnvs.create_text(540, 30, font = headFont, text = "Encryption Decryption")

    subHead01 = font.Font(family = 'Orator Std', weight = "bold", size = 15)

    cnvs.create_rectangle(130, 80, 950, 350, width=1.5)
    cnvs.create_rectangle(145, 90, 315, 120, width=1.5, fill="#33cc33")

    cnvs.create_text(230, 105, font=subHead01, text="Enter Message")

    inpout_font = font.Font(family='@Kozuka Gothic Pro H', weight = 'bold', size = 10)
    
    mail = tk.Text(cnvs, font=inpout_font)
    cnvs.create_window(540, 235, height = 200, width = 800, window=mail)

    btnFont = font.Font(family='Ubuntu Medium', weight = 'bold', size = 10)

    result = tk.Text(cnvs, font=inpout_font)

    enc_btn = tk.Button(cnvs, text = "Encode", font=btnFont, bg='#1a8cff', command = lambda : Encode(mail, result, cnvs))
    dec_btn = tk.Button(cnvs, text = "Decode", font=btnFont, bg='#ff3300', command = lambda : Decode(mail, result, cnvs))
    enc_btn.place(x = 450, y = 360)
    dec_btn.place(x = 550, y = 360)

    cnvs.create_window(540, 535, height = 275, width = 800, window=result)

    cnvs.pack()
    top.mainloop()

if __name__ == "__main__":
    GUI()
