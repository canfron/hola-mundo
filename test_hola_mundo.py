#!/usr/bin/env python3
"""Test mínimo: verificar que index.html existe y contiene 'hola mundo'."""
import os
import sys

def test_index_exists():
    path = os.path.join(os.path.dirname(__file__), "index.html")
    assert os.path.isfile(path), "index.html no existe"
    print("✓ index.html existe")

def test_index_contains_hola_mundo():
    path = os.path.join(os.path.dirname(__file__), "index.html")
    content = open(path).read().lower()
    assert "hola mundo" in content, "index.html no contiene 'hola mundo'"
    print("✓ index.html contiene 'hola mundo'")

if __name__ == "__main__":
    test_index_exists()
    test_index_contains_hola_mundo()
    print("Todos los tests pasaron.")
