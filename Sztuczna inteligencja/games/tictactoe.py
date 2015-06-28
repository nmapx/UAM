# -*- coding: utf-8 -*-

"""Gra w kółko i krzyżyk."""

import random
import string

class TicTacToe(object):
    """Klasa reprezentująca kółko i krzyżyk."""

    def __init__(self):
        pass

    @staticmethod
    def __is_empty_field_description(mark):
        """Sprawdza, czy znak pustego pola."""
        return mark == ' '

    @staticmethod
    def __count_single_field(mark):
        """Zwraca jedynkę, jeśli pole nie jest puste (do zliczania)."""
        if TicTacToe.__is_empty_field_description(mark):
            return 0
        else:
            return 1

    @staticmethod
    def __count_non_empty_fields(board):
        """Zwraca liczbę niepustych pól."""
        return sum(
            TicTacToe.__count_single_field(board[y][x])
            for y in range(3) for x in range(3))

    @staticmethod
    def player_to_go(board):
        """Zwraca gracza przy ruchu."""
        non_empty_fields = TicTacToe.__count_non_empty_fields(board)
        if non_empty_fields % 2 == 0:
            return 'max'
        else:
            return 'min'

    @staticmethod
    def __player_mark(player_id):
        """Zwraca znaczek gracza."""
        if player_id == 'max':
            return 'x'
        else:
            return 'o'

    @staticmethod
    def moves(board):
        """Zwraca ruchy z danej pozycji."""
        current_player = TicTacToe.player_to_go(board)
        return TicTacToe.__remove_symmetries(
            [TicTacToe.__play(board, TicTacToe.__player_mark(current_player), y, x)
             for y in range(3)
             for x in range(3)
             if TicTacToe.__is_empty_field_description(board[y][x])])

    @staticmethod
    def __mark_to_value(mark):
        """Zamienia znaczek na wypłatę."""
        if mark == 'x':
            return 1
        else:
            return -1

    @staticmethod
    def __check_line(cell1, cell2, cell3):
        """
        Sprawdza, czy 3 pola należą do tego samego gracza. Jeśli tak,
        zwraca odpowiednią wypłatę. Jeśli nie - zwraca None.
        """
        if cell1 == cell2 and cell2 == cell3 \
                and not TicTacToe.__is_empty_field_description(cell1):
            return TicTacToe.__mark_to_value(cell1)

        return None

    @staticmethod
    def check_final_state(board):
        """Sprawdza, czy końcowa pozycja."""
        for y in range(3):
            ret = TicTacToe.__check_line(board[y][0], board[y][1], board[y][2])
            if ret != None:
                return ret

        for x in range(3):
            ret = TicTacToe.__check_line(board[0][x], board[1][x], board[2][x])
            if ret != None:
               return ret

        ret = TicTacToe.__check_line(board[0][0], board[1][1], board[2][2])
        if ret != None:
            return ret

        ret = TicTacToe.__check_line(board[0][2], board[1][1], board[2][0])
        if ret != None:
            return ret

        if all([not TicTacToe.__is_empty_field_description(board[y][x])
                for y in range(3)
                for x in range(3)]):
            return 0

        return None

    @staticmethod
    def __play(board, mark, y, x):
        """Zagrywa znaczek `mark` na pozycji y/x."""
        return tuple([TicTacToe.__play_in_row(rowy, board[rowy], mark, y, x)
                      for rowy in range(3)])

    @staticmethod
    def __play_in_row(rowy, row, mark, y, x):
        """Zwraca wiersz zmieniony przez zagranie."""
        if rowy == y:
            return TicTacToe.__mark_in_row(row, mark, x)
        else:
            return row

    @staticmethod
    def __mark_in_row(row, mark, x):
        """Zagrywa w wierszu."""
        return tuple([TicTacToe.__play_in_cell(cellx, row[cellx], mark, x)
                      for cellx in range(3)])

    @staticmethod
    def __play_in_cell(cellx, cell, mark, x):
        """Zwraca pole zmienione przez zagranie."""
        if cellx == x:
            return mark
        else:
            return cell

    @staticmethod
    def __get_symmetries(board):
        """Zwraca symetryczne układy."""
        return [
            board,
            TicTacToe.__rotate_90(board),
            TicTacToe.__rotate_180(board),
            TicTacToe.__rotate_270(board),
            TicTacToe.__flip_y(board),
            TicTacToe.__flip_x(board),
            TicTacToe.__diag_a(board),
            TicTacToe.__diag_b(board) ]

    @staticmethod
    def __remove_symmetries(boards):
        """Usuwa symetryczne układy."""
        returned = []
        already_found = set()
        for board in boards:
            if not board in already_found:
                returned.append(board)
                for sym in TicTacToe.__get_symmetries(board):
                    already_found.add(sym)
        return returned

    @staticmethod
    def __rotate_90(board):
        """Obrót o 90 stopni."""
        return ( (board[2][0], board[1][0], board[0][0]),
                 (board[2][1], board[1][1], board[0][1]),
                 (board[2][2], board[1][2], board[0][2]))

    @staticmethod
    def __rotate_180(board):
        """Obrót o 180 stopni."""
        return TicTacToe.__rotate_90(TicTacToe.__rotate_90(board))

    @staticmethod
    def __rotate_270(board):
        """Obrót o 270 stopni."""
        return TicTacToe.__rotate_90(TicTacToe.__rotate_180(board))

    @staticmethod
    def __flip_y(board):
        """Odbicie horyzontalne."""
        return (board[2], board[1], board[0])

    @staticmethod
    def __flip_x(board):
        """Odbicie wertykalne."""
        return tuple([(row[2], row[1], row[0]) for row in board])

    @staticmethod
    def __diag_a(board):
        """Odbicie względem przekątnej."""
        return ( (board[0][0], board[1][0], board[2][0]),
                 (board[0][1], board[1][1], board[2][1]),
                 (board[0][2], board[1][2], board[2][2]))

    @staticmethod
    def __diag_b(board):
        """Odbicie względem przekątnej."""
        return ( (board[2][2], board[1][2], board[0][2]),
                 (board[2][1], board[1][1], board[0][1]),
                 (board[2][0], board[1][0], board[0][0]))

    @staticmethod
    def show_boards(boards):
        """Wypisuje układy."""
        for board in boards:
           print " --- "
           for row in board:
               print "|","".join([str(cell) for cell in row]),"|"
           print " --- "
           print ""

    @staticmethod
    def initial_state():
        """Zwraca początkową pozycję."""
        return ((' ', ' ', ' '),
                (' ', ' ', ' '),
                (' ', ' ', ' '))

if __name__ == '__main__':
    TICTACTOE = TicTacToe()
    TICTACTOE.show_boards(TICTACTOE.moves(
            (('o', 'x', 'o'),
             ('x', ' ', 'o'),
             ('x', ' ', ' '))))
    TICTACTOE.show_boards(TICTACTOE.moves(
            TICTACTOE.initial_state()))
