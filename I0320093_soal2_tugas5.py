# Program Grading Nilai

Nama = input('Masukkan Nama Anda : ')
Nilai = int(input('Masukkan nilai Anda: '))

if Nilai < 60 :
    Hasil_Konversi = 'E'
    print('Halo,', Nama + '! Nilai anda setelah dikonversi adalah', Hasil_Konversi)
elif Nilai <= 64 :
    Hasil_Konversi = 'C'
    print('Halo,', Nama + '! Nilai anda setelah dikonversi adalah', Hasil_Konversi)
elif Nilai <= 69:
    Hasil_Konversi = 'C+'
    print('Halo,', Nama + '! Nilai anda setelah dikonversi adalah', Hasil_Konversi)
elif Nilai <= 74:
    Hasil_Konversi = 'B'
    print('Halo,', Nama + '! Nilai anda setelah dikonversi adalah', Hasil_Konversi)
elif Nilai <= 79:
    Hasil_Konversi = 'B+'
    print('Halo,', Nama + '! Nilai anda setelah dikonversi adalah', Hasil_Konversi)
elif Nilai <= 84:
    Hasil_Konversi = 'A-'
    print('Halo,', Nama + '! Nilai anda setelah dikonversi adalah', Hasil_Konversi)
elif Nilai <= 100:
    Hasil_Konversi = 'A'
    print('Halo,', Nama + '! Nilai anda setelah dikonversi adalah', Hasil_Konversi)
else:
    print('NILAI INVALID, INPUT ULANG NILAI !')
