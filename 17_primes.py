# 17_primes.py — the dict method .get()
#
# Stage 5 — Lists and dicts
#
# Why this exercise: in 15 you counted words with an if/else ladder, and in 16
# reading a missing key crashed with KeyError. One dict method fixes both.
#
# Part 1 — predict, then check
#   Take this dict:
#       ages = {"ali": 30, "sara": 25}
#   Before running anything, write down what you think each line prints:
#       print(ages.get("ali"))
#       print(ages.get("reza"))
#       print(ages.get("reza", 0))
#       print(ages["reza"])
#   Then run them and compare. Which one crashes? Which one prints None?
#
# Part 2 — the counter from 15, in fewer lines
#   Ask for a sentence, count how many times each word appears, and print
#   one line per word, for example:
#       the: 2
#   Same cleaning as in 15 (lowercase, strip punctuation, skip empty words)
#   and the same output as before — but the counting itself must be ONE line
#   inside the loop. No if/else, no `in` check.
#
# Part 3 — safe lookup
#   After counting, ask "Which word?" and print how many times it appeared.
#   A word that never appeared must print 0 — no KeyError, no `in` check.
#
# Challenge (optional)
#   Count how many times each letter appears in one word (e.g. "banana").
#   Same one-line counting idea, but the loop walks characters, not words.
#
# Test shapes, not just values:
#   - "the cat, the dog!"   (same word, different punctuation)
#   - "!!!"                 (only punctuation)
#   - an empty line
#   - looking up a word that is not there
#
# Stuck? Ask for a hint, not the answer.

# Part 2 — count words
sentence = input("> Enter a sentence: ")
counts = {}

for word in sentence.lower().split():
    word = word.strip(",.!/'?:")
    if word:
        counts[word] = counts.get(word, 0) + 1

if not counts:
    print("No words entered.")
else:
    for word, count in counts.items():
        print(f"{word}: {count}")

    search = input("> Which word? ").lower().strip(",.!/'?:")
    if not search:
        print("No word entered.")
    else:
        print(f"{search}: {counts.get(search, 0)}")
