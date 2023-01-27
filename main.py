import random

def battlefield():
    print("-------İlk Kahraman-------")
    oyuncu1 = input("Birinci kahramanın adını girin:")  # Kahramanların isimleri sorulur boşluk ve aynı isim alınamaz

    while oyuncu1 == "":
        print("-------İlk Kahraman-------")
        oyuncu1 = input("Boşluk alınamaz, birinci kahramanın adını girin:")

    print("-------İkinci Kahraman-------")
    oyuncu2 = input("İkinci kahramanın adını girin:")

    while oyuncu1 == oyuncu2 or oyuncu2 == "":
        print("-------İkinci Kahraman-------")
        print(oyuncu2, "alınamaz tekrar gir.")
        oyuncu2 = input("İkinci kahramanın adını girin:")

    yazi_kucult = "evet"  # oyunu tekrar oynamak için sorulan sorunun cevabıdır
    while yazi_kucult == "evet":

        oyuncular = [oyuncu1, oyuncu2]
        kimin_sirasi = random.choice(oyuncular)  # Kimin oyuna başlayacağı seçilir
        print("Vuruş önceliği ", kimin_sirasi, " adlı oyuncuda.")

        oyuncu1_can = 100
        oyuncu2_can = 100

        if kimin_sirasi == oyuncu1:
            while oyuncu1_can != 0 or oyuncu2_can != 0:
                print(oyuncular[0],"                                                                                                                " +oyuncular[1], "\n", "hp""[", oyuncu1_can, "]:" + oyuncu1_can * "|", "                  ", "hp""[",oyuncu2_can, "]:", oyuncu2_can * "|")
                print("Saldırı sırası", oyuncu1)
                birinci_oyuncu_vurus = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))

                while birinci_oyuncu_vurus > 50:  # kullanıcıdan saldırı büyüklüğü istenir
                    print("Saldırı Saldırı büyüklüğü 1 ile 50 arasında olmalıdır!!!!!!")
                    birinci_oyuncu_vurus = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))

                hasar = (100 - birinci_oyuncu_vurus)
                vurma_ihtimali = random.randint(1, 100)  # vuruş ihtimali hesaplanır

                if vurma_ihtimali < hasar:
                    oyuncu2_can -= birinci_oyuncu_vurus
                elif vurma_ihtimali > hasar:
                    bir = "OOOPPSSY saldırı kaçtı!!!!"
                    iki = "Çok yakındı tekrar dene...."
                    uc = "Daha hızlı olmalıydın saldırını atlattı."  # vuruş kaçarsa random bir şekilde gelen metinler
                    dort = "Çok yakındı ayınısını tekrar dene."
                    bes = "HAYIRRRRRRRR!!!!!....."

                    kacirma = (bir, iki, uc, dort, bes)
                    secme = random.choice(kacirma)
                    print(secme)

                if oyuncu2_can <= 0 or oyuncu1_can <= 0:
                    print(oyuncular[0],"                                                                                                                ",oyuncular[1], "\n", "hp""[", oyuncu1_can, "]:" + oyuncu1_can * "|", "                  ","hp""[", oyuncu2_can, "]:", oyuncu2_can * "|")
                    print(oyuncu1, "kazandı.")
                    break

                print(oyuncular[0],"                                                                                                                ",oyuncular[1], "\n", "hp""[", oyuncu1_can, "]:" + oyuncu1_can * "|", "                  ", "hp""[",oyuncu2_can, "]:", oyuncu2_can * "|")
                print("Saldırı sırası", oyuncu2)
                ikinci_oyuncu_vurus = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))

                while ikinci_oyuncu_vurus > 50:
                    print("Saldırı Saldırı büyüklüğü 1 ile 50 arasında olmalıdır!!!!!!!!")
                    ikinci_oyuncu_vurus = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))

                hasar = (100 - ikinci_oyuncu_vurus)
                vurma_ihtimali = random.randint(1, 100)

                if vurma_ihtimali < hasar:
                    oyuncu1_can -= ikinci_oyuncu_vurus

                elif vurma_ihtimali > hasar:
                    bir = "OOOPPSSY saldırı kaçtı!!!!"
                    iki = "Çok yakındı tekrar dene...."
                    uc = "Daha hızlı olmalıydın saldırını atlattı."
                    dort = "Çok yakındı ayınısını tekrar dene."
                    bes = "HAYIRRRRRRRR!!!!!....."

                    kacirma = (bir, iki, uc, dort, bes)
                    secme = random.choice(kacirma)
                    print(secme)

                if oyuncu1_can <= 0 or oyuncu2_can <= 0:
                    print(oyuncular[0],"                                                                                                                ",oyuncular[1], "\n", "hp""[", oyuncu1_can, "]:" + oyuncu1_can * "|", "                  ","hp""[", oyuncu2_can, "]:", oyuncu2_can * "|")
                    print(oyuncu2, "kazandı.")
                    break

        elif kimin_sirasi == oyuncu2:
            while oyuncu1_can != 0 or oyuncu2_can != 0:
                print(oyuncular[0],
                      "                                                                                                                ",
                      oyuncular[1], "\n", "hp""[", oyuncu1_can, "]:" + oyuncu1_can * "|", "                  ", "hp""[",
                      oyuncu2_can, "]:", oyuncu2_can * "|")
                print("Saldırı sırası", oyuncu2)
                ikinci_oyuncu_vurus = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))

                while ikinci_oyuncu_vurus > 50:
                    print("Saldırı Saldırı büyüklüğü 1 ile 50 arasında olmalıdır!!!!!!")
                    ikinci_oyuncu_vurus = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))

                hasar = (100 - ikinci_oyuncu_vurus)
                vurma_ihtimali = random.randint(1, 100)

                if vurma_ihtimali < hasar:
                    oyuncu1_can -= ikinci_oyuncu_vurus

                elif vurma_ihtimali > hasar:
                    bir = "OOOPPSSY saldırı kaçtı!!!!"
                    iki = "Çok yakındı tekrar dene...."
                    uc = "Daha hızlı olmalıydın saldırını atlattı."
                    dort = "Çok yakındı ayınısını tekrar dene."
                    bes = "HAYIRRRRRRRR!!!!!....."

                    kacirma = (bir, iki, uc, dort, bes)
                    secme = random.choice(kacirma)
                    print(secme)

                if oyuncu1_can <= 0 or oyuncu2_can <= 0:
                    print(oyuncular[0],"                                                                                                                ",oyuncular[1], "\n", "hp""[", oyuncu1_can, "]:" + oyuncu1_can * "|", "                  ","hp""[", oyuncu2_can, "]:", oyuncu2_can * "|")
                    print(oyuncu2, "kazandı.")
                    break

                print(oyuncular[0],"                                                                                                                " +oyuncular[1], "\n", "hp""[", oyuncu1_can, "]:" + oyuncu1_can * "|", "                  ", "hp""[",oyuncu2_can, "]:", oyuncu2_can * "|")
                print("Saldırı sırası", oyuncu2)
                birinci_oyuncu_vurus = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))

                while birinci_oyuncu_vurus > 50:
                    print("Saldırı Saldırı büyüklüğü 1 ile 50 arasında olmalıdır!!!!!!!!")
                    birinci_oyuncu_vurus = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))

                hasar = (100 - birinci_oyuncu_vurus)
                vurma_ihtimali = random.randint(1, 100)

                if vurma_ihtimali < hasar:
                    oyuncu2_can -= birinci_oyuncu_vurus

                elif vurma_ihtimali > hasar:
                    bir = "OOOPPSSY saldırı kaçtı!!!!"
                    iki = "Çok yakındı tekrar dene...."
                    uc = "Daha hızlı olmalıydın saldırını atlattı."
                    dort = "Çok yakındı ayınısını tekrar dene."
                    bes = "HAYIRRRRRRRR!!!!!....."

                    kacirma = (bir, iki, uc, dort, bes)
                    secme = random.choice(kacirma)
                    print(secme)

                if oyuncu2_can <= 0 or oyuncu1_can <= 0:
                    print(oyuncular[0],"                                                                                                                ",oyuncular[1], "\n", "hp""[", oyuncu1_can, "]:" + oyuncu1_can * "|", "                  ","hp""[", oyuncu2_can, "]:", oyuncu2_can * "|")
                    print(oyuncu1, "kazandı.")
                    break

        tekrar_oynama = input("Tekrar oynamak ister misin?(evet veya hayır)")  # tekrar oynamak istediği sorulur ve evetse başa döner
        yazi_kucult = tekrar_oynama.lower()
    print("Oynadığınız için teşekkürler tekrar görüşmek üzere")

battlefield()