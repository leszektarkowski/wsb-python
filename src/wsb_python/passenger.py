"""Moduł z modelem danych: pasażer jako @dataclass."""

from dataclasses import dataclass


# Funkcja number_or_none(text) z lekcji 4 (już w szkielecie).
def number_or_none(text):
    return float(text) if text.strip() else None


# Klasa Passenger jako @dataclass: wypisujemy pola z typami, a dekorator sam pisze
# __init__, __repr__ i __eq__. Pola z wartością domyślną muszą być na końcu:
#   nazwisko: str, klasa: int, plec: str, przezyl: bool,
#   wiek: float | None = None, krewni: int = 0, oplata: float | None = None
@dataclass
class Passenger:
    name: str
    pclass: int
    sex: str
    survived: bool
    age: float | None = None
    relatives: int = 0
    fare: float | None = None

    # __post_init__: wywoływana zaraz po automatycznym __init__; tu sprawdzamy dane.
    # Klasa spoza (1, 2, 3) albo ujemny wiek → ValueError.
    def __post_init__(self):
        if self.pclass not in (1, 2, 3):
            raise ValueError(f"nieznana klasa: {self.pclass}")
        if self.age is not None and self.age < 0:
            raise ValueError(f"ujemny wiek: {self.age}")

    # Alternatywny konstruktor: metoda KLASY (dostaje cls, nie self).
    # from_csv_row(cls, row): pasażer z jednego wiersza csv.DictReader, konwersja typów w jednym miejscu:
    #   name → nazwisko, pclass → klasa (int), sex → plec, survived == "1" → przezyl,
    #   age → wiek, sibsp + parch → krewni, fare → oplata.
    @classmethod
    def from_csv_row(cls, row):
        return cls(
            name=row["name"],
            pclass=int(row["pclass"]),
            sex=row["sex"],
            survived=row["survived"] == "1",
            age=number_or_none(row["age"]),
            relatives=int(row["sibsp"]) + int(row["parch"]),
            fare=number_or_none(row["fare"]),
        )

    # Metoda age_group(): zwykła metoda, jak w klasie bez @dataclass (już w szkielecie).
    def age_group(self):
        if self.age is None:
            return "nieznany"
        if self.age < 18:
            return "dziecko"
        if self.age < 60:
            return "dorosły"
        return "senior"


# --- szybkie testy: if __name__ == "__main__", tylko przy uruchomieniu pliku ----------------
if __name__ == "__main__":
    # Tworzenie: argumenty pozycyjne w kolejności pól, dalej nazwane.
    p = Passenger("Allen, Miss. Elisabeth Walton", 1, "female", True, age=29.0, fare=211.3375)

    # __repr__ za darmo: wszystkie pola z nazwami.
    print(p)
    print(p.age_group())

    # __eq__ za darmo: porównuje wszystkie pola po kolei.
    duplicate = Passenger("Allen, Miss. Elisabeth Walton", 1, "female", True, age=29.0, fare=211.3375)
    print("p == duplicate:", p == duplicate)

    # __post_init__ odrzuca błędne dane: obiekt w ogóle nie powstaje.
    try:
        Passenger("X", 4, "male", False)
    except ValueError as e:
        print("Odrzucono:", e)

    # Wiersz z pliku (wszystko jest tekstem) zamieniony na obiekt z poprawnymi typami.
    # Słownik w układzie wiersza z csv.DictReader (już w szkielecie).
    row = {"pclass": "1", "survived": "1", "name": "Allen, Miss. Elisabeth Walton",
           "sex": "female", "age": "29", "sibsp": "0", "parch": "0", "fare": "211.3375"}

    # Konwersja przez alternatywny konstruktor from_csv_row().
    print(Passenger.from_csv_row(row))
