from datetime import datetime


def este_format_data_valid(data, format_data="%Y-%m-%d"):
    """
       Verifică dacă o dată este într-un format valid.

       :param data: Data de verificat.
       :param format_data: Formatul dată (implicit "%Y-%m-%d").
       :return: True dacă data este în formatul specificat, False în caz contrar.
       """
    try:
        datetime.strptime(data, format_data)
        return True
    except ValueError:
        return False


def validare_numar_apartament(apartament):
    """
        Validează dacă numărul apartamentului este un număr întreg.

        :param apartament: Numărul apartamentului de validat.
        :return: Numărul apartamentului validat.
        :raises: ValueError dacă numărul nu este un număr întreg.
        """
    if not isinstance(apartament, int):
        raise ValueError("Eroare: Numărul apartamentului trebuie să fie un număr întreg.")
    return apartament


def validare_tip_cheltuiala(tip):
    """
        Validează dacă tipul cheltuielii este unul din valorile acceptate.

        :param tip: Tipul cheltuielii de validat.
        :return: Tipul cheltuielii validat.
        :raises: ValueError dacă tipul cheltuielii nu este valid.
        """
    if tip not in ["apa", "gaz", "lumina"]:
        raise ValueError("Eroare: Tipul cheltuielii trebuie să fie 'apa', 'gaz' sau 'lumina.")
    return tip


def validare_suma(suma):
    """
       Validează suma cheltuielii.

       :param suma: Suma cheltuielii de validat.
       :return: Suma cheltuielii validată.
       :raises: ValueError dacă suma nu este un număr valid sau este negativă.
       """
    try:
        suma = float(suma)
    except ValueError:
        raise ValueError("Eroare: Suma cheltuielii trebuie să fie un număr valid.")
    if suma < 0:
        raise ValueError("Eroare: Suma cheltuielii nu poate fi negativă.")
    return suma


def validare_data(zi):
    """
        Validează formatul datei.

        :param zi: Data de validat (format: yyyy-mm-dd).
        :return: Data validată.
        :raises: ValueError dacă data nu este în formatul specificat.
        """
    if not este_format_data_valid(zi):
        raise ValueError("Eroare: Data introdusă nu este în formatul corect (yyyy-mm-dd).")
    return zi


def adauga_cheltuiala(apartamente, apartament, tip, suma, zi):
    """
    Adaugă o cheltuială în dicționarul apartamentelor.

    :param apartamente: Dicționarul care conține datele despre apartamente.
    :param apartament: Numărul apartamentului.
    :param tip: Tipul cheltuielii (apa, gaz, lumina).
    :param suma: Suma cheltuielii.
    :param zi: Data cheltuielii (format: yyyy-mm-dd).
    :return: Dicționarul actualizat cu noua cheltuială.

    """

    new_apartamente = dict(apartamente)  # Face o copie a dicționarului existent

    apartament = validare_numar_apartament(apartament)
    tip = validare_tip_cheltuiala(tip)
    suma = validare_suma(suma)
    zi = validare_data(zi)

    if apartament not in new_apartamente:
        new_apartamente[apartament] = {}

    if tip not in new_apartamente[apartament]:
        new_apartamente[apartament][tip] = []

    new_apartamente[apartament][tip].append((suma, zi))

    return new_apartamente


def modifica_cheltuiala(apartamente, apartament, tip, suma_veche, suma_noua):
    """
        Modifică o cheltuială existentă în dicționarul apartamentelor.

        :param apartamente: Dicționarul care conține datele despre apartamente.
        :param apartament: Numărul apartamentului.
        :param tip: Tipul cheltuielii (apa, gaz, lumina).
        :param suma_veche: Suma cheltuielii veche.
        :param suma_noua: Suma cheltuielii noi.
        :return: Dicționarul actualizat cu cheltuiala modificată.
        :raises: ValueError dacă suma veche nu este găsită.
        """
    apartament = validare_numar_apartament(apartament)
    suma_veche = validare_suma(suma_veche)
    suma_noua = validare_suma(suma_noua)

    if apartament in apartamente and tip in apartamente[apartament]:
        cheltuieli = apartamente[apartament][tip]
        found = False

        for i, (suma, data) in enumerate(cheltuieli):
            if suma == suma_veche:
                cheltuieli[i] = (suma_noua, data)
                found = True
                break
        if not found:
            raise ValueError('Eroare: Suma veche nu a fost găsită')

    return apartamente


def sterge_apartament(apartamente, apartament):
    """
            Sterge Apartament din dictionar
            :param apartament: Numarul Apartamentului
            :param apartamente: Dicționarul care conține datele despre apartamente.
            :return: Dicționarul actualizat cu apartamentul sters.
            :raises: ValueError dacă apartamentul nu exista
            """
    apartament = validare_numar_apartament(apartament)

    if apartament in apartamente:
        del apartamente[apartament]
        return apartamente
    else:
        raise ValueError('Eroare: Apartamentul nu există în înregistrări.')


def sterge_apartamente_consecutive(apartamente, apartament_start, apartament_end):
    """
                Sterge Apartamente consecutive din dictionar
                :param apartament_start: Numarul primul apartament
                :param apartament_end: Numarul al doilea apartament
                :param apartamente: Dicționarul care conține datele despre apartamente.
                :return: Dicționarul actualizat cu apartamentele sterse.

                """
    apartament_start = validare_numar_apartament(apartament_start)
    apartament_end = validare_numar_apartament(apartament_end)
    new_apartamente = apartamente.copy()

    for apartament in range(apartament_start, apartament_end + 1):
        if apartament in new_apartamente:
            new_apartamente.pop(apartament)

    return new_apartamente


def sterge_cheltuieli_tip(apartamente, tip):
    """
                 Sterge cheltuieli de un anumit tip
                 :param tip: Tipul cheltuielii
                 :param apartamente: Dicționarul care conține datele despre apartamente.
                 :return: Dicționarul actualizat cu cheltuielile ramase.

                 """
    tip = validare_tip_cheltuiala(tip)

    new_apartamente = apartamente.copy()

    for apartament in new_apartamente:
        if tip in new_apartamente[apartament]:
            new_apartamente[apartament].pop(tip)

    return new_apartamente


def afiseaza_apartamente_cu_cheltuieli_mai_mari_decat(apartamente, suma):
    """
        Afișează apartamentele cu cheltuieli mai mari decât o anumită sumă.

        :param apartamente: Dicționarul care conține datele despre apartamente.
        :param suma: Suma minimă pentru afișare.
    """

    suma = validare_suma(suma)
    rezultat = []

    for apartament, cheltuieli in apartamente.items():
        for tip, lista_cheltuieli in cheltuieli.items():
            for suma_cheltuiala, _ in lista_cheltuieli:
                if suma_cheltuiala > suma:
                    rezultat.append(
                        f"Apartamentul {apartament} | Cheltuiala: {tip} | Suma ce depășește: {suma_cheltuiala}.")

    if not rezultat:
        print(f"Nicio cheltuială depășește suma {suma}.")

    return rezultat


def afiseaza_cheltuieli_tip(apartamente, tip):
    """
        Afișează cheltuielile de un anumit tip pentru toate apartamentele.

        :param apartamente: Dicționarul care conține datele despre apartamente.
        :param tip: Tipul cheltuielii de afișat (apa, gaz, lumina).
        """

    tip = validare_tip_cheltuiala(tip)
    rezultat = []

    for apartament, cheltuieli in apartamente.items():
        if tip in cheltuieli:
            rezultat.append(f"Apartamentul {apartament}: Cheltuiala de tip {tip} este {cheltuieli[tip]}.")

    return rezultat


def afiseaza_cheltuieli_inainte_de_o_zi(apartamente, suma, zi):
    rezultat = []

    for apartament, cheltuieli in apartamente.items():
        cheltuiala_gasita = False  # Variabilă pentru a verifica dacă s-a găsit o cheltuială validă
        for tip, lista_cheltuieli in cheltuieli.items():
            for suma_cheltuiala, data in lista_cheltuieli:
                if data < zi and suma_cheltuiala > suma:
                    rezultat.append(
                        f"Apartament {apartament}: Cheltuiala {tip} efectuată înainte de {zi} și mai mare decât {suma}.")
                    cheltuiala_gasita = True  # O cheltuială a fost găsită
        if not cheltuiala_gasita:
            rezultat.append(f'Nu a fost efectuată o astfel de cheltuială în apartamentul {apartament}')

    return rezultat


def tipareste_apartamente_sortate_dupa_tip(apartamente, tip):
    """
    Tipărește toate cheltuielile de un anumit tip, sortate după valoare.

    :param apartamente: Dicționarul care conține datele despre apartamente.
    :param tip: Tipul de cheltuială după care se face sortarea.
    :return: Lista de cheltuieli de tipul specificat sortate după valoare sau None dacă nu există cheltuieli de tipul
    """
    try:
        tip = validare_tip_cheltuiala(tip)
    except ValueError as e:
        print(e)
        return None

    cheltuieli_tip = [cheltuiala for apartament in apartamente.values() for cheltuiala in apartament.get(tip, [])]

    if not cheltuieli_tip:
        return None

    cheltuieli_sortate = sorted(cheltuieli_tip, key=lambda x: x[0])

    return cheltuieli_sortate


def suma_cheltuieli_tip(apartamente, tip):
    """
                Calculeaza suma cheltuielilor de un anumit tip

                 :param tip: Tipul cheltuielii
                 :param apartamente: Dicționarul care conține datele despre apartamente.
                 :return: Dicționarul actualizat cu suma cheltuielilor.

                 """

    tip = validare_tip_cheltuiala(tip)

    suma = 0

    for cheltuieli in apartamente.values():
        if tip in cheltuieli:
            for suma_cheltuiala, _ in cheltuieli[tip]:
                suma += suma_cheltuiala

    return suma


def calculeaza_total_cheltuieli(apartamente, numar_apartament):
    """
    Calculează totalul de cheltuieli pentru un apartament dat.

    :param apartamente: Dicționarul care conține datele despre apartamente.
    :param numar_apartament: Numărul apartamentului pentru care se dorește calculul totalului de cheltuieli.
    :return: Totalul de cheltuieli sau None dacă apartamentul nu există în înregistrări.
    """
    numar_apartament = validare_numar_apartament(numar_apartament)

    if numar_apartament in apartamente:
        total = 0
        for cheltuieli in apartamente[numar_apartament].values():
            for suma_cheltuiala, _ in cheltuieli:
                total += suma_cheltuiala
        return total
    else:
        return None


def elimina_cheltuiala(apartamente, tip):
    """
                 Elimina o cheltuiala a unui apartament
                 :param tip: Tipul cheltueielii
                 :param apartamente: Dicționarul care conține datele despre apartamente.
                 :return: Dicționarul actualizat cu cheltuieli ramase.

                 """
    tip = validare_tip_cheltuiala(tip)

    new_apartamente = apartamente.copy()

    for apartament in new_apartamente:
        if tip in new_apartamente[apartament]:
            new_apartamente[apartament].pop(tip)

    return new_apartamente


def elimina_cheltuieli_mai_mici_decat(apartamente, suma_minima):
    for ap in apartamente:
        for tip, lista_cheltuieli in apartamente[ap].items():
            lista_cheltuieli[:] = [(suma, data) for suma, data in lista_cheltuieli if suma >= suma_minima]
    return apartamente


def test_adauga_cheltuiala():
    apartamente = []
    apartament = 101
    tip = "apa"
    suma = 50.0
    zi = "2023-11-02"

    # Adaugăm o cheltuială
    apartamente_actualizat = adauga_cheltuiala(apartamente, apartament, tip, suma, zi)

    # Verificăm dacă cheltuiala a fost adăugată corect
    assert apartament in apartamente_actualizat
    assert tip in apartamente_actualizat[apartament]
    assert (suma, zi) in apartamente_actualizat[apartament][tip]


def test_modifica_cheltuiala():
    apartamente = {1: {"apa": [(100, "2023-10-30")]}}

    # Testăm funcția cu date corecte
    modifica_cheltuiala(apartamente, 1, "apa", 100, 150)
    assert apartamente == {1: {"apa": [(150, "2023-10-30")]}}

    # Testăm funcția cu suma veche inexistentă
    try:
        modifica_cheltuiala(apartamente, 1, "apa", 200, 250)
        assert False  # Dacă nu se ridică o excepție, testul a eșuat
    except ValueError:
        assert True  # Se așteaptă o excepție ValueError


def test_sterge_apartament():
    apartamente = {1: {"apa": [(100, "2023-10-30")]}}

    # Testăm funcția cu un număr de apartament valid
    sterge_apartament(apartamente, 1)
    assert apartamente == {}  # După ștergere, dictionarul ar trebui să fie gol

    # Testăm funcția cu un număr de apartament inexistent
    try:
        sterge_apartament(apartamente, 2)
        assert False  # Dacă nu se ridică o excepție, testul a eșuat
    except ValueError:
        assert True  # Se așteaptă o excepție ValueError


def test_sterge_cheltuieli_tip():
    apartamente = {1: {"apa": [(200, "2023-10-30")], "gaz": [(60, "2023-10-29")], "lumina": [(275, "2023-10-28")]}}

    tip = "apa"
    rezultat_asteptat = {1: {"gaz": [(60, "2023-10-29")], "lumina": [(275, "2023-10-28")]}}

    assert sterge_cheltuieli_tip(apartamente, tip) == rezultat_asteptat


def test_afiseaza_apartamente_cu_cheltuieli_mai_mari_decat():
    apartamente = {1: {"apa": [(155, "2023-10-30")], "gaz": [(55, "2023-10-29")]}}
    suma = 75
    rezultat_asteptat = ["Apartamentul 1 | Cheltuiala: apa | Suma ce depășește: 155."]

    assert afiseaza_apartamente_cu_cheltuieli_mai_mari_decat(apartamente, suma) == rezultat_asteptat


def test_afiseaza_cheltuieli_tip():
    apartamente = {1: {"apa": [(333, "2023-10-30")], "gaz": [(650, "2023-10-29")]}}

    tip = "apa"
    rezultat_valid = ["Apartamentul 1: Cheltuiala de tip apa este [(333, '2023-10-30')]."]

    assert afiseaza_cheltuieli_tip(apartamente, tip) == rezultat_valid


def test_afiseaza_cheltuieli_inainte_de_o_zi():
    apartamente = {
        1: {"apa": [(230, "2023-10-30")], "gaz": [(50, "2023-10-29")]},
        2: {"apa": [(120, "2023-10-28")], "gaz": [(40, "2023-10-30")]}
    }

    suma_valida = 30
    zi_valida = "2023-10-30"
    rezultat_valid = [
        "Apartament 1: Cheltuiala gaz efectuată înainte de 2023-10-30 și mai mare decât 30.",
        "Apartament 2: Cheltuiala apa efectuată înainte de 2023-10-30 și mai mare decât 30."
    ]

    suma_invalida = 60
    zi_invalida = "2023-10-27"
    rezultat_invalid = ["Nu a fost efectuată o astfel de cheltuială în apartamentul 1",
                        "Nu a fost efectuată o astfel de cheltuială în apartamentul 2"]

    assert afiseaza_cheltuieli_inainte_de_o_zi(apartamente, suma_valida, zi_valida) == rezultat_valid
    assert afiseaza_cheltuieli_inainte_de_o_zi(apartamente, suma_invalida, zi_invalida) == rezultat_invalid


def test_suma_cheltuieli_tip():
    apartamente = {
        1: {"apa": [(100, "2023-10-30")], "gaz": [(50, "2023-10-29")], "lumina": [(75, "2023-10-28")]},
        2: {"apa": [(120, "2023-10-28")], "gaz": [(40, "2023-10-30")]}
    }

    # Testăm funcția cu un tip valid și suma așteptată
    assert suma_cheltuieli_tip(apartamente, "apa") == 220

    # Testăm funcția cu un tip valid și suma așteptată
    assert suma_cheltuieli_tip(apartamente, "lumina") == 75


def test_calculeaza_total_cheltuieli():
    # Dicționarul de apartamente pentru testare
    apartamente = {
        1: {"apa": [(100, "2023-10-30")], "gaz": [(50, "2023-10-29")]},
        2: {"apa": [(120, "2023-10-28")], "gaz": [(40, "2023-10-30")]}
    }

    # Testăm funcția pentru un apartament existent
    total_apartament_1 = calculeaza_total_cheltuieli(apartamente, 1)
    assert total_apartament_1 == 150  # 100 (apa) + 50 (gaz)

    # Testăm funcția pentru un apartament inexistent
    total_apartament_3 = calculeaza_total_cheltuieli(apartamente, 3)
    assert total_apartament_3 is None  # Apartamentul 3 nu există în înregistrări


def test_tipareste_apartamente_sortate_dupa_tip():
    # Definiți un dicționar de apartamente pentru test
    apartamente = {
        1: {"apa": [(230, "2023-10-30")], "gaz": [(50, "2023-10-29")]},
        2: {"apa": [(120, "2023-10-28")], "gaz": [(40, "2023-10-30")]}
    }

    # Specificați un tip de cheltuială pentru sortare
    tip = "apa"

    # Rezultatul așteptat
    rezultat_asteptat_valid = [(120, '2023-10-28'), (230, '2023-10-30')]
    # Apelați funcția pentru a obține rezultatul real
    rezultat_real_valid = tipareste_apartamente_sortate_dupa_tip(apartamente, tip)

    # Folosiți assert pentru a verifica dacă rezultatul real este cel așteptat
    assert rezultat_real_valid == rezultat_asteptat_valid, "Testul pentru tipareste_apartamente_sortate_dupa_tip a eșuat."


def test_elimina_cheltuiala():
    # Definiți un dicționar de apartamente pentru test
    apartamente = {
        1: {"apa": [(230, "2023-10-30")], "gaz": [(50, "2023-10-29")]},
        2: {"apa": [(120, "2023-10-28")], "gaz": [(40, "2023-10-30")]}
    }

    # Specificați un tip de cheltuială care va fi eliminat
    tip_existent = "apa"
    rezultat_asteptat_existent = {
        1: {"gaz": [(50, "2023-10-29")]},
        2: {"gaz": [(40, "2023-10-30")]}
    }
    # Apelați funcția pentru a obține rezultatul real
    rezultat_real_existent = elimina_cheltuiala(apartamente, tip_existent)

    # Folosiți assert pentru a verifica dacă rezultatul real este cel așteptat
    assert rezultat_real_existent == rezultat_asteptat_existent, "Testul pentru eliminarea cheltuielii existente a eșuat."


def test_elimina_cheltuieli_mai_mici_decat():
    # Creăm un dicționar de apartamente pentru test
    apartamente = {
        1: {
            'apa': [(20, '2023-01-01'), (30, '2023-02-01')],
            'gaz': [(25, '2023-01-01'), (35, '2023-02-01')],
        },
        2: {
            'apa': [(15, '2023-01-01')],
            'gaz': [(40, '2023-01-01')],
        },
    }

    # Testăm eliminarea cheltuielilor mai mici decât 20 pentru toate apartamentele
    suma_minima = 20
    rezultat_asteptat = {
        1: {
            'apa': [(20, '2023-01-01'), (30, '2023-02-01')],
            'gaz': [(25, '2023-01-01'), (35, '2023-02-01')],
        },
        2: {
            'apa': [],
            'gaz': [(40, '2023-01-01')],
        },
    }

    rezultat = elimina_cheltuieli_mai_mici_decat(apartamente, suma_minima)
    # Verificăm dacă rezultatul obținut este cel așteptat
    assert rezultat == rezultat_asteptat, "Test failed: Suma minimă nu a fost aplicată corect."


if __name__ == "__main__":
    test_adauga_cheltuiala()
    test_modifica_cheltuiala()
    test_sterge_cheltuieli_tip()
    test_sterge_apartament()
    test_afiseaza_apartamente_cu_cheltuieli_mai_mari_decat()
    test_afiseaza_cheltuieli_tip()
    test_afiseaza_cheltuieli_inainte_de_o_zi()
    test_suma_cheltuieli_tip()
    test_calculeaza_total_cheltuieli()
    test_tipareste_apartamente_sortate_dupa_tip()
    test_elimina_cheltuiala()
    test_elimina_cheltuieli_mai_mici_decat()
