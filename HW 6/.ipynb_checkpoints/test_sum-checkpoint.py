{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f748635f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def test_sum_with_list():\n",
    "    assert sum([1, 2, 3]) == 6, \"Should be 6\"\n",
    "\n",
    "def test_sum_with_tuple():\n",
    "    assert sum((1, 2, 3)) == 6, \"Should be 6\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8498c762",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "01351a5c",
   "metadata": {},
   "outputs": [
    {
     "ename": "AssertionError",
     "evalue": "Should be 6",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[0;32mIn [4], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mtest_sum_with_tuple\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "Cell \u001b[0;32mIn [3], line 5\u001b[0m, in \u001b[0;36mtest_sum_with_tuple\u001b[0;34m()\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mtest_sum_with_tuple\u001b[39m():\n\u001b[0;32m----> 5\u001b[0m     \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28msum\u001b[39m((\u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m, \u001b[38;5;241m2\u001b[39m)) \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m6\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mShould be 6\u001b[39m\u001b[38;5;124m\"\u001b[39m\n",
      "\u001b[0;31mAssertionError\u001b[0m: Should be 6"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15a13348",
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
