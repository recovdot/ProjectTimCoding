import random as rand

acak = rand.randint(0, 10)

if (acak >= 5):
    print("Clue nih: Angka lebih dari 5")
elif (acak <= 5):
    print("Clue nih: Angka kurang dari 5")

# Aktifkan kode dibawah ini untuk debugging Angka
# print(f"Angka Debug: {acak}\n")

inputAngka = input("Hayooo tebak Angkanya: ")

if(inputAngka == f"{acak}"):
    print("KAMU BENAR, Selamat ya udah ga Jomblo lagi :P")
else:
    print(f"Kamu Harusnya Jawab Angka {acak}!!")
    print("Yahaha Salah, kasian Jomblo :P")