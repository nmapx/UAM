# -*- coding: utf-8 -*-

"""Wyszukiwanie wszerz."""

def breadth_first(puzzle, node):
    """
    Wyszukuje wszerz w zadaniu `puzzle` poczynając od stanu `node`.
    Zwraca ścieżkę od `node` do stanu docelowego lub wartość
    specjalną None, jeśli nie ma takiej ścieżki.
    """
    path_tree_node = __breadth_first_core(puzzle, node)
    if path_tree_node == None:
        return None
    return __get_path(path_tree_node)

def __breadth_first_core(puzzle, initial_node):
    """Główna część algorytmu."""
    path_tree_frontier = [(initial_node, None)]

    while path_tree_frontier:
        print path_tree_frontier

        # wyciągamy docelowe stany z "granicy"
        target_states = [node for node in path_tree_frontier
                         if puzzle.is_target(node[0])]
        # ...jeśli w ogóle takie są, zwracamy pierwszy lepszy
        if target_states:
            return target_states[0]

        path_tree_frontier = sum(
            [__expand_node(puzzle, node) for node in path_tree_frontier],
            [])

    return None

def __expand_node(puzzle, path_tree_node):
    """Rozwija pojedynczy stan."""
    return [(next_node, path_tree_node)
            for next_node in puzzle.transition(path_tree_node[0])]

def __get_path(path_tree_node):
    """Zwraca ostateczną ścieżkę."""
    # prościej najpierw uzyskać odwróconą ścieżkę i potem ją odwrócić
    return list(reversed(__get_reversed_path(path_tree_node)))

def __get_reversed_path(path_tree_node):
    """Zwraca odwróconą ścieżkę."""
    if path_tree_node[1] == None:
        return [path_tree_node[0]]
    return [path_tree_node[0]] + __get_reversed_path(path_tree_node[1])
