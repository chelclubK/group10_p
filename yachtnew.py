import csv
import random
import datetime
from tkinter import *
import tkinter.messagebox as mb
FILENAME = "recordsyacht.csv"
def nameget():
    global name
    name=pole.get()
fh=False
yacht=False
kindof4=False
straight5=False
straight4=False
fhcan=True
yachtcan=True
kindof4can=True
straight5can=True
straight4can=True
sixescan=True
fivescan=True
fourscan=True
threescan=True
twoscan=True
onescan=True
choicecan=True
Sum=0
rollnum=[]
roll=0
i=0
hod1=0
hod2=0
spisok=[]
kol=0
name=""


def newkosti():
    global Sum
    global f
    global roll
    global rollnum
    global hod1
    global hod2
    global kol
    
    
    if hod1<13:
        if roll==0:
            hod1=hod1+1
            helping.config(text="")
            spisok.clear()
            f=[]
            for i in range(5):
                rand=random.randint(1,6)
                spisok.append(rand)
                pict=Button(root,image=kosti[rand-1],text=str(2*10+i),anchor='nw')
                pict.bind('<Button-1>',pictcom)
                pict.place(x=10+80*i, y=50)
                f.append(pict)
            rollnum=[]
            
            check()
            roll=roll+1
        elif roll==1 and rollnum:
            for i in rollnum:
                spisok[i]=(random.randint(1, 6))
                f[i].config(image=kosti[spisok[i]-1])
            rollnum=[]
            for i in range(len(f)):
                f[i].config(text=str(2*10+i))
            roll=roll+1
            check()
        elif roll==2 and rollnum:
            for i in rollnum:
                spisok[i]=(random.randint(1, 6))
                f[i].config(image=kosti[spisok[i]-1])
 
            rollnum=[]
            for i in range(len(f)):
                f[i].config(text=str(2*10+i))
            roll=roll+1
            check()
        elif roll==3:
            helping.config(text="Вы уже использовали все перебросы!")
            
def endgame():
    global name
    if hod1==12:
        if name=="":
            name='Player'
        msg=str(name)+"! Поздравляем вы набрали "+str(kol)+" очков."
        mb.showinfo("Результаты", msg)
        with open(FILENAME, "a", newline="") as file:
            columns = ["name", "score", "date"]
            now = datetime.datetime.now()
            user =  {"name": name, "score": kol,"date":now.strftime("%d-%m-%Y %H:%M")}
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writerow(user)

        
def pictcom(event):
    global rollnum
    global roll
    if hod1<13:
        knopka=event.widget
        r=int(knopka.cget('text'))
        if roll!=3 and roll!=0:
            if r//10==2:
                f[r%10].config(image=ckosti[spisok[r%10]-1],text=str(1*10+r%10))
                if not(r%10 in rollnum):
                    rollnum.append(r%10)
            else:
                f[r%10].config(image=kosti[spisok[r%10]-1],text=str(2*10+r%10))
                if r%10 in rollnum:
                    rollnum.remove(r%10)
        
    
def check():
    global Sum
    global fh
    global yacht
    global kindof4
    global straight5
    global straight4
    Sum=0
    fh=False
    yacht=False
    kindof4=False
    straight5=False
    straight4=False
    for i in range(6):
        a=spisok.count(i+1)
        Sum=Sum+(a*(i+1))
        if a==5:
            yacht=True
    for i in range(6):
        a=spisok.count(i+1)    
        if a==4 or a==5:
            kindof4=True
    for i in range(6):
        a=spisok.count(i+1) 
        if  a==3:
            for i in range(6):
                a=spisok.count(i+1)
                if a==2:
                    fh=True

            

    a=spisok.count(1)
    if a==1:
        a=spisok.count(2)
        if a==1:
            a=spisok.count(3)
            if a==1:
                a=spisok.count(4)
                if a==1:
                    a=spisok.count(5)
                    if a==1:
                        straight5=True
                 
    a1=spisok.count(2)
    if a1==1:
        i=i+1
        a1=spisok.count(3)
        if a1==1:
            i=i+1
            a1=spisok.count(4)    
            if a1==1:
                i=i+1
                a1=spisok.count(5)
                if a1==1:
                    i=i+1
                    a1=spisok.count(6)
                    if a1==1:
                        straight5=True                   
                            

    
    a=spisok.count(1)    
    if a==1 or a==2:
        a=spisok.count(2)
        if a==1 or a==2:
            a=spisok.count(3)
            if a==1 or a==2:
                a=spisok.count(4)
                if a==1 or a==2:
                    straight4=True
        

    a1=spisok.count(2)
    if a1==1 or a1==2:
        a1=spisok.count(3)
        if a1==1 or a1==2:
            a1=spisok.count(4)
            if a1==1 or a1==2:
                a1=spisok.count(5)
                if a1==1 or a1==2:
                    straight4=True
        

    a2=spisok.count(3)
    if a2==1 or a2==2:
        a2=spisok.count(4)
        if a2==1 or a2==2:
            a2=spisok.count(5)
            if a2==1 or a2==2:
                a2=spisok.count(6)
                if a2==1 or a2==2:
                    straight4=True
    i=0
def onesbut():
    global kol
    global onescan
    global roll
    global hod1
    global hod2
    if onescan==True and hod2+1==hod1:
        roll=0
        hod2=hod2+1
        kol=kol+spisok.count(1)*1
        onesbut.config(text=spisok.count(1)*1)
        onescan=False
        helping.config(text='Перебросьте кости!')
    total2.config(text=kol)
    
    endgame()
    
def twosbut():
    global kol
    global twoscan
    global roll
    global hod1
    global hod2
    global notswap
    if twoscan==True and hod2+1==hod1:
        roll=0
        hod2=hod2+1
        kol=kol+spisok.count(2)*2
        twosbut.config(text=spisok.count(2)*2)
        twoscan=False
        notswap = True
        helping.config(text='Перебросьте кости!')
    total2.config(text=kol)
    
    endgame()
def threesbut():
    global kol
    global threescan
    global roll
    global hod1
    global hod2
    if threescan==True and hod2+1==hod1:
        roll=0
        hod2=hod2+1
        kol=kol+spisok.count(3)*3
        threesbut.config(text=spisok.count(3)*3)
        threescan=False
        notswap = True
        helping.config(text='Перебросьте кости!')
    total2.config(text=kol)
    
    endgame()
def foursbut():
    global kol
    global fourscan
    global roll
    global hod1
    global hod2
    if fourscan==True and hod2+1==hod1:
        roll=0
        hod2=hod2+1
        kol=kol+spisok.count(4)*4
        foursbut.config(text=spisok.count(4)*4)
        fourscan=False
        helping.config(text='Перебросьте кости!')
    total2.config(text=kol)
    
    endgame()
def fivesbut():
    global kol
    global fivescan
    global roll
    global hod1
    global hod2
    if fivescan==True and hod2+1==hod1:
        roll=0
        hod2=hod2+1
        kol=kol+spisok.count(5)*5
        fivesbut.config(text=spisok.count(5)*5)
        fivescan=False
        helping.config(text='Перебросьте кости!')
    total2.config(text=kol)
    
    endgame()
def sixesbut():
    global kol
    global sixescan
    global roll
    global hod1
    global hod2
    if sixescan==True and hod2+1==hod1:
        roll=0
        hod2=hod2+1
        kol=kol+spisok.count(6)*6
        sixesbut.config(text=spisok.count(6)*6)
        sixescan=False
        helping.config(text='Перебросьте кости!')
    total2.config(text=kol)
    
    endgame()
def straight4but():
    global straight4
    global straight4can
    global kol
    global roll
    global hod1
    global hod2
    if straight4can==True and hod2+1==hod1:
        roll=0
        hod2=hod2+1
        straight4can=False
        if straight4==True:
            kol=kol+25
            straight4but.config(text=25)
            straight4=False
        else:
            straight4but.config(text=0)
        helping.config(text='Перебросьте кости!')
    total2.config(text=kol)
   
    endgame()
def straight5but():
    global straight5
    global straight5can
    global kol
    global roll
    global hod1
    global hod2
    if straight5can==True and hod2+1==hod1:
        roll=0
        hod2=hod2+1
        straight5can=False
        if straight5==True:
            kol=kol+30
            straight5but.config(text=30)
            straight5=False
        else:
            straight5but.config(text=0)
        helping.config(text='Перебросьте кости!')
    total2.config(text=kol)
    
    endgame()
def fhbut():
    global fh
    global fhcan
    global kol
    global Sum
    global roll
    global hod1
    global hod2
    if fhcan==True and hod2+1==hod1:
        roll=0
        hod2=hod2+1
        fhcan=False
        if fh==True:
            kol=kol+Sum
            fhbut.config(text=Sum)
            fh=False
        else:
            fhbut.config(text=0)
        helping.config(text='Перебросьте кости!')
    total2.config(text=kol)
    
    endgame()
def kindof4but():
    global kindof4
    global kindof4can
    global kol
    global Sum
    global roll
    global hod1
    global hod2
    if kindof4can==True and hod2+1==hod1:
        roll=0
        hod2=hod2+1
        kindof4can=False
        if kindof4==True:
            kol=kol+Sum
            kindof4but.config(text=Sum)
            kindof4=False
        else:
            kindof4but.config(text=0)
        helping.config(text='Перебросьте кости!')
    total2.config(text=kol)
  
    endgame()
def yachtbut():
    global yacht
    global yachtcan
    global kol
    global roll
    global hod1
    global hod2
    if yachtcan==True and hod2+1==hod1:
        roll=0
        hod2=hod2+1
        yachtcan=False
        if yacht==True:
            kol=kol+50
            yachtbut.config(text=50)
            yacht=False
        else:
            yachtbut.config(text=0)
        helping.config(text='Перебросьте кости!')
    total2.config(text=kol)
    endgame()
def choicebut():
    global choicecan
    global kol
    global Sum
    global roll
    global hod1
    global hod2
    if choicecan==True and hod2+1==hod1:
        roll=0
        hod2=hod2+1
        choicecan=False
        kol=kol+Sum
        choicebut.config(text=Sum)
        choicecan=False
    helping.config(text='Перебросьте кости!')
    total2.config(text=kol)

    endgame()
root=Tk()
root.title("Yacht")
root.geometry("740x560")
root.config(bg="green")
root.resizable(width=False, height=False)
kosti=[]
ckosti=[]
for i in range(6):
    kosti.append(PhotoImage(file=str(i+1)+'.png'))
for i in range(6):
    ckosti.append(PhotoImage(file='c'+str(i+1)+'.png'))

helping=Label(root,anchor='nw',text='',font="Georgia 19",bg='green',fg='white')
helping.place(x=10, y=140)    

btn=Button(root,fg="white",font="Georgia 13",text="Ввести имя",bg="black",command=nameget)
btn.place(x=10, y=500)

btn2=Button(root,fg="white",font="Georgia 13",text="Бросить кости",bg="black",command=newkosti)
btn2.place(x=10, y=10)

pole=Entry(root,fg="white",width="10",font="Georgia 20",bg="black")
pole.place(x=120, y=500)

ones=Label(root,anchor='nw',text='Ones',font="Georgia 19",bg='white',fg='black',width="8")
ones.place(x=500, y=10)
twos=Label(root,anchor='nw',text='Twos',font="Georgia 19",bg='white',fg='black',width="8")
twos.place(x=500, y=50)
threes=Label(root,anchor='nw',text='Threes',font="Georgia 19",bg='white',fg='black',width="8")
threes.place(x=500, y=90)
fours=Label(root,anchor='nw',text='Fours',font="Georgia 19",bg='white',fg='black',width="8")
fours.place(x=500, y=130)
fives=Label(root,anchor='nw',text='Fives',font="Georgia 19",bg='white',fg='black',width="8")
fives.place(x=500, y=170)
sixes=Label(root,anchor='nw',text='Sixes',font="Georgia 19",bg='white',fg='black',width="8")
sixes.place(x=500, y=210)
straight4=Label(root,anchor='nw',text='Straight 4',font="Georgia 19",bg='white',fg='black',width="8")
straight4.place(x=500, y=250)
straight5=Label(root,anchor='nw',text='Straight 5',font="Georgia 19",bg='white',fg='black',width="8")
straight5.place(x=500, y=290)
fh=Label(root,anchor='nw',text='Full House',font="Georgia 19",bg='white',fg='black',width="8")
fh.place(x=500, y=330)
kindof4=Label(root,anchor='nw',text='Kind of 4',font="Georgia 19",bg='white',fg='black',width="8")
kindof4.place(x=500, y=370)
yacht=Label(root,anchor='nw',text='Yacht',font="Georgia 19",bg='white',fg='black',width="8")
yacht.place(x=500, y=410)
choice=Label(root,anchor='nw',text='Choice',font="Georgia 19",bg='white',fg='black',width="8")
choice.place(x=500, y=450)


onesbut=Button(root,anchor='nw',text='',font="Georgia 14",bg='white',fg='black',width="3",command=onesbut)
onesbut.place(x=640, y=10)
twosbut=Button(root,anchor='nw',text='',font="Georgia 14",bg='white',fg='black',width="3",command=twosbut)
twosbut.place(x=640, y=50)
threesbut=Button(root,anchor='nw',text='',font="Georgia 14",bg='white',fg='black',width="3",command=threesbut)
threesbut.place(x=640, y=90)
foursbut=Button(root,anchor='nw',text='',font="Georgia 14",bg='white',fg='black',width="3",command=foursbut)
foursbut.place(x=640, y=130)
fivesbut=Button(root,anchor='nw',text='',font="Georgia 14",bg='white',fg='black',width="3",command=fivesbut)
fivesbut.place(x=640, y=170)
sixesbut=Button(root,anchor='nw',text='',font="Georgia 14",bg='white',fg='black',width="3",command=sixesbut)
sixesbut.place(x=640, y=210)
straight4but=Button(root,anchor='nw',text='',font="Georgia 14",bg='white',fg='black',width="3",command=straight4but)
straight4but.place(x=640, y=250)
straight5but=Button(root,anchor='nw',text='',font="Georgia 14",bg='white',fg='black',width="3",command=straight5but)
straight5but.place(x=640, y=290)
fhbut=Button(root,anchor='nw',text='',font="Georgia 14",bg='white',fg='black',width="3",command=fhbut)
fhbut.place(x=640, y=330)
kindof4but=Button(root,anchor='nw',text='',font="Georgia 14",bg='white',fg='black',width="3",command=kindof4but)
kindof4but.place(x=640, y=370)
yachtbut=Button(root,anchor='nw',text='',font="Georgia 14",bg='white',fg='black',width="3",command=yachtbut)
yachtbut.place(x=640, y=410)
choicebut=Button(root,anchor='nw',text='',font="Georgia 14",bg='white',fg='black',width="3",command=choicebut)
choicebut.place(x=640, y=450)

total=Label(root,anchor='nw',text='Total',font="Georgia 19",bg='white',fg='black',width="8")
total.place(x=500, y=510)
total2=Label(root,anchor='nw',text='',font="Georgia 19",bg='white',fg='black',width="3")
total2.place(x=640, y=510)




root.mainloop()
