# Wprowadzenie do programowania w języku Python

Kurs na WSB-NLU. Materiały: [tarkowski.org/wsbnlu](https://tarkowski.org/wsbnlu/)

## Jak zainstalować Pythona

### Instalacja interpretera

**Windows:** instalator z [python.org](https://www.python.org/downloads/)

- zaznaczyć **„Add python.exe to PATH”**
- w terminalu działa polecenie `py` lub `python`

**macOS:** instalator z [python.org](https://www.python.org/downloads/) lub [Homebrew](https://brew.sh) (`brew install python`)

- w terminalu: `python3`

**Alternatywa:** [`uv`](https://docs.astral.sh/uv/), czyli szybki menedżer Pythona i pakietów

```bash
uv python install
```

### Sprawdzenie instalacji

```bash
python --version      # Windows
python3 --version     # macOS, Linux
```

Uruchomienie interaktywnej konsoli (REPL):

```text
$ python3
>>> 2 + 2
4
>>> exit()
```

**REPL** = *Read, Eval, Print, Loop*: wczytaj, wykonaj, wypisz, powtórz.

### VS Code

1. Zainstalować VS Code ([code.visualstudio.com](https://code.visualstudio.com)).
2. Zainstalować rozszerzenie **Python** (Microsoft).
3. Wybrać interpreter: <kbd>Ctrl+Shift+P</kbd> → *Python: Select Interpreter*.
4. Utworzyć plik `.py` i uruchomić przyciskiem ▶ lub w terminalu.

> Na macOS zamiast <kbd>Ctrl</kbd> używamy <kbd>Cmd</kbd>.

### Notatniki: Jupyter i Colab

- Kod podzielony na **komórki**, wynik pod każdą komórką.
- Dobre do eksperymentów i analizy danych krok po kroku.
- **Google Colab** ([colab.research.google.com](https://colab.research.google.com)): notatnik w przeglądarce, bez instalacji.

| Skrypt `.py` | Notatnik `.ipynb` |
| --- | --- |
| program uruchamiany w całości | kod wykonywany fragmentami |
| automatyzacja, narzędzia | eksploracja, prezentacja wyników |

### Pakiety i środowiska wirtualne

Pakiety spoza biblioteki standardowej instalujemy przez `pip`:

```bash
python -m pip install matplotlib
```

**Środowisko wirtualne** to osobny „katalog z Pythonem” dla jednego projektu:

```bash
python -m venv .venv
source .venv/bin/activate      # macOS, Linux
.venv\Scripts\activate         # Windows
```

Po co? Różne projekty mogą potrzebować różnych wersji tych samych pakietów.

## Bibliografia

### Podstawowa

1. E. Matthes, *Python. Instrukcje dla programisty. Wydanie III*, Helion, Gliwice 2023.
2. A. Sweigart, *Automatyzacja nudnych zadań z Pythonem. Wydanie II*, Helion, Gliwice 2021.

### Uzupełniająca

1. J. VanderPlas, *Python Data Science. Niezbędne narzędzia do pracy z danymi. Wydanie II*, Helion, Gliwice 2024.
2. M. Lutz, *Python. Wprowadzenie. Wydanie VI*, Helion, Gliwice 2025.

### Źródła otwarte

- Oficjalny samouczek Pythona: [docs.python.org/pl/3/tutorial](https://docs.python.org/pl/3/tutorial/).
- Samouczki matplotlib: [matplotlib.org/stable/tutorials](https://matplotlib.org/stable/tutorials/index.html).
- A. Sweigart, *Automate the Boring Stuff with Python. 3rd Edition* (No Starch Press, 2025), bezpłatnie online: [automatetheboringstuff.com](https://automatetheboringstuff.com).
