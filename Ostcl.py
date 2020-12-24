'''
this is the ostcl sentiment analysis project TE (EXTC)
69 Tikam Madhav
70 Verma Aditi
71 Prasad Pooja
72 Naik Govind 
73 Mishra Nitesh

to use this application
1.enter user name
2.choose image to comment
3.add comment
4.click analyse and you get the result about the comment
5.click save button and your all data is stored in an csv file in same folder
'''

from tkinter import *
#showiamge
from PIL import ImageTk, Image
from tkinter import filedialog

import os#access the files
#sentiment analyse
import nltk
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
#colours
bmg = '#bae6df'
buttfg = '#000000'
buttbg = '#36bcc7'
lebfg = '#000000'
lebbg = bmg
etyfg = '#000000'
etybg = '#49a396'

root = Tk()
root.geometry("620x500")
root.resizable(width=True, height=True)
root.configure(background=bmg)
root.title('OSTCL PROJECT')

#storing results
import pandas as pd
df = pd.DataFrame()

score = []
users = []
images = []
comments = []
cuser = StringVar()
ccomment = StringVar()

def openfn():
    filename = filedialog.askopenfilename(title='open')
    global name
    name= filename[filename.rindex('/')+1:]
    return filename

def open_img():
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.grid(column = 3,row =6)
    global txtEntry
    txtEntry = Entry(root, width= 50,  fg=etyfg,bd =3, bg = etybg,textvariable = ccomment).grid(column = 3,row =8)
    analysisBton = Button(root, text='Analyse', command=analyse,fg = buttfg, bg = buttbg).grid(column = 2,row =10)
    pad81 = Label(root,text = 'Add Comment :',bg = lebbg ,fg = lebfg).grid(column = 2,row =8)

def analyse():
    c = sia.polarity_scores(str(ccomment.get()))['compound']
    if c > 0:
        score.append("Positive")
    elif c == 0:
        score.append("Neutral")
    else:
        score.append("Negative")
    users.append(cuser.get())
    images.append(name)
    comments.append(ccomment.get())
    pad102 = Label(root,text = score[-1]+' Review',bg = lebbg ,fg = lebfg).grid(column = 3,row =10)
    print(cuser.get())
    print(name)
    print(score[-1])

def save():
    df["image"] = images
    df["users"] = users
    df["comment"] = comments
    df["opinion"] = score
    df.to_csv('reviews.csv')
    exit()

#gui
uiuser = Label(root,text = 'Enter user name : ',bg = lebbg ,fg = lebfg).grid(column = 2,row =2)
userEntry = Entry(root, width=15,textvariable  = cuser, fg=etyfg, bg = etybg,bd=3).grid(column = 3,row =2)
OpenBton = Button(root, text='Choose a image to comment', fg = buttfg, bg = buttbg,command=open_img).grid(column = 2,row = 4)
exitbton = Button(root, text='Save and Close',fg = buttfg, bg = buttbg, command=save).grid(column = 3,row =4)

#padding
pad1 = Label(root,text = '         ',bg = bmg ).grid(column = 1,row =1)
pad3 = Label(root,text = '         ',bg = bmg ).grid(column = 1,row =3)
pad5 = Label(root,text = '         ',bg = bmg ).grid(column = 1,row =5)
pad7 = Label(root,text = '         ',bg = bmg ).grid(column = 1,row =7)
pad9 = Label(root,text = '         ',bg = bmg ).grid(column = 1,row =9)

pad2 = Label(root,text = '    ',bg = bmg ).grid(column = 1,row =2)
pad4 = Label(root,text = '    ',bg = bmg ).grid(column = 1,row =4)
pad6 = Label(root,text = '    ',bg = bmg ).grid(column = 1,row =6)
pad8 = Label(root,text = ' ',bg = bmg ).grid(column = 1,row =8)
pad10 = Label(root,text = '   ',bg = bmg ).grid(column = 1,row =10)



root.mainloop()
