{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ca7dedb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "###1a test \n",
    "def test_cipher_singleword():\n",
    "    actual = cipher('Potato', 2, encrypt=True)\n",
    "    expected = 'Rqvcvq'\n",
    "    assert actual == expected"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "11b2c7d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "###1b test\n",
    "def test_cipher_negshift():\n",
    "    actual = cipher('Carrot',-54, encrypt=True)\n",
    "    expected = \"AYppmr\"\n",
    "    assert actual == expected"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9b4c5ca3",
   "metadata": {},
   "outputs": [],
   "source": [
    "###1c test\n",
    "def test_cipher_symbols():\n",
    "    actual = cipher(\"-\", 3, encrypt=True)\n",
    "    expected = \"-\"\n",
    "    assert actual == expected"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4c14ac31",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'cipher' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn [4], line 4\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpytest\u001b[39;00m\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m pytest\u001b[38;5;241m.\u001b[39mraises(\u001b[38;5;167;01mAssertionError\u001b[39;00m):\n\u001b[0;32m----> 4\u001b[0m     \u001b[43mcipher\u001b[49m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLeek\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtwo\u001b[39m\u001b[38;5;124m\"\u001b[39m, encrypt\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'cipher' is not defined"
     ]
    }
   ],
   "source": [
    "###1d test\n",
    "import pytest\n",
    "with pytest.raises(AssertionError):\n",
    "    cipher(\"Leek\", \"two\", encrypt=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e18399f0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
