def get_nr(apartament):
    # return student['nr_matricol']
    return apartament[0]


def get_tip(apartament):
    return apartament[1]


def get_suma(apartament):
    return apartament[2]


def get_zi(apartament):
    return apartament[3]


def set_tip(apartament, tip):
    apartament[1] = tip


def set_suma(apartament, suma):
    apartament[2] = suma


def set_zi(apartament, zi):
    apartament[3] = zi


def create_apartament(nr, tip, suma, zi):
    """
    Create a new apartament
    :param nr: apartam id number
    :param tip: tipul cheltuielii
    :param suma: suma cheltuielii
    :param zi: data efectuarii
    :return:
    """
    return [nr, tip, suma, zi]
