veri=input("bir sayı girin: ")
try:
    sayi=int(veri)
    print(f"girdiğiniz sayı: {sayi}")

except ValueError:
    print("lütfen bir sayı giriniz")
