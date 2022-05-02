inA = input("Masukkan angka A: ")
inB = input("Masukkan Angka B: ")

inO = input("Masukkan Operator Angka: ")

if(inO == '+'):
    print("Hasilnya adalah:", int(inA) + int(inB))
elif(inO == "x"):
    print("Hasilnya adalah:", int(inA) * int(inB))
elif(inO == ":"):
    print("Hasilnya adalah:", int(inA) / int(inB))
elif(inO == "-"):
    print("Hasilnya adalah:", int(inA) - int(inB))