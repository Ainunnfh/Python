print('-------------------Operasi Aritmatika-------------------')
a = 10
b = 3

# Operasi Penjumlahan
hasil = a + b
print(a, '+',b,'=',hasil)

# Operasi Pengurangan
hasil = a - b
print(a, '-',b,'=',hasil)

# Operasi Perkalian
hasil = a * b
print(a, '*',b,'=',hasil)

# Operasi Pembagian
hasil = a / b
print(a, '/',b,'=',hasil)

# Operasi Pangkat(Eksponen)
hasil = a ** b
print(a, '**',b,'=',hasil)

# Operasi Modulus (sisa bagi)
hasil = a % b
print(a, '%',b,'=',hasil)

# Operasi Floor Division (Kebalikannya Modulus)
hasil = a // b
print(a, '//',b,'=',hasil)

print('-------------------Prioritas Operasi-------------------')
'''
    1. () (tanda kurung)
    2. Eksponen
    3. Perkalian, Pembagian, Modulus, Floor Division
    4. Penjumlahan, Pengurangan
''' 
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**' ,y, '*' ,z, '+' ,x, '/' ,y, '-' ,y, '%' ,z, '//' ,x, '=', hasil)

'''
Keterangan Langkah
3 ** 2 * 4 + 3 / 2 - 2 % 4 // 3
    1. Kerjakan Eksponen terlebih dahulu, shg hasilnya menjadi
        9 * 4 + 3 / 2 - 2 % 4 // 3
    2. Kerjakan Perkalian dan Pembagian dan Floor Division, shg hasilnya menjadi
        36 + 1,5 -  0
    3. Kerjakan Penjumlahan dan Pengurangan, shg hasil akhir
        37,5
# '''
