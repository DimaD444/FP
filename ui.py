from bussines import (adauga_cheltuiala, modifica_cheltuiala, sterge_apartament, sterge_apartamente_consecutive,
                      sterge_cheltuieli_tip, afiseaza_apartamente_cu_cheltuieli_mai_mari_decat,
                      afiseaza_cheltuieli_tip, afiseaza_cheltuieli_inainte_de_o_zi,
                      tipareste_apartamente_sortate_dupa_tip, suma_cheltuieli_tip,
                      calculeaza_total_cheltuieli, elimina_cheltuiala, elimina_cheltuieli_mai_mici_decat)


def afiseaza_apartamente(apartamente):
    """
    Afiseaza apartamentele existenye
    :param apartamente: Dicționarul care conține datele despre apartamente.
    """
    print("Apartamente disponibile:")
    for apartament_tip, cheltuieli in apartamente.items():
        apartament, tip = apartament_tip
        print(f"Apartamentul {apartament} | Tip cheltuială: {tip}")
        for suma, data in cheltuieli:
            print(f"  - Suma: {suma}, Data: {data}")


def main():
    apartamente = {}

    print("Menu:")
    print("1. Adaugă cheltuială")
    print("2. Modifică cheltuială")
    print("3. Șterge toate cheltuielile unui apartament")
    print("4. Șterge apartamente consecutive")
    print("5. Șterge cheltuieli de un anumit tip")
    print("6. Afișează apartamente cu cheltuieli mai mari decât o sumă")
    print("7. Afișează cheltuieli de un anumit tip")
    print("8. Afișează cheltuieli efectuate înainte de o zi și mai mari decât o sumă")
    print("9. Tipareste suma cheltuielilor de un anumi tip")
    print("10. Tipareste toate apartamentele sortate dupa tip")
    print("11. Tipareste suma cheltuielilor pentur un apartament")
    print("12. Elimina chelutieli de un tip")
    print("13. Elimină toate cheltuielile mai mici decât o sumă dată")
    print("15. Afisare apartamentele existente")
    print("16. Ieși din aplicație")

    while True:
        optiune = input("Alege o opțiune: ")

        if optiune == "1":
            try:
                apartament = int(input("Număr apartament: "))
                while True:
                    tip = input("Tip cheltuială (apa, gaz, lumina sau 'stop' pentru a încheia): ")
                    if tip == "stop":
                        break
                    suma = float(input("Suma cheltuielii: "))
                    zi = input("Data cheltuielii (format: yyyy-mm-dd): ")
                    apartamente = adauga_cheltuiala(apartamente, apartament, tip, suma, zi)
            except AssertionError as e:
                print(str(e))

        elif optiune == "2":
            try:
                apartament = int(input("Număr apartament: "))
                tip = input("Tip cheltuială (apa, gaz, lumina): ")
                suma_veche = float(input("Suma cheltuielii veche: "))
                suma_noua = float(input("Suma cheltuielii nouă: "))

                modifica_cheltuiala(apartamente, apartament, tip, suma_veche, suma_noua)

            except ValueError as e:
                print(str(e))

        elif optiune == "3":
            try:
                apartament = int(input("Număr apartament: "))
                sterge_apartament(apartamente, apartament)

            except ValueError as e:
                print(e)

        elif optiune == "4":
            try:
                apartament_start = int(input("Primul apartament: "))
                apartament_end = int(input("Ultimul apartament: "))
                sterge_apartamente_consecutive(apartamente, apartament_start, apartament_end)

            except ValueError as e:
                print(e)

        elif optiune == "5":
            try:
                tip = input("Tip cheltuială (apa, gaz, lumina): ")
                sterge_cheltuieli_tip(apartamente, tip)
            except ValueError as e:
                print(e)

        elif optiune == "6":
            try:
                suma = float(input("Suma minimă: "))
                afiseaza_apartamente_cu_cheltuieli_mai_mari_decat(apartamente, suma)

            except ValueError as e:
                print(e)

        elif optiune == "7":
            try:
                tip = input("Tip cheltuială (apa, gaz, lumina): ")
                rezultat = afiseaza_cheltuieli_tip(apartamente, tip)
                for linie in rezultat:
                    print(linie)
            except ValueError as e:
                print(e)

        elif optiune == "8":
            try:
                suma = int(input("Suma minimă: "))
                zi = input("Data (format: yyyy-mm-dd): ")
                rezultat8 = afiseaza_cheltuieli_inainte_de_o_zi(apartamente, suma, zi)
                for linie in rezultat8:
                    print(linie)
            except ValueError as e:
                print(e)
        elif optiune == "9":
            try:
                tip = input("Tip cheltuială (apa, gaz, lumina): ")

                suma = suma_cheltuieli_tip(apartamente, tip)
                if tip in ["apa", "gaz", "lumina"]:
                    print(f"Suma cheltuielilor de tip '{tip}' este: {suma}")
                else:
                    print("Tipul cheltuielii introdus nu este valid.")
            except ValueError as e:
                print(e)

        elif optiune == "10":
            try:
                tip = input("Tip cheltuială (apa, gaz, lumina): ")

                rezultat = tipareste_apartamente_sortate_dupa_tip(apartamente, tip)

                if not rezultat:
                    print(f"Niciun apartament nu are cheltuieli de tipul '{tip}'.")
                else:
                    for apartament, cheltuieli in rezultat:
                        print(
                            f"Apartamentul {apartament}: Cheltuieli de tip '{tip}': {cheltuieli.get(tip, [])}")

            except ValueError as e:
                print(e)

        elif optiune == "11":
            try:
                numar_apartament = int(input("Introduceți numărul apartamentului: "))

                total_cheltuieli = calculeaza_total_cheltuieli(apartamente, numar_apartament)

                if total_cheltuieli is not None:
                    print(f"Total cheltuieli pentru apartamentul {numar_apartament}: {total_cheltuieli}")
                else:
                    print(f"Apartamentul {numar_apartament} nu există în înregistrări.")
            except ValueError as e:
                print(e)
        elif optiune == "12":
            try:
                tip = input("Tip cheltuială (apa, gaz, lumina): ")
                elimina_cheltuiala(apartamente, tip)

            except ValueError as e:
                print(e)

        elif optiune == "13":
            try:
                suma_minima = float(input("Suma minimă pentru eliminare: "))
                elimina_cheltuieli_mai_mici_decat(apartamente, suma_minima)

            except ValueError as e:
                print(e)

        elif optiune == "15":
            afiseaza_apartamente(apartamente)
        elif optiune == "16":
            break
        else:
            print("Opțiune invalidă. Încearcă din nou.")
