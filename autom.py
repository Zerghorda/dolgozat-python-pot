from Auto import Auto



def faljBeolvas():
    f = open("auto.txt", "r", encoding="utf-8")
    f.readline()
    sorok = f.readlines()
    f.close()
    autok = []
    for i in range(len(sorok)):
        sor = sorok[i].strip().split(":")
        nev = sor[0]
        gyartas = sor[1]
        auto = Auto(nev, int(gyartas))
        autok.append(auto)
    return autok


def kor(obj):
    szoveg = ""
    print("III/Kor:")
    szoveg += f"\t{obj.nev} - {2024-obj.gyartas} éves"
    szoveg += "\n"
    print(f"{szoveg}")
    return szoveg


def flotta(autok):
    print("III/Flotta:")
    print(f"\tAutók száma: {len(autok)}")
    print()


def ertekes(autok):
    legidosebb: int = 2024
    hely = 0
    print("III/Értékes")
    for i in range(len(autok)):
        if autok[i].gyartas < legidosebb:
            legidosebb = autok[i].gyartas
            hely = i
    print(f"\tA legöregebb autó:{autok[hely].nev}, {legidosebb}")


def kiir(metodus):
    f = open("kiir.txt", "w", encoding="utf-8")
    f.write(metodus)
    f.close()


# kiir(kor("mercedes", 7))
