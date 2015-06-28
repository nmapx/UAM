#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Zadanie 103."""

def oov(text, vocab):
    """Zwraca liste"""
    text = text.lower().split()
    vocab = [i.lower() for i in vocab]
    return [voc for voc in set(text) if voc not in vocab]
