from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
import sys
from mysql.connector import cursor
from datetime import datetime
from tkcalendar import Calendar
import datetime
import tkinter as tk
from tkinter import ttk

pen = Tk()
pen.title("DOKUZ EYLÜL ÜNİVERSİTE VE ARAŞTIRMA HASTANESİ")
myFont = ("Helvetica", 12, "italic", "bold")
carpici_font = ("Helvetica", 20, "bold", "italic", "underline")
pen.resizable(width=False, height=False)
pen.config(bg="Light Sea Green")
icon_path = "images/penİco.ico"
pen.iconbitmap(icon_path)

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='hastane'
)

cursor = conn.cursor()

def merkez_pencere(pencere, genislik, yukseklik):
    ekran_genisligi = pencere.winfo_screenwidth()
    ekran_yuksekligi = pencere.winfo_screenheight()
    x = (ekran_genisligi - genislik) // 2
    y = (ekran_yuksekligi - yukseklik) // 2
    pencere.geometry(f"{genislik}x{yukseklik}+{x}+{y}")



def programdan_cik():
    pen.destroy()
    sys.exit()
def hastaGirisForm():
    def clear_entries():
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
    win = Toplevel()
    has.withdraw()
    win.config(bg="Light Sea Green")
    win.resizable(width=False, height=False)
    win.title("Hasta Giriş")
    pencere_genisligi1 = 400
    pencere_yuksekligi1 = 400
    merkez_pencere(win, pencere_genisligi1, pencere_yuksekligi1)
    icon_path1 = "images/iconico32.ico"
    win.iconbitmap(icon_path1)
    win.protocol("WM_DELETE_WINDOW", lambda: on_closing_two(win))

    hastagpng_original = Image.open("images/hastaLog.png")
    hastagpng = ImageTk.PhotoImage(hastagpng_original.resize((128, 128)))
    hastagpng_label = tk.Label(win, image=hastagpng)
    hastagpng_label.grid(row=0, column=0, pady=5, padx=5)

    Label(win, text="Kullanıcı Adı:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=1, column=0, pady=10)
    username_entry = Entry(win, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    username_entry.grid(row=1, column=1, pady=5)
    Label(win, text="Şifre:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=2, column=0, pady=10)
    password_entry = Entry(win, show="*", width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    password_entry.grid(row=2, column=1, pady=5)
    login_button = Button(win, bg="Floral White", fg="Gray21", borderwidth=7, text="Giriş Yap", command=lambda: login_clicked(username_entry, password_entry, win))
    clear_button = Button(win, bg="Floral White", fg="Gray21", borderwidth=7, text="Temizle", command=clear_entries)
    clear_button.grid(row=3, column=1, sticky=E, pady=10, padx=10)
    login_button.grid(row=3, column=1, pady=10, padx=10, sticky=W)
    win.mainloop()
def on_closing_two(win):
    win.destroy()
    pen.destroy()
def login_clicked(username_entry, password_entry, win):
    kullanici_adi = username_entry.get()
    sifre = password_entry.get()
    sql = "SELECT * FROM hastalar WHERE kullanici_adi = %s AND sifre = %s"
    values = (kullanici_adi, sifre)
    try:
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if result:
            show_success_message("Giriş Başarılı")
            win.destroy()
            hastaForm(result)
        else:
            messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre")
    except Exception as e:
        print(f"Giriş kontrolünde hata oluştu: {e}")
        messagebox.showerror("Hata", "Giriş kontrolünde bir hata oluştu")
def show_success_message(message):
    messagebox.showinfo("Başarılı", message)
def hastaKayitForm():
    global wen
    def clear_entries():
        for entry in entry_dict.values():
            entry.delete(0, 'end')
    wen = Toplevel()
    has.withdraw()
    wen.config(bg="Light Sea Green")
    wen.resizable(width=False, height=False)
    wen.title("Hasta Kayıt")
    pencere_genisligi6 = 700
    pencere_yuksekligi6 = 500
    merkez_pencere(wen, pencere_genisligi6, pencere_yuksekligi6)
    icon_path1 = "images/iconico32.ico"
    wen.iconbitmap(icon_path1)
    wen.protocol("WM_DELETE_WINDOW", lambda: on_closing_one(wen))
    hastapngg_original = Image.open("images/user_102890.png")
    hastapngg = ImageTk.PhotoImage(hastapngg_original.resize((96, 96)))
    hastapngg_label = tk.Label(wen, image=hastapngg)
    hastapngg_label.grid(row=0, column=0, pady=10, padx=50)

    Label(wen, text="Ad:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=1, column=0, pady=10, padx=5)
    ad_entry = Entry(wen, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    ad_entry.grid(row=1, column=1, pady=10, padx=5)
    Label(wen, text="Soyad:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=1, column=2, pady=10, padx=5)
    soyad_entry = Entry(wen, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    soyad_entry.grid(row=1, column=3, pady=10, padx=5)
    Label(wen, text="TC Kimlik:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=2, column=0, pady=10, padx=5)
    tc_kimlik_entry = Entry(wen, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    tc_kimlik_entry.grid(row=2, column=1, pady=10, padx=5)
    Label(wen, text="Doğum Tarihi:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=2, column=2, pady=10, padx=5)
    dogum_tarihi_entry = Entry(wen, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    dogum_tarihi_entry.grid(row=2, column=3, pady=10, padx=5)
    Label(wen, text="Cinsiyet:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=3, column=0, pady=10, padx=5)
    cinsiyet_entry = Entry(wen, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    cinsiyet_entry.grid(row=3, column=1, pady=10, padx=5)
    Label(wen, text="Telefon:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=3, column=2, pady=10, padx=5)
    telefon_entry = Entry(wen, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    telefon_entry.grid(row=3, column=3, pady=10, padx=5)
    Label(wen, text="Email:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=4, column=0, pady=10, padx=5)
    email_entry = Entry(wen, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    email_entry.grid(row=4, column=1, pady=10, padx=5)
    Label(wen, text="Adres:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=4, column=2, pady=10, padx=5)
    adres_entry = Entry(wen, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    adres_entry.grid(row=4, column=3, pady=10, padx=5)
    Label(wen, text="Kullanıcı Adı:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=5, column=0, pady=10, padx=5)
    kullanici_adi_entry = Entry(wen, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    kullanici_adi_entry.grid(row=5, column=1, pady=10, padx=5)
    Label(wen, text="Şifre:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=5, column=2, pady=10, padx=5)
    sifre_entry = Entry(wen, show="*", width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    sifre_entry.grid(row=5, column=3, pady=10, padx=5)
    save_button = Button(wen, bg="Floral White", fg="Gray21", borderwidth=7, text="Kaydet", command=lambda: hasta_kayit(entry_dict))
    save_button.grid(row=6, column=3, pady=10, padx=5,sticky=W)
    clear_button = Button(wen, bg="Floral White", fg="Gray21", borderwidth=7, text="Temizle", command=clear_entries)
    clear_button.grid(row=6, column=3, pady=10, padx=5,sticky=E)
    entry_dict = {
        'ad': ad_entry,
        'soyad': soyad_entry,
        'tc_kimlik': tc_kimlik_entry,
        'dogum_tarihi': dogum_tarihi_entry,
        'cinsiyet': cinsiyet_entry,
        'telefon': telefon_entry,
        'email': email_entry,
        'adres': adres_entry,
        'kullanici_adi': kullanici_adi_entry,
        'sifre': sifre_entry
    }
    wen.mainloop()
def hasta_kayit(entry_dict):
    ad = entry_dict['ad'].get()
    soyad = entry_dict['soyad'].get()
    tc_kimlik = entry_dict['tc_kimlik'].get()
    dogum_tarihi = entry_dict['dogum_tarihi'].get()
    cinsiyet = entry_dict['cinsiyet'].get()
    telefon = entry_dict['telefon'].get()
    email = entry_dict['email'].get()
    adres = entry_dict['adres'].get()
    kullanici_adi = entry_dict['kullanici_adi'].get()
    sifre = entry_dict['sifre'].get()
    if not ad or not soyad or not tc_kimlik or not dogum_tarihi or not cinsiyet or not telefon or not email or not adres or not kullanici_adi or not sifre:
        show_error_message("Lütfen tüm bilgileri doldurun.")
        return
    sql = "INSERT INTO hastalar (ad, soyad, tc_kimlik, dogum_tarihi, cinsiyet, telefon, email, adres, kullanici_adi, sifre) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (ad, soyad, tc_kimlik, dogum_tarihi, cinsiyet, telefon, email, adres, kullanici_adi, sifre)
    try:
        cursor.execute(sql, values)
        conn.commit()
        show_success_message("Hasta kaydı başarıyla eklendi.")
        wen.destroy()
        hastaGirisForm()
    except Exception as e:
        show_success_message(f"Hasta kaydı eklenirken hata oluştu: {e}")
def on_closing_one(wen):
    wen.destroy()
    pen.destroy()


def get_all_doctors():
    try:
        sorgu = "SELECT ad, uzmanlik_alani FROM doktorlar"
        cursor.execute(sorgu)
        doktorlar = cursor.fetchall()
        doktorlar_dict = {doktor[0]: doktor[1] for doktor in doktorlar}
        return doktorlar_dict
    except Exception as e:
        print("Doktorlar çekilirken hata oluştu:", str(e))
        return {}




def hastaForm(result):

    def update_doktor_combo(event):
        selected_uzmanlik = uzmanlik_combo.get()
        doktorlar = get_doktorlar_by_uzmanlik(selected_uzmanlik)
        doktorlar_combo["values"] = doktorlar

    def randevu_al(result, selected_doktor, sikayet, selected_date_str):
        # Eğer bir tarih seçilmemişse hata mesajı göster
        if not selected_date_str:
            messagebox.showerror("Hata", "Lütfen bir tarih seçin.")
            return

        # Seçilen tarihi çözümlemeye çalış
        try:
            selected_date = datetime.datetime.strptime(selected_date_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            messagebox.showerror("Hata", "Geçersiz tarih formatı. Lütfen doğru bir tarih seçin.")
            return

        # Seçilen tarihi istenen formata çevir
        tarih = selected_date.strftime("%Y-%m-%d %H:%M:%S")

        # Sonuçtan hasta ID'sini al
        hasta_id = result[0]

        # Seçilen doktorun adını kullanarak doktor ID'sini al
        doktor_id = get_doktor_id(selected_doktor)

        # Eğer doktor_id geçerli değilse hata mesajı göster
        if doktor_id is None:
            messagebox.showerror("Hata", "Geçersiz doktor seçimi.")
            return

        # Randevu durumunu "Planlanan" olarak ayarla
        durum = "Planlanan"

        # Randevuyu veritabanına ekleyin
        sorgu = "INSERT INTO randevular (tarih, hasta_id, doktor_id, durum, sikayet) VALUES (%s, %s, %s, %s, %s)"
        veri = (tarih, hasta_id, doktor_id, durum, sikayet)
        cursor.execute(sorgu, veri)
        conn.commit()

        # Başarı mesajı göster
        messagebox.showinfo("Başarılı", "Randevu başarıyla alındı.")

        # Gösterilen randevuları yenile
        load_randevular()

    def get_doktor_id(doktor_adi):
        sorgu = "SELECT doktor_id FROM doktorlar WHERE ad = %s"
        cursor.execute(sorgu, (doktor_adi,))
        doktor_id = cursor.fetchone()
        return doktor_id[0] if doktor_id else None

    def get_doktorlar_by_uzmanlik(uzmanlik_alani):
        sorgu = "SELECT ad FROM doktorlar WHERE uzmanlik_alani LIKE %s"
        cursor.execute(sorgu, (f"%{uzmanlik_alani}%",))
        doktorlar = cursor.fetchall()
        return [doktor[0] for doktor in doktorlar]

    def get_all_uzmanliklar():
        sorgu = "SELECT DISTINCT uzmanlik_alani FROM doktorlar"
        cursor.execute(sorgu)
        uzmanliklar = cursor.fetchall()
        return [uzmanlik[0] for uzmanlik in uzmanliklar]

    def load_randevular():
        hasta_id = result[0]
        sorgu = "SELECT tarih, doktor_id, durum, sikayet FROM randevular WHERE hasta_id = %s AND (durum = 'Planlanan' OR durum = 'Onaylanan')"
        cursor.execute(sorgu, (hasta_id,))
        randevular = cursor.fetchall()
        for row in randevu_tree.get_children():
            randevu_tree.delete(row)
        for randevu in randevular:
            randevu_tree.insert("", "end", values=randevu)

    def load_completed_randevular():
        hasta_id = result[0]
        sorgu = "SELECT tarih, doktor_id, durum ,sikayet FROM randevular WHERE hasta_id = %s AND durum = 'Tamamlandı'"
        cursor.execute(sorgu, (hasta_id,))
        completed_randevular = cursor.fetchall()
        for row in completed_randevu_tree.get_children():
            completed_randevu_tree.delete(row)
        for randevu in completed_randevular:
            completed_randevu_tree.insert("", "end", values=randevu)

    def temizle():
        uzmanlik_combo.set('')
        doktorlar_combo.set('')
        sikayet_entry.delete(0, 'end')
        date_entry.delete(0, 'end')


    hastaform = Toplevel()
    hastaform.state("zoomed")
    hastaform.title("HastaForm")
    hastaform.resizable(width=True, height=True)
    hastaform.config(bg="Light Sea Green")
    icon_path1 = "images/iconico32.ico"
    hastaform.iconbitmap(icon_path1)

    hasta_bilgileri_frame = Frame(hastaform, padx=40, pady=20, bg="Medium Turquoise")
    hasta_bilgileri_frame.grid(row=0, column=1, padx=40, pady=10)

    hastapng_original = Image.open("images/17_113699 (1).png")
    hastapng = ImageTk.PhotoImage(hastapng_original.resize((128, 128)))
    hastapng_label = tk.Label(hasta_bilgileri_frame, image=hastapng)
    hastapng_label.grid(row=0, column=0,pady=10,padx=5)

    Label(hasta_bilgileri_frame, text="Hasta Bilgileri", font=("Helvetica", 25), bg="Turquoise4", fg="white").grid(row=1, column=0, pady=0)
    hasta_ad_soyad_tc_label = Label(hasta_bilgileri_frame, text=f"Ad: {result[1]}\nSoyad: {result[2]}\nTC No: {result[3]}", bg="Turquoise4", fg="white", font=("Helvetica", 20))
    hasta_ad_soyad_tc_label.grid(row=2, column=0, pady=5, sticky=W)

    randevu_paneli_frame = Frame(hastaform, padx=60, pady=20, bg="Medium Turquoise")
    randevu_paneli_frame.grid(row=0, column=0, sticky=W, padx=30, pady=20)
    Label(randevu_paneli_frame, text="Randevu Paneli", font=("Helvetica", 25), bg="Turquoise4", fg="white").grid(row=1, column=0, pady=5, sticky=W)
    uzmanliklar = get_all_uzmanliklar()
    uzmanlik_combo = ttk.Combobox(randevu_paneli_frame, values=uzmanliklar, state="readonly")
    Label(randevu_paneli_frame, text="Branş :", font=("Helvetica", 20), bg="Turquoise4", fg="white").grid(row=2, column=0, pady=5, sticky=W)
    uzmanlik_combo.grid(row=2, column=1, pady=5, sticky=W)
    doktorlar_combo = ttk.Combobox(randevu_paneli_frame, state="readonly")
    Label(randevu_paneli_frame, text="Doktorlar :", font=("Helvetica", 20), bg="Turquoise4", fg="white").grid(row=3, column=0, pady=5, sticky=W)
    doktorlar_combo.grid(row=3, column=1, pady=5, sticky=W)
    uzmanlik_combo.bind("<<ComboboxSelected>>", update_doktor_combo)
    Label(randevu_paneli_frame, text="Şikayet :", font=("Helvetica", 20), bg="Turquoise4", fg="white").grid(row=4, column=0, pady=5, sticky=W)
    sikayet_entry = Entry(randevu_paneli_frame, width=30, borderwidth=5, bg="Floral White", fg="Black")
    sikayet_entry.grid(row=4, column=1, pady=5, sticky=W)
    Label(randevu_paneli_frame, text="Tarih :", font=("Helvetica", 20), bg="Turquoise4", fg="white").grid(row=5, column=0, pady=5, sticky=W)

    def open_calendar():
        def on_date_select(calendar, top):
            selected_date = calendar.selection_get()
            date_entry.config(state="normal")
            date_entry.delete(0, END)
            date_entry.insert(0, selected_date.strftime("%Y-%m-%d %H:%M:%S"))
            top.destroy()
        top = Toplevel(hastaform)
        top.title("Tarih Seç")
        top.geometry("300x300")
        cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1", year=2023, month=12, day=15)
        cal.pack(fill="both", expand=True)
        select_button = Button(top, text="Seç", bg="Floral White", fg="Gray21", borderwidth=7, command=lambda: on_date_select(cal, top))
        select_button.pack()
        def on_closing():
            top.destroy()
        top.protocol("WM_DELETE_WINDOW", on_closing)

    tarihButon = Button(randevu_paneli_frame, text="Tarih seç", bg="Floral White", fg="Gray21", borderwidth=7, command=open_calendar)
    tarihButon.grid(row=5, column=2, pady=5, padx=5, sticky=W)
    date_entry = Entry(randevu_paneli_frame, width=30, borderwidth=5, bg="Floral White", fg="Black")
    date_entry.grid(row=5, column=1, pady=5, sticky=W)
    today = datetime.datetime.today()
    date_entry.insert(0, today.strftime("%Y-%m-%d %H:%M:%S"))
    randevupng_original = Image.open("images/coronovirus_call_doctor_hospital_icon_134909.png")
    randevupng = ImageTk.PhotoImage(randevupng_original.resize((96, 96)))
    randevupng_label = tk.Label(randevu_paneli_frame, image=randevupng)
    randevupng_label.grid(row=1, column=3, pady=5, padx=5, sticky=E)
    Button(randevu_paneli_frame, text="Randevu Al", bg="Floral White", fg="Gray21", borderwidth=7, command=lambda: randevu_al(result, doktorlar_combo.get(), sikayet_entry.get(), date_entry.get())).grid(row=6, column=3, columnspan=2, pady=5, sticky=E)
    temizlebuton = (Button(randevu_paneli_frame,text="Temizle",bg="Floral White",fg="Gray21",borderwidth="7",command=temizle))
    temizlebuton.grid(row=6, column=2, pady=5, padx=5, sticky=W)
    randevu_listesi_frame = Frame(hastaform, padx=55, pady=20, bg="Medium Turquoise")
    randevu_listesi_frame.grid(row=2, column=0, sticky=W, padx=30, pady=20)
    Label(randevu_listesi_frame, text="Randevu Listesi", font=("Helvetica", 16), bg="Turquoise4", fg="white").grid(row=0, column=0, pady=5, sticky=W)
    columns = ("Tarih", "Doktor ID", "Durum", "Şikayet")
    randevu_tree = ttk.Treeview(randevu_listesi_frame, columns=columns, show="headings", selectmode="browse")
    for col in columns:
        randevu_tree.heading(col, text=col)
        randevu_tree.column(col, width=150)
    yscroll = Scrollbar(randevu_listesi_frame, orient="vertical", command=randevu_tree.yview)
    yscroll.grid(row=1, column=1, sticky='nsew')
    xscroll = Scrollbar(randevu_listesi_frame, orient="horizontal", command=randevu_tree.xview)
    xscroll.grid(row=2, column=0, sticky='nsew')
    randevu_tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
    randevu_tree.grid(row=1, column=0, pady=5, sticky='nsew')
    randevu_tree.grid(row=1, column=0, pady=5, sticky=W)
    load_randevular()
    completed_randevu_frame = Frame(hastaform, padx=40, pady=20, bg="Medium Turquoise")
    completed_randevu_frame.grid(row=2, column=1, sticky=W, padx=40, pady=20)
    Label(completed_randevu_frame, text="Geçmiş Randevular", font=("Helvetica", 16), bg="Turquoise4", fg="white").grid(row=0, column=0, pady=5, sticky=W)
    completed_columns = ("Tarih", "Doktor ID", "Durum", "Şikayet")
    completed_randevu_tree = ttk.Treeview(completed_randevu_frame, columns=completed_columns, show="headings", selectmode="browse")
    for col in completed_columns:
        completed_randevu_tree.heading(col, text=col)
        completed_randevu_tree.column(col, width=150)
    yyscroll = Scrollbar(completed_randevu_frame, orient="vertical", command=completed_randevu_tree.yview)
    yyscroll.grid(row=1, column=1, sticky='nsew')
    xxscroll = Scrollbar(completed_randevu_frame, orient="horizontal", command=completed_randevu_tree.xview)
    xxscroll.grid(row=2, column=0, sticky='nsew')
    completed_randevu_tree.configure(yscrollcommand=yyscroll.set, xscrollcommand=xxscroll.set)
    completed_randevu_tree.grid(row=1, column=0, pady=5, sticky='nsew')
    load_completed_randevular()
    hastaform.protocol("WM_DELETE_WINDOW", lambda: on_closing_the(hastaform))
    hastaform.mainloop()
def on_closing_hasw(hastaform):
    hastaform.destroy()



def hastaSecim():
    global has
    has = Toplevel()
    has.title("HASTA SEÇİM")
    pencere_genisligi = 800
    pencere_yuksekligi = 600
    merkez_pencere(has, pencere_genisligi, pencere_yuksekligi)
    pen.withdraw()
    has.protocol("WM_DELETE_WINDOW", lambda: on_closing_for(has))
    has.resizable(width=False, height=False)
    has.config(bg="Light Sea Green")
    icon_path = "images/penİco.ico"
    has.iconbitmap(icon_path)
    hastasignin_image = Image.open("images/hastaLog.png")
    hastasignup_image = Image.open("images/hastaKay.png")
    hastasignin_image = ImageTk.PhotoImage(hastasignin_image.resize((250, 250)))
    hastasignup_image = ImageTk.PhotoImage(hastasignup_image.resize((250, 250)))
    hastaLabel1 = Label(has, text="Hasta Giriş", font=myFont, bg="Dark Turquoise", fg="white")
    hastaLabel2 = Label(has, text="Hasta Kayıt", font=myFont, bg="Dark Turquoise", fg="white")
    hasta1Buton = Button(has, image=hastasignin_image, command=hastaGirisForm, bd=0)
    hasta2Buton = Button(has, image=hastasignup_image, command=hastaKayitForm, bd=0)
    hasta1Buton.grid(row=0, column=0, sticky=W, padx=75, pady=100)
    hasta2Buton.grid(row=0, column=1, sticky=E, padx=75, pady=100)
    hastaLabel1.grid(row=1, column=0)
    hastaLabel2.grid(row=1, column=1)
    has.mainloop()
def on_closing_for(has):
    has.destroy()
    pen.destroy()
def personelGirisForm():
    def clear_entries():
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
    global wan
    wan = Toplevel()
    pen.withdraw()
    wan.config(bg="Light Sea Green")
    wan.resizable(width=False, height=False)
    wan.title("Personel Giriş")
    pencere_genisligi2 = 400
    pencere_yuksekligi2 = 400
    merkez_pencere(wan, pencere_genisligi2, pencere_yuksekligi2)
    icon_path2 = "images/nurse_icon_140488.ico"
    wan.iconbitmap(icon_path2)
    wan.protocol("WM_DELETE_WINDOW", lambda: on_closing_the(wan))

    perpng_original = Image.open("images/nurse_icon_140488.png")
    perpng = ImageTk.PhotoImage(perpng_original.resize((128, 128)))
    perpng_label = tk.Label(wan, image=perpng)
    perpng_label.grid(row=0, column=0, pady=5, padx=5, sticky=W)

    Label(wan, text="Kullanıcı Adı:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=1, column=0, pady=10)
    username_entry = Entry(wan, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    username_entry.grid(row=1, column=1, pady=5)
    Label(wan, text="Şifre:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=2, column=0, pady=10)
    password_entry = Entry(wan, show="*", width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    password_entry.grid(row=2, column=1, pady=5)
    login_button = Button(wan, bg="Floral White", fg="Gray21", borderwidth=7, text="Giriş Yap", command=lambda: login_clickedd(username_entry, password_entry, wan))
    login_button.grid(row=3, column=1, pady=10, padx=10,sticky=W)
    clear_button = Button(wan, bg="Floral White", fg="Gray21", borderwidth=7, text="Temizle", command=clear_entries)
    clear_button.grid(row=3, column=1, sticky=E, pady=10, padx=10)


    wan.mainloop()
def on_closing_the(wan):
    wan.destroy()
    pen.destroy()
def login_clickedd(username_entry, password_entry, wan):
    kullanici_adi = username_entry.get()
    sifre = password_entry.get()
    sql = "SELECT * FROM sekreterler WHERE kullanici_adi = %s AND sifre = %s"
    values = (kullanici_adi, sifre)
    try:
        cursor.execute(sql, values)
        resultt = cursor.fetchone()
        if resultt:
            show_success_message("Giriş Başarılı")
            wan.destroy()
            sekreterForm(resultt)
        else:
            messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre")
    except Exception as e:
        print(f"Giriş kontrolünde hata oluştu: {e}")
        messagebox.showerror("Hata", "Giriş kontrolünde bir hata oluştu")
def show_success_message(message):
    messagebox.showinfo("Başarılı", message)


def show_error_message(message):
    messagebox.showerror("Hata", message)


def sekreterForm(resultt):
    def load_randevular():
        sorgu = "SELECT tarih, doktor_id, durum, sikayet FROM randevular"
        cursor.execute(sorgu)
        randevular = cursor.fetchall()
        for row in randevu_tree.get_children():
            randevu_tree.delete(row)
        for randevu in randevular:
            randevu_tree.insert("", "end", values=randevu)

    def doktorlari():
        sorgu = "SELECT doktor_id,ad,soyad,uzmanlik_alani,telefon,email FROM doktorlar"
        cursor.execute(sorgu)
        doktorlar = cursor.fetchall()
        for row in doktorlar_tree.get_children():
            doktorlar_tree.delete(row)
        for doktor in doktorlar:
            doktorlar_tree.insert("", "end", values=doktor)
    per = Toplevel()
    per.state("zoomed")
    per.config(bg="Light Sea Green")
    per.resizable(width=True, height=True)
    per.title("SekreterForm")
    icon_path3 = "images/doctorhospital_101095.ico"
    per.iconbitmap(icon_path3)

    sekreter_bilgileri_frame = Frame(per, padx=35, pady=30, bg="Medium Turquoise")
    sekreter_bilgileri_frame.grid(row=0, column=1, padx=40, pady=10)

    sekpng_original = Image.open("images/nurse_icon_140488.png")
    sekpng = ImageTk.PhotoImage(sekpng_original.resize((128, 128)))
    sekpng_label = tk.Label(sekreter_bilgileri_frame, image=sekpng)
    sekpng_label.grid(row=0, column=0, pady=5, padx=5)

    Label(sekreter_bilgileri_frame, text="Sekreter Bilgileri", font=("Helvetica", 25), bg="Turquoise4", fg="white").grid(row=1, column=0, pady=5)
    sekreter_ad_soyad_label = Label(sekreter_bilgileri_frame, text=f"Ad: {resultt[1]}\nSoyad: {resultt[2]}", bg="Turquoise4", fg="white", font=("Helvetica", 20))
    sekreter_ad_soyad_label.grid(row=2, column=0, pady=5)


    randevu_listesi_frame = Frame(per, padx=10, pady=20, bg="Medium Turquoise")
    randevu_listesi_frame.grid(row=0, column=0, sticky=W, pady=10, padx=40)
    Label(randevu_listesi_frame, text="Randevu Listesi", font=("Helvetica", 16), bg="Turquoise4", fg="white").grid(row=0, column=0, pady=5, sticky=W)
    columns = ("Tarih", "Doktor ID", "Durum", "Şikayet")
    randevu_tree = ttk.Treeview(randevu_listesi_frame, columns=columns, show="headings", selectmode="browse")
    for col in columns:
        randevu_tree.heading(col, text=col)
        randevu_tree.column(col, width=225)
    yscroll = Scrollbar(randevu_listesi_frame, orient="vertical", command=randevu_tree.yview)
    yscroll.grid(row=1, column=1, sticky='nsew')
    xscroll = Scrollbar(randevu_listesi_frame, orient="horizontal", command=randevu_tree.xview)
    xscroll.grid(row=2, column=0, sticky='nsew')
    randevu_tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
    randevu_tree.grid(row=1, column=0, pady=5, sticky='nsew')
    randevu_tree.grid(row=1, column=0, pady=5, sticky=W)
    load_randevular()

    def doktor_kayit():
        def clear_entries():
            for entry in entry_dict.values():
                entry.delete(0, 'end')
        dor = Toplevel(per)
        dor.title("Doktor Kayit")
        dor.resizable(width=False, height=False)
        dor.config(bg="Light Sea Green")
        pencere_genisligid = 600
        pencere_yuksekligid = 400
        merkez_pencere(dor, pencere_genisligid, pencere_yuksekligid)
        Label(dor, text="Ad:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=1, column=0, pady=10, padx=5)
        ad_entry = Entry(dor, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
        ad_entry.grid(row=1, column=1, pady=10, padx=5)
        Label(dor, text="Soyad:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=1, column=2, pady=10, padx=5)
        soyad_entry = Entry(dor, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
        soyad_entry.grid(row=1, column=3, pady=10, padx=5)
        Label(dor, text="Uzmanlık :", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=2, column=0, pady=10, padx=5)
        uzmanlik_alani_entry = Entry(dor, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
        uzmanlik_alani_entry.grid(row=2, column=1, pady=10, padx=5)
        Label(dor, text="Telefon:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=2, column=2, pady=10, padx=5)
        telefon_entry = Entry(dor, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
        telefon_entry.grid(row=2, column=3, pady=10, padx=5)
        Label(dor, text="E-mail:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=3, column=0, pady=10, padx=5)
        email_entry = Entry(dor, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
        email_entry.grid(row=3, column=1, pady=10, padx=5)
        Label(dor, text="Adres:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=3, column=2, pady=10, padx=5)
        adres_entry = Entry(dor, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
        adres_entry.grid(row=3, column=3, pady=10, padx=5)
        Label(dor, text="Kullanıcı Adı:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=4, column=0, pady=10, padx=5)
        kullanici_adi_entry = Entry(dor, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
        kullanici_adi_entry.grid(row=4, column=1, pady=10, padx=5)
        Label(dor, text="Şifre:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=4, column=2, pady=10, padx=5)
        sifre_entry = Entry(dor, show="*", width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
        sifre_entry.grid(row=4, column=3, pady=10, padx=5)
        save_button = Button(dor, bg="Floral White", fg="Gray21", borderwidth=7, text="Kaydet", command=lambda: dok_kayit(entry_dict))
        save_button.grid(row=5, column=3, pady=10, padx=5,sticky=W)
        clear_button = Button(dor, bg="Floral White", fg="Gray21", borderwidth=7, text="Temizle", command=clear_entries)
        clear_button.grid(row=5, column=3, pady=10,padx=5,sticky=E)

        entry_dict = {
            'ad': ad_entry,
            'soyad': soyad_entry,
            'uzmanlik_alani': uzmanlik_alani_entry,
            'telefon': telefon_entry,
            'email': email_entry,
            'adres': adres_entry,
            'kullanici_adi': kullanici_adi_entry,
            'sifre': sifre_entry
        }

        def on_closing():
            dor.destroy()
        dor.protocol("WM_DELETE_WINDOW", on_closing)

        def dok_kayit(entry_dict):
            ad = entry_dict['ad'].get()
            soyad = entry_dict['soyad'].get()
            uzmanlik_alani = entry_dict['uzmanlik_alani'].get()
            telefon = entry_dict['telefon'].get()
            email = entry_dict['email'].get()
            adres = entry_dict['adres'].get()
            kullanici_adi = entry_dict['kullanici_adi'].get()
            sifre = entry_dict['sifre'].get()
            if not ad or not soyad or not uzmanlik_alani or not telefon or not email or not adres or not kullanici_adi or not sifre:
                show_error_message("Lütfen tüm bilgileri doldurun.")
                return
            sql = "INSERT INTO doktorlar (ad, soyad,uzmanlik_alani ,telefon, email, adres, kullanici_adi, sifre) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (ad, soyad, uzmanlik_alani, telefon, email, adres, kullanici_adi, sifre)
            try:
                cursor.execute(sql, values)
                conn.commit()
                show_success_message("Doktor kaydı başarıyla eklendi.")
                doktorlari()
                dor.destroy()
            except Exception as e:
                show_success_message(f"Doktor kaydı eklenirken hata oluştu: {e}")

    def onayla():
        selected_item = randevu_tree.selection()
        if not selected_item:
            show_error_message("Lütfen bir randevu seçin.")
            return

        randevu_id = randevu_tree.item(selected_item, 'values')[1]

        update_query = "UPDATE randevular SET durum = 'Onaylanan' WHERE doktor_id = %s"

        try:
            cursor.execute(update_query, (randevu_id,))
            conn.commit()
            show_success_message("Randevu onaylandı.")
            load_randevular()
        except Exception as e:
            show_error_message(f"Hata oluştu: {e}")

    hizlierisim_frame = Frame(per, padx=10, pady=5, bg="Medium Turquoise")
    hizlierisim_frame.grid(row=1, column=0, pady=20)
    doktorekleB = Button(hizlierisim_frame, bg="Floral White", fg="Gray21", borderwidth=7, text="Doktor Ekle", command=doktor_kayit)
    doktorekleB.grid(row=0, column=1, padx=5, pady=10)
    onayla = Button(hizlierisim_frame, bg="Floral White", fg="Gray21", borderwidth=7, text="Randevu Onayla", command= onayla)
    onayla.grid(row=0, column=0, padx=5, pady=10)


    doktor_listesi_frame = Frame(per, padx=10, pady=10, bg="Medium Turquoise")
    doktor_listesi_frame.grid(row=2, column=0, sticky=W, pady=10, padx=40)
    Label(doktor_listesi_frame, text="Doktor Listesi", font=("Helvetica", 16), bg="Turquoise4", fg="white").grid(
        row=0, column=0, pady=5, sticky=W)
    columns = ("ID", "Ad", "Soyad", "Uzmanlık", "Telefon", "E-mail")
    doktorlar_tree = ttk.Treeview(doktor_listesi_frame, columns=columns, show="headings", selectmode="browse")
    for col in columns:
        doktorlar_tree.heading(col, text=col)
        doktorlar_tree.column(col, width=150)
    yscroll = Scrollbar(doktor_listesi_frame, orient="vertical", command=doktorlar_tree.yview)
    yscroll.grid(row=1, column=1, sticky='nsew')
    xscroll = Scrollbar(doktor_listesi_frame, orient="horizontal", command=doktorlar_tree.xview)
    xscroll.grid(row=2, column=0, sticky='nsew')
    doktorlar_tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
    doktorlar_tree.grid(row=1, column=0, pady=5, sticky='nsew')
    doktorlar_tree.grid(row=1, column=0, pady=5, sticky=W)
    doktorlari()

    hospng_original = Image.open("images/588hospital_100778.png")
    hospng = ImageTk.PhotoImage(hospng_original.resize((256, 256)))
    hospng_label = tk.Label(per, image=hospng)
    hospng_label.grid(row=2, column=1, pady=5, padx=5)


    per.protocol("WM_DELETE_WINDOW", lambda: on_closing_the(per))
    per.mainloop()

def on_closing_theasd(per):
    per.destroy()
def doktorGirisForm():
    def clear_entries():
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
    global won
    won = Toplevel()
    pen.withdraw()
    won.config(bg="Light Sea Green")
    won.resizable(width=False, height=False)
    won.title("Personel Giriş")
    pencere_genisligi9 = 400
    pencere_yuksekligi9 = 400
    merkez_pencere(won, pencere_genisligi9, pencere_yuksekligi9)
    icon_path3 = "images/doctor_icon_140508.ico"
    won.iconbitmap(icon_path3)
    won.protocol("WM_DELETE_WINDOW", lambda: on_closing_theds(won))
    docpng_original = Image.open("images/doctor_icon_140508.png")
    docpng = ImageTk.PhotoImage(docpng_original.resize((128, 128)))
    docpng_label = tk.Label(won, image=docpng)
    docpng_label.grid(row=0, column=0, pady=5, padx=5, sticky=W)
    Label(won, text="Kullanıcı Adı:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=1, column=0, pady=10)
    username_entry = Entry(won, width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    username_entry.grid(row=1, column=1, pady=5)
    Label(won, text="Şifre:", font=myFont, bg="Dark Turquoise", fg="Snow").grid(row=2, column=0, pady=10)
    password_entry = Entry(won, show="*", width=25, borderwidth=10, bg="Medium Turquoise", fg="Black")
    password_entry.grid(row=2, column=1, pady=5)
    login_button = Button(won, bg="Floral White", fg="Gray21", borderwidth=7, text="Giriş Yap", command=lambda: login_clickeddd(username_entry, password_entry, won))
    clear_button = Button(won, bg="Floral White", fg="Gray21", borderwidth=7, text="Temizle", command=clear_entries)
    clear_button.grid(row=3, column=1, sticky=E, pady=10, padx=10)
    login_button.grid(row=3, column=1, pady=10, padx=10, sticky=W)
    won.mainloop()
def on_closing_theds(won):
    won.destroy()
    pen.destroy()
def login_clickeddd(username_entry, password_entry, won):
    kullanici_adi = username_entry.get()
    sifre = password_entry.get()
    sql = "SELECT * FROM doktorlar WHERE kullanici_adi = %s AND sifre = %s"
    values = (kullanici_adi, sifre)
    try:
        cursor.execute(sql, values)
        resulttt = cursor.fetchone()
        if resulttt:
            show_success_message("Giriş Başarılı")
            won.destroy()
            doktorForm(resulttt)
        else:
            messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre")
    except Exception as e:
        print(f"Giriş kontrolünde hata oluştu: {e}")
        messagebox.showerror("Hata", "Giriş kontrolünde bir hata oluştu")

def doktorForm(resulttt):

    def load_randevular():
        doktor_id = resulttt[0]
        sorgu = "SELECT tarih, doktor_id, hasta_id, durum FROM randevular  WHERE doktor_id = %s AND durum = 'Onaylanan'"
        cursor.execute(sorgu, (doktor_id,))
        randevular = cursor.fetchall()
        for row in randevu_tree.get_children():
            randevu_tree.delete(row)
        for randevu in randevular:
            randevu_tree.insert("", "end", values=randevu)

    def hastalari():
        sorgu = "SELECT hasta_id,ad,soyad,tc_kimlik,dogum_tarihi,cinsiyet,telefon,email FROM hastalar"
        cursor.execute(sorgu)
        hastalar = cursor.fetchall()
        for row in hastalar_tree.get_children():
            hastalar_tree.delete(row)
        for hasta in hastalar:
            hastalar_tree.insert("", "end", values=hasta)

    def sikayet():
        doktor_id = resulttt[0]
        sorgu = "SELECT doktor_id, hasta_id, sikayet FROM randevular WHERE doktor_id = %s AND durum = 'Onaylanan'"
        cursor.execute(sorgu, (doktor_id,))
        randevular = cursor.fetchall()
        for row in sikayet_tree.get_children():
            sikayet_tree.delete(row)
        for randevu in randevular:
            sikayet_tree.insert("", "end", values=randevu)


    dok = Toplevel()
    dok.state("zoomed")
    dok.config(bg="Light Sea Green")
    dok.resizable(width=True, height=True)
    dok.title("DoktorForm")
    icon_path3 = "images/doctorhospital_101095.ico"
    dok.iconbitmap(icon_path3)

    doktor_bilgileri_frame = Frame(dok, padx=40, pady=20, bg="Medium Turquoise")
    doktor_bilgileri_frame.grid(row=0, column=0, pady=20, padx=40)

    dokpng_original = Image.open("images/doctor_icon_140508.png")
    dokpng = ImageTk.PhotoImage(dokpng_original.resize((128, 128)))
    dokpng_label = tk.Label(doktor_bilgileri_frame, image=dokpng)
    dokpng_label.grid(row=0, column=0, pady=5, padx=5)

    Label(doktor_bilgileri_frame, text="Doktor Bilgileri", font=("Helvetica", 25), bg="Turquoise4", fg="white").grid(row=1, column=0, pady=5)
    doktor_ad_soyad_label = Label(doktor_bilgileri_frame, text=f"Ad: {resulttt[1]}\nSoyad: {resulttt[2]}", bg="Turquoise4", fg="white", font=("Helvetica", 20))
    doktor_ad_soyad_label.grid(row=2, column=0, pady=5)

    randevu_listesi_frame = Frame(dok, padx=40, pady=20, bg="Medium Turquoise")
    randevu_listesi_frame.grid(row=1, column=1, sticky=W, pady=5, padx=40)

    Label(randevu_listesi_frame, text="Randevu Listesi", font=("Helvetica", 16), bg="Turquoise4", fg="white").grid(
        row=0, column=0, pady=5, sticky=W)
    columns = ("Tarih", "Doktor ID", "Hasta ID", "Durum")
    randevu_tree = ttk.Treeview(randevu_listesi_frame, columns=columns, show="headings", selectmode="browse")
    for col in columns:
        randevu_tree.heading(col, text=col)
        randevu_tree.column(col, width=200)
    yscroll = Scrollbar(randevu_listesi_frame, orient="vertical", command=randevu_tree.yview)
    yscroll.grid(row=1, column=1, sticky='nsew')
    xscroll = Scrollbar(randevu_listesi_frame, orient="horizontal", command=randevu_tree.xview)
    xscroll.grid(row=2, column=0, sticky='nsew')
    randevu_tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
    randevu_tree.grid(row=1, column=0, pady=5, sticky='nsew')
    randevu_tree.grid(row=1, column=0, pady=5, sticky=W)
    load_randevular()

    def onayla():
        selected_item = randevu_tree.selection()
        if not selected_item:
            show_error_message("Lütfen bir randevu seçin.")
            return

        randevu_id = randevu_tree.item(selected_item, 'values')[1]

        update_query = "UPDATE randevular SET durum = 'Tamamlandı' WHERE doktor_id = %s"
        try:
            cursor.execute(update_query, (randevu_id,))
            conn.commit()
            show_success_message("Randevu tamamlandı.")
            load_randevular()
        except Exception as e:
            show_error_message(f"Hata oluştu: {e}")



    hizlierisim_frame = Frame(dok, padx=10, pady=5, bg="Medium Turquoise")
    hizlierisim_frame.grid(row=2, column=0, padx=40)
    onayla = Button(hizlierisim_frame, bg="Floral White", fg="Gray21", borderwidth=7, text="Randevu Tamamla", command=onayla)
    onayla.grid(row=2, column=0, padx=5, pady=10)


    hasta_listesi_frame = Frame(dok, padx=40, pady=20, bg="Medium Turquoise")
    hasta_listesi_frame.grid(row=0, column=1, sticky=W, pady=20, padx=40)

    Label(hasta_listesi_frame, text="Hasta Listesi", font=("Helvetica", 16), bg="Turquoise4", fg="white").grid(
        row=0, column=0, pady=5, sticky=W)
    columns = ("ID", "Ad", "Soyad", "TC Kimlik", "Doğum Tarihi", "Cinsiyet", "Telefon", "E-mail")
    hastalar_tree = ttk.Treeview(hasta_listesi_frame, columns=columns, show="headings", selectmode="browse")
    for col in columns:
        hastalar_tree.heading(col, text=col)
        hastalar_tree.column(col, width=100)
    yscroll = Scrollbar(hasta_listesi_frame, orient="vertical", command=hastalar_tree.yview)
    yscroll.grid(row=1, column=1, sticky='nsew')
    xscroll = Scrollbar(hasta_listesi_frame, orient="horizontal", command=hastalar_tree.xview)
    xscroll.grid(row=2, column=0, sticky='nsew')
    hastalar_tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
    hastalar_tree.grid(row=1, column=0, pady=5, sticky='nsew')
    hastalar_tree.grid(row=1, column=0, pady=5, sticky=W)
    hastalari()

    sikayet_frame = Frame(dok, padx=10, pady=10, bg="Medium Turquoise")
    sikayet_frame.grid(row=1, column=0, pady=5, padx=40)
    columns = ("Dc.ID", "HastaID", "Sikayet")
    sikayet_tree = ttk.Treeview(sikayet_frame, columns=columns, show="headings", selectmode="browse")
    for col in columns:
        sikayet_tree.heading(col, text=col)
        sikayet_tree.column(col, width=150)
    yscroll = Scrollbar(sikayet_frame, orient="vertical", command=sikayet_tree.yview)
    yscroll.grid(row=1, column=1, sticky='nsew')
    xscroll = Scrollbar(sikayet_frame, orient="horizontal", command=sikayet_tree.xview)
    xscroll.grid(row=2, column=0, sticky='nsew')
    sikayet_tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
    sikayet_tree.grid(row=1, column=0, pady=5, sticky='nsew')
    sikayet_tree.grid(row=1, column=0, pady=5, sticky=W)
    sikayet()

    dok.protocol("WM_DELETE_WINDOW", lambda: on_closing_the(dok))
    dok.mainloop()

def on_closing_theasda(dok):
    dok.destroy()

fonts= ("Helvetica", 32, "bold italic underline")
pencere_genisligi = 800
pencere_yuksekligi = 600
merkez_pencere(pen, pencere_genisligi, pencere_yuksekligi)
hasta_image = Image.open("images/hastaGiriş.png")
personel_image = Image.open("images/personelGiriş.png")
doktor_image = Image.open("images/doktorGiriş.png")
hastane_image = Image.open("images/hospitalasıl.png")
hasta_image = ImageTk.PhotoImage(hasta_image.resize((250, 250)))
personel_image = ImageTk.PhotoImage(personel_image.resize((250, 250)))
doktor_image = ImageTk.PhotoImage(doktor_image.resize((250, 250)))
hastane_image = ImageTk.PhotoImage(hastane_image.resize((200, 200)))
hastaLabel = Label(pen, text="Hasta", font=myFont, bg="Dark Turquoise", fg="white")
personelLabel = Label(pen, text="Personel", font=myFont, bg="Dark Turquoise", fg="white")
doktorLabel = Label(pen, text="Doktor", font=myFont, bg="Dark Turquoise", fg="white")
hastaButon = Button(pen, image=hasta_image, command=hastaSecim, bd=0)
personelButon = Button(pen, image=personel_image, command=personelGirisForm, bd=0)
doktorButon = Button(pen, image=doktor_image, command=doktorGirisForm, bd=0)
hastane_girisi_label = Label(pen, image=hastane_image, bg="Medium Turquoise")
hastane_girisi_label.grid(row=0, column=2, pady=5, padx=5)
hosgeldinizLabel = Label(pen, text="Hoş geldiniz", font=fonts, bg="Medium Turquoise", fg="white")
hosgeldinizLabel.grid(row=0, column=0)
hastaLabel.grid(row=2, column=0, pady=5, padx=5)
personelLabel.grid(row=2, column=1, pady=5, padx=5)
doktorLabel.grid(row=2, column=2, pady=5, padx=5)
hastaButon.grid(row=1, column=0, pady=5, padx=10)
personelButon.grid(row=1, column=1, pady=5, padx=2)
doktorButon.grid(row=1, column=2, pady=5, padx=10)
pen.mainloop()