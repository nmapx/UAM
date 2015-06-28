# -*- coding: utf-8 -*-

"""Przykład nieskończonej łamigłówki."""

class InfinitePuzzle(object):
    """... bez jakiegoś specjalnego sensu."""

    def __init__(self):
        pass

    @staticmethod
    def is_target(state):
        """Sprawdza, czy stan docelowy."""
        return state == ('s', 'b', 'b', 'b', 'b')

    @staticmethod
    def transition(state):
        """Zwraca listę możliwych stanów docelowych."""
        return [state + ('a',), state + ('b',)]


if __name__ == '__main__':
    INFINITY = InfinitePuzzle()
    print INFINITY.transition(('s', 'a', 'a'))
