from datetime import datetime
try:
    tarih_metni=input("sınav tarih ve saatini giriniz (GG.AA.YYYY HH:MM): ")
    sınav_tarihi=datetime.strptime(tarih_metni, "%d.%m.%Y %H:%M")
    suan=datetime.now()
    fark=sınav_tarihi-suan
    if fark.days<0:
        print("sınav tarihi geçmiş.")
    else:
        print(f"sınava kalan süre: {fark.days} gün, {fark.seconds//3600} saat, {fark.seconds//60%60} dakika.")

except ValueError:
    print("lütfen geçerli tarih giriniz.")




    