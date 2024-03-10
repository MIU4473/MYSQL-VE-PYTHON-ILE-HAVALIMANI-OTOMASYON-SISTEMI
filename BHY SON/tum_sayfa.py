import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

customtkinter.set_appearance_mode("white")
customtkinter.set_default_color_theme("blue")
customtkinter.deactivate_automatic_dpi_awareness() #farklı ekranlara geçince otomatik ölçeklendirmeyi iptal edebilmek için

app=customtkinter.CTk()
app.geometry("1000x700")
app.resizable(False,False)
app.title("Giriş yap")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def clear_widgets(frame):
	# select all frame widgets and delete them
	for widget in frame.winfo_children():
		widget.destroy()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

global verilerim
global kullanici
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def login_():
    




    clear_widgets(app)
    app.tkraise()
    def Giriş_yap():
            global verilerim

            
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="havaalani"
            )
            E_mail=MAIL_.get()
            
            sifre=Sifre.get()
            
           


          
           
            yonetici=check_var.get()
            if yonetici=='on':
                mycursor=mydb.cursor()
                mycursor.execute("SELECT ID,KULLANICI_ADI,KULLANICI_SOYADI,E_MAIL,SIFRE FROM yoneticigiris WHERE E_MAIL=%s and SIFRE=%s",(E_mail,sifre))
        
                verilerim=mycursor.fetchall() 

                if verilerim:
                    sefer_()
                else:
                    # Veri bulunamadı, hata mesajı göster
                    messagebox.showerror("Hata", "Yanlış şifre veya kullanıcı adı!")

                
            else:
               mycursor=mydb.cursor()
               mycursor.execute("SELECT ID,KULLANICI_ADI,KULLANICI_SOYADI,E_MAIL,SIFRE FROM kayit WHERE E_MAIL=%s and SIFRE=%s",(E_mail,sifre))
        
               verilerim=mycursor.fetchall() 
               if verilerim:
                    bilet()    
               else:
                    # Veri bulunamadı, hata mesajı göster
                    messagebox.showerror("Hata", "Yanlış şifre veya kullanıcı adı!")

           
            
            
                
          
          


    img = Image.open("arka.jpg")
    width, height = 1000, 700
    img_resized = img.resize((width, height), Image.LANCZOS)
    img1 = ImageTk.PhotoImage(img_resized)
    arkatema = tk.Label(master=app, image=img1)
    arkatema.pack()

    frame=customtkinter.CTkFrame(master=app,width=500,height=500,fg_color="white",corner_radius=20,bg_color="#aeb3b9")
    frame.place(x=450,y=100)

    label1=customtkinter.CTkLabel(master=frame,text="Hoşgeldiniz giriş yapınız",font=('century gothic',25),text_color="black")
    label1.place(x=110,y=40)





    MAIL_=customtkinter.CTkEntry(master=frame,width=380,placeholder_text="E-mail",border_color="#673d35",font=('Microsoft YaHei UI Lıght',20))
    MAIL_.place(x=60,y=130)


    Sifre=customtkinter.CTkEntry(master=frame,width=380,placeholder_text="Şifre",border_color="#673d35",font=('Microsoft YaHei UI Lıght',20),text_color="black")
    Sifre.place(x=60,y=180)

    Button3=customtkinter.CTkButton(master=frame,text="Şifrenizi mi unuttunuz?",width=50,fg_color="white",text_color="#820000",hover_color="white",font=('Microsoft YaHei UI Lıght',15))
    Button3.place(x=285,y=220)

    check_var = customtkinter.StringVar(value="off")
    checkbox = customtkinter.CTkCheckBox(master=frame, text="Yönetici girişi",variable=check_var, onvalue="on", offvalue="off",fg_color="#820000",hover_color="#673d35")
    checkbox.place(x=60,y=260)

    Button1=customtkinter.CTkButton(master=frame,text="Giriş yapınız",width=280,corner_radius=10,hover_color="#673d35",fg_color="#820000",font=('Microsoft YaHei UI Lıght',17),command=Giriş_yap)
    Button1.place(x=110,y=300)

    label2=customtkinter.CTkLabel(master=frame,text="Kullanıcı hesabınız yok mu?",font=('Microsoft YaHei UI Lıght',15),text_color="black")
    label2.place(x=135,y=350)

   

    Button2=customtkinter.CTkButton(master=frame,text="Kayıt ol",width=50,fg_color="white",text_color="#820000",hover_color="white",font=('Microsoft YaHei UI Lıght',15),command=kayit_)
    Button2.place(x=305,y=350)

    label3=customtkinter.CTkLabel(master=frame,text="BHY iyi yolculuklar diler...",font=('Microsoft YaHei UI Lıght',15),text_color="black")
    label3.place(x=300,y=450)


    app.mainloop()
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def kayit_():

    clear_widgets(app)
    app.tkraise()

    def Kayıt_ol():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="havaalani"
    )

        mycursor = mydb.cursor()

        Ad=Kullanici_adi.get()
        Soyad=Kullaci_soyad.get()
        Password=Sifre.get()
        E_mail=Mail.get()
        Tel=Telefon.get()
        Dogum=Dogum_tarihi.get()
        Cins=Cinsiyet.get()

        dizi = [Ad,Soyad,Password,E_mail,Tel,Dogum,Cins]

        a = 1

        for i in dizi:
            if  i.strip() == '': #strip() fonksiyonu: bir kelime alıyor sağındaki ve solundaki boşlukları siliyor yaptığı bu 
                messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!') 
                a += 1 
                break
        if a == 1:
            insert2 = "INSERT INTO kayit (KULLANICI_ADI,KULLANICI_SOYADI,SIFRE,E_MAIL,CINSIYET,DOGUM_TARIHI,TELEFON) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            degerler2 = (Ad,Soyad,Password,E_mail,Cins,Dogum,Tel)
            mycursor.execute(insert2, degerler2)
            mydb.commit()
            messagebox.showinfo("Bilgi", "Başarıyla kayıt olundu")

    frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
    frame_sol.place(x=0,y=0)

    my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))
    image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
    image_label.place(x=30,y=20)

    my_image1 = customtkinter.CTkImage(dark_image=Image.open("img/register.png"), size=(30,30))
    image_label1 = customtkinter.CTkLabel(app, image=my_image1,text="",bg_color="#6b6b6b")
    image_label1.place(x=10,y=145)



    label1=customtkinter.CTkLabel(master=frame_sol,text="Hoş geldiniz",font=('century gothic',23))
    label1.place(x=110,y=35)


    Button1=customtkinter.CTkButton(master=frame_sol,text="Kayıt ekle",width=180,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17),text_color="black")
    Button1.place(x=50,y=150)
    Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Giriş yap",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17),command=login_)
    Btn_cıkıs.place(x=50,y=630)




    #Bt1=customtkinter.CTkButton(master=frame_sol,width=250,height=30,text="Bora Altun",compound="left",text_color="white",bg_color="#1f2021",fg_color="#1f2021",hover_color="#1f2021")
    #Bt1.place(x=70,y=10)



    frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=700,fg_color="white")
    frame_sag_ust.place(x=300,y=0)

    label1=customtkinter.CTkLabel(master=frame_sag_ust,text="Hoşgeldiniz giriş yapınız",font=('century gothic',23),text_color="black")
    label1.place(x=200,y=35)


    Kullanici_adi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Adınız :",font=('century gothic',16),text_color="black")
    Kullanici_adi_label.place(x=50,y=100)
    Kullanici_adi=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Kullanici_adi.place(x=200,y=100)

    Kullaci_soyad_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Soyadınız :",font=('century gothic',16),text_color="black")
    Kullaci_soyad_label.place(x=50,y=150)
    Kullaci_soyad=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Kullaci_soyad.place(x=200,y=150)

    Sifre_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Şifre :",font=('century gothic',16),text_color="black")
    Sifre_label.place(x=50,y=200)
    Sifre=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Sifre.place(x=200,y=200)

    Mail_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Mail :",font=('century gothic',16),text_color="black")
    Mail_label.place(x=50,y=250)
    Mail=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Mail.place(x=200,y=250)

    Telefon_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Telefon :",font=('century gothic',16),text_color="black")
    Telefon_label.place(x=50,y=300)
    Telefon=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Telefon.place(x=200,y=300)

    Dogum_tarihi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Dogum tarihiniz :",font=('century gothic',16),text_color="black")
    Dogum_tarihi_label.place(x=50,y=350)
    Dogum_tarihi=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Dogum_tarihi.place(x=200,y=350)

    Cinsiyet_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Cinsiyet :",font=('century gothic',16),text_color="black")
    Cinsiyet_label.place(x=50,y=400)
    Cinsiyet=customtkinter.CTkComboBox(master=frame_sag_ust,values=["K","E"],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    Cinsiyet.place(x=200,y=400)


    Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Kayıt ekle",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17),command=Kayıt_ol)
    Button1.place(x=380,y=450)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sefer_():
            
            clear_widgets(app)
            app.tkraise()
            global kullanici
            for row in verilerim:  
              kullanici=row[1]+ " " +row[2]

            def sefer_olustur():
                mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="1234",
                        database="havaalani"
                )
                mycursor = mydb.cursor()

                kalkis_nokta=Kalkıs_noktasi.get()
                varis_nokta=Varis_noktasi.get()
                yolcu=yolcu_sayisi.get()
                bilet_fiyat=Bilet_fiyati.get()
                kalkis_zamani=Tarih.get()
                kuyruk_numarasi=kuyruk_no.get()
                
                
                

                select="SELECT ID FROM sehir WHERE SEHIR_ISMI=%s"
                mycursor.execute(select,(kalkis_nokta,))
                Kalkis = mycursor.fetchone()
                mycursor.execute(select,(varis_nokta,))
                Varis=mycursor.fetchone()
                

                mycursor.execute("SELECT SEHIR_ISMI FROM sehir")
                deneme = mycursor.fetchall()
                
                a=1
                i=0
                
            # Herhangi bir boşalan varmı kontrol sağlar
                dizi = [yolcu,bilet_fiyat,kalkis_zamani,kuyruk_numarasi]
                
                for i in dizi:
                    if  i.strip() == '' or kalkis_nokta == "" or varis_nokta == "": #strip() fonksiyonu: bir kelime alıyor sağındaki ve solundaki boşlukları siliyor yaptığı bu 
                      messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
                    
                      a += 1
                      break
                
            #girilen şehir ismi doğrumu diye kontrol eder
                if Kalkis is  None:
                    messagebox.showerror("Uyarı", "Kalkış şehrini kontrol ediniz")
                if Varis is  None:
                    messagebox.showerror("Uyarı", "Varış şehrini kontrol ediniz")

                

                
                #Girilen şehir ismi ve boş bir alan yoksa kayıt eder    
                if a == 1 :
                    insert = "INSERT INTO seferler (KALKIS_SEHIR_ID,VARIS_SEHIR_ID,KUYRUK_NO,KALKIS_ZAMANI,BILET_TUTARI,YOLCU_SAYISI) VALUES (%s, %s, %s, %s, %s, %s)"
                    degerler = (Kalkis[0],Varis[0],kuyruk_numarasi,kalkis_zamani,bilet_fiyat,yolcu)
                    mycursor.execute(insert, degerler)
                    messagebox.showinfo("Bilgi", "Başarıyla kayıt olundu")
                    mydb.commit()
                    mydb.close()

            def verileri_listele():
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="havaalani"
                )
                mycursor = mydb.cursor()

                # Veritabanındaki kayıtları seç
                mycursor.execute("SELECT ID,KALKIS_SEHIR_ID, VARIS_SEHIR_ID, KUYRUK_NO, KALKIS_ZAMANI, BILET_TUTARI, YOLCU_SAYISI FROM seferler")
                kayıtlar = mycursor.fetchall()

                # Treeview'i temizle
                for row in tree.get_children():
                    tree.delete(row)

                #mycursor kayıtları Treeview'e ekle
                for kayıtlar in kayıtlar:
                    tree.insert("", "end", values=kayıtlar)

                mydb.close()



            def kayit_sil():
                selected_item = tree.selection()

                if not selected_item:
                    messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
                    return

                confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

                if confirm:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="1234",
                        database="havaalani"
                    )
                    mycursor = mydb.cursor()

                    # Seçilen kaydın KALKIS_SEHIR_ID değerini al
                    selected_id = tree.item(selected_item, 'values')[0]

                    # Kaydı sil
                    mycursor.execute("DELETE FROM seferler WHERE ID = %s", (selected_id,))

                    mydb.commit()
                    mydb.close()

                    # Kayıtları güncelle
                    verileri_listele()





            frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
            frame_sol.place(x=0,y=0)

            my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))

            image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
            image_label.place(x=30,y=20)
            
            label_text = tk.StringVar()
            label_text.set(kullanici)    
            label1=customtkinter.CTkLabel(master=frame_sol,textvariable=label_text,font=('century gothic',23))
            label1.place(x=110,y=35)

            Btn_sefer=customtkinter.CTkButton(master=frame_sol,text="Sefer ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=sefer_)
            Btn_sefer.place(x=50,y=200)

            Btn_ucak=customtkinter.CTkButton(master=frame_sol,text="Uçak ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=ucak)
            Btn_ucak.place(x=50,y=260)

            Btn_paket=customtkinter.CTkButton(master=frame_sol,text="Paket ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=paket)
            Btn_paket.place(x=50,y=320)

            Btn_calisan=customtkinter.CTkButton(master=frame_sol,text="Çalışan ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=calisan)
            Btn_calisan.place(x=50,y=380)

            Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Çıkış yap",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=login_)
            Btn_cıkıs.place(x=50,y=630)

            #Bt1=customtkinter.CTkButton(master=frame_sol,width=250,height=30,text="Bora Altun",compound="left",text_color="white",bg_color="#1f2021",fg_color="#1f2021",hover_color="#1f2021")
            #Bt1.place(x=70,y=10)



            frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=400,fg_color="white")
            frame_sag_ust.place(x=300,y=0)

            label1=customtkinter.CTkLabel(master=frame_sag_ust,text="SEFER OLUŞTUR",font=('century gothic',25),text_color="black")
            label1.place(x=300,y=5)


            Kalkıs_noktasi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kalkış noktası :",font=('century gothic',16),text_color="black")
            Kalkıs_noktasi_label.place(x=50,y=50)
            Kalkıs_noktasi=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
            Kalkıs_noktasi.place(x=180,y=50)

            Varis_noktasi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Varış noktası :",font=('century gothic',16),text_color="black")
            Varis_noktasi_label.place(x=50,y=100)
            Varis_noktasi=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
            Varis_noktasi.place(x=180,y=100)

            yolcu_sayisi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Yolcu Sayısı :",font=('century gothic',16),text_color="black")
            yolcu_sayisi_label.place(x=50,y=150)
            yolcu_sayisi=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
            yolcu_sayisi.place(x=180,y=150)

            Bilet_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Bilet fiyatı :",font=('century gothic',16),text_color="black")
            Bilet_label.place(x=50,y=200)
            Bilet_fiyati=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
            Bilet_fiyati.place(x=180,y=200)

            Tarih_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kalkış zamanı:",font=('century gothic',16),text_color="black")
            Tarih_label.place(x=50,y=250)
            Tarih=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
            Tarih.place(x=180,y=250)

            kuyruk_no_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kuyruk no:",font=('century gothic',16),text_color="black")
            kuyruk_no_label.place(x=50,y=300)
            kuyruk_no=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
            kuyruk_no.place(x=180,y=300)

            Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Sefer ekle",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17),command=sefer_olustur)
            Button1.place(x=360,y=350)

            frame_sag_alt=customtkinter.CTkFrame(master=app,width=700,height=300,fg_color="#e6e8e7",bg_color="#e6e8e7")
            frame_sag_alt.place(x=300,y=400)

            # ... Diğer arayüz elemanları ...

            # Treeview widget'i oluştur
            tree_columns = ("ID","KALKIS_SEHIR_ID", "VARIS_SEHIR_ID", "KUYRUK_NO", "KALKIS_ZAMANI", "BILET_TUTARI", "YOLCU_SAYISI")
            tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings")

            # Treeview kolon başlıklarını ayarla
            for col in tree_columns:
                tree.heading(col, text=col)
                tree.column(col, width=40)

            # Treeview'i paketle ve yerleştir
            tree.place(x=0, y=25, width=700, height=300)

            # "Verileri Listele" butonu
            button_listele = tk.Button(frame_sag_alt, text="Verileri Listele",width=50, command=verileri_listele)
            button_listele.place(x=0, y=0)

            button_sil = tk.Button(frame_sag_alt, text="Kayıt Sil",command=kayit_sil,width=50)
            button_sil.place(x=350, y=0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def odeme():
        clear_widgets(app)
        app.tkraise()
        global kullanici
        for row in verilerim:
            kullanici_idim = row[0]  
            kullanici=row[1]+ " " +row[2]
            

        
        def yonetici_kayit():
            mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="havaalani"
            )
            mycursor = mydb.cursor()

            BANKA=banka.get()
            KART_ISIM =isim.get()
            KART_NO =kart_no.get()
            AY= ay.get()
            YIL=yıl.get()
            CVV=cvv.get()
        
            
            
            

        
            


            
            a=1
            
        # Herhangi bir boşalan var mı kontrol sağlar
            dizi = [KART_NO,KART_ISIM,BANKA,AY,YIL,CVV]
            
            for i in dizi:
                if  i.strip()=='': #strip() fonksiyonu: bir kelime alıyor sağındaki ve solundaki boşlukları siliyor yaptığı bu 
                 messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
                
                 a += 1
                 break
            


                          

            
            #Girilen şehir ismi ve boş bir alan yoksa kayıt eder    
            if a == 1 :
                
                insert = "INSERT INTO odeme (KULLANICI_ID,KART_ISIM,KART_NO,KART_SON_AY,KART_SON_YIL,KART_CVV,BANKA) VALUES (%s,%s, %s, %s, %s,%s,%s)"
                degerler = (kullanici_idim,KART_ISIM,KART_NO,AY,YIL,CVV,BANKA)
                mycursor.execute(insert, degerler)
                messagebox.showinfo("Bilgi", "Başarıyla kayıt olundu")
                mydb.commit()
                mydb.close()

        def verileri_listele():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="havaalani"
            )
            mycursor = mydb.cursor()
            for row in verilerim:
                kullanici_idim = row[0]      

            # Veritabanındaki kayıtları seç
            mycursor.execute("SELECT ID,KULLANICI_ID,BANKA,KART_ISIM FROM odeme WHERE KULLANICI_ID=%s", (kullanici_idim, ))
            kayıtlar = mycursor.fetchall()

            # Treeview'i temizle
            for row in tree.get_children():
                tree.delete(row)

            #mycursor kayıtları Treeview'e ekle
            for kayıtlar in kayıtlar:
                tree.insert("", "end", values=kayıtlar)

            mydb.close()



        def kayit_sil():
            selected_item = tree.selection()

            if not selected_item:
                messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
                return

            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="havaalani"
                )
                mycursor = mydb.cursor()

                # Seçilen kaydın ID değerini al
                selected_id = tree.item(selected_item, 'values')[0]

                # Kaydı sil
                mycursor.execute("DELETE FROM odeme WHERE ID = %s", (selected_id,))

                mydb.commit()
                mydb.close()

                # Kayıtları güncelle
                verileri_listele()


        frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
        frame_sol.place(x=0,y=0)

        my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))

        image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
        image_label.place(x=30,y=20)
        
        label_text = tk.StringVar()
        label_text.set(kullanici)    

        label1=customtkinter.CTkLabel(master=frame_sol,textvariable=label_text,font=('century gothic',17))
        label1.place(x=110,y=35)

        Btn_sefer=customtkinter.CTkButton(master=frame_sol,text="Bilet al",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=bilet)
        Btn_sefer.place(x=50,y=200)

        Btn_ucak=customtkinter.CTkButton(master=frame_sol,text="Ödeme bilgileri",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17))
        Btn_ucak.place(x=50,y=260)


        Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Çıkış yap",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17), command=login_)
        Btn_cıkıs.place(x=50,y=630)

        #Bt1=customtkinter.CTkButton(master=frame_sol,width=250,height=30,text="Bora Altun",compound="left",text_color="white",bg_color="#1f2021",fg_color="#1f2021",hover_color="#1f2021")
        #Bt1.place(x=70,y=10)



        frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=400,fg_color="white")
        frame_sag_ust.place(x=300,y=0)

        label1=customtkinter.CTkLabel(master=frame_sag_ust,text="KART BİLGİLERİNİZİ GİRİNİZ",font=('century gothic',25),text_color="black")
        label1.place(x=200,y=5)


        banka_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Banka :",font=('century gothic',16),text_color="black")
        banka_label.place(x=50,y=50)
        banka=customtkinter.CTkComboBox(master=frame_sag_ust,values=["Ziraat","Garanti","Kuveyt","Akbank","İş bankası","Yapıkredi","Denizbank","Vakıf bank","Finansbank"],width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20))
        banka.place(x=180,y=50)

        isim_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kart üzerindeki isim :",font=('century gothic',16),text_color="black")
        isim_label.place(x=50,y=100)
        isim=customtkinter.CTkEntry(master=frame_sag_ust,width=340,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
        isim.place(x=220,y=100)

        kart_no_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kart no :",font=('century gothic',16),text_color="black")
        kart_no_label.place(x=50,y=150)
        kart_no=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
        kart_no.place(x=180,y=150)

        tarih_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Son kullanım tarihi :",font=('century gothic',16),text_color="black")
        tarih_label.place(x=50,y=200)
        ay=customtkinter.CTkComboBox(master=frame_sag_ust,values=["01","02","03","04","05","06","07","08","09","10","11","12"],width=100,border_color="white",font=('Microsoft YaHei UI Lıght',20))
        ay.place(x=300,y=200)
        yıl=customtkinter.CTkComboBox(master=frame_sag_ust,values=["23","24","25","26","27","28","29","30","31","32"],width=100,border_color="white",font=('Microsoft YaHei UI Lıght',20))
        yıl.place(x=455,y=200)


        cvv_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Cvv :",font=('century gothic',16),text_color="black")
        cvv_label.place(x=50,y=250)
        cvv=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
        cvv.place(x=180,y=250)



        Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Kaydet",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17),command=yonetici_kayit)
        Button1.place(x=360,y=350)


        frame_sag_alt=customtkinter.CTkFrame(master=app,width=700,height=400,fg_color="white")
        frame_sag_alt.place(x=300,y=400)

        # ... Diğer arayüz elemanları ...

        # Treeview widget'i oluştur
        tree_columns = ("ID","KULLANICI_ID","BANKA","KART_ISIM")
        tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings")
        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=700, height=300)

        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_sag_alt, text="Verileri Listele",width=50, command=verileri_listele)
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_sag_alt, text="Kayıt Sil",command=kayit_sil,width=50)
        button_sil.place(x=350, y=0)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def calisan():
 
    def calisan_ekle():
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="havaalani"
        )
        mycursor = mydb.cursor()

        calisanadi=calisan_ad.get()
        calisansoyadi=calisan_soyad.get()
        tel=telefon.get()
        cins=cinsiyet.get()
        poz=pozisyon.get()
        ucret=maas.get()
        sube=sube_id.get()
        
    
        
        a=1
        
    # Herhangi bir boşalan varmı kontrol sağlar
        dizi = [calisanadi,calisansoyadi,tel,cins,poz,ucret,sube]
        
        for i in dizi:
            if  i.strip() == '': #strip() fonksiyonu: bir kelime alıyor sağındaki ve solundaki boşlukları siliyor yaptığı bu 
             messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
            
             a += 1
             break

        #Girilen şehir ismi ve boş bir alan yoksa kayıt eder    
        if a == 1 :
            insert1 = "INSERT INTO calisanlar (CALISAN_AD, CALISAN_SOYAD, TELEFON, CINSIYET, MAAS, SUBE_ID) VALUES (%s, %s, %s, %s, %s, %s)"
            degerler1 = (calisanadi,calisansoyadi,tel,cins,ucret,sube)
            mycursor.execute(insert1, degerler1)

            insert2 = "INSERT INTO personelpozisyonu (pozisyon) VALUES (%s)"
            mycursor.execute(insert2, (poz, ))


            messagebox.showinfo("Bilgi", "Paket başarıyla eklendi")
            mydb.commit()
            mydb.close()


    def verileri_listele():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="havaalani"
        )
        mycursor = mydb.cursor()

        # Veritabanındaki kayıtları seç
        join = "SELECT C.ID, P.ID, C.CALISAN_AD, C.CALISAN_SOYAD, C.TELEFON, C.CINSIYET, P.POZISYON, C.MAAS, C.SUBE_ID FROM havaalani.calisanlar C INNER JOIN havaalani.personelpozisyonu P ON C.ID=P.ID"
        mycursor.execute(join)
        kayıtlar = mycursor.fetchall()

        # Treeview'i temizle
        for row in tree.get_children():
            tree.delete(row)

        #mycursor kayıtları Treeview'e ekle
        for kayıtlar in kayıtlar:
            tree.insert("", "end", values=kayıtlar)

        mydb.close()



    def kayit_sil():
        selected_item = tree.selection()

        if not selected_item:
            messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
            return

        confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

        if confirm:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="havaalani"
            )
            mycursor = mydb.cursor()

            # Seçilen kaydın KALKIS_SEHIR_ID değerini al
            
            selected_id = tree.item(selected_item, 'values')[0]
            
            selected_id2 = tree.item(selected_item, 'values')[1]

            # Kaydı sil
            mycursor.execute("DELETE FROM calisanlar WHERE ID = %s", (selected_id,))
            mycursor.execute("DELETE FROM personelpozisyonu WHERE ID = %s", (selected_id2,))

            mydb.commit()
            mydb.close()

            # Kayıtları güncelle
            verileri_listele()





    frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
    frame_sol.place(x=0,y=0)

    my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))

    image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
    image_label.place(x=30,y=20)
    label_text = tk.StringVar()
    label_text.set(kullanici)    
    label1=customtkinter.CTkLabel(master=frame_sol,textvariable=label_text,font=('century gothic',17))
    label1.place(x=110,y=35)

    Btn_sefer=customtkinter.CTkButton(master=frame_sol,text="Sefer ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=sefer_)
    Btn_sefer.place(x=50,y=200)

    Btn_ucak=customtkinter.CTkButton(master=frame_sol,text="Uçak ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=ucak)
    Btn_ucak.place(x=50,y=260)

    Btn_paket=customtkinter.CTkButton(master=frame_sol,text="Paket ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=paket)
    Btn_paket.place(x=50,y=320)

    Btn_calisan=customtkinter.CTkButton(master=frame_sol,text="Çalışan ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=calisan)
    Btn_calisan.place(x=50,y=380)

    Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Çıkış yap",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=login_)
    Btn_cıkıs.place(x=50,y=630)

    #Bt1=customtkinter.CTkButton(master=frame_sol,width=250,height=30,text="Bora Altun",compound="left",text_color="white",bg_color="#1f2021",fg_color="#1f2021",hover_color="#1f2021")
    #Bt1.place(x=70,y=10)



    frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=400,fg_color="white")
    frame_sag_ust.place(x=300,y=0)

    label1=customtkinter.CTkLabel(master=frame_sag_ust,text="CALISAN EKLE",font=('century gothic',25),text_color="black")
    label1.place(x=300,y=5)


    calisan_ad_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Çalışan ad :",font=('century gothic',16),text_color="black")
    calisan_ad_label.place(x=50,y=50)
    calisan_ad=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    calisan_ad.place(x=180,y=50)

    calisan_soyad_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Çalışan soyad :",font=('century gothic',16),text_color="black")
    calisan_soyad_label.place(x=50,y=100)
    calisan_soyad=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    calisan_soyad.place(x=180,y=100)

    telefon_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Telefon :",font=('century gothic',16),text_color="black")
    telefon_label.place(x=50,y=150)
    telefon=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    telefon.place(x=180,y=150)

    cinsiyet_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Cinsiyet :",font=('century gothic',16),text_color="black")
    cinsiyet_label.place(x=50,y=200)
    cinsiyet=customtkinter.CTkComboBox(master=frame_sag_ust,values=["K","E"],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    cinsiyet.place(x=180,y=200)

    pozisyon_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Pozisyon :",font=('century gothic',16),text_color="black")
    pozisyon_label.place(x=50,y=250)
    pozisyon=customtkinter.CTkComboBox(master=frame_sag_ust,values=["Pilot","Yrd.Pilot","Hostes","Personel","Teknisyen"],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    pozisyon.place(x=180,y=250)

    maas_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Maaş :",font=('century gothic',16),text_color="black")
    maas_label.place(x=50,y=300)
    maas=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    maas.place(x=180,y=300)

    sube_id_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Şube No :",font=('century gothic',16),text_color="black")
    sube_id_label.place(x=50,y=350)
    sube_id=customtkinter.CTkComboBox(master=frame_sag_ust,values=["656123","876789","768456","656234","324567","874890","432123","432678","654345","764901","345678","864234","786567", "342890","542123","653456","546789","653345","214901","167678"],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    sube_id.place(x=180,y=350)

    Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Çalışan ekle",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17), command=calisan_ekle)
    Button1.place(x=360,y=350)

    frame_sag_alt=customtkinter.CTkFrame(master=app,width=700,height=300,fg_color="#e6e8e7",bg_color="#e6e8e7")
    frame_sag_alt.place(x=300,y=400)

    # ... Diğer arayüz elemanları ...

    # Treeview widget'i oluştur
    tree_columns = ("CALISAN_ID", "POZ_ID", "AD", "SOYAD", "TELEFON", "CINSIYET", "POZISYON", "MAAS", "SUBE_ID")
    tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings")

    # Treeview kolon başlıklarını ayarla
    for col in tree_columns:
        tree.heading(col, text=col)
        tree.column(col, width=60)

    # Treeview'i paketle ve yerleştir
    tree.place(x=0, y=25, width=700, height=300)

    # "Verileri Listele" butonu
    button_listele = tk.Button(frame_sag_alt, text="Verileri Listele",width=50, command=verileri_listele)
    button_listele.place(x=0, y=0)

    button_sil = tk.Button(frame_sag_alt, text="Kayıt Sil",command=kayit_sil,width=50)
    button_sil.place(x=350, y=0)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def paket():
    def paket_ekle():
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="havaalani"
        )
        mycursor = mydb.cursor()

        packet=paket_adi.get()
        koltuk=bg2.get()
        bagaj=bagaj_hakki.get()
        ucretim=ucret.get()
        ucus=ucus_adi.get()
        ikram=ikram_servis.get()
        
        
    
        
        a=1
        
    # Herhangi bir boşalan varmı kontrol sağlar
        dizi = [packet,koltuk,bagaj,ucretim,ucus,ikram]
        
        for i in dizi:
            if  i.strip() == '': #strip() fonksiyonu: bir kelime alıyor sağındaki ve solundaki boşlukları siliyor yaptığı bu 
             messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
            
             a += 1
             break

        #Girilen şehir ismi ve boş bir alan yoksa kayıt eder    
        if a == 1 :
            insert1 = "INSERT INTO paketdetay (PAKET_ADI, IKRAM_SERVIS, BAGAJ_HAKKI, bg2, UCRET) VALUES (%s, %s, %s, %s, %s)"
            degerler1 = (packet,ikram,bagaj,koltuk,ucretim)
            mycursor.execute(insert1, degerler1)

            insert2 = "INSERT INTO ucussinifi (paket) VALUES (%s)"
            mycursor.execute(insert2, (ucus, ))


            messagebox.showinfo("Bilgi", "Paket başarıyla eklendi")
            mydb.commit()
            mydb.close()


    def verileri_listele():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="havaalani"
        )
        mycursor = mydb.cursor()

        # Veritabanındaki kayıtları seç
        join = "SELECT S.ID, C.ID, S.PAKET_ADI, S.IKRAM_SERVIS, S.BAGAJ_HAKKI, S.bg2, S.UCRET, C.paket FROM havaalani.paketdetay S INNER JOIN havaalani.ucussinifi C ON S.ID=C.ID"
        mycursor.execute(join)
        kayıtlar = mycursor.fetchall()

        # Treeview'i temizle
        for row in tree.get_children():
            tree.delete(row)

        #mycursor kayıtları Treeview'e ekle
        for kayıtlar in kayıtlar:
            tree.insert("", "end", values=kayıtlar)

        mydb.close()



    def kayit_sil():
        selected_item = tree.selection()

        if not selected_item:
            messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
            return

        confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

        if confirm:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="havaalani"
            )
            mycursor = mydb.cursor()

            # Seçilen kaydın KALKIS_SEHIR_ID değerini al
            
            selected_id = tree.item(selected_item, 'values')[0]
            
            selected_id2 = tree.item(selected_item, 'values')[1]

            # Kaydı sil
            mycursor.execute("DELETE FROM paketdetay WHERE ID = %s", (selected_id,))
            mycursor.execute("DELETE FROM ucussinifi WHERE ID = %s", (selected_id2,))

            mydb.commit()
            mydb.close()

            # Kayıtları güncelle
            verileri_listele()





    frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
    frame_sol.place(x=0,y=0)

    my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))

    image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
    image_label.place(x=30,y=20)

    label_text = tk.StringVar()
    label_text.set(kullanici)    

    label1=customtkinter.CTkLabel(master=frame_sol,textvariable=label_text,font=('century gothic',17))
    label1.place(x=110,y=35)

    Btn_sefer=customtkinter.CTkButton(master=frame_sol,text="Sefer ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=sefer_)
    Btn_sefer.place(x=50,y=200)

    Btn_ucak=customtkinter.CTkButton(master=frame_sol,text="Uçak ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=ucak)
    Btn_ucak.place(x=50,y=260)

    Btn_paket=customtkinter.CTkButton(master=frame_sol,text="Paket ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=paket)
    Btn_paket.place(x=50,y=320)

    Btn_calisan=customtkinter.CTkButton(master=frame_sol,text="Çalışan ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=calisan)
    Btn_calisan.place(x=50,y=380)

    Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Çıkış yap",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=login_)
    Btn_cıkıs.place(x=50,y=630)

    #Bt1=customtkinter.CTkButton(master=frame_sol,width=250,height=30,text="Bora Altun",compound="left",text_color="white",bg_color="#1f2021",fg_color="#1f2021",hover_color="#1f2021")
    #Bt1.place(x=70,y=10)



    frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=400,fg_color="white")
    frame_sag_ust.place(x=300,y=0)

    label1=customtkinter.CTkLabel(master=frame_sag_ust,text="PAKET EKLE",font=('century gothic',25),text_color="black")
    label1.place(x=300,y=5)


    paket_adi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Paket Adı :",font=('century gothic',16),text_color="black")
    paket_adi_label.place(x=50,y=50)
    paket_adi=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    paket_adi.place(x=180,y=50)

    bagaj_hakki_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Bagaj Hakkı :",font=('century gothic',16),text_color="black")
    bagaj_hakki_label.place(x=50,y=100)
    bagaj_hakki=customtkinter.CTkComboBox(master=frame_sag_ust,values=["10kg","20kg","30kg"],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    bagaj_hakki.place(x=180,y=100)

    bg2_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Koltuk Seçimi :",font=('century gothic',16),text_color="black")
    bg2_label.place(x=50,y=150)
    bg2=customtkinter.CTkComboBox(master=frame_sag_ust,values=["ekonomik","standart","vip"],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    bg2.place(x=180,y=150)

    ucret_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Ücret:",font=('century gothic',16),text_color="black")
    ucret_label.place(x=50,y=200)
    ucret=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    ucret.place(x=180,y=200)

    ucus_adi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Uçuş sınıfı:",font=('century gothic',16),text_color="black")
    ucus_adi_label.place(x=50,y=250)
    ucus_adi=customtkinter.CTkComboBox(master=frame_sag_ust,values=["ekonomi","business","first class"],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    ucus_adi.place(x=180,y=250)

    ikram_servis_label=customtkinter.CTkLabel(master=frame_sag_ust,text="İkram Servis :",font=('century gothic',16),text_color="black")
    ikram_servis_label.place(x=50,y=300)
    ikram_servis=customtkinter.CTkComboBox(master=frame_sag_ust,values=["var","yok"],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    ikram_servis.place(x=180,y=300)

    Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Paket ekle",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17), command=paket_ekle)
    Button1.place(x=360,y=350)

    frame_sag_alt=customtkinter.CTkFrame(master=app,width=700,height=300,fg_color="#e6e8e7",bg_color="#e6e8e7")
    frame_sag_alt.place(x=300,y=400)

    # ... Diğer arayüz elemanları ...

    # Treeview widget'i oluştur
    tree_columns = ("PAKET_ID", "SINIF_ID", "PAKET_ADI", "IKRAM_SERVIS", "BAGAJ_HAKKI", "KOLTUK_TUR", "UCRET", "paket")
    tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings")

    # Treeview kolon başlıklarını ayarla
    for col in tree_columns:
        tree.heading(col, text=col)
        tree.column(col, width=40)

    # Treeview'i paketle ve yerleştir
    tree.place(x=0, y=25, width=700, height=300)

    # "Verileri Listele" butonu
    button_listele = tk.Button(frame_sag_alt, text="Verileri Listele",width=50, command=verileri_listele)
    button_listele.place(x=0, y=0)

    button_sil = tk.Button(frame_sag_alt, text="Kayıt Sil",command=kayit_sil,width=50)
    button_sil.place(x=350, y=0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def ucak():
    def ucak_ekle():
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="havaalani"
        )
        mycursor = mydb.cursor()

        marka=marka_ismi.get()
        modeli=model.get()
        kuyruk_no=kuyruk_numarasi.get()
        
    
        
        a=1
        
    # Herhangi bir boşalan var mı kontrol sağlar
        dizi = [marka,modeli,kuyruk_no]
        
        for i in dizi:
            if  i.strip() == '': #strip() fonksiyonu: bir kelime alıyor sağındaki ve solundaki boşlukları siliyor yaptığı bu 
             messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
            
             a += 1
             break

        #Girilen şehir ismi ve boş bir alan yoksa kayıt eder    
        if a == 1 :
            insert1 = "INSERT INTO ucaklar (MODEL, KUYRUK_NUMARASI) VALUES (%s, %s)"
            degerler1 = (modeli,kuyruk_no)
            mycursor.execute(insert1, degerler1)

            insert2 = "INSERT INTO ucakmarka (MARKA_ISMI) VALUES (%s)"
            mycursor.execute(insert2, (marka, ))


            messagebox.showinfo("Bilgi", "Paket başarıyla eklendi")
            mydb.commit()
            mydb.close()

            
    def verileri_listele():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="havaalani"
        )
        mycursor = mydb.cursor()

        # Veritabanındaki kayıtları seç
        join = "SELECT U.ID, M.ID, M.MARKA_ISMI, U.MODEL, U.KUYRUK_NUMARASI FROM havaalani.ucaklar U INNER JOIN havaalani.ucakmarka M ON U.ID=M.ID"
        mycursor.execute(join)
        kayıtlar = mycursor.fetchall()

        # Treeview'i temizle
        for row in tree.get_children():
            tree.delete(row)

        #mycursor kayıtları Treeview'e ekle
        for kayıtlar in kayıtlar:
            tree.insert("", "end", values=kayıtlar)

        mydb.close()



    def kayit_sil():
        selected_item = tree.selection()

        if not selected_item:
            messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
            return

        confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

        if confirm:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="havaalani"
            )
            mycursor = mydb.cursor()

            # Seçilen kaydın KALKIS_SEHIR_ID değerini al
            
            selected_id = tree.item(selected_item, 'values')[0]
            
            selected_id2 = tree.item(selected_item, 'values')[1]

            # Kaydı sil
            mycursor.execute("DELETE FROM ucaklar WHERE ID = %s", (selected_id,))
            mycursor.execute("DELETE FROM ucakmarka WHERE ID = %s", (selected_id2,))

            mydb.commit()
            mydb.close()

            # Kayıtları güncelle
            verileri_listele()





    frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
    frame_sol.place(x=0,y=0)

    my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))

    image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
    image_label.place(x=30,y=20)
    label_text = tk.StringVar()
    label_text.set(kullanici)    
    label1=customtkinter.CTkLabel(master=frame_sol,textvariable=label_text,font=('century gothic',17))
    label1.place(x=110,y=35)

    Btn_sefer=customtkinter.CTkButton(master=frame_sol,text="Sefer ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=sefer_)
    Btn_sefer.place(x=50,y=200)

    Btn_ucak=customtkinter.CTkButton(master=frame_sol,text="Uçak ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=ucak)
    Btn_ucak.place(x=50,y=260)

    Btn_paket=customtkinter.CTkButton(master=frame_sol,text="Paket ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=paket)
    Btn_paket.place(x=50,y=320)

    Btn_calisan=customtkinter.CTkButton(master=frame_sol,text="Çalışan ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=calisan)
    Btn_calisan.place(x=50,y=380)

    Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Çıkış yap",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=login_)
    Btn_cıkıs.place(x=50,y=630)

    #Bt1=customtkinter.CTkButton(master=frame_sol,width=250,height=30,text="Bora Altun",compound="left",text_color="white",bg_color="#1f2021",fg_color="#1f2021",hover_color="#1f2021")
    #Bt1.place(x=70,y=10)



    frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=400,fg_color="white")
    frame_sag_ust.place(x=300,y=0)

    label1=customtkinter.CTkLabel(master=frame_sag_ust,text="UCAK EKLE",font=('century gothic',25),text_color="black")
    label1.place(x=300,y=5)


    marka_ismi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Marka :",font=('century gothic',16),text_color="black")
    marka_ismi_label.place(x=50,y=50)
    marka_ismi=customtkinter.CTkComboBox(master=frame_sag_ust,values=["Boeing","Airbus","Embraer","Bombardier","Cessna","Gulfstream"],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    marka_ismi.place(x=180,y=50)

    model_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Model :",font=('century gothic',16),text_color="black")
    model_label.place(x=50,y=100)
    model=customtkinter.CTkComboBox(master=frame_sag_ust,values=["737","747", "777", "787 Dreamliner", "A320", "A330", "A350", "A380", "E-Jet E2 series", "ERJ145", "CRJ Series", "Challenger", "Global Express", "172", "Citation series", "G550", "G650"],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    model.place(x=180,y=100)

    kuyruk_numarasi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kuyruk no :",font=('century gothic',16),text_color="black")
    kuyruk_numarasi_label.place(x=50,y=150)
    kuyruk_numarasi=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    kuyruk_numarasi.place(x=180,y=150)


    Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Uçak ekle",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17), command=ucak_ekle)
    Button1.place(x=360,y=200)

    frame_sag_alt=customtkinter.CTkFrame(master=app,width=700,height=300,fg_color="#e6e8e7",bg_color="#e6e8e7")
    frame_sag_alt.place(x=300,y=400)

    # ... Diğer arayüz elemanları ...

    # Treeview widget'i oluştur
    tree_columns = ("UCAK_ID", "MARKA_ID", "MARKA_ISMI", "MODEL", "KUYRUK_NUMARASI")
    tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings")

    # Treeview kolon başlıklarını ayarla
    for col in tree_columns:
        tree.heading(col, text=col)
        tree.column(col, width=60)

    # Treeview'i paketle ve yerleştir
    tree.place(x=0, y=25, width=700, height=300)

    # "Verileri Listele" butonu
    button_listele = tk.Button(frame_sag_alt, text="Verileri Listele",width=50, command=verileri_listele)
    button_listele.place(x=0, y=0)

    button_sil = tk.Button(frame_sag_alt, text="Kayıt Sil",command=kayit_sil,width=50)
    button_sil.place(x=350, y=0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def bilet():
            clear_widgets(app)
            app.tkraise()
            global kullanici
            for row in verilerim:  
              kullanici=row[1]+ " " +row[2]

           
 

            def verileri_listele():
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="havaalani"
                )
                mycursor = mydb.cursor()

                # Veritabanındaki kayıtları seç
                mycursor.execute("SELECT ID,KALKIS_SEHIR_ID, VARIS_SEHIR_ID, KUYRUK_NO, KALKIS_ZAMANI, BILET_TUTARI, YOLCU_SAYISI FROM seferler")
                kayıtlar = mycursor.fetchall()

                # Treeview'i temizle
                for row in tree.get_children():
                    tree.delete(row)

                #mycursor kayıtları Treeview'e ekle
                for kayıtlar in kayıtlar:
                    tree.insert("", "end", values=kayıtlar)

                mydb.close()



            def filtre():
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="havaalani"
                )
                mycursor = mydb.cursor()
                kalkis_nokta=Kalkıs_noktasi.get()
                varis_nokta=Varis_noktasi.get()
                
                
                

                select="SELECT ID FROM sehir WHERE SEHIR_ISMI=%s"
                mycursor.execute(select,(kalkis_nokta,))
                Kalkis = mycursor.fetchone()
                mycursor.execute(select,(varis_nokta,))
                Varis=mycursor.fetchone()

                #girilen şehir ismi doğrumu diye kontrol eder
                if Kalkis is  None:
                    messagebox.showerror("Uyarı", "Kalkış şehrini kontrol ediniz")
                if Varis is  None:
                    messagebox.showerror("Uyarı", "Varış şehrini kontrol ediniz")

                # Veritabanındaki kayıtları seç
                sql="SELECT ID,KALKIS_SEHIR_ID, VARIS_SEHIR_ID, KUYRUK_NO, KALKIS_ZAMANI, BILET_TUTARI, YOLCU_SAYISI FROM seferler WHERE KALKIS_SEHIR_ID=%s and VARIS_SEHIR_ID=%s"
                deger=(Kalkis[0],Varis[0])
                mycursor.execute(sql,deger)
                kayıtlar = mycursor.fetchall()

                 

                # Treeview'i temizle
                for row in tree.get_children():
                    tree.delete(row)

                #mycursor kayıtları Treeview'e ekle
                for kayıtlar in kayıtlar:
                    tree.insert("", "end", values=kayıtlar)

                mydb.close()

            def sefer_sec():
                selected_item = tree.selection()

                if not selected_item:
                    messagebox.showwarning("Uyarı", "Lütfen sefer seçin.")
                    return

                confirm = messagebox.askyesno("Onay", "Bu seferi seçmek istediğinizden emin misiniz ?")

                if confirm:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="1234",
                        database="havaalani"
                    )
                    mycursor = mydb.cursor()

                    # Seçilen kaydın KALKIS_SEHIR_ID değerini al
                    selected_id = tree.item(selected_item, 'values')[0]

                    # Kaydı sil
                    mycursor.execute("SELECT BILET_TUTARI FROM seferler WHERE ID = %s", (selected_id,))
                    global tutar
                    tutar=mycursor.fetchone()


                    mydb.commit()
                    mydb.close()

                    # Kayıtları güncelle
                    verileri_listele()



            

            frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
            frame_sol.place(x=0,y=0)

            my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))

            image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
            image_label.place(x=30,y=20)
            
            label_text = tk.StringVar()
            label_text.set(kullanici)    
            label1=customtkinter.CTkLabel(master=frame_sol,textvariable=label_text,font=('century gothic',17))
            label1.place(x=110,y=35)

            Btn_sefer=customtkinter.CTkButton(master=frame_sol,text="Bilet al",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=bilet)
            Btn_sefer.place(x=50,y=200)

            Btn_ucak=customtkinter.CTkButton(master=frame_sol,text="Ödeme bilgileri",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=odeme)
            Btn_ucak.place(x=50,y=260)

            Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Çıkış yap",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=login_)
            Btn_cıkıs.place(x=50,y=630)

            def hesapla():

                hes1=bagaj_hakki_label.get()
                hes2=bg2_label.get()
                hes3=ikram_servis_label.get()
                hes4=paket_label.get()
                hes5=hes1+hes2+hes3+hes4+tutar[0]
                label_text = customtkinter.IntVar()
                label_text.set(hes5)    
                label1=customtkinter.CTkLabel(master=frame_sag_ust,textvariable=label_text,font=('century gothic',17),fg_color="#808080",width=300,corner_radius=10,bg_color="white")
                label1.place(x=400,y=350)




            frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=500,fg_color="white")
            frame_sag_ust.place(x=300,y=200)


            Kalkıs_noktasi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kalkış nokta :",font=('century gothic',16),text_color="black")
            Kalkıs_noktasi_label.place(x=5,y=50)
            Kalkıs_noktasi=customtkinter.CTkEntry(master=frame_sag_ust,width=210,border_color="white",font=('Microsoft YaHei UI Lıght',16),fg_color="#b2b2b2")
            Kalkıs_noktasi.place(x=105,y=50)

            Varis_noktasi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Varış nokta :",font=('century gothic',16),text_color="black")
            Varis_noktasi_label.place(x=330,y=50)
            Varis_noktasi=customtkinter.CTkEntry(master=frame_sag_ust,width=210,border_color="white",font=('Microsoft YaHei UI Lıght',16),fg_color="#b2b2b2")
            Varis_noktasi.place(x=430,y=50)

            Button1=customtkinter.CTkButton(master=frame_sag_ust,text="S",width=40,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',16),command=filtre)
            Button1.place(x=650,y=50)

            label1=customtkinter.CTkLabel(master=frame_sag_ust,text="Ek Özellikler",font=('century gothic',25),text_color="black")
            label1.place(x=300,y=100)
            

            bagaj_hakki_label=customtkinter.IntVar(value=0)
            bagaj_hakki=customtkinter.CTkCheckBox(master=frame_sag_ust,text="Bagaj hakkı 20kg (+200)",variable=bagaj_hakki_label, onvalue=200, offvalue=0,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17))
            bagaj_hakki.place(x=80,y=150)

            bg2_label=customtkinter.IntVar(value=0)
            bg2=customtkinter.CTkCheckBox(master=frame_sag_ust,text="Bagaj hakkı 40kg (+400)",variable=bg2_label, onvalue=400, offvalue=0,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17))
            bg2.place(x=80,y=200)

            ikram_servis_label=customtkinter.IntVar(value=0)
            ikram_servis=customtkinter.CTkCheckBox(master=frame_sag_ust,text="İkram servis (+400)",variable=ikram_servis_label, onvalue=400, offvalue=0,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17))
            ikram_servis.place(x=80,y=250)

            paket_label=customtkinter.IntVar(value=0)
            paket=customtkinter.CTkCheckBox(master=frame_sag_ust,text="Premium paket (+1000)",variable=paket_label, onvalue=1000, offvalue=0,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17))
            paket.place(x=80,y=300)

            label1=customtkinter.CTkLabel(master=frame_sag_ust,text=" 0 TL ",font=('century gothic',17),fg_color="#808080",width=300,corner_radius=10,bg_color="white")
            label1.place(x=400,y=350)

            Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Hesapla",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17),command=hesapla)
            Button1.place(x=100,y=400)

            Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Ödeme yap",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17))
            Button1.place(x=400,y=400)


            frame_sag_alt=customtkinter.CTkFrame(master=app,width=700,height=200,fg_color="#e6e8e7",bg_color="#e6e8e7")
            frame_sag_alt.place(x=300,y=0)

            # ... sefer seç ...

            # Treeview widget'i oluştur
            tree_columns = ("ID","KALKIS_SEHIR_ID", "VARIS_SEHIR_ID", "KUYRUK_NO", "KALKIS_ZAMANI", "BILET_TUTARI", "YOLCU_SAYISI")
            tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings")

            # Treeview kolon başlıklarını ayarla
            for col in tree_columns:
                tree.heading(col, text=col)
                tree.column(col, width=40)

            # Treeview'i paketle ve yerleştir
            tree.place(x=0, y=25, width=700, height=300)

            # "Verileri Listele" butonu

            button_sil = tk.Button(frame_sag_alt, text="Sefer seç",command=sefer_sec,width=100)
            button_sil.place(x=0, y=0)

            verileri_listele()
            
            

login_()
app.mainloop()    



