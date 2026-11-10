def spracuj_riadok(riadok):
    vys = []
    for i in range(0, len(riadok), 2):
        cislo = int(riadok[i:i + 2], 16)
        if cislo >= 128:
            vys.append("1")
        else:
            vys.append("0")
    return " ".join(vys)


with open("ciernobiely_obrazok_1.txt", "r") as fr:
    a, b = fr.readline().split()
    roz = int(a) * int(b)
    print(f"{a},{b} - počet pixelov: {roz}")
    riadky = [r.strip() for r in fr if r.strip()]

print("Prvý riadok:", spracuj_riadok(riadky[0]))

with open("konverzia_suboru_vystup.txt", "w") as fw:
    fw.write(f"{a} {b}\n")
    for riadok in riadky:
        fw.write(spracuj_riadok(riadok) + "\n")