import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "pulsar.csv"

# Dane pulsara: macierz 80 x 300; oś x to numery próbek 0–299 (już w szkielecie).
data = np.loadtxt(DATA_FILE, delimiter=",")
x = np.arange(data.shape[1])

plt.plot(x, data[9])
plt.show()