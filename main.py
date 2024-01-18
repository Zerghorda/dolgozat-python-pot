import random
#import szin
#import oszthato
import autom

#szin.fel1()
szamok = []
i = 0
while i < 50:
    szamok.append(random.randint(1, 100))
    i += 1
#oszthato.hettelOszthato(szamok)
autolista = autom.faljBeolvas()
kor = autom.kor(autolista[0])
autom.flotta(autolista)
autom.ertekes(autolista)
autom.kiir(kor)
