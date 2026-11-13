print(2 ** 1000)

print(0.1 + 0.2)
total = 0

for i in range(10):
    total += 0.1

print(total)

from decimal import Decimal
d = Decimal("0.1")
total = d * 10
print(total)

import statistics as st


data = list(range(10))
print(data)
print(st.mean(data))
print(st.stdev(data))

print("-------")

from passenger_list import DATA_FILE, PassengerList
passengers = PassengerList.from_csv_file(DATA_FILE)
print(passengers)

ages = []
for p in passengers:
#    if p.age is None:
#        ages.append(0)
#    else:
#        ages.append(p.age)
    if p.age is not None:
        ages.append(p.age)

ages = [p.age for p in passengers if p.age is not None]

print(len(ages))
print(st.mean(ages))
print(st.stdev(ages))

fares = [p.fare for p in passengers if p.fare is not None]
print("mean:", st.mean(fares))
print("median:", st.median(fares))