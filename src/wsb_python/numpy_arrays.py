import numpy as np

a = np.array(range(10))
a = a * 10
print(a)

l = list(range(10))
l = l * 2
print(l)

from passenger_list import DATA_FILE, PassengerList
passengers = PassengerList.from_csv_file(DATA_FILE)
print(passengers)
ages = np.array([p.age for p in passengers if p.age is not None])
print(ages.shape)
print(ages.mean())
