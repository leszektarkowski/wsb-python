# Dane do kursu

Pliki pobrane 7.10.2026. Wszystkie są w formacie CSV, kodowanie ASCII, końce linii LF.

## `titanic3.csv`: pasażerowie Titanica

- **Źródło:** F. E. Harrell Jr., T. Cason, Vanderbilt University, Department of Biostatistics,
  https://hbiostat.org/data/repo/titanic3.csv (opis: https://hbiostat.org/data/repo/titanic.html)
- **Rozmiar:** 1309 pasażerów (bez załogi), 14 kolumn, wiersz nagłówka.
- **Licencja:** zbiór udostępniony publicznie (w OpenML oznaczony jako „publicly available”);
  jawnej licencji nie podano, więc przy wykorzystaniu podajemy źródło i autorów.

| Kolumna | Znaczenie |
| --- | --- |
| `pclass` | klasa biletu (1, 2, 3) |
| `survived` | przeżył (1) / zginął (0) |
| `name` | nazwisko i imię z tytułem (Mr., Mrs., Miss, Master…) |
| `sex` | płeć (`female`, `male`) |
| `age` | wiek w latach; ułamki dla niemowląt; puste pole = brak danych |
| `sibsp` | liczba rodzeństwa i małżonków na pokładzie |
| `parch` | liczba rodziców i dzieci na pokładzie |
| `ticket` | numer biletu |
| `fare` | opłata w funtach brytyjskich |
| `cabin` | kabina; zwykle pusta |
| `embarked` | port zaokrętowania: S = Southampton, C = Cherbourg, Q = Queenstown |
| `boat` | numer szalupy ratunkowej |
| `body` | numer zidentyfikowanego ciała |
| `home.dest` | miejsce zamieszkania / cel podróży |

## Pulsar CP 1919 (PSR B1919+21)

80 kolejnych profili impulsów pierwszego odkrytego pulsara, po 300 próbek każdy.
Dane zdigitalizowano z rysunku w pracy doktorskiej H. D. Crafta Jr. (Cornell, 1970),
więc skala natężenia jest umowna. To te same dane, z których powstała okładka
albumu *Unknown Pleasures* (Joy Division, 1979).

### `cp1919.csv`: format długi

- **Źródło:** https://github.com/pachadotdev/cp1919 (plik `dev/cp1919.csv`)
- **Licencja:** CC0 (domena publiczna)
- **Rozmiar:** 24 000 wierszy + nagłówek, kolumny `x,y,z`:
  - `x`: numer próbki w profilu (1–300), czyli oś czasu
  - `y`: numer profilu (impulsu), 1–80
  - `z`: natężenie sygnału (jednostki umowne)

Wariant do ćwiczenia z modułem `csv` i grupowaniem w słownik list.

### `pulsar.csv`: macierz 80 × 300

- **Źródło:** https://gist.github.com/borgar/31c1e476b8e92a11d7e9 (`pulsar.csv`)
- **Licencja:** nie podano; dane pochodne tego samego rysunku Crafta
- **Rozmiar:** 80 wierszy (profile) × 300 kolumn (próbki), bez nagłówka;
  brak znaku nowej linii na końcu ostatniego wiersza (nie przeszkadza `np.loadtxt`)

Wariant do wczytania jednym wywołaniem:

```python
import numpy as np
dane = np.loadtxt("pulsar.csv", delimiter=",")   # dane.shape == (80, 300)
```

Oba pliki zawierają te same wartości: wiersz `i` w `pulsar.csv` odpowiada
wierszom `cp1919.csv` z `y == i + 1`.
