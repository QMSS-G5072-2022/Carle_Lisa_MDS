import pytest
from cipher import cipher

@pytest.mark.parametrize ("text, shift, anticipated", [("Potato", 2,'Rqvcvq'),("celery", 4,'gipivC'),
                                                       ("BEANS", 6,'HKGTY'),("Soup for Dinner", 8,'awCx nwz Lqvvmz')])
def test_cipher_diffexamples(text, shift, anticipated):
    actual=cipher(text, shift, encrypt=True)
    expected = anticipated
    assert actual == expected
