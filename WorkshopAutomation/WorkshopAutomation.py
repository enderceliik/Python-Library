#https://github.com/Enderceliik
#Ender ÇELİK

import random #Sevkiyatlara random ID vermek icin
def ekle():
    sayilar = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    def cost(amount_c):      #Kullanicinin girdigi hacim bilgisine gore maliyet hesaplayan fonksiyon
        amount_c = str(amount_c)
        amt_string = amount_c[0:2]
        amt_string_1 = amount_c[2]
        amt_string = int(amt_string)
        amt_string_1 = int(amt_string_1)

        price_amount = amt_string * 700
        if(amt_string_1 == 1):
            price_amount += 70
        if(amt_string_1 == 2):
            price_amount += 140
        if(amt_string_1 == 3):
            price_amount += 210
        if(amt_string_1 == 4):
            price_amount += 280
        if(amt_string_1 == 5):
            price_amount += 350
        if(amt_string_1 == 6):
            price_amount += 420
        if(amt_string_1 == 7):
            price_amount += 490
        if(amt_string_1 == 8):
            price_amount += 560
        if(amt_string_1 == 9):
            price_amount += 630
        return price_amount
    def profit(amount_c,cost):  #hacim ve maliyete gore kar hesaplayan fonksiyon
        price_amount = 0
        if(amount_c > 20000):
            price_amount -= 800
        if (amount_c > 21000):
            price_amount -= 80
        if (amount_c > 22000):
            price_amount -= 80
        if (amount_c > 23000):
            price_amount -= 80
        if (amount_c > 24000):
            price_amount -= 80
        if (amount_c > 25000):
            price_amount -= 80
        if (amount_c > 26000):
            price_amount -= 80
        if (amount_c > 27000):
            price_amount -= 80
        if (amount_c > 28000):
            price_amount -= 80
        if (amount_c > 29000):
            price_amount -= 80
        if (amount_c > 30000):
            price_amount -= 80
        if (amount_c > 31000):
            price_amount -= 80
        if (amount_c > 32000):
            price_amount -= 80
        if (amount_c > 33000):
            price_amount -= 80
        if (amount_c > 34000):
            price_amount -= 80
        amount_c = (amount_c * 80) / 100
        amount_c = str(amount_c)
        amt_string = amount_c[0:2]
        amt_string_1 = amount_c[2]
        amt_string = int(amt_string)
        amt_string_1 = int(amt_string_1)
        price_amount += amt_string * 1400
        if (amt_string_1 == 1):
            price_amount += 140
        if (amt_string_1 == 2):
            price_amount += 280
        if (amt_string_1 == 3):
            price_amount += 420
        if (amt_string_1 == 4):
            price_amount += 560
        if (amt_string_1 == 5):
            price_amount += 700
        if (amt_string_1 == 6):
            price_amount += 840
        if (amt_string_1 == 7):
            price_amount += 980
        if (amt_string_1 == 8):
            price_amount += 1120
        if (amt_string_1 == 9):
            price_amount += 1260
        price_amount -= cost
        return  price_amount
    while (True):
        name_control = 0
        print("Eklemek istediğiniz sevkiyatın; ")
        name = input("\tşoförünün ismini giriniz: ")
        plate = input("\taraç plakasını giriniz:(Orn: 29 AAP 533) ")
        amount = input("\thacim bilgisini giriniz: ")
        date = input("\ttarihini giriniz: ")
        print("\n" * 50)
        name_list = name.split(" ")
        for i in range(0, len(name_list)):
            name_krk = name_list[i]
            name_krk = str(name_krk)
            if (name_krk.isalpha() == False):
                name_control = 1
        if (name_control == 1):
            print("\n" * 50)
            print("İsmi doğru bir şekilde girdiğinizden emin olun")
            continue
        name = name.upper()
        if (len(plate) != 10 or plate.startswith(sayilar) == False or plate[1] in sayilar == False or plate.endswith(sayilar) == False or plate[8] in sayilar == False):
            print("\n" * 50)
            print("Girdiğiniz plakanın standartlara uymasına dikkat ediniz\n(sayı-sayı-boşluk-harf-harf-harf-boşluk-sayı-sayı-sayı)")
            continue
        if (plate[3] in sayilar == True or plate[4] in sayilar == True or plate[5] in sayilar == True):
            print("\n" * 50)
            print("Girdiğiniz plakanın standartlara uymasına dikkat ediniz\n(sayı-sayı-boşluk-harf-harf-harf-boşluk-sayı-sayı-sayı)")
            continue
        plate_control = plate[0:2]
        plate_control = int(plate_control)
        if(plate_control < 1 or plate_control > 81):
            print("\n" * 50)
            print("Girdiğiniz plaka kodu 0 ile 81 arasında olmalı")
            continue
        if (amount.isdigit() == False):
            print("\n" * 50)
            print("Sevkiyat hacmini doğru girmeye dikkat ediniz")
            continue
        amount_c = int(amount)
        if (amount_c < 20000 or amount_c > 35000):
            print("\n" * 50)
            print("Girdiğiniz hacimdeki sevkiyatlar sisteme kabul edilmemektedir(20000<x<35000)")
            continue
        if (len(date) != 10 or date.startswith(sayilar) == False or date[1] in sayilar == False or date.endswith(sayilar) == False or plate[8] in sayilar == False):
            print("\n" * 50)
            print("Tarihi doğru biçimde girmeye dikkat ediniz(orn: 06.03.2021)")
            continue
        if (date[2] != "." or date[5] != "."):
            print("\n" * 50)
            print("Tarihi doğru biçimde girmeye dikkat ediniz(orn: 06.03.2021)")
            continue
        date_list = date.split(".")
        date_day = int(date_list[0])
        date_month = int(date_list[1])
        date_year = int(date_list[2])
        if (date_day < 0 or date_day > 31 or date_month < 0 or date_month > 12 or date_year < 1960 or date_year > 2021):
            print("\n" * 50)
            print("Tarihi doğru girmeye dikkat ediniz(orn: 06.03.2021)")
            continue
        plate = plate.upper()
        break

    try:                #Kayit dosyasinin mevcut oldugu ve program tarafindan bulunabildigi durum
        dosya = open("19010011069.txt", "r+", encoding="utf-8")
        satir_1 = dosya.readlines()
        line_counter = len(satir_1)
        liste = []
        dosya.seek(0)
        if (line_counter == 0):
            use_will = cost(amount_c)
            use_will_v2 = profit(amount_c, use_will)
            use_will = str(use_will)
            use_will_v2 = str(use_will_v2)
            user_id = random.randint(100, 999)
            user_id = str(user_id)
            liste.append([name, plate, amount, use_will, use_will_v2, user_id, date])
            karakter = liste[0][0] + "-" + liste[0][1] + "-" + liste[0][2] + "-" + liste[0][3] + "-" + liste[0][4] + "-" + liste[0][5] + "-" + liste[0][6] + "\n"
            satir_1.append(karakter)
            print(satir_1[0], file=dosya, end="")
            dosya.close()
            return
        else:
            while (satir_1[line_counter - 1] == '\n'):   #Txt'nin sonunda bosluk varsa diye
                satir_1.pop()
                line_counter -= 1
            for i in range(0, line_counter):
                karakter = satir_1[i]
                karakter = karakter[:-1]
                satir_1[i] = karakter
            for i in range(0, line_counter):
                karakter = str(satir_1[i])
                liste.append(karakter.split("-"))
            use_will = cost(amount_c)
            use_will_v2 = profit(amount_c, use_will)
            use_will = str(use_will)
            use_will_v2 = str(use_will_v2)
            for i in range(0, line_counter):
                user_id = random.randint(100, 999)
                if(int(liste[i][5]) == user_id):
                    i = 0
                    continue
            user_id = str(user_id)
            liste.append([name, plate, amount, use_will, use_will_v2, user_id, date])
            for i in range(0, line_counter + 1):
                if (i != line_counter):
                    karakter = liste[i][0] + "-" + liste[i][1] + "-" + liste[i][2] + "-" + liste[i][3] + "-" + liste[i][4] + "-" + liste[i][5] + "-" + liste[i][6] + "\n"
                    satir_1[i] = karakter
                else:
                    karakter = liste[i][0] + "-" + liste[i][1] + "-" + liste[i][2] + "-" + liste[i][3] + "-" + liste[i][4] + "-" + liste[i][5] + "-" + liste[i][6] +  "\n"
                    satir_1.append(karakter)
            for i in range(0, line_counter + 1):
                print(satir_1[i], file=dosya, end="")
            dosya.close()
            return
    except FileNotFoundError:    #Kayit dosyasinin mevcut olmadigi ve program tarafindan bulunamadigi durum
        dosya = open("19010011069.txt", "w", encoding="utf-8")
        satir_1 = []
        liste = []
        dosya.seek(0)
        use_will = cost(amount_c)
        use_will_v2 = profit(amount_c, use_will)
        use_will = str(use_will)
        use_will_v2 = str(use_will_v2)
        user_id = random.randint(100, 999)
        user_id = str(user_id)
        liste.append([name, plate, amount, use_will, use_will_v2, user_id, date])
        karakter = liste[0][0] + "-" + liste[0][1] + "-" + liste[0][2] + "-" + liste[0][3] + "-" + liste[0][4] + "-" + liste[0][5] + "-" + liste[0][6] + "\n"
        satir_1.append(karakter)
        print(satir_1[0], file=dosya, end="")
        dosya.close()
        return
def listele():     #Kayitlardaki sevkiyatlari listeleyen fonksiyon
    try:
        dosya = open("19010011069.txt", "r", encoding="utf-8")
        satir_1 = dosya.readlines()
        dosya.close()
        line_counter = len(satir_1)
        if (line_counter == 0):
            print("Listelenebilecek herhangi bir sevkiyat bilgisi bulunmamaktadır.")
        else:
            print("||      Şoför Adı      ||   Plaka    ||Metre^3||Maliyet||  Kâr  || Sevkiyat id ||   Tarih    ||")
            while (satir_1[line_counter - 1] == '\n'):
                satir_1.pop()
                line_counter -= 1
            liste = []
            for i in range(0, line_counter):
                karakter = str(satir_1[i])
                karakter = karakter[:-1]
                satir_1[i] = karakter
            for i in range(0, line_counter):
                karakter = satir_1[i]
                liste.append(karakter.split("-"))
            for i in range(0, line_counter):
                for j in range(0, 7):
                    if (j == 0):
                        karakter = liste[i][j]
                        karakter = str(karakter)
                        bosluk = 20 - len(karakter)
                        print("||".format(i + 1), end=" ")
                        print(liste[i][j], end="")
                        for t in range(0, bosluk):
                            print(" ", end="")
                        print("|| ", end="")
                    if(j == 4):
                        karakter = liste[i][j]
                        karakter = str(karakter)
                        if(len(karakter) == 4):
                            print(liste[i][j], end="  || ")
                        else:
                            print(liste[i][j], end=" || ")

                    if(j == 5):
                        print("    {}     ".format(liste[i][j]),end="|| ")
                    if (j != 6 and j != 0 and j!=5 and j!=4):
                        print(liste[i][j], end=" || ")
                    if (j == 6):
                        print(liste[i][j], end=" ||\n")
            for i in range(0, 48):
                if(i != 47):
                    print("-", end="-")
                else:
                    print("-")
    except FileNotFoundError:
        print("\n" * 50)
        print("Listelenebilecek herhangi bir sevkiyat bilgisi bulunmamaktadır.")
        return
def guncelle():
    try:
        dosya = open("19010011069.txt", "r", encoding="utf-8")  #read modunda acip okuyup tekrar w ile acmak icin kapattigim kisim
        satir_1 = dosya.readlines()
        dosya.close()
        line_counter = len(satir_1)
        if (line_counter == 0):
            print("\n" * 50)
            print("Güncellenebilecek herhangi bir sevkiyat bilgisi bulunmamaktadır.")
        else:
            satir_2 = []

            while (satir_1[line_counter - 1] == '\n'):
                satir_1.pop()
                line_counter -= 1
            liste = []
            for i in range(0, line_counter):
                karakter = str(satir_1[i])
                karakter = karakter[:-1]
                satir_1[i] = karakter
            for i in range(0, line_counter):
                karakter = satir_1[i]
                liste.append(karakter.split("-"))
            while(True):
                print("     ||      Şoför Adı      ||   Plaka    ||Metre^3||Maliyet||  Kâr  || Sevkiyat id ||   Tarih    ||")
                for i in range(0, line_counter):
                    for j in range(0, 7):
                        if (j == 0):
                            karakter = liste[i][j]
                            karakter = str(karakter)
                            bosluk = 20 - len(karakter)
                            print(" {}-) ||".format(i + 1), end=" ")
                            print(liste[i][j], end="")
                            for t in range(0, bosluk):
                                print(" ", end="")
                            print("|| ", end="")
                        if (j == 4):
                            karakter = liste[i][j]
                            karakter = str(karakter)
                            if (len(karakter) == 4):
                                print(liste[i][j], end="  || ")
                            else:
                                print(liste[i][j], end=" || ")
                        if (j == 5):
                            print("    {}     ".format(liste[i][j]), end="|| ")
                        if (j != 6 and j != 0 and j != 5 and j != 4):
                            print(liste[i][j], end=" || ")
                        if (j == 6):
                            print(liste[i][j], end=" ||\n")
                for i in range(0, 48):
                    if (i != 47):
                        print("-", end="-")
                    else:
                        print("-")

                secim_numP = input("Güncellemek istediğiniz profilin numarasını giriniz: ")
                if (secim_numP.isdigit() is False):  # Kullanicinin absurt degerler girmesinin onune gecmeye calistim
                    print("\n" * 50)
                    print("Lütfen menüden seçim yapınız")
                    continue
                secim_numP = int(secim_numP)
                secim_numP -= 1
                if (secim_numP > len(liste)-1 or secim_numP < 0):
                    print("\n" * 50)
                    print("Lütfen menüden seçim yapınız")
                    continue
                print("\n" * 50)
                break

            while (True):
                secim_numI = input("Güncellemek istediğiniz bilgiyi menüden seçiniz:\n(Güncelleme yapmadan ana menüye dönmek için <0>'a basın)"
                                   " \n 1-)İsim güncelleme\n 2-)Plaka bilgisi güncelleme\n"
                                   " 3-)M^3 bilgisi güncelleme\n 4-)Tarih bilgisi güncelleme")
                if(secim_numI == "0"):
                    print("\n" * 50)
                    return
                if (secim_numI.isdigit() is False):  # Kullanicinin absurt degerler girmesinin onune gecmeye calistim
                    print("\n" * 50)
                    print("Lütfen menüden seçim yapınız")
                    continue
                secim_numI = int(secim_numI)
                if (secim_numI > 4 or secim_numI < 1):
                    print("\n" * 50)
                    print("Lütfen menüden seçim yapınız")
                    continue
                print("\n" * 50)
                break
            sayilar = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
            if (secim_numI == 1):
                while (True):
                    name_control = 0
                    new_name = input("Yeni ismi giriniz:\n(Güncellemekten vazgeçip ana menüye dönmek için <0> giriniz)")
                    if (new_name == "0"):
                        break
                    name_list = new_name.split(" ")
                    for i in range(0, len(name_list)):
                        name_krk = name_list[i]
                        name_krk = str(name_krk)
                        if (name_krk.isalpha() == False):
                            name_control = 1
                    if (name_control == 1):
                        print("\n" * 50)
                        print("İsmi doğru bir şekilde girdiğinizden emin olun")
                        continue
                    new_name = new_name.upper()
                    liste[secim_numP][0] = new_name
                    print("\n" * 50)
                    break
            if(secim_numI == 2):
                sayilar = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
                while(True):
                    new_plate = input("\tYeni araç plakasını giriniz:(Orn: 29 AAP 533) ")
                    if (len(new_plate) != 10 or new_plate.startswith(sayilar) == False or new_plate[1] in sayilar == False or new_plate.endswith(sayilar) == False or new_plate[8] in sayilar == False):
                        print("\n" * 50)
                        print("Girdiğiniz plakanın standartlara uymasına dikkat ediniz\n(sayı-sayı-boşluk-harf-harf-harf-boşluk-sayı-sayı-sayı)")
                        continue
                    if (new_plate[3] in sayilar == True or new_plate[4] in sayilar == True or new_plate[5] in sayilar == True):
                        print("\n" * 50)
                        print("Girdiğiniz plakanın standartlara uymasına dikkat ediniz\n(sayı-sayı-boşluk-harf-harf-harf-boşluk-sayı-sayı-sayı)")
                        continue
                    plate_control = new_plate[0:2]
                    plate_control = int(plate_control)
                    if (plate_control < 1 or plate_control > 81):
                        print("\n" * 50)
                        print("Girdiğiniz plaka kodu 0 ile 81 arasında olmalı")
                        continue
                    new_plate = new_plate.upper()
                    liste[secim_numP][1] = new_plate
                    print("\n" * 50)
                    break
            if(secim_numI == 3):
                def cost(amount_c):
                    amount_c = str(amount_c)
                    amt_string = amount_c[0:2]
                    amt_string_1 = amount_c[2]
                    amt_string = int(amt_string)
                    amt_string_1 = int(amt_string_1)

                    price_amount = amt_string * 700
                    if (amt_string_1 == 1):
                        price_amount += 70
                    if (amt_string_1 == 2):
                        price_amount += 140
                    if (amt_string_1 == 3):
                        price_amount += 210
                    if (amt_string_1 == 4):
                        price_amount += 280
                    if (amt_string_1 == 5):
                        price_amount += 350
                    if (amt_string_1 == 6):
                        price_amount += 420
                    if (amt_string_1 == 7):
                        price_amount += 490
                    if (amt_string_1 == 8):
                        price_amount += 560
                    if (amt_string_1 == 9):
                        price_amount += 630
                    return price_amount

                def profit(amount_c, cost):
                    price_amount = 0
                    if (amount_c > 20000):
                        price_amount -= 800
                    if (amount_c > 21000):
                        price_amount -= 80
                    if (amount_c > 22000):
                        price_amount -= 80
                    if (amount_c > 23000):
                        price_amount -= 80
                    if (amount_c > 24000):
                        price_amount -= 80
                    if (amount_c > 25000):
                        price_amount -= 80
                    if (amount_c > 26000):
                        price_amount -= 80
                    if (amount_c > 27000):
                        price_amount -= 80
                    if (amount_c > 28000):
                        price_amount -= 80
                    if (amount_c > 29000):
                        price_amount -= 80
                    if (amount_c > 30000):
                        price_amount -= 80
                    if (amount_c > 31000):
                        price_amount -= 80
                    if (amount_c > 32000):
                        price_amount -= 80
                    if (amount_c > 33000):
                        price_amount -= 80
                    if (amount_c > 34000):
                        price_amount -= 80
                    amount_c = (amount_c * 80) / 100
                    amount_c = str(amount_c)
                    amt_string = amount_c[0:2]
                    amt_string_1 = amount_c[2]
                    amt_string = int(amt_string)
                    amt_string_1 = int(amt_string_1)
                    price_amount += amt_string * 1400
                    if (amt_string_1 == 1):
                        price_amount += 140
                    if (amt_string_1 == 2):
                        price_amount += 280
                    if (amt_string_1 == 3):
                        price_amount += 420
                    if (amt_string_1 == 4):
                        price_amount += 560
                    if (amt_string_1 == 5):
                        price_amount += 700
                    if (amt_string_1 == 6):
                        price_amount += 840
                    if (amt_string_1 == 7):
                        price_amount += 980
                    if (amt_string_1 == 8):
                        price_amount += 1120
                    if (amt_string_1 == 9):
                        price_amount += 1260
                    price_amount -= cost
                    return price_amount
                while(True):
                    new_amount = input("\tYeni hacim bilgisini giriniz: ")
                    if (new_amount.isdigit() == False):
                        print("\n" * 50)
                        print("Sevkiyat hacmini doğru girmeye dikkat ediniz")
                        continue
                    new_amount_c = int(new_amount)
                    if (new_amount_c < 20000 or new_amount_c > 35000):
                        print("\n" * 50)
                        print("Girdiğiniz hacimdeki sevkiyatlar sisteme kabul edilmemektedir(20000<x<35000)")
                        continue
                    break

                new_use_will = cost(new_amount_c)
                new_use_will_v2 = profit(new_amount_c, new_use_will)
                new_use_will = str(new_use_will)
                new_use_will_v2 = str(new_use_will_v2)
                new_amount_c = str(new_amount)
                liste[secim_numP][2] = new_amount_c
                liste[secim_numP][3] = new_use_will
                liste[secim_numP][4] = new_use_will_v2
            if(secim_numI == 4):
                while(True):
                    new_date = input("\ttarihini giriniz: ")
                    if (len(new_date) != 10 or new_date.startswith(sayilar) == False or new_date[1] in sayilar == False or new_date.endswith(sayilar) == False or new_date[8] in sayilar == False):
                        print("\n" * 50)
                        print("Tarihi doğru biçimde girmeye dikkat ediniz(orn: 06.03.2021)")
                        continue
                    if (new_date[2] != "." or new_date[5] != "."):
                        print("\n" * 50)
                        print("Tarihi doğru biçimde girmeye dikkat ediniz(orn: 06.03.2021)")
                        continue
                    date_list = new_date.split(".")
                    date_day = int(date_list[0])
                    date_month = int(date_list[1])
                    date_year = int(date_list[2])
                    if (date_day < 0 or date_day > 31 or date_month < 0 or date_month > 12 or date_year < 1960 or date_year > 2021):
                        print("\n" * 50)
                        print("Tarihi doğru girmeye dikkat ediniz(orn: 06.03.2021)")
                        continue
                    break
                liste[secim_numP][6] = new_date
            for i in range(0, line_counter):
                karakter = liste[i][0] + "-" + liste[i][1] + "-" + liste[i][2] + "-" + liste[i][3] + "-" + liste[i][4] + "-" + liste[i][5] + "-" + liste[i][6]+ "\n"
                satir_2.append(karakter)
            dosya = open("19010011069.txt", "w", encoding="utf-8")
            for i in range(0, line_counter):
                print(satir_2[i], file=dosya, end="")
            dosya.close()
    except FileNotFoundError:
        print("\n" *50)
        print("Güncellenebilecek herhangi bir sevkiyat bilgisi bulunmamaktadır.")
        return
def sil():    #Veriyi silmeye yarayan fonksiyon
    try:
        dosya = open("19010011069.txt", "r", encoding="utf-8")
        satir_1 = dosya.readlines()
        dosya.close()
        satir_2 = []
        line_counter = len(satir_1)
        if (line_counter == 0):
            print("Silinebilecek herhangi bir sevkiyat bilgisi bulunmamaktadır.")
        else:
            print("     ||      Şoför Adı      ||   Plaka    ||Metre^3||Maliyet||  Kâr  || Sevkiyat id ||   Tarih    ||")
            while (satir_1[line_counter - 1] == '\n'):
                satir_1.pop()
                line_counter -= 1
            dosya = open("19010011069.txt", "w", encoding="utf-8")
            liste = []
            for i in range(0, line_counter):
                karakter = str(satir_1[i])
                karakter = karakter[:-1]
                satir_1[i] = karakter
            for i in range(0, line_counter):
                karakter = satir_1[i]
                liste.append(karakter.split("-"))
            while (True):
                for i in range(0, line_counter):
                    for j in range(0, 7):
                        if (j == 0):
                            karakter = liste[i][j]
                            karakter = str(karakter)
                            bosluk = 20 - len(karakter)
                            print(" {}-) ||".format(i + 1), end=" ")
                            print(liste[i][j], end="")
                            for t in range(0, bosluk):
                                print(" ", end="")
                            print("|| ", end="")
                        if (j == 4):
                            karakter = liste[i][j]
                            karakter = str(karakter)
                            if (len(karakter) == 4):
                                print(liste[i][j], end="  || ")
                            else:
                                print(liste[i][j], end=" || ")
                        if (j == 5):
                            print("    {}     ".format(liste[i][j]), end="|| ")
                        if (j != 6 and j != 0 and j != 5 and j != 4):
                            print(liste[i][j], end=" || ")
                        if (j == 6):
                            print(liste[i][j], end=" ||\n")
                for i in range(0, 48):
                    if (i != 47):
                        print("-", end="-")
                    else:
                        print("-")
                del_sevk = input("Silmek istediğiniz sevkiyatın numarasını tuşlayınız: ")
                if (del_sevk.isdigit() is False):  # Kullanicinin absurt degerler girmesinin onune gecmeye calistim
                    print("\n" * 50)
                    print("Lütfen menüden seçim yapınız")
                    continue
                del_sevk = int(del_sevk)
                del_sevk -= 1
                if (del_sevk > len(satir_1)-1 or del_sevk < 0):
                    print("\n" * 50)
                    print("Lütfen menüden seçim yapınız")
                    continue
                print("\n" * 50)
                break
            liste.pop(del_sevk)
            for i in range(0, line_counter - 1):
                karakter = liste[i][0] + "-" + liste[i][1] + "-" + liste[i][2] + "-" + liste[i][3] + "-" + liste[i][4] + "-" + liste[i][5] + "-" + liste[i][6]+ "\n"
                satir_2.append(karakter)
            for i in range(0, line_counter - 1):
                print(satir_2[i], file=dosya, end="")
            dosya.close()
    except FileNotFoundError:
        print("\n" * 50)
        print("Silinebilecek herhangi bir sevkiyat bilgisi bulunmamaktadır.")
        return
def arama():
    try:
        dosya = open("19010011069.txt", "r", encoding="utf-8")
        satir_1 = dosya.readlines()
        dosya.close()
        line_counter = len(satir_1)
        if(line_counter == 0):
            print("Sorgulanabilecek herhangi bir sevkiyat bilgisi bulunmamaktadır.")
        else:
            while (satir_1[line_counter - 1] == '\n'):
                satir_1.pop()
                line_counter -= 1
            liste = []
            for i in range(0, line_counter):
                karakter = str(satir_1[i])
                karakter = karakter[:-1]
                satir_1[i] = karakter
            for i in range(0, line_counter):
                karakter = satir_1[i]
                liste.append(karakter.split("-"))
            id_dict = {}
            for i in range(0, line_counter):
                karakter = liste[i][0] + "-" + liste[i][1] + "-" + liste[i][2] + "-" + liste[i][3] + "-" + liste[i][4] + "-" + liste[i][5] + "-" +  liste[i][6]
                id_dict[liste[i][5]] = karakter
            while(True):
                secim = input("Yapmak istediğiniz arama çeşidini seçiniz:\n <1> Sevkiyat ID'si ile arama\n <2> İsim ile arama (O isme ait tüm sevkiyatları listeler)")
                if (secim.isdigit() is False):  # Kullanicinin absurt degerler girmesinin onune gecmeye calistim
                    print("\n" * 50)
                    print("Lütfen menüden seçim yapınız")
                    continue
                secim = int(secim)
                if (secim < 1 or secim > 2):
                    print("\n" * 50)
                    print("Lütfen menüden seçim yapınız")
                    continue
                print("\n" * 50)
                break
            if(secim == 1):
                while(True):
                    while (True):
                        search_ID = input("Sorgulamak istediğiniz sevkiyatın ID'sini giriniz giriniz:\n(*ID bilmiyorsanız menüye dönüp ana listeden ilgili şoförün ID'sini öğrenip daha sonra sorgulayabilirsiniz.\nAna menüye dönmek için <0>'a basın)")
                        print("\n" * 50)
                        if(search_ID == "0"):
                            print("\n" * 50)
                            print("Ana menüye yönlendiriliyorsunuz")
                            return
                        if (search_ID.isdigit() == False):
                            print("\n" * 50)
                            print("Düzgün değer girmeye dikkat ediniz")
                            continue
                        if(len(search_ID) != 3):
                            print("\n" * 50)
                            print("Düzgün değerler girmeye özen gözteriniz")
                        break
                    result = id_dict.get(search_ID)
                    if(result == None):
                        print("\n" * 50)
                        print("Aradığınız ID'de bir sevkiyat bulunamadı")
                        return
                    else:
                        print("||      Şoför Adı      ||   Plaka    ||Metre^3||Maliyet||  Kâr  || Sevkiyat id ||   Tarih    ||")
                        menu = []
                        menu.append(result.split("-"))
                        for j in range(0, 7):
                            if (j == 0):
                                karakter = menu[0][j]
                                karakter = str(karakter)
                                bosluk = 20 - len(karakter)
                                print("||".format(1), end=" ")
                                print(menu[0][j], end="")
                                for t in range(0, bosluk):
                                    print(" ", end="")
                                print("|| ", end="")
                            if (j == 4):
                                karakter = menu[0][j]
                                karakter = str(karakter)
                                if (len(karakter) == 4):
                                    print(menu[0][j], end="  || ")
                                else:
                                    print(menu[0][j], end=" || ")

                            if (j == 5):
                                print("    {}     ".format(menu[0][j]), end="|| ")
                            if (j != 6 and j != 0 and j != 5 and j != 4):
                                print(menu[0][j], end=" || ")
                            if (j == 6):
                                print(menu[0][j], end=" ||\n")
                        for i in range(0, 48):
                            if (i != 47):
                                print("-", end="-")
                            else:
                                print("-")
            if(secim == 2):
                while(True):
                    while(True):
                        name_control = 0
                        name = input("Aradığınız ismi giriniz: \n(*Ana menüye dönmek isterseniz <0>'a basın)")
                        print("\n" * 50)
                        if (name == "0"):
                            print("\n" * 50)
                            print("Ana menüye yönlendiriliyorsunuz")
                            return
                        name_list = name.split(" ")
                        for i in range(0, len(name_list)):
                            name_krk = name_list[i]
                            name_krk = str(name_krk)
                            if (name_krk.isalpha() == False):
                                name_control = 1
                        if (name_control == 1):
                            print("\n" * 50)
                            print("İsmi doğru bir şekilde girdiğinizden emin olun")
                            continue
                        break
                    name = name.upper()
                    enter_control = 0
                    tablo = 0
                    for i in range(0, line_counter):
                        if(name == liste[i][0]):
                            if(tablo == 0):
                                print("||      Şoför Adı      ||   Plaka    ||Metre^3||Maliyet||  Kâr  || Sevkiyat id ||   Tarih    ||")
                                tablo += 1
                            for j in range(0, 7):
                                if (j == 0):
                                    karakter = liste[i][j]
                                    karakter = str(karakter)
                                    bosluk = 20 - len(karakter)
                                    print("||".format(i + 1), end=" ")
                                    print(liste[i][j], end="")
                                    for t in range(0, bosluk):
                                        print(" ", end="")
                                    print("|| ", end="")
                                if (j == 4):
                                    karakter = liste[i][j]
                                    karakter = str(karakter)
                                    if (len(karakter) == 4):
                                        print(liste[i][j], end="  || ")
                                    else:
                                        print(liste[i][j], end=" || ")
                                if (j == 5):
                                        print("    {}     ".format(liste[i][j]), end="|| ")
                                if (j != 6 and j != 0 and j != 5 and j != 4):
                                    print(liste[i][j], end=" || ")
                                if (j == 6):
                                    print(liste[i][j], end=" ||\n")
                            enter_control = 1
                    if(enter_control != 1):
                        print("Girdiğiniz ismi içeren herhangi bir sevkiyat bulunamadı")
                    else:
                        for i in range(0, 48):
                            if (i != 47):
                                print("-", end="-")
                            else:
                                print("-")
    except FileNotFoundError:
        print("\n" * 50)
        print("Sorgulanabilecek herhangi bir sevkiyat bilgisi bulunmamaktadır.")
def total_profit_expenditure():   #Toplam sevkiyat hacmi maliyeti ve karı hesaplayan fonksiyon
    try:
        dosya = open("19010011069.txt", "r", encoding="utf-8")
        satir_1 = dosya.readlines()
        line_counter = len(satir_1)
        if (line_counter == 0):
            print("Hesaplanacak herhangi bir sevkiyat bilgisi bulunmamaktadır")
        else:
            while (satir_1[line_counter - 1] == '\n'):
                satir_1.pop()
                line_counter -= 1
            dosya.seek(0)
            liste = []
            for i in range(0, line_counter):
                karakter = str(satir_1[i])
                karakter = karakter[:-1]
                satir_1[i] = karakter
            for i in range(0, line_counter):
                karakter = satir_1[i]
                liste.append(karakter.split("-"))
            total_amount = 0
            total_expenditure = 0
            total_profit = 0
            for i in range(0, line_counter):
                total_amount += int(liste[i][2])
                total_expenditure += int(liste[i][3])
                total_profit += int(liste[i][4])
            print("||     Brüt m^3   || Toplam harcama || Toplam kâr || Sevkiyat sayısı ||")
            print("||    {}       ||   {}       ||   {}    ||       {}         ||".format(total_amount, total_expenditure, total_profit, line_counter))

    except FileNotFoundError:
        print("\n" * 50)
        print("Hesaplanacak herhangi bir sevkiyat bilgisi bulunmamaktadır")
        return
def menu():   #Otomasyonun uzerinde isledigi ana fonksiyon
    while (True):
        secim = input("Atölye otomasyonuna hoşgeldiniz:\n\n Lütfen yapmak istediğiniz işlemi seçiniz:\n (1) - Sevkiyat ekle -\n (2) - Geçmiş sevkiyatları listele -\n (3) - Geçmiş sevkiyat bilgisini guncelle -\n (4) - Sevkiyat bilgisi sil -\n (5) - Sevkiyat arama seçenekleri -\n (6) - Total atölye verileri\n (7) - Ekranı temizle - \n (8) - Cikis - ")

        if (secim.isdigit() is False):  # Kullanicinin absurt degerler girmesinin onune gecmeye calistim
            print("\n" * 50)
            print("Lütfen menüden seçim yapınız")
            continue
        secim = int(secim)
        if (secim > 8 or secim < 1):
            print("\n" * 50)
            print("Lütfen menüden seçim yapınız")
            continue
        print("\n" * 50)

        if(secim == 1):
            ekle()
        if(secim == 2):
            listele()
        if(secim == 3):
            guncelle()
        if(secim == 4):
            sil()
        if(secim == 5):
            arama()
        if(secim == 6):
            total_profit_expenditure()
        if(secim == 7):
            print("\n" * 50)
        if(secim == 8):
            break
menu()
exit()