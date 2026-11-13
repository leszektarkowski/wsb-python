"""Moduł z klasą PassengerList: kompozycja i protokoły (len, for, in)."""

import csv
from pathlib import Path

from passenger import Passenger

# Plik z danymi: od skryptu cztery poziomy w górę, potem data/titanic3.csv.
DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "titanic3.csv"


# Klasa PassengerList ZAWIERA obiekty Passenger (kompozycja: „ma”, nie „jest”).
# Obliczenia na całej grupie mieszkają w klasie, która tę grupę przechowuje.
class PassengerList:
    def __init__(self, passengers):
        self._passengers = list(passengers)

    # from_csv_file(cls, path): drugi konstruktor klasowy, wczytuje cały plik;
    # każdy wiersz zamienia na obiekt Passenger.from_csv_row(w).
    @classmethod
    def from_csv_file(cls, path):
        with open(path, encoding="utf-8", newline="") as f:
            rows = csv.DictReader(f)
            return cls(Passenger.from_csv_row(w) for w in rows)

    # Metoda survival_rate(): odsetek ocalałych; dla pustej listy None.
    # sum() po wartościach True/False liczy True jako 1.
    def survival_rate(self):
        if not self._passengers:
            return None
        survivors = sum(p.survived for p in self._passengers)
        return survivors / len(self._passengers)

    # Metoda filter(condition): warunek to FUNKCJA, która dla pasażera zwraca True/False.
    # Wynik to nowa PassengerList, więc filtry można łączyć.
    def filter(self, condition):
        return PassengerList(p for p in self._passengers if condition(p))

    # Protokoły: dzięki tym metodom obiekt działa z len(), for i in jak wbudowana kolekcja:
    #   __len__ → len(passengers),  __iter__ → for p in passengers,  __contains__(name) → "..." in passengers.
    # __repr__: krótki opis, np. <PassengerList: 1309 osób>.
    def __len__(self):
        return len(self._passengers)

    def __iter__(self):
        return iter(self._passengers)

    def __contains__(self, name):
        return any(p.name == name for p in self._passengers)

    def __repr__(self):
        return f"<PassengerList: {len(self)} osób>"


# --- szybkie testy: if __name__ == "__main__", tylko przy uruchomieniu pliku ----------------
if __name__ == "__main__":
    passengers = PassengerList.from_csv_file(DATA_FILE)
    print(passengers)

    # len() wywołuje __len__,  in wywołuje __contains__.
    print(len(passengers))
    print("Allen, Miss. Elisabeth Walton" in passengers)
    print("Kowalski, Mr. Jan" in passengers)

    # sum() i for korzystają z __iter__.
    print(sum(p.survived for p in passengers), "ocalałych")
    print(f"przeżywalność: {passengers.survival_rate():.1%}")
