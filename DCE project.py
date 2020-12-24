from tkinter import *
import onetimepad
    

#colours
bmg = '#bae6df'
buttfg = '#000000'
buttbg = '#36bcc7'
lebfg = '#000000'
lebbg = bmg
etyfg = '#000000'
etybg = '#49a396'
red = '#ff0000'
blue = '#0000ff'

root = Tk()
root.geometry("620x500")
root.resizable(width=True, height=True)
root.configure(background=bmg)
root.title('DCE PROJECT')

atyp = StringVar()
atyp.set('One Time Pad cypher')

atk = StringVar()
atk.set('Encryption')

atxt = StringVar()

akey = StringVar()
op = '........'

#backend
def oencrypt(string, key):
    cipher = onetimepad.encrypt(string, key)
    print("Encrypted text is :- ")
    print(cipher)
    return cipher



def odecrypt(string, key):
    cipher = onetimepad.decrypt(string, key)
    print("The Decoded message is ")
    return cipher


def cencrypt(string, shift):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    print("The Encrypted message is ")
    print(cipher)
    return cipher

def cdecrypt(string, shift):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher - chr((ord(char) - shift - 65) % 26 + 65)
        else:
            cipher = cipher - chr((ord(char) - shift - 97) % 26 + 97)
    print("The Decoded message is ")
    print(cipher)
    return cipher    

def geret():
    if(atk.get()== "Encryption"):
        if(atyp.get() == "One Time Pad cypher"):
            result = oencrypt(str(atxt.get()), str(akey.get()))
        else:
            result= cencrypt(str(atxt.get()), int(akey.get()))
            
    elif(atk.get()== "Decryption"):
        if(atyp.get() == "One Time Pad cypher"):
            result= odecrypt(str(atxt.get()), str(akey.get()))
       
        else:
            result= cencrypt(str(atxt.get()), int(akey.get()))
    code = Label(root,text = 'Code is: '+ result ,bg = lebbg ,fg = red).grid(column = 3,row =12)



#giu
typLabel = Label(root,text = 'Choose the Technique : ',bg = lebbg ,fg = lebfg).grid(column = 2,row =2)

typ = OptionMenu(root, atyp,  "Caser cypher", "One Time Pad cypher").grid(column = 3,row =2)

tskLabel = Label(root,text = 'Choose the process : ',bg = lebbg ,fg = lebfg).grid(column = 2,row =4)

tsk = OptionMenu(root, atk,  "Encryption", "Decryption").grid(column = 3,row =4)

textLabel = Label(root,text = 'Enter text : ',bg = lebbg ,fg = lebfg).grid(column = 2,row =8)

textEntry = Entry(root, width=20,textvariable  = atxt, fg=etyfg, bg = etybg,bd=3).grid(column = 3,row =8)

keyLabel = Label(root,text = 'Enter key : ',bg = lebbg ,fg = lebfg).grid(column = 2,row =10)

keyEntry = Entry(root, width=20,textvariable  = akey, fg=etyfg, bg = etybg,bd=3).grid(column = 3,row =10)


instruct = Label(root,text = 'Key Length:   \n  for Caser = 1                       \nfor OTP < massage length ',bg = lebbg ,fg = blue).grid(column = 3,row =20)


OpenBton = Button(root, text='Generate code', fg = buttfg, bg = buttbg, command=geret).grid(column = 2,row = 12)



#padding
pad1 = Label(root,text = '         ',bg = bmg ).grid(column = 1,row =1)
pad3 = Label(root,text = '         ',bg = bmg ).grid(column = 1,row =3)
pad5 = Label(root,text = '         ',bg = bmg ).grid(column = 1,row =5)
pad7 = Label(root,text = '         ',bg = bmg ).grid(column = 1,row =7)
pad9 = Label(root,text = '         ',bg = bmg ).grid(column = 1,row =9)
pad9 = Label(root,text = '         ',bg = bmg ).grid(column = 1,row =11)
pad9 = Label(root,text = '         ',bg = bmg ).grid(column = 1,row =13)

pad2 = Label(root,text = '',bg = bmg ).grid(column = 1,row =2)
pad4 = Label(root,text = '',bg = bmg ).grid(column = 1,row =4)
pad6 = Label(root,text = '',bg = bmg ).grid(column = 1,row =6)
pad8 = Label(root,text = '',bg = bmg ).grid(column = 1,row =8)
pad10 = Label(root,text = '',bg = bmg ).grid(column = 1,row =10)



root.mainloop()
