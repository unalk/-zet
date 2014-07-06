import tkinter as tk
import özet as ö
from TrDenetle import küçült
class uyg(tk.Frame):
    def __init__(self,abi=None):
        tk.Frame.__init__(self,abi)
        self.grid
        self.hazırla()
    def hazırla(self):
        self.master.title("Özetleme")
        self.seçke=tk.Menu(self)
        ayarlarS=tk.Menu(self.seçke,tearoff=0)
        self.DeğerYaz=tk.IntVar()
        ayarlarS.add_checkbutton(label="Özette tümce değerlerini göster",variable=self.DeğerYaz, \
                                 onvalue=1,offvalue=0)
        ayarlarS.add_separator()
        ayarlarS.add_command(label="Çıkış",command=self.master.destroy)
        self.seçke.add_cascade(label="Ayarlar",menu=ayarlarS)
        yardımS=tk.Menu(self.seçke,tearoff=0)
        yardımS.add_command(label="Özet Oranı",command=self.özetlemeOranıYardım)
        yardımS.add_command(label="Kişisel Sözcükler",command=self.kişiselSözcükYardım)
        self.seçke.add_cascade(label="Yardım",menu=yardımS)

        self.master.config(menu=self.seçke)

        tk.Label(self.master,
                 text=("Özetlenecek metin: ")).grid(row=0,column=0,columnspan=4)
        self.girdi=tk.Text(self.master,width=80,height=20)
        self.girdi.insert(tk.INSERT,"""\
ÖZETLEME YAZILIMI

Özetleme yazılımına hoşggeldiniz! Bu yazılım adından da anlayabilce\
ğiniz gibi metinden tümceler seçerek özetleme yapar. Özetlemek \
istediğiniz metni buraya giriniz. Yanlız şunları unutmayınız:
- Başlıkların TÜM harflerini BÜYÜK giriniz.
- Paragraflar arasında satır atlayınız.
- Metni girerken bu yazıyı silmeyi unutmayın.

İPUÇLARI
- Yazılımın daha az tümce sayısı ve daha yüksek özet oranında daha \
başarılı olduğu deneysel olarak kanıtlanmıştır. Eğer özetlenen metin \
anlaşılmıyorsa, beğenmediyseniz ya da beklentilerinizi \
karşılamadıysa özet oranını yükseltmek, tümce sayısını düşürmek daha \
iyi sonuçlar almanızı sağlayabilir.""")
        self.girdi.grid(row=1,column=0,columnspan=4)
        tk.Label(self.master,text="Özetleme oranı (%) :").grid(row=2,column=0)

        self.öO=tk.Scale(self.master,
                    orient=tk.HORIZONTAL,from_=1,to=100,length=200)
        self.öO.grid(row=2,column=1)
        self.öO.set(50)
        tk.Button(self.master,text="Özetleme oranı nedir?",
                  command=self.özetlemeOranıYardım).grid(row=2,column=3)
        
        tk.Label(self.master,text="Kişisel sözcükler belirlemek"+
                 " isterseniz giriniz:").grid(row=3,column=0)

        self.kS=tk.Entry(self.master,text="Kişisel sözcükleri virgülle ayırın.",
                         width=35)
        self.kS.grid(row=3,column=1,columnspan=2)
        self.kS.insert(tk.INSERT,"kişisel sözcükleri virgülle ayırın")
        tk.Button(self.master,text="Kişisel sözcük nedir?",
                  command=self.kişiselSözcükYardım).grid(row=3,column=3)
        tk.Button(self.master,text="ÖZETLE",width=30,
                  command=self.özetle).grid(row=4,column=1)

    def kişiselSözcükYardım(self):
        tk.messagebox.showinfo("Kişisel sözcük",
        ("Belirlediğiniz kişisel sözcüklere özetlemede önem verilir.\n"+
         "İsterseniz, kişisel sözcük belirlemezsiniz, ancak eğer\n"+
         "özette aradığınızı bulamadıysanız aradığınız neyse onunla\n"+
         "ilgili kişisel sözcük girebilirsiniz. Bir kişisel sözcüğü\n"+
         "birden çok kez girebilir, böylece onun katsayısını arttırabilirsiniz.\n"+
         "Kişisel sözcüklerinizi virgülle ayırmayı unutmayın."))
    def özetlemeOranıYardım(self):
        tk.messagebox.showinfo("Özetleme Oranı",
        ("Özetleme oranı, özetin metnin gerçeğinin yüzde kaçı\n"+
         "olacağını belirler. Örneğin; metinde 10 tümce varsa,\n"+
         "özetleme oranı da %50 ise özette 5 tümce bulunur.\n"+
         "Bu yazılımın daha yüksek özetleme oranında daha \n"+
         "başarılı olduğu deneysel olarak kanıtlanmıştır."))
    def özetle(self):
        if self.DeğerYaz.get():
            ö.DEĞERYAZ=True
        else:
            ö.DEĞERYAZ=False
        ö.ÖZETORANI=self.öO.get()/100
        ö.kSVer(self.kS.get())
        çıktı=ö.özetle(self.girdi.get(1.0,tk.END))
        G=göster(çıktı,tk.Tk())

class göster(tk.Frame):
    def __init__(self,yazı="çıktı verilmedi",abi=None):
        tk.Frame.__init__(self,abi)
        self.yazı=yazı
        self.grid
        self.hazırla()
    def hazırla(self):
        self.master.title("Özetlenmiş metin")
        self.çıktı=tk.Text(self.master,width=80,height=20)
        self.çıktı.grid(row=0,column=0,columnspan=4)
        self.çıktı.insert(tk.INSERT,self.yazı)
        tk.Button(self.master,text="Tümünü Kopyala",width=30,
                  command=self.kopyala).grid(row=1,column=0)
    def kopyala(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.yazı)
        
if __name__=="__main__":
    U=uyg(tk.Tk())
    U.mainloop()
    
