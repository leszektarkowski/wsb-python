with open("data/swannsway.txt", encoding="utf-8") as f:
    counter = 0
    all_words = []
    for line in f:
        counter += 1
        words = line.split()
        for word in words:
            all_words.append(word.strip(""",.?!":""").lower())

    freq = {}
    for word in all_words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    results = {}
    for word, f in freq.items():
        if f in results:
            results[f].append(word)
        else:
            results[f] = [word]

    print(counter)
    print(len(all_words))
    print(len(freq))
    print(len(results))

    print(results)

    print("---------")
    for k in sorted(results.keys(), reverse=True)[:100]:
        print(k, ":", results[k])


