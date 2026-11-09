def clean(text):
    words = []
    for word in text.lower().split():
        word = word.strip(",.!/'?:")
        if word:
            words.append(word)
    return words


def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def most_common(counts):
    best_word = None
    best_count = 0
    for word in counts:
        if counts[word] > best_count:
            best_word = word
            best_count = counts[word]
    return best_word, best_count


sentence = input("> Enter a sentence: ")
words = clean(sentence)
counts = count_words(words)
if not counts:
    print("No words entered.")
else:
    for word, count in counts.items():
        print(f"{word}: {count}")
    best_word, best_count = most_common(counts)
    print(f"Most common word: {best_word} ({best_count} times)")

    search = input("> Which word? ").lower().strip(",.!/'?:")
    if not search:
        print("No word entered.")
    else:
        print(f"{search}: {counts.get(search, 0)}")

