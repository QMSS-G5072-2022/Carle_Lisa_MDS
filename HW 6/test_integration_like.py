from cipher import cipher

def test_integration_like():
    text="Olive Bread"
    encrypted=""
    decrypted=""
    for i in range(1,11):
        encrypted = cipher(text, i)
        decrypted = cipher(encrypted, i, encrypt= False)
        assert decrypted == text
