from tkinter import Tk , StringVar, ttk
from tkinter import*

root=Tk()
root.title("Distance Converter")
root.geometry('800x300+0+0')
root.configure(background='black')


Tops=Frame(root,width=1000,height=50,bd=16,relief="raise")
Tops.pack(side=TOP)
LeftMainFrame=Frame(root,width=100,height=300,bd=8,relief="raise")
LeftMainFrame.pack(side=LEFT)
RightMainFrame=Frame(root,width=80,height=300,bd=8,relief="raise")
RightMainFrame.pack(side=RIGHT)
#---------------------------------------------------------------------
value0 = StringVar()
convert = DoubleVar()
Distance = DoubleVar()
#-------------------------------------------------------------------------------------
def ConDistance():
    if value0.get() == "Miles to Kilometers":
        convert1 = float(convert.get() * 1.609344)
        convert2 = str('%.1f'%(convert1)),'kilometers'
        Distance.set(convert2)
    elif (value0.get() == "Kilometers to Miles"):
        convert1 = float(convert.get() / 1.609344)
        convert2 = str('%.1f'%(convert1)),'Miles '
        Distance.set(convert2)
    elif (value0.get() == " kilometer to cm"):
        convert1 = float(convert.get() *100000 )
        convert2 = str('%.1f'%(convert1)),'cm '
        Distance.set(convert2)
 
    elif (value0.get() == "Nautical mile to cm"):
        convert1 = float(convert.get() *185200)
        convert2 = str('%.1f'%(convert1)),'cm '
        Distance.set(convert2)
    elif (value0.get() == "Nautical mile to miles"):
        convert1 = float(convert.get() *1.151)
        convert2 = str('%.1f'%(convert1)),'miles '
        Distance.set(convert2)
    
#--------------------------------------------------------------------------------------------
def Reset(): 
    value0.set("")
    convert.set("0.0")
    Distance.set("0.0")


#-------------------------------------------------------------------------------------------------------------
lblMiles=Label(Tops,font=('arial',30 ,'bold'),text='Distance Converter',padx=2,
               pady=2,bd=2, fg="black",)
lblMiles.grid(row=0,column=2 ,sticky=W)
#-----------------------------------------------------------------------------------------------------------------
box = ttk.Combobox(LeftMainFrame,textvariable=value0,state='readonly',font=('arial',14,'bold'),width=25)
box ['values']=('','Miles to Kilometers','Kilometers to Miles',' kilometer to cm','Nautical mile to miles','Nautical mile to cm')
box.current(0)
box.grid(row=0,column=0)

#-----------------------------------------------------------------------------------------------------------------
EntMils=Entry(LeftMainFrame,font=('arial',20,'bold'),textvariable=convert, bd=2, width=31, justify='center')
EntMils.grid(row=1,column=0 )
lblconvert=Label(LeftMainFrame,font=('arial',20 ,'bold'), textvariable=Distance,padx=2,width=27,
               pady=2,bd=2, bg="white",relief='sunken')
lblconvert.grid(row=2,column=0 )


lblSpace=Label(LeftMainFrame,font=('arial',20 ,'bold'),padx=2,width=27,
               pady=2,bd=2,relief='sunken')
lblSpace.grid(row=3,column=0 )

#------------------------------------------------------------------------------------               

btnConvert = Button(RightMainFrame, text="Convert",padx=2, pady=2, bd=2, fg="black",
                    font=('arial',20 ,'bold'),width=20,height=0,command=ConDistance ).grid(row=1,column=0)
btnReset = Button(RightMainFrame, text="Reset",padx=2, pady=2, bd=2, fg="black",
                    font=('arial',20 ,'bold'),width=20,height=0,command=Reset ).grid(row=2,column=0)


root.mainloop()
