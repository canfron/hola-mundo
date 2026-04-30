#!/usr/bin/env python3
"""Test mínimo: verificar que index.html existe y contiene las trazas de los agentes."""
import os
import sys

AGENTES = ["bestia", "planner", "executor", "reviewer", "publisher"]

def test_index_exists():
    path = os.path.join(os.path.dirname(__file__), "index.html")
    assert os.path.isfile(path), "index.html no existe"
    print("✓ index.html existe")

def test_index_contains_trazabilidad():
    path = os.path.join(os.path.dirname(__file__), "index.html")
    content = open(path).read().lower()
    assert "trazabilidad" in content or "traza" in content, "index.html no contiene 'trazabilidad' o 'traza'"
    print("✓ index.html contiene 'trazabilidad' o 'traza'")

def test_index_contains_agents():
    path = os.path.join(os.path.dirname(__file__), "index.html")
    content = open(path).read().lower()
    for agente in AGENTES:
        assert agente in content, f"index.html no contiene '{agente}'"
    print(f"✓ index.html contiene los {len(AGENTES)} agentes: {', '.join(AGENTES)}")

def test_index_contains_agente():
    path = os.path.join(os.path.dirname(__file__), "index.html")
    content = open(path).read().lower()
    assert "agente" in content, "index.html no contiene 'agente'"
    print("✓ index.html contiene 'agente'")

if __name__ == "__main__":
    test_index_exists()
    test_index_contains_trazabilidad()
    test_index_contains_agents()
    test_index_contains_agente()
    print("Todos los tests pasaron.")
