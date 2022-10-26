import pytest
from cipher import cipher

def test_cipher_singleword():
    actual = cipher('Potato', 2, encrypt=True)
    expected = 'Rqvcvq'
    assert actual == expected

def test_cipher_negshift():
    actual = cipher('Carrot',-54, encrypt=True)
    expected = "AYppmr"
    assert actual == expected

def test_cipher_symbols():
    actual = cipher("-", 3, encrypt=True)
    expected = "-"
    assert actual == expected

def test_cipher_exceptionerror():
    expected = "AssertionError:"
    try:
        cipher("Leek", "two")
    except AssertionError:
        actual = "AssertionError:"
    assert expected == actual
