import random
print("Vítejte ve hře Chicago! Pokud chcete začít hru, napište do konzole zacit. Budete-li chtít hru ukončit, napište do konzole konec.")
zacit = input()

def hra():
    hrac1_body = 0
    hrac2_body = 0
    for kolo in range(1, 8):
        print(kolo, "Kolo")
        print("Hráč 1:", hrac1_body)
        print("Hráč 2:", hrac2_body)
        print("Hráč 1 hází kostkou")

        def hod_kostkou():
            hod = random.randint(1, 6)  
            if hod == 1:
                print("Hodil jsi 1, získáváš 100 bodů!")
                return 100
            elif hod == 6:
                print("Hodil jsi 6, získáváš 60 bodů!")
                return 60
            else:
                print(f"Hodil jsi {hod}, získáváš {hod} body!")
                return hod

        hod1 = hod_kostkou()
        hod2 = hod_kostkou()
        hod3 = hod_kostkou()

        print("Hod 1:", hod1)
        print("Hod 2:", hod2)
        print("Hod 3:", hod3)

hra()