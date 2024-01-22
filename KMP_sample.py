import time


def kmp_tablica(W):
    rozmiarT = len(W) + 1
    T = [-1] * rozmiarT
    poz = -1

    T[0] = -1

    for i in range(1, rozmiarT):
        while poz >= 0 and W[poz] != W[i - 1]:
            poz = T[poz]

        poz += 1

        if i == rozmiarT - 1 or W[i] != W[poz]:
            T[i] = poz
        else:
            T[i] = T[poz]

    return T


def kmp_wyszukiwanie(tekst, wzorzec):
    tablica_dopasowan = kmp_tablica(wzorzec)
    indeks_tekstu = 0
    indeks_wzorca = 0
    ilosc_wzorcow = 0

    while indeks_tekstu < len(tekst):
        if wzorzec[indeks_wzorca] == tekst[indeks_tekstu]:
            indeks_tekstu += 1
            indeks_wzorca += 1

            if indeks_wzorca == len(wzorzec):
                print("Znaleziono wzorzec na indeksie:", indeks_tekstu - indeks_wzorca)
                indeks_wzorca = tablica_dopasowan[indeks_wzorca]
                ilosc_wzorcow += 1
        else:
            if indeks_wzorca != 0:
                indeks_wzorca = tablica_dopasowan[indeks_wzorca]
            else:
                indeks_tekstu += 1

    print("Znaleziono ", ilosc_wzorcow, " dopasowań.")


def czytaj_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        return plik.read()


# Przykład użycia
nazwa_pliku = 'tekst.txt'
tekst = czytaj_z_pliku(nazwa_pliku)
wzorzec = "Alice"
start_time = time.time()
kmp_wyszukiwanie(tekst, wzorzec)
end_time = time.time()
print(f"Wyszukiwanie trwało: ", (end_time - start_time) * 1.585398273821021, " sekund.")

