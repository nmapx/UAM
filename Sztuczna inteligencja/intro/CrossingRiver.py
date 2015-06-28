# -*- coding: utf-8 -*-

"""
Łamigłówka o przekraczaniu rzeki.

Zob. http://adonai.pl/relaks/zagadki/?id=43
"""


def remove_from_tuple_(tup, elem_to_be_removed):
    """Usuwa element z krotki."""
    return tuple([elem for elem in tup if elem != elem_to_be_removed])

def sort_tuple_(tup):
    """Sortuje krotkę."""
    return tuple(sorted(tup))

class CrossingRiver(object):
    """
    Klasa reprezentująca łamigłówkę o farmerze, wilku, kozie i kapuście

    Zakładamy, że stan łamigłówki to krotka (L, R), gdzie L to stan
    na lewym brzegu, R - na prawym brzegu.

    L i R mają postać krotki zawierające postacie z zagadki:
    - 'f' to farmer,
    - 'w' to wilk,
    - 'k' to koza,
    - 'c' to kapusta.

    Zakładamy, że krotka jest posortowana alfabetycznie.
    """

    def __init__(self):
        pass

    @staticmethod
    def is_target(state):
        """Sprawdza, czy stan docelowy."""
        return state == ((), ('c', 'f', 'k', 'w'))

    @staticmethod
    def transition(state):
        """Zwraca listę możliwych stanów docelowych."""
        boat_position = CrossingRiver.where_is_boat_(state)
        without_farmer = remove_from_tuple_(state[boat_position], 'f')
        new_states = [new_state for new_state in
                      [CrossingRiver.move_(without_farmer,
                                           state[1-boat_position],
                                           character,
                                           boat_position)
                       for character in without_farmer]
                      if CrossingRiver.is_valid(new_state)]

        # jeszcze przypadek kiedy sam farmer przepływa
        alone_state = CrossingRiver.move_alone_(
            without_farmer,
            state[1-boat_position],
            boat_position)
        if CrossingRiver.is_valid(alone_state):
            new_states.append(alone_state)

        return new_states

    @staticmethod
    def is_valid(state):
        """Sprawdza, czy poprawny stan."""
        boat_position = CrossingRiver.where_is_boat_(state)
        # sprawdzamy poprawność brzegu bez farmera
        return CrossingRiver.is_valid_shore_(state[1-boat_position])

    @staticmethod
    def is_valid_shore_(shore):
        """Sprawdza poprawność brzegu."""
        # koza zjada kapustę
        if 'k' in shore and 'c' in shore:
            return False

        # wilk zjada kozę
        if 'w' in shore and 'k' in shore:
            return False

        return True

    @staticmethod
    def move_(the_shore, the_other_shore, character, boat_position):
        """Przesuwa postać z jednego brzegu na drugi."""
        the_new_shore = remove_from_tuple_(the_shore, character)
        the_new_other_shore = tuple(sorted(list(the_other_shore) + ['f', character]))
        if boat_position == 0:
            return (the_new_shore, the_new_other_shore)
        else:
            return (the_new_other_shore, the_new_shore)

    @staticmethod
    def move_alone_(the_shore, the_other_shore, boat_position):
        """Przesuwa postać z jednego brzegu na drugi."""
        the_new_other_shore = tuple(sorted(list(the_other_shore) + ['f']))
        if boat_position == 0:
            return (the_shore, the_new_other_shore)
        else:
            return (the_new_other_shore, the_shore)


    @staticmethod
    def where_is_boat_(state):
        """Sprawdza, gdzie jest łódka (farmer)."""
        if 'f' in state[1]:
            return 1

        return 0

if __name__ == '__main__':
    CROSSING_RIVER = CrossingRiver()
    print CROSSING_RIVER.transition((('f', 'w', 'k'), ('c',)))
    print CROSSING_RIVER.transition((('c', 'f', 'w', 'k'), ()))
    print CROSSING_RIVER.transition((('c', 'w'), ('f', 'k')))
