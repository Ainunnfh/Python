# latihan konfersi satuan temperature

#program konversi celcius ke satuan lainnya

print('\nPROGRAM KONVERSI TEMPERATURE\n')

celcius = float(input('Masukkan suhu dalam celcius : '))
print('Suhu adalah', celcius, 'Celcius')

#Reamur
#4/5 C
reamur = (4/5) * celcius
print('Suhu adalah', reamur, 'Reamur')
#Fahrenhait
fahrenhait = ((9/5) * celcius) + 32
print('Suhu adalah', fahrenhait, 'Fahrenhait')
#Kelvin
kelvin = celcius + 273
print('Suhu adalah', kelvin, 'Kelvin')

'''
Rumus konversi temperature
               Celcius  Reamur    Fahrenhait  Kelvin
Celcius                  4/5C      9/5C+32     C+273
Reamur           5/4R              9/4R+32     5/4R+273      
Fahrenhait   5/9F(F-32) 4/9F(F-32)
Kelvin      K-273       4/5(K-273)
'''