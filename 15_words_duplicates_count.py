
while True:
    sentence = input("> Enter your sentence (press Enter to stop): ")
    words = sentence.lower().split()
    if len(words) == 0:
        print("Stopped")
        break
    counts = {}
    for word in words:
        word = word.strip(".,!?")
        if word == "":
            continue
        elif word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    best_word = ""
    best_count = 0
    for word in counts:
        if counts[word] > best_count:
            best_word = word
            best_count = counts[word]
        print(f"{word} = {counts[word]}")
    print(f"Most frequent: {best_word} ({best_count})")
