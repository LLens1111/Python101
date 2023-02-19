from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() # หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดโปรแกรม

L1 = Label(GUI,text='ประกาศงบQ465',font=('Angsana New',30),fg='green')
L1.place(x=150,y=20)
###################
def Button2():
    text = 'BH,GULF,LPN,PTT,SC,SVI,THANI'
    messagebox.showinfo('บริษัท@16FEB66',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='16FEB66',command=Button2)
B2.pack(ipadx=20,ipady=20)


def Button3():
    text = 'CPNREIT,HENG,PSH,STA,STGT,TFM,TIDLOR'
    messagebox.showinfo('บริษัท@21FEB66',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=80)
B3 = ttk.Button(FB1,text='21FEB66',command=Button3)
B3.pack(ipadx=20,ipady=20)


def Button4():
    text = 'BOFFICE,BRI,B-WORK,CHG,CPF,DDD,EGCO,IVL,LHSC,MICRO,MOSHIMSPRCMSPRIME,TPRIME,TVO,VIBHA,WHART'
    messagebox.showinfo('บริษัท@24FEB66',text)

FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=100,y=80)
B4 = ttk.Button(FB1,text='24FEB66',command=Button4)
B4.pack(ipadx=20,ipady=20)

###################
def Button5():
    text = 'GLOBAL,INETREIT,PTTGC,SGC,SINGER'
    messagebox.showinfo('บริษัท@17FEB66',text)

FB4 = Frame(GUI) #คล้ายกระดาน
FB4.place(x=215,y=80)
B5 = ttk.Button(FB4,text='17FEB66',command=Button5)
B5.pack(ipadx=20,ipady=20)

def Button6():
    text = 'AAI,ASIAN,BDMS,BEM,BJC,BPP,OSP,PR9,SNNP,TU'
    messagebox.showinfo('บริษัท@22FEB66',text)

FB5 = Frame(GUI) #คล้ายกระดาน
FB5.place(x=215,y=80)
B6 = ttk.Button(FB4,text='22FEB66',command=Button6)
B6.pack(ipadx=20,ipady=20)

def Button7():
    text = 'ACE,AURA,CK,EKH,LH,SENA,SSP,TEGH,TOA,WARRIX,ZEN'
    messagebox.showinfo('บริษัท@27FEB66',text)

FB5 = Frame(GUI) #คล้ายกระดาน
FB5.place(x=215,y=80)
B6 = ttk.Button(FB4,text='27FEB66',command=Button7)
B6.pack(ipadx=20,ipady=20)
###################
def Button8():
    text = 'BCP,BCPG,CKP,MAKRO,RJH'
    messagebox.showinfo('บริษัท@20FEB66',text)

FB6 = Frame(GUI) #คล้ายกระดาน
FB6.place(x=330,y=80)
B5 = ttk.Button(FB6,text='20FEB66',command=Button8)
B5.pack(ipadx=20,ipady=20)

def Button9():
    text = 'ALLY,ANAN,BAREIT,CPALL,CPN,M,QH,SAT,SYNEX,TEAMG,THG,TKN'
    messagebox.showinfo('บริษัท@23FEB66',text)

FB5 = Frame(GUI) #คล้ายกระดาน
FB5.place(x=330,y=80)
B6 = ttk.Button(FB6,text='23FEB66',command=Button9)
B6.pack(ipadx=20,ipady=20)

def Button10():
    text = 'AMATA,BCH,BGRIM,BTG,CRC,D,JWD,ORI,PLANB,SAPPE,SIRI'
    messagebox.showinfo('บริษัท@28FEB66',text)

FB5 = Frame(GUI) #คล้ายกระดาน
FB5.place(x=330,y=80)
B6 = ttk.Button(FB6,text='28FEB66',command=Button10)
B6.pack(ipadx=20,ipady=20)
