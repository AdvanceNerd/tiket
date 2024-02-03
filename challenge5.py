print("1. Prabumulih")
print("2. Muara Enim")
print("3. Lubuk Linggau")
kota = int(input("Pilihan Kota (1/2/3): "))

print("Kode Kelas : ")
print("1. Ekonomi")
print("2. Bisnis")
print("3. Esekutif")
kelas = int(input("Pilihan Kelas (1/2/3): "))
quantity = int(input("Banyak Tiket: "))
kode_promo = input("Masukkan Kode Promo (Jika ada): ")
print("-" * 15)
def calculate_discount(subtotal, promo_code):
    if promo_code.upper() == "IGS":
        discount = 0.1 * subtotal
        return discount
    else:
        return 0

if kota == 1:
    if kelas == 1:
        harga_tiket = 100000
        subtotal = harga_tiket * quantity
    elif kelas == 2:
        harga_tiket = 400000
        subtotal = harga_tiket * quantity
    else:
        harga_tiket = 700000
        subtotal = harga_tiket * quantity

elif kota == 2:
    if kelas == 1:
        harga_tiket = 200000
        subtotal = harga_tiket * quantity
    elif kelas == 2:
        harga_tiket = 500000
        subtotal = harga_tiket * quantity
    else:
        harga_tiket = 800000
        subtotal = harga_tiket * quantity

elif kota == 3:
    if kelas == 1:
        harga_tiket = 300000
        subtotal = harga_tiket * quantity
    elif kelas == 2:
        harga_tiket = 600000
        subtotal = harga_tiket * quantity
    else:
        harga_tiket = 900000
        subtotal = harga_tiket * quantity

else:
    print("Pilihan kota tidak valid.")

discount = calculate_discount(subtotal, kode_promo)

print("Harga Tiket  :", harga_tiket)
print("Sub Total    :", subtotal)
print("Discount     :", discount)
total_payment = subtotal - discount
print("Total Bayar  :", total_payment)