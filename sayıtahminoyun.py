import random
secret_number = random.randint(1, 100)
attempts = 0
print("1 ile 100 arasında bir sayı tuttum. tahmin etmeye çalış!")
while True:
    try:
        guess = int(input("tahmininiz nedir? "))
        attempts +=1
        if guess < secret_number:
            print("daha büyük sayı söyleyin.")
        elif guess > secret_number:
            print("daha küçük sayı söyleyin.")
        else:
            print(f"tebrikler! {attempts} denemede doğru tahmin ettiniz.")
            break
    except ValueError:
        print("lütfen geçerli sayı girin.")
     