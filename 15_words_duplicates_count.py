from collections import Counter

while True:
    sentence = input("> Enter your sentence (press Enter to stop): ")
    words = sentence.lower().split()

    if not words:
        print("Stopped")
        break

    cleaned_words = []
    for word in words:
        cleaned = word.strip(".,!?")
        if cleaned:
            cleaned_words.append(cleaned)

    if not cleaned_words:
        print("No valid words entered.")
        continue

    word_counts = Counter(cleaned_words)

    for word, count in word_counts.items():
        print(f"{word} = {count}")

    max_count = word_counts.most_common(1)[0][1]

    most_common_words = []
    for word, count in word_counts.items():
        if count == max_count:
            most_common_words.append(word)

    print(f"Most frequent: {', '.join(most_common_words)} ({max_count})")
