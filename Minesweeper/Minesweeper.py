#https://github.com/Enderceliik
#Ender ÇELİK

import random
BattleField= list()    #Fonksiyonlarla manipüle edilen listeler
Check_BattleField= list()

def MineCount(fire_row_axis,fire_column_axis,BattleField_dimensions, Battle_Mode): #Etrafında kaç mayın var
    MineCounter= 0
    globals()['BattleField']
    globals()['Check_BattleField']
    if fire_column_axis != 0:
        if Check_BattleField[fire_row_axis][fire_column_axis - 1] == "X":
            MineCounter= MineCounter+1
    if fire_row_axis != 0 and fire_column_axis != 0:
        if Check_BattleField[fire_row_axis-1][fire_column_axis - 1] == "X":
            MineCounter= MineCounter+1
    if fire_row_axis != 0:
        if Check_BattleField[fire_row_axis - 1][fire_column_axis] == "X":
            MineCounter= MineCounter+1
    if fire_row_axis != 0 and fire_column_axis != BattleField_dimensions - 1:
        if Check_BattleField[fire_row_axis-1][fire_column_axis+1]=="X":
            MineCounter= MineCounter+1
    if fire_column_axis != BattleField_dimensions - 1:
        if Check_BattleField[fire_row_axis][fire_column_axis + 1] == "X":
            MineCounter= MineCounter+1
    if fire_row_axis != BattleField_dimensions - 1 and fire_column_axis != BattleField_dimensions - 1:
        if Check_BattleField[fire_row_axis + 1][fire_column_axis + 1] == "X":
            MineCounter= MineCounter+1
    if fire_row_axis != BattleField_dimensions - 1:
        if Check_BattleField[fire_row_axis + 1][fire_column_axis] == "X":
            MineCounter= MineCounter+1
    if fire_row_axis != 0 and fire_column_axis != 0:
        if Check_BattleField[fire_row_axis + 1][fire_column_axis - 1] == "X":
            MineCounter= MineCounter+1
    if Battle_Mode == "1":          #Gizli modda oynanıyor ise işaretleyen
        BattleField[fire_row_axis][fire_column_axis]= MineCounter
    elif Battle_Mode == "2":    #Açık modda oynanıyor ise işaretleyen
        Check_BattleField[fire_row_axis][fire_column_axis]= MineCounter

def numberc(variable):      #Try-Except ile programın hata vermesini önleyen fonk.
    try:
        variable= int(variable)
    except TypeError:
        print("Lütfen geçerli bir değer girin. :")
        return False
    except ValueError:
        print("Lütfen geçerli bir değer girin. :")
        return False
    return variable

def Draw_BattleFied(variable):    #Print fonk.
    for i in range(variable):
        for j in range(variable):
            print(BattleField[i][j], end=" ")
        print("")

def Draw_Check_BattleField(variable):    #Print fonk.
    for i in range(variable):
        for j in range(variable):
            print(Check_BattleField[i][j], end=" ")
        print("")

def Installation_BattleField(variable): #Mayınları random yerleştiren fonk.
    globals()['BattleField']
    globals()['Check_BattleField']
    for i in range(variable*variable):
        BattleField.append(["?"]*variable)
        Check_BattleField.append(["?"]*variable)
    QuantityOfMine=(variable*variable * 3 / 10)
    for i in range(int(QuantityOfMine)):
        x_axis= random.randint(0, variable-1)
        y_axis= random.randint(0, variable-1)
        if Check_BattleField[x_axis][y_axis] != "X":
            Check_BattleField[x_axis][y_axis]= "X"
        else:
            while True:
                x_axis= random.randint(0,variable- 1)
                y_axis= random.randint(0,variable- 1)
                if Check_BattleField[x_axis][y_axis] != "X":
                    Check_BattleField[x_axis][y_axis]= "X"
                    break
    return int(QuantityOfMine)

def BattleMode(BattleField_dimensions, Battle_Mode):
    QuantityOfMine=Installation_BattleField(BattleField_dimensions)
    PointCounter= 0
    print("Açık oyun modunu oynamaktasınız. :")
    while True:
        if Battle_Mode == "1":    #Gizli oyun modu seçildi ise
            Draw_BattleFied(BattleField_dimensions)      #Çizim fonk. çağırma
        elif Battle_Mode == "2":     #Açık oyun modu seçildi ise
            Draw_Check_BattleField(BattleField_dimensions)     #Çizim fonk. çağırma
        if PointCounter == int((BattleField_dimensions**2)-QuantityOfMine):
            print("Tebrikler mayın tarlasındaki bütün puanları toplayarak oyunu başarıyla tamamladınız:\nPuanınız: {}".format(PointCounter))
            return None
        fire_row_axis=input("Hedef almak istediğiniz koordinatın satır numarasını girin. :")
        fire_column_axis= input("Hedef almak istediğiniz koordinatın sütun numarasını girin. :")
        print("",end="\n\n")
        if numberc(fire_row_axis) is False or numberc(fire_column_axis) is False:
            continue
        fire_row_axis= numberc(fire_row_axis)- 1
        fire_column_axis= numberc(fire_column_axis)- 1
        if fire_row_axis >= BattleField_dimensions or fire_column_axis >= BattleField_dimensions:
            print("Geçersiz koordinat girişi!\nTekrar deneyin. :")
            continue
        if fire_row_axis < 0 or fire_column_axis < 0:
            print("Geçersiz koordinat girişi!\nTekrar deneyin. :")
            continue
        if Battle_Mode == "1" and BattleField[fire_row_axis][fire_column_axis] != "?":
            print("Daha önce hedef almadığınız bir koordinatı deneyin")
            continue
        if Check_BattleField[fire_row_axis][fire_column_axis] == "X":
            print("Mayına denk geldiniz. Oyununuz sonlandırılıyor...")
            print("Puan: {}".format(PointCounter))
            Draw_Check_BattleField(BattleField_dimensions)
            return None
        if Battle_Mode == "2" and Check_BattleField[fire_row_axis][fire_column_axis] != "?":
            print("Daha önce hedef almadığınız bir koordinatı deneyin")
            continue
        PointCounter= PointCounter + 1
        MineCount(fire_row_axis, fire_column_axis, BattleField_dimensions, Battle_Mode)      #Mayın sayan fon. un çağrılması

def menu():        #Temel menü fonk.
    globals()['BattleField']
    globals()['Check_BattleField']
    while True:
        BattleField_Dimensions=input("Mayın tarlanızın boyutunuz girin:\n(minimum: 10)")
        if numberc(BattleField_Dimensions) is False:
            continue
        BattleField_Dimensions= numberc(BattleField_Dimensions)
        if BattleField_Dimensions< 10:
            print("Lütfen 10 veya daha büyük bir değer giriniz. :")
            continue
        Battle_Mode= input("Oyunu açık modda oynamak istiyorsanız 1'e gizli modda oynamak istiyorsanız 2'ye basın")
        if Battle_Mode == "1":
            BattleMode(BattleField_Dimensions, Battle_Mode)
        elif Battle_Mode == "2":
            BattleMode(BattleField_Dimensions, Battle_Mode)
        else:
            print("Seçimi doğru yaptığınızdan emin olun. :")
            continue
        BattleField.clear()
        Check_BattleField.clear()
        select= input("Yeniden oynamak için 0'a Oyunu kapatmak için 1'e basın. :")
        if select == "0":        #Oyun sonu
            continue
        else:
            print("Mayın tarlası sonlandırılıyor...")
            return None

menu()           #Temel fonk. çağrılması

