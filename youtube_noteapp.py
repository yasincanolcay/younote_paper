#code=utf8


import tkinter
from tkinter import Tk
from tkinter import messagebox
import tkcalendar
import requests
from tkinter import *
import datetime
import random
from random import randint
from tkcalendar import DateEntry
from threading import Thread
import os
#----------------------#

# not ekleme fonksiyonu
def add_note():

    frame1 = Frame(master,bg="grey")
    frame1.place(relx=0.3,rely=0.2,relwidth=0.7,relheight=0.1)
    Label(frame1,text="Not Başlığı",bg="grey",fg="white",font="Sans-serif 12 bold").pack(padx=10,pady=5,side=LEFT)
    e1 = Entry(frame1,bd=2,relief=SOLID,font="Sans-serif 10 bold")
    e1.pack(padx=5,pady=5,side=LEFT)

    Label(frame1,text="TARİH",bg="grey",fg="white",font="Sans-serif 12 bold").pack(padx=10,pady=5,side=LEFT)
    date_ent = DateEntry(frame1,width=15,background="grey",foreground="white",locale="de_DE",relief=SOLID)
    date_ent._top_cal.overrideredirect(False)
    date_ent.pack(padx=10,pady=5,side=LEFT)


    def save():


        if e1.get():

            baslik = e1.get()
            tarih = date_ent.get()
            new_note = not_alani.get("1.0","end")

            metin = "{}\t {}\n_______________________________________________\n{}".format(baslik,tarih,new_note)

            file = "mynotes/{}.txt".format(baslik)

            with open(file,"w") as dosya:
                
                dosya.write(metin)
                dosya.close()

            log_file = open("log/notlarLog.txt","a")
            yazdir = "{}\n".format(baslik)
            log_file.write(yazdir)
            log_file.close()
            messagebox.showinfo("BAŞARILI","NOTUNUZ BAŞARIYLA KAYDEDİLDİ")

        else:
            messagebox.showwarning("BAŞLIK BOŞ","LÜTFEN NOTUNUZA BAŞLIK EKLEYİNİZ")
            





    save_btn = Button(frame1,bg="green",fg="white",text="Kaydet",command=save)
    save_btn.pack(padx=20,pady=10,side=LEFT)

    def kapat():
        frame1.place(relwidth=0,relheight=0)
        frame2.place(relwidth=0,relheight=0)



    off = Button(frame1,text="❌",bg="grey",fg="red",font="Sans-serif 12 bold",relief=FLAT,command=kapat)
    off.pack(padx=10,pady=10,side=LEFT)

    frame2 = Frame(master,bg="grey")
    frame2.place(relx=0.3,rely=0.3,relwidth=0.7,relheight=0.7)

    not_alani = Text(frame2,width=70,height=19,fg="black",font="Sans-serif 12 bold")
    not_alani.tag_configure("style",foreground="#333",font=("Sans-serif",12,"bold"))
    not_alani.pack(anchor=S)

    ilk_metin = "THİS İS MY NOTE AREA..."
    not_alani.insert(END,ilk_metin,"style")

    #--------------------------------------------#

def edit_note():

    def okumaislemi():
        try:

            not_basligi = mynote_list.get(mynote_list.curselection())

            frame3 = Frame(master,bg="grey")
            frame3.place(relx=0.3,rely=0.2,relwidth=0.7,relheight=0.1)
            mod_label = Label(frame3,text="--OKUMA MODU AÇIK--",fg="#d1d1d1",bg="grey",font="Sans-serif 12 bold").pack(side=LEFT,padx=10,pady=10)


            def edit_mode():

                cikis2.place(relwidth=0,relheight=0)
                frame6 = Frame(master,bg="grey")
                frame6.place(relx=0.3,rely=0.3,relwidth=0.7,relheight=0.7)
                edit_alani = Text(frame6,width=70,height=19,fg="black",font="Sans-serif 12 bold")
                edit_alani.tag_configure("style",foreground="#333",font=("Sans-serif",12,"bold"))
                edit_alani.pack(anchor=S)
                file = "mynotes/{}.txt".format(not_basligi)
                not_oku = open(str(file),"r")
                notu_oku = not_oku.read()
                not_oku.close()
   
                edit_alani.insert(END,notu_oku,"style")
                edit_btn.place(relwidth=0,relheight=0)

                def save_mode():

                    baslik = mynote_list.get(mynote_list.curselection())
                    filename = "mynotes/{}.txt".format(baslik)
                    editle = open(filename,"w")
                    al=edit_alani.get("1.0","end")
                    editle.write(al)
                    editle.close()
                    Label(frame3,text="not düzenlendi..",bg="grey",fg="#d1d1d1",font="Sans-serif 12 bold").pack(side=LEFT,padx=15)




                save_btn = Button(frame3,bg="green",text="SAVE",fg="white",font="Sans-serif 12 bold",command=save_mode)
                save_btn.pack(side=LEFT,padx=15,pady=5)

                def kapat():

                    frame3.place(relwidth=0,relheight=0)
                    frame4.place(relwidth=0,relheight=0)
                    frame6.place(relwidth=0,relheight=0)

                cikis = Button(frame3,text="❌",bg="grey",fg="red",font="Sans-serif 12 bold",relief=FLAT,command=kapat)
                cikis.pack(side=LEFT)
                

            edit_btn = Button(frame3,bg="green",text="EDİT MODU",fg="white",font="Sans-serif 12 bold",command=edit_mode)
            edit_btn.pack(side=LEFT,padx=10,pady=5)

            def cikis_panel():
                frame3.place(relwidth=0,relheight=0)
                frame4.place(relwidth=0,relheight=0)

            cikis2 = Button(frame3,text="❌",bg="grey",fg="red",font="Sans-serif 12 bold",relief=FLAT,command=cikis_panel)
            cikis2.pack(side=LEFT)
            frame4 = Frame(master,bg="grey")
            frame4.place(relx=0.3,rely=0.3,relwidth=0.7,relheight=0.7)

            edit_alani = Text(frame4,width=70,height=19,fg="black",font="Sans-serif 12 bold")
            edit_alani.tag_configure("style",foreground="#333",font=("Sans-serif",12,"bold"))
            edit_alani.pack(anchor=S)

            file = "mynotes/{}.txt".format(not_basligi)
            not_oku = open(str(file),"r")
            notu_oku = not_oku.read()
            not_oku.close()
   
            edit_alani.insert(END,notu_oku,"style")
            edit_alani["state"] = DISABLED

        except:

            frame5 = Frame(master,bg="grey")
            frame5.place(relx=0.3,rely=0.2,relwidth=0.7,relheight=0.1)
            Label(frame5,text="LÜTFEN OKUMAK VEYA DÜZENLEMEK İSTEDİĞİNİZ NOTU SEÇİNİZ!!",fg="red",bg="grey",font="Sans-serif 13 bold").pack()
    t1 = Thread(target=okumaislemi)
    t1.start()




def not_sil():

    try:

        silineceknot = mynote_list.get(mynote_list.curselection())
        file = "mynotes/{}.txt".format(silineceknot)
        os.unlink(file)

        f = open("log/notlarLog.txt","r")
        lines = f.readlines()
        f.close()

        f = open("log/notlarLog.txt","w")
        yazi = mynote_list.get(mynote_list.curselection())
        silinecek_satir = "{}".format(yazi)
        for line in lines:
            if line != silinecek_satir+"\n":
                f.write(line)
        f.close()

    except:
        messagebox.showwarning("SEÇİM YAPILMADI","LÜTFEN SİLMEK İSTEDİGİNİZ NOTU SEÇİNİZ!")





      


master = Tk()
master.geometry("950x550+150+100")
master.title("NOTEPAPER TK PLUS")
master.resizable(False,False)
icon = PhotoImage(file="icons/younote.png")
master.iconphoto(False,icon)

#-----------------------#
#-----------------------#
#all notes

all_notes = Frame(master,bg="#deb887")
all_notes.place(relx=0,rely=0,relwidth=0.3,relheight=0.65)

allnotes_label = Label(all_notes,text="Tüm notlar",bg="#deb887",fg="white",font="Sans-serif 14 bold")
allnotes_label.pack()

scroll = Scrollbar(master,width=10,elementborderwidth=-10)
scroll.pack(side=LEFT,fill=Y)
mynote_list = Listbox(all_notes,yscrollcommand=scroll.set,width=28,height=15,bg="#f08080",fg="black",font="Sans-serif 13 bold",selectbackground="#deb887")

#DÜZENLENECEK
ac = open("log/notlarLog.txt","r")
oku = ac.read()
ac.close()
for i in oku.splitlines():

    mynote_list.insert(END,i)
    mynote_list.pack(padx=5,pady=0)
    scroll.config(command=mynote_list.yview)





#--
buton_frame = Frame(master,bg="#deb887")
buton_frame.place(relx=0,rely=0.65,relwidth=0.3,relheight=0.35)
#----not ekleme butonu
add = PhotoImage(file="icons/add.png")
add_btn = Button(buton_frame,image=add,bg="#deb887",relief=FLAT,activebackground="#deb887",command=add_note)
add_btn.pack(pady=10)
#-----------------#
#not düzenleme butonu
edit = PhotoImage(file="icons/edit.png")
edit_btn = Button(buton_frame,image=edit,bg="#deb887",relief=FLAT,activebackground="#deb887",command=edit_note)
edit_btn.pack(pady=10)
#-----------------#
#silme butonu
delete = PhotoImage(file="icons/delete.png")
delete_btn = Button(buton_frame,image=delete,bg="#deb887",relief=FLAT,activebackground="#deb887",command=not_sil)
delete_btn.pack(pady=10)



#------------------#
#------------------#
#top frame

top_frame = Frame(master,bg="#deb887")
top_frame.place(relx=0.3,rely=0,relwidth=0.7,relheight=0.2)

weather_icon = PhotoImage(file="icons/weather.png")
weather_label = Label(top_frame,bg="#deb887",image=weather_icon)
weather_label.pack(side=LEFT,padx=10,pady=5)

#--------------
try:
    url = "http://api.openweathermap.org/data/2.5/weather?q=izmir&appid="
    api = "e7d2c6c38b9ae7616ec4a3579c9313cf&lang=tr"

    ara = url+api
    r = requests.get(ara)
    yaz = r.json()
    isim = yaz["name"]
    country = yaz["sys"]["country"]
    temp = int(yaz["main"]["temp"]-273.15)
    con = yaz["weather"][0]["description"]
    hava_durumu = "{} {} {}∘ {}".format(isim,country,temp,con)


    weather_text = Label(top_frame,text=hava_durumu,bg="#deb887",fg="white",font="Sans-serif 12 bold")
    weather_text.pack(side=LEFT,padx=5,pady=10)
except:
    weather_text = Label(top_frame,text="İNTERNET YOK..",bg="#deb887",fg="white",font="Sans-serif 12 bold")
    weather_text.pack(side=LEFT,padx=5,pady=10)

#-----------------------

date = datetime.datetime.now()
date_text = "{}/{}/{} - {}".format(date.day,date.month,date.year,datetime.datetime.strftime(date,"%A"))

date_icon = PhotoImage(file="icons/date.png")
date_label = Label(top_frame,bg="#deb887",image=date_icon)
date_label.pack(side=LEFT,padx=30,pady=5)
date_text_label = Label(top_frame,text=date_text,bg="#deb887",fg="white",font="Sans-serif 12 bold")
date_text_label.pack(padx=5,pady=5,side=LEFT)

#----------------#
#----------------#
#wallpaper frame

r = random.randint(2,6)
file_image ="images/plaj{}.png".format(r)
wallpaper_pic = PhotoImage(file=file_image)

wallpaper_frame = Frame(master,bg="red")
wallpaper_frame.place(relx=0.3,rely=0.2,relwidth=0.7,relheight=0.8)
wallpaper = Label(wallpaper_frame,image=wallpaper_pic,height=1350)
wallpaper.pack(padx=0,pady=0)



master.mainloop()

