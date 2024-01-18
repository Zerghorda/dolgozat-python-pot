def hettelOszthato(lista):
    db: int = 0
    for i in range(len(lista)):
        if i == len(lista)-1:
            print(lista[i], end="")
        else:
            print(lista[i], end=",")
        if lista[i] % 7 == 0:
            db += 1
    print()
    print(f"A listában {db} darab héttel osztható szám van.")

