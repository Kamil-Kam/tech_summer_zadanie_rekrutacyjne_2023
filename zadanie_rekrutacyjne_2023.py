"""
W zeszłym roku żółte, gumowe kaczuszki towarzyszyły nam przez całe lato i przez całe RAS TECH Summer. Były bardzo pomocne. Dzielnie wspierały naszych stażystów podczas
 debugowania. Słuchały do czego służą poszczególne segmenty kodu, a w chwilach wielkiej chwały – rozwiązania problemu – były dumne jak nikt inny. Po zimowej przerwie
  wymagają wyjątkowej uwagi. Muszą przygotować się na powitanie i RAS TECH Summer 2023. Pomóż nam ujarzmić gumowe kaczuszki i zagwarantuj sobie dobre lato!

Twoje zadanie:
Dane jest N kaczuszek gumowych, które należy ułożyć w rzędzie. Każda kaczuszka ma określoną wysokość i szerokość. Potrzebujemy ułożyć kaczuszki w taki sposób, aby suma 
wysokości wykorzystanych kaczuszek była jak największa, a ich sumaryczna szerokość nie przekroczyła maksymalnej szerokości rzędu.

Wejście: W pierwszym wierszu standardowego wejścia znajdują się dwie liczby całkowite N, M (1 <= N, M <= 50) pooddzielane pojedynczymi odstępami oznaczające odpowiednio:
 liczbę dostępnych kaczuszek oraz maksymalną szerokość rzędu. W każdym kolejnym N wierszu znajdują się dwie liczby całkowite w, s (1 <= w, s <=9) oddzielone pojedynczym 
 odstępem oznaczające wysokość (w) i szerokość (s) kaczuszki Wyjście: Twój program powinien wypisać na standardowe wyjście maksymalną dostępną sumę wysokości użytych 
 kaczuszek do ustawienia ich w rzędzie.

Wyjście: Twój program powinien wypisać na standardowe wyjście maksymalną dostępną sumę wysokości użytych kaczuszek do ustawienia ich w rzędzie.
Dane do zadania możesz pobrać poniżej. W oknie poniżej wpisz sam wynik. Nie sprawdzamy twojego kodu. Możesz próbować do skutku, tyle razy ile potrzebujesz – do 23:59 
we wtorek 11.04.
"""

import openpyxl

exercise_file = 'zadanie-rekrutacyjne.xlsx'


def extraxt_data_from_file(file_name: str) -> tuple:
    workbook = openpyxl.load_workbook(file_name)
    worksheet = workbook.active

    dane_f = []

    for count, row in enumerate(worksheet.iter_rows()):
        if count == 0:
            liczba_dostepnych_kaczuszek_f = row[0].value
            maksymalna_szerokosc_rzedu_f = row[1].value

        else:
            wskaznik = row[0].value - row[1].value
            dane_f.append([row[0].value, row[1].value, wskaznik])

    return liczba_dostepnych_kaczuszek_f, maksymalna_szerokosc_rzedu_f, dane_f


def extract_key(data: list) -> list:
    return data[2]


def get_max_row_height(dane_f: list, maksymalna_szerokosc_rzedu_f: int) -> tuple:
    wykorzystane_kaczuszki = 0
    szerokosc_rzedu = 0
    wysokosc_kaczuszek = 0

    for row in dane_f:

        if (szerokosc_rzedu + row[1]) <= maksymalna_szerokosc_rzedu_f:
            szerokosc_rzedu += row[1]
            wysokosc_kaczuszek += row[0]
            wykorzystane_kaczuszki += 1

    return szerokosc_rzedu, wysokosc_kaczuszek, wykorzystane_kaczuszki


def main():
    liczba_dostepnych_kaczuszek, maksymalna_szerokosc_rzedu, dane = extraxt_data_from_file(exercise_file)
    dane.sort(key=extract_key, reverse=True)
    szerokosc_rzedu, wysokosc_kaczuszek, wykorzystane_kaczuszki = get_max_row_height(dane, maksymalna_szerokosc_rzedu)

    print(f"szerokosc rzedu: {szerokosc_rzedu}, wysokosc kaczuszek: {wysokosc_kaczuszek}, wykorzystane kaczuszki: {wykorzystane_kaczuszki}")


if __name__ == '__main__':
    main()



