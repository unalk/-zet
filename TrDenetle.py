


HARF="ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZXQ"
KHARF="abcçdefgğhıijklmnoöprsştuüvyzxq"
ÜNLÜLER={"tümü":"aeıioöuü", "kalın":"aıou", "ince":"eiöü", "dar":"ıiuü",
         "geniş":"aeoö", "düz":"aeıi", "yuvarlak": "oöuü"}
HARFVB=HARF+"abcçdefgğhıijklmnoöprsştuüvyz"+" \n\t"
HARFVBN=HARF+"abcçdefgğhıijklmnoöprsştuüvyzxq"+"0123456789 \n\t"

def köşeliAyraçKaldır(girdi):
    ekle=True
    çkt=""
    for d in girdi:
        if ekle:
            if d != "[":
                çkt+=d
            else:
                ekle=False
        else:
            if d=="]":
                ekle=True
    return çkt

def tümOlasıEkleriyle(sözcük,tekil=True):
    eklerle=[sözcük]
    for ek in ÜNLÜLER["tümü"]:
        eklerle.append(sözcük+ek)
    #ünsüz yumuşaması
    if sözcük[-1]=="p":
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük[0:-1]+"b"))
    elif sözcük[-1]=="ç":
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük[0:-1]+"c"))
    elif sözcük[-1]=="t":
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük[0:-1]+"d"))
    elif sözcük[-1]=="k":
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük[0:-1]+"g"))
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük[0:-1]+"ğ"))
    #kaynaştırma
    elif sözcük[-1] in ÜNLÜLER["tümü"]:
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük+"y"))
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük+"n"))
    eklerle.append(sözcük+"la")
    eklerle.append(sözcük+"le")
    if tekil:
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük+"ler",False))
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük+"lar",False))
    return eklerle

def temelleştir(yazı):
    çıktı=""
    for i in yazı:
        if i in HARF:
            çıktı+=KHARF[HARF.find(i)]
        elif i == " " or i in KHARF:
            çıktı+=i
        elif i== "\n":
            çıktı+=" "

    return çıktı

def temelleştirSayı(yazı):
    çıktı=""
    for i in yazı:
        if i in HARF:
            çıktı+=KHARF[HARF.find(i)]
        elif i == " " or i in KHARF or i in "1234567890":
            çıktı+=i

    return çıktı

def küçült(yazı):
    çıktı=""
    for i in yazı:
        if i in HARF:
            çıktı+=KHARF[HARF.find(i)]
        else:
            çıktı+=i

    return çıktı

def büyüt(yazı):
    çıktı=""
    for i in yazı:
        if i in KHARF:
            çıktı+=HARF[KHARF.find(i)]
        else:
            çıktı+=i

    return çıktı

def tümüBüyükMü(y):
    for d in y:
        if d in KHARF:
            return False
    return True
            
