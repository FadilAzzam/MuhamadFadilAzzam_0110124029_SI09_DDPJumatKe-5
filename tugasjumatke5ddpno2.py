angka_pilihan = int(input("""Masukkan Pilihan :
                          1. menghitung luas persegi
                          2. menghitung luas lingkaran
                          3. menghitung luas segitiga 
                          """))
match angka_pilihan:
    case 1 :
        print("menghitung luas persegi")
        sisi = int(input("masukkan nilai sisi :"))
        luas_persegi = sisi ** 2
        print(f"luas persegi dengan sisi {sisi} cm, adalah {luas_persegi} cm^2")
    case 2 :
        print("menghitung luas lingkaran")
        jari_jari = float(input("masukkan nilai jari-jari :"))
        luas_lingkaran = 22/7 * jari_jari ** 2
        print(f"luas lingkaran dengan jari jari {jari_jari} cm, adalah {luas_lingkaran} cm^2")
    case 3 :
        print("menghitung luas segitiga :")
        alas = float(input("masukkan nilai alas :"))
        tinggi = float(input("masukkan nilai tinggi :"))
        luas_segitiga = 1/2 * alas * tinggi
        print(f"luas segitiga dengan alas{alas}cm dan tinggi{tinggi}cm, adalah {luas_segitiga} cm^2")