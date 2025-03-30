def binary_search(element_do_znalezienia, lista_do_przeszukania):
    low = 0
    high = len(lista_do_przeszukania) - 1

    while low <= high:
        mid = (low + high) // 2
        wartosc_srodek = lista_do_przeszukania[mid]
        if wartosc_srodek > element_do_znalezienia:
            high = mid - 1
        elif wartosc_srodek < element_do_znalezienia:
            low = mid + 1
        else:
            return mid
    return -1


def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Lista to: ", lista)
    target = int(input("Podaj element szukany: "))
    print("Szukany element jest na indexie: ", binary_search(target, lista))

main()
