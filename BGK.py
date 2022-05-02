import random as rand

# Komputer
BGK = ['Batu', 'Gunting', 'Kertas']
pilihan_komputer = rand.choice(BGK)

# Debugging
print(f"Pilihan Komputer: {pilihan_komputer}")

pilihan_user = input("Batu, Gunting, atau Kertas?: ")

if(pilihan_user == pilihan_komputer or pilihan_user == pilihan_komputer.lower()):
    print(f"Seri!, Karena kalian sama sama Menjawab {pilihan_komputer}")
elif(pilihan_user == "Batu" or pilihan_user == "batu"):
    if(pilihan_komputer == BGK[2]):
        print("Kamu Kalah!")
    elif(pilihan_komputer == BGK[1]):
        print("kamu Menang!")
elif(pilihan_user == "Gunting" or pilihan_user == "gunting"):
    if(pilihan_komputer == BGK[0]):
        print("Kamu Kalah!")
    elif(pilihan_komputer == BGK[2]):
        print("kamu Menang!")
elif(pilihan_user == "Kertas" or pilihan_user == "kertas"):
    if(pilihan_komputer == BGK[1]):
        print("Kamu Kalah!")
    elif(pilihan_komputer == BGK[0]):
        print("kamu Menang!")