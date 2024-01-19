
# Modification date: Mon Sep 28 14:11:12 2020

# Production date: Sun Sep  3 15:43:24 2023

canta = []

def h(x):
    p = (x + "\n: ")
    if p == "çanta":
        print(canta)
        u = -1
        u = input("Kullanmak istediğin eşyayı seç.(çantayı kapatmak için 0 yaz.)\n: ")
        if u + 1 == 1:
            print("yakında bu özellik gelecek.")
        else:
            print("yakında bu özellik gelecek.")
        q = "Çantayı kapattın."
    return q
    
    

print("Bütün hakları bana aittir.\n\n")
input("Ormanda yürüyorsun.")
input("Ağaçların arasından geçerken, karşına bir yol çıkıyor.(eğer seçimsiz \'^:\' görürsen Şans veya Cesaret yazabilirsin.)")
ilk_yol_secimi = int(input("Yolun:\n-Sağ tarafı bir dağa,\n-sol tarafı da ucunu göremediğin bir yokuşa gidiyor.\n\nHangi tarafa gideceksin?(1-Sağ, 2-Sol)\n: "))

if ilk_yol_secimi == 1:
    input("Bir süre yokuş çıktıktan sonra yorulduğundan dinlenmeye karar veriyorsun.")
    input("Bir anda bir ses duyuyorsun. Ses aynen şöyle:")
    sanssiz_karsilasma = input("NABER MÜDÜR?\n^: ")
    if sanssiz_karsilasma == "Şans":
        input("Son anda sıyrılıyorsun.")
        input("Kendini dağa çıktığın yoldan aşağı atıyorsun.")
        input("Yuvarlanırken dinlendiğin yerin paramparça olduğunu görüyorsun ama neyin öyle bir hasar verdiğini göremiyorsun.")
    elif sanssiz_karsilasma == "Cesaret":
        input("Sesi duyar duymaz hızlı bir şekilde savaş pozisyonu alıyorsun.")
        input("Ama nafile, arkandan gelen şey seni ışığıyla kör etmekle kalmadı, senin üzerine hızla gelerek paramparça etti.")
        while True:
            input("Öldün.")
    else:
        input("Arkandan bir ışık geldiğini farkettiğin anda paramparça oluyorsun.")
        while True:
            input("Öldün.")
elif ilk_yol_secimi == 2:
    input("Yokuşun çok dik olduğunu farkettin")
    input("Dikkatlice bir şekilde inerken bazı hışırtılar duyuyorsun.")
    input("Seslerin geldiği yere baktığında bir ışık görüyorsun.")
    input("İçgüdülerin düşerken parçalanma ihtimaline rağmen atlamanı söylüyor.")
    sanssiz_karsilasma_2 = input("Hızlı olmalısın.\n^: ")
    
    if sanssiz_karsilasma_2 == "Şans":
        input("Hızlıca inmek için aşağıya doğru atıldın ama düşerken tutunacak bir yer bulamadığından yuvarlanmaya başladın.")
    elif sanssiz_karsilasma_2 == "Cesaret":
        input("Hemen saldırı yapabileceğin bir yere geçtin ve oradaki sesi yapan şeye seslendin.")
        input("Bir ışık gözünü almaya başladı, aniden bir ses duydun ve birkaç saniye sonra paramparça oldun.")
        while True:
            input("Öldün.")
input("...")









