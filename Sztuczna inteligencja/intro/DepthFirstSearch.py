# -*- coding: utf-8 -*-

"""Wyszukiwanie w głąb."""

def depth_first(puzzle, node):
    """
    Wyszukuje w głąb w zadaniu `puzzle` poczynając od stanu `node`.
    Zwraca ścieżkę od `node` do stanu docelowego lub wartość
    specjalną None, jeśli nie ma takiej ścieżki.
    """

    if puzzle.is_target(node):
        return [node]

    for next_node in puzzle.transition(node):
        path_found = depth_first(puzzle, next_node)
        if path_found != None:
            return [node] + path_found

    return None
