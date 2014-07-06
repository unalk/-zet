from TrDenetle import *
from math import ceil as tavan
AÇKISÖZCÜKSIRALA=False
AÇAKSÖZCÜKORANI=1/10
NOKTALAMADEĞERLENDİR=True
DEĞERYAZ=False
ÖZETORANI=.2
assert ÖZETORANI>0.0 and ÖZETORANI<=1.0,"Özet oranı geçersiz."
assert AÇAKSÖZCÜKORANI>0.0 and AÇAKSÖZCÜKORANI<=1.0,"açak sözcük oranı geçersiz."
DEĞERLER={"açkı":10,"olumlu":15,"olumsuz":-20,"noktalama":5,"kişisel":10,
          "başlık":20,"uzunluk":10,"sayı":3,"günay":5,"giriş":20}

NOKTALAMA=".!?"
ÖNEMLİNOKTALAMA="!?"
OLUMLUSÖZCÜKLER=["sonuçta","sonuç olarak","nitekim","neticede","özetle","demek"]
OLUMSUZSÖZCÜKLER=["ancak","ama","fakat","çünkü"]
GÜNAY=["ocak","şubat","mart","nisan","mayıs","haziran","temmuz","ağustos",
       "eylül","ekim","kasım","aralık"]

adımsılar=("bu bunu bunun böyle şöyle şu şunu şunun o onu ona"+
" onu onun için da de şimdi biraz hiç hep şey hiçbir bir"+
" tüm tümü tümünü ben beni bana benim sen seni sana senin"+
" ile benimle seninle onunla onlarla bizlerle sizlerle biz"+
" bizi bize bizim siz sizi size sizin onlar onları "+
"onların onlara mı mi mu mü ve veya ya olarak olan yaklaşık").split(" ")
kişiselSözcükler=[]
başlıkSözcükler=[]
açak={}
ortalama=0

def tümceDeğerlendir(tümce,konum):
    değer=0
    tTümce=temelleştirSayı(tümce)
    çTümce=tTümce.split(" ")
    if açak:
        enBüyükAçkı=açak[sorted(açak,key=açak.get,reverse=True)[0]]
        for a in sorted(açak,key=açak.get,reverse=True):
            for ekli in tümOlasıEkleriyle(a):
                for sözcük in çTümce:
                    if sözcük==ekli:
                        if AÇKISÖZCÜKSIRALA:
                            değer+=DEĞERLER["açkı"]*(açak[a]/enBüyükAçkı)
                        else:
                            değer+=DEĞERLER["açkı"]
                        break
    else:
        print("Açkı sözcükler yok!?")
    for o in OLUMLUSÖZCÜKLER:
        for sözcük in çTümce:
            if o == sözcük:
                değer+=DEĞERLER["olumlu"]
    for o in OLUMSUZSÖZCÜKLER:
        for sözcük in çTümce:
            if o == sözcük:
                değer+=DEĞERLER["olumsuz"]
    if NOKTALAMADEĞERLENDİR:
        if tümce[-1] in ÖNEMLİNOKTALAMA:
            değer+=DEĞERLER["noktalama"]
    for a in kişiselSözcükler:
        for ekli in tümOlasıEkleriyle(a):
            for söz in çTümce:
                if söz==ekli:
                    değer+=DEĞERLER["kişisel"]
                    break

    for a in başlıkSözcükler:
        for ekli in tümOlasıEkleriyle(a):
            for söz in çTümce:
                if söz==ekli:
                    değer+=DEĞERLER["başlık"]
                    break
    for a in GÜNAY:
        for ekli in tümOlasıEkleriyle(a):
            for söz in çTümce:
                if söz==ekli:
                    değer+=DEĞERLER["günay"]
                    break
    for s in range(0,10):
        if str(s) in tTümce:
            değer+=DEĞERLER["sayı"]
            break
    if ortalama < len(çTümce):
        değer+=DEĞERLER["uzunluk"]
    if konum==0:
        değer+=DEĞERLER["giriş"]
    return değer
    

    
def açakSözcükler(girdi):
    girdi=temelleştir(girdi)
    sözcükler=girdi.split(" ")
    açkı={}
    for s in sözcükler:
        if s in açkı:
            açkı[s]+=1
        else:
            açkı[s]=1
    for s in açkı.copy():
        if s in adımsılar or s=="":
            del açkı[s]

    uzunluk=tavan(len(açkı)*AÇAKSÖZCÜKORANI)
    elenmişAçkı={}
    u=0
    en=0
    for s in sorted(açkı,key=açkı.get,reverse=True):
        if u>=uzunluk and en>açkı[s]:
            break
        if u<uzunluk or en<=açkı[s]:
            elenmişAçkı[s]=açkı[s]
            if u<uzunluk:en=açkı[s]
        u+=1
    return elenmişAçkı #sorted(açkı,key=açkı.get,reverse=True)

def parçalaraAyır(girdi):
    global başlıkSözcükler
    parçalar=girdi.split("\n")
    for p in parçalar[:]:
        if not p:
            parçalar.remove(p)
        else:
            if tümüBüyükMü(p):
                for ağü in temelleştir(p).split(" "):
                    if ağü:
                        başlıkSözcükler.append(ağü)
                parçalar.remove(p)
                
    return parçalar

def tümcelereAyır(girdi):
    ayır=girdi.split(" ")
    tümceler=[]
    tümce=""
    for ayrık in ayır:
        if ayrık:
            tümce+=ayrık
            if ayrık[-1] in NOKTALAMA:
                tümceler.append(tümce)
                tümce=""
            else:
                tümce+=" ";
    return tümceler

def kSVer(girdi):
    global kişiselSözcükler
    kişiselSözcükler=küçült(girdi).split(",")
    for sayı,s in enumerate(kişiselSözcükler[:]):
        if not s:
            kişiselSözcükler.remove(s)
        else:
            kişiselSözcükler[sayı]=s.strip()

def özetle(girdi):
    global parçalar,açak,ortalama,tümceler,tümceSayısı
    Çıktı=""
    parçalar=parçalaraAyır(girdi)
    açak=açakSözcükler(girdi)
    sp=[]
    for p in parçalar:
        sp.append(tümcelereAyır(p))
    tümceler={}
    tümceSayısı=0
    sözcükSayısı=0
    for p in sp:
        for t in p:
            tümceSayısı+=1
            sözcükSayısı+=len(temelleştir(t).split(" "))
    ortalama=sözcükSayısı/tümceSayısı
    for p in sp:
        for t in p:
            tümceler[t]=tümceDeğerlendir(t,p)

    uzunluk=tavan(tümceSayısı*ÖZETORANI)
    u=0
    sonuç=[]
    gösterSonuç=[]
    enDeğer=0
    for asd in sorted(tümceler,key=tümceler.get,reverse=True):
        if u>=uzunluk and tümceler[asd]<enDeğer:
            break
        if u<uzunluk or tümceler[asd]>=enDeğer:
            sonuç.append(asd) #
            if DEĞERYAZ:
                gösterSonuç.append(asd+" (Değeri "+str(tümceler[asd])+")")
            else:
                gösterSonuç.append(asd)
            if u<uzunluk:
                enDeğer=tümceler[asd]
            u+=1
    uzunluk=tavan(tümceSayısı*ÖZETORANI)
    u=0
    for p in sp:
        if u>=uzunluk:
            break
        for t in p:
            if u>=uzunluk:
                break
            try:
                #print(gösterSonuç[sonuç.index(t)])
                Çıktı+=gösterSonuç[sonuç.index(t)]+" "
                u+=1
            except:
                pass
    return Çıktı
        

if __name__=="__main__":
    print("Örnek bir özet:")
    g="""ZEMBEREK
Zemberek, açık kaynak kodlu Türkçe Doğal dil işleme kütüphanesi ve OpenOffice , LibreOffice eklentisidir. İlk sürümü BSD lisansı ile dağıtılmıştır. Tamamen Java ile geliştirilen kütüphane, yazım denetimi, hatalı kelimeler için öneri, heceleme, deascifier, hatalı kodlama temizleme gibi işlevlere sahiptir.

Zemberek2 kodlu ikinci sürümünde MPL lisansına geçilmiş, genel olarak tüm Türk dilleri için bir DDİ altyapısı oluşturulması için gerekli mimari değişiklikler yapılmıştır. Zemberek kullanılarak yazılmış bir sunucu Pardus için genel yazım denetimi desteği vermektedir. Sunucu TCP-IP soketleri üzerinden ISpell benzeri basit bir protokolle diğer uygulamalarla haberleşmektedir, yeni sürümünde DBUS arayüzü de sunucuya eklenmiştir. Zemberek kütüphanesinin .net sürümünü oluşturmak üzere NZemberek projesi başlatılmıştır.

Zemberek kütüphanesi ve LibreOffice eklentisi java dilinde yazıldığı için platform bağımsızdır.

2005 yılında LKD 4.Linux ve Özgür Yazılım şenliğinde yılın en iyi Özgür Yazılım'ı ödülünü almıştır."""

    print(özetle(köşeliAyraçKaldır(g)))
