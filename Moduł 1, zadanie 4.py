import random   # Importuje bibliotekę random, pozwalającą korzystać między innymi z funkcji pseudolosowości

liczbaWybrana = random.randint(1, 101)  # Losowanie liczby od 1 do 100
licznik = 1     # Dodatkowa zmienna

print("Wylosowana została liczba z zakresu od 1 do 100. Spróbuj ją znaleźć.")   # Wstęp informacyjny dla użytkownika

while True:  # Cała gra

    while True:  # Sprawdzanie
        try:
            x = int(input(": \n"))  # czy da się skonwertować dane od użytkownika na liczbe całtowitą
            break
        except ValueError:  # Gdy konwersja typu nie powiedzie się, zamiast wyrzucić błąd, wyświetla się komunikat
            print("Spróbuj podać jednak liczbę")

    if liczbaWybrana == x:  # Warunek zakończenia pętli
        print("Hurra! Udało Ci się za ", licznik, " razem")  # Czyli odgadnięcie cyfry, która została wygenerowana
        break  # Przerwanie pętli

    print("Twoja próba nr ", licznik, " nie wyszła\n")

    if liczbaWybrana < x:  # Sprawdzanie, czy liczba jest
        print("Liczba jest za duża!!!!")  # Za duża
    else:
        print("Liczba jest za mała~~~~")  # Lub za mała
    licznik += 1  # Dodanie do licznika +1, liczba przebiegu petli
