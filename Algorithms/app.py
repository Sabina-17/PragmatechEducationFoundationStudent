programMenusu="""
    ----Proqram Menusu----
    1-Yeni Tələbə Əlavə Et
    2-Tələbələrin siyahısı gör
    3-Proqramdan cıx
    4-Əsas menuye qayit
    ----------------------
    """  
# telebeAd,telebeSoyad,telebeYas
# telebeler=[]
telebeler=[]
def telebeElaveEt():
    def yeniTelebe():
        ad=input('Ad : ')
        soyad=input('Soyad : ')
        yas=input('Yas :')

        telebe={
            'Ad':ad,
            'Soyad':soyad,
            'Yas':yas
        }
        telebeler.append(telebe)
    while True:
        emr=input('Yeni telebe elave etmek isteyirsiniz mi (Y/N) :')
        if(emr=='Y'):
            yeniTelebe()
        else:
            break
def telebeSiyahisiGor():
    for telebe in telebeler:
        print(f'{telebe["Ad"]} | {telebe["Soyad"]} | {telebe["Yas"]}')

def menuGoster():
    print(programMenusu)


menuGoster()

while True:

    emr=input('Istədiyiniz əməlyatın nömrəsini daxil edin :')
    if int(emr)==3:
        break
    elif int(emr)==1:
        telebeElaveEt()
    elif int(emr)==2:
        telebeSiyahisiGor()
    elif int(emr)==4:
        menuGoster()
    else:
        print('Sehv emelyat nomresini daxil edildiyi ucun proqram dayandirilir')
        break
