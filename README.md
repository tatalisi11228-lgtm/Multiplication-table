# Python Practice — Hamid

A graded exercise track, starting from zero. You write the code; the reviewer
runs it, checks the logic, and explains what to improve.

## How this works

1. Read the task in the file's header comment.
2. Write your solution below the `# your code here` line.
3. Run it: `python <filename>.py`
4. Tell me what happened — including the exact error, if there is one.

Rules: don't look up a full solution before trying. Getting it wrong, then
finding out why, is the entire point. Ask for a hint instead of an answer.

## Track

### Stage 1 — Input, variables, arithmetic
- [x] `01_temperature.py` — Celsius to Fahrenheit converter ✅
- [x] `02_madlib.py` — fill-in-the-blank story ✅
- [x] `03_bill_split.py` — split a bill with tip ✅

### Stage 2 — Conditionals (if / elif / else)
- [x] `04_grade.py` — turn a score into a letter grade ✅
- [x] `05_leap_year.py` — is this year a leap year? ✅
- [x] `06_largest.py` — largest of three numbers ✅

### Stage 3 — Loops (for / while)
- [x] `07_times_table.py` — print a multiplication table ✅
- [x] `08_average.py` — average N numbers read from input ✅
- [x] `09_guess_game.py` — number guessing game ✅

### Stage 4 — Strings
- [x] `10_reverse.py` — reverse a string ✅
- [x] `11_palindrome.py` — palindrome checker ✅
- [x] `12_word_count.py` — count words in a sentence ✅

### Stage 5 — Lists and dicts
- [x] `13_max_no_builtin.py` — find the maximum without `max()` ✅
- [ ] `14_unique.py` — remove duplicates, keep order
- [ ] `15_frequency.py` — count each word's occurrences

### Stage 6 — Functions
- [ ] `16_refactor.py` — rewrite earlier exercises as functions
- [ ] `17_primes.py` — print primes up to N
- [ ] `18_calculator.py` — a menu-driven calculator

### Stage 7 — Files and structure
- [ ] `19_save_load.py` — write data to a file, read it back
- [ ] `20_todo.py` — a small to-do list app that persists

## Concepts covered so far

**Exercise 01 — temperature converter**
- `input("...")` — asks the user for text and returns it as a **string**
- `float(...)` — converts a string into a decimal number
- `print(...)` — displays output
- f-strings — `f"{value}"` drops a value into text
- Variables and `=` assignment
- `TypeError: unsupported operand type(s) for /: 'str' and 'int'` — what happens
  when you do arithmetic on text instead of converting it first
- Reading a traceback: bottom line = cause, arrow `^` = the guilty variable

**Exercise 02 — mad libs story**
- Storing several `input()` results in separate variables
- When NOT to convert: text stays text when you only want to place it in a sentence
- f-strings with the same variable used more than once
- `\n` — the newline character, for breaking one string across lines
- One `print` = one line of output

**Exercise 03 — split a bill with tip**
- `int(...)` vs `float(...)` — whole numbers vs decimals, and why it matters
- `round(value, n)` — rounding for money output
- Several inputs feeding several calculations
- **Naming matters:** a variable named `tip_amount` that holds a *percentage*
  hides a real bug behind a believable-looking line of code
- `ZeroDivisionError` — dividing by zero
- `ValueError` — `float("abc")` when the user types text
- A silent bug: `float()` accepts `3.5` people and returns a nonsense answer,
  while `int()` refuses it — catching mistakes instead of hiding them
- Always test with several different inputs, not just one

**Exercise 04 — score to letter grade**
- `if / elif / else` — one ladder, checked top to bottom: the **first** True branch wins
  and every branch after it is skipped
- `elif` continues the *same* ladder; a fresh `if` starts an independent one — which is
  why two separate `if`s can both fire for the same input
- Indentation *is* the block: a branch with no indented body is an `IndentationError`
- `else` takes **no** condition — `else: score < 60:` is a `SyntaxError`
- Direction matters: `>= 90` means "90 and above"; `<= 90` means the opposite
- Text typed by the user stays text: `"100" < "90"` is `True`, because two strings compare
  character by character instead of by value
- **Placement is logic:** a range guard (`score < 0 or score > 100`) only works as the
  first rung — put it later and half of it is unreachable dead code
- `or` — "either of these two bad cases is enough"
- A branch that prints nothing is a *silent* bug: no output, no error, and the program
  just ends. Worse than a crash, and the reason we test many inputs

**Exercise 05 — leap year**
- `%` gives the **remainder**, not the quotient: `2024 % 4 == 0` means "divisible by 4"
- `year % 100 != 0` — "not divisible by 100"
- `int()` for a year (a whole number), `float()` for a score — pick by what the value means
- f-strings put the variable **inside** the text: `f"{year} is a leap year"`. Two string
  literals written next to each other glue together instead: `'year'"is a leap year"`
  prints the literal word `yearis a leap year` — not the variable
- Nested exceptions ("divisible by 4, **except** 100, **except** 400") must be checked
  **most specific first**: 400 → 100 → 4 → else
- Branches placed after a broader condition are unreachable **dead code**: once `% 4 == 0`
  is checked, neither `% 100 == 0` nor `% 400 == 0` can ever be true below it
- A ladder with no final `else` can fall off the end and print nothing at all — the
  silent bug again. Every input should produce some output
- `ValueError` — `int("abc")` when the user types text instead of a number

**Exercise 06 — largest of three**
- Each branch asks one question about **one** candidate: `a >= b and a >= c` — "is *a* at
  least as big as both others?" A chain like `a >= b and b >= c` instead describes the
  *ordering* of b and c, and misses every case where a is largest but b < c
- `and` joins two conditions that must both be true
- `>=` instead of `>` handles ties: with plain `>`, the input (5, 5, 3) fell through to
  the `else` branch and announced that 3 was the largest
- The last `else` needs no condition: if neither a nor b is the largest, it has to be c
- **Test shapes, not just values.** (12,45,7), (45,12,7) and (7,12,45) all hid the same
  bug, because in each of them the stray conditions happened to hold. The missing shape
  was "a is the largest, but b < c"

**Exercise 07 — multiplication table (first loop)**
- `for i in range(1, 11):` — run the body once for every number in the range
- `range(a, b)` **excludes** `b`: `range(1, 11)` counts 1…10. This off-by-one is one of the
  most common mistakes in programming
- The loop variable is a box that gets a new value every round — never reuse a name that
  already holds something you still need. `i` first held the user's number; the loop
  overwrote it and the number was gone (the output was just 1…10)
- The loop body is indented, exactly like an `if` body. A line at the outer indentation
  runs only once, not once per round
- f-strings can hold a whole calculation, not just a variable: `f"{number} x {i} = {number * i}"`
- `int()` here, because the sample output shows `7`, not `7.0`
- A stray character can hide inside a name: `دnumber` is *legal* Python (Unicode letters are
  allowed in identifiers), so it runs fine while looking like a typo — it only bites later,
  when you type the name differently somewhere else

**Exercise 08 — average of N numbers (first accumulator)**
- The accumulator pattern: an **empty box before the loop**, add to it **inside**, use the
  result **after** the loop
- Zero, because it is the identity for addition (`0 + x = x`). A product would start at 1
- The box must be *before* the loop: put it inside and it is reset every round — the total
  ends up holding only the last number, with no error at all (a silent bug)
- The box also has to *exist* first, because `total = total + x` reads the old value before
  writing the new one. Without `total = 0` the first round is a `NameError`
- `input()` inside the loop is the whole point of the loop: one line, asked n times
- `int()` for the **count** ("how many"), `float()` for the **values** (quantities)
- The counter and the reading need two names: `i` is the round number, `x` holds the number
- An `if` alone does not stop a program — it only chooses. To guard `n == 0` the whole
  computation has to sit in the `else` of the guard
- `ZeroDivisionError` — what `n = 0` hits on `total / n`
- `round(average, 2)` keeps the output readable: `2.33` instead of `2.3333333333333335`
- **First-round trick (the challenge):** for a maximum or minimum there is no neutral
  starting value — `largest = 0` breaks on negative numbers. So round one is special:
  `if i == 1:` seeds both boxes with the first number, and the comparisons start at round two

**Exercise 09 — guess the number (first `while`)**
- `while` repeats **until a condition turns false**; `for` repeats a **known** number of times
- Python checks the condition *before* every round: true → run the body, then check again;
  false → leave the loop
- Nothing that should stay fixed may be created *inside* the loop: with
  `secret = random.randint(...)` in the body, every round gets a new secret and the game is
  unwinnable — and there is no error message, only an unwinnable game
- `import random` belongs at the top of the file, once
- `random.randint(1, 100)` includes **both** ends — unlike `range`
- `while True:` + `break` needs no fake starting value. The alternative condition
  `while guess != secret:` does need `guess = 0` before the loop, because the condition is
  checked before the first round
- Something inside the loop must move the condition towards false, otherwise: infinite loop
- Binary search: guess the middle and every wrong guess throws away half of what is left.
  100 numbers need at most 7 guesses (log2 100 ≈ 6.6), against 50 on average for 1, 2, 3, 4…

**Exercise 10 — reverse a string (Stage 4 begins)**
- A string is a **sequence**: index from 0, and negative indices count from the end
  (`word[0]`, `word[5]`, `word[-1]`), with `len(word)` for the length
- `IndexError: string index out of range` — asking for a character that is not there
- `for char in word:` walks the characters directly — no `range`, no counter needed
- A text accumulator starts as the **empty string** `""`, not `0` (`0 + "a"` is a `TypeError`)
- Order matters here, unlike addition: `result = char + result` **prepends** (reverses),
  while `result = result + char` **appends** (the string comes back unchanged)
- An indented `print` inside the loop fires once per round — a great debug window, but the
  final answer wants one line after the loop
- `len` is a **function**: `len(word)`. Square brackets are for indexing (`word[0]`), so
  `len[word]` gives `TypeError: 'builtin_function_or_method' object is not subscriptable`
- A line whose result is neither printed nor stored is dead code — `len(word)` alone does nothing
- **The challenge:** `split()` turns a sentence into a list of words, a **nested** loop
  reverses each word, `parts.append(rev)` collects them, `" ".join(parts)` glues them back

**Exercise 11 — palindrome checker (two ways)**
- A palindrome compares equal to its own reverse: build the reverse and use `==` on strings
- `==` on strings compares **character by character**, so case matters: `"L" != "l"`.
  `.lower()` normalises before comparing — keep the original for display, compare the cleaned one
- `str.lower()` / `.upper()` are **methods**: attached to the string with a dot, unlike `len(word)`
  which is a function taking the string as an argument
- **The two-pointer method** needs no second string: `left` starts at 0, `right` at
  `len(word) - 1`, compare, then move both inward (`left + 1`, `right - 1`) until they meet
- `right` counts *down*. Writing `right = right + 1` walks off the end of the string →
  `IndexError: string index out of range`
- A **flag** (`is_palindrome = True`) can hold a boolean and be set to `False` inside the loop
- Two pointers stop at the first mismatch (1 step for `hello`), while the reverse method always
  does the whole word (5 steps) — faster, but the reverse method reads more simply
- A guard for the empty input (`if word == "":`) keeps the program from announcing that
  "nothing" is a palindrome
- Testing only non-palindromes hid a real bug: with `hello` the mismatch broke out before the
  broken line ever ran. Palindrome shapes were the missing test

**Exercise 12 — count the words (Stage 4 complete)**
- `split()` returns a list of words and `len(list)` says how many — counting a sentence is two calls
- Counting by hand is the same counter as before: `count = 0` before the loop, `count + 1` inside.
  `len` is simply that loop, already written for you
- `len` counts **items**: `len(sentence)` is characters, `len(sentence.split())` is words
- `split()` with no argument collapses runs of whitespace, so `"I  am"` still gives two words — and
  `"   ".split()` gives `[]`, i.e. zero words
- A line whose result is neither printed nor stored is **dead code** (`len(sentence)` alone). This
  appeared a second time — the same mistake as `len(word)` in exercise 10. Worth watching for
- Naming: after `split()` the variable holds a *list of words*, not a sentence. `words` says what it is
- Singular/plural again: `1 word` but `4 words`, and `0 words` takes the plural
- An empty sentence gets its own message instead of "0 words" — the guard pattern, once more
- **The three challenges in one pass:** longest word with `longest = ""` (length 0 is the neutral
  starting value for a *length* comparison, and it is safe when the list is empty), the letter
  count with `letters = letters + len(word)`, and the average **after** the loop. Inside the loop
  the division ran every round and the intermediate values were meaningless (`0.75`, `2.0`, `3.25`)

**Exercise 13 — max without `max()` (Stage 5 begins)**
- A list holds many values under one name: `numbers = []`, then `numbers.append(x)` per item
- Indexing works just like strings: `numbers[0]`, `numbers[-1]`, `len(numbers)`; a loop with
  `for num in numbers:` walks the items
- **Current-champion algorithm:** start with `largest = numbers[0]`, then
  `if num > largest: largest = num` for the rest
- Start from `numbers[0]`, never `0` — with negative numbers 0 would win while not even being in
  the list (`-5, -1, -3` → the answer is `-1`)
- Comparing a number against the **list** is a `TypeError: '>' not supported between instances of
  'float' and 'list'`. The comparison is always against `largest`
- Two passes are normal: first collect, then analyse. Keeping the list lets you get max, min, sum
  and average afterwards; a running max inside the reading loop throws that ability away
- **Re-prompt loop:** `while True:` + `continue` while the input is invalid + `break` when it is
  good. A plain `if` cannot guard code that crashes inside the same expression — `int(input())`
  dies before any check on the next line
- `int('')` → `ValueError: invalid literal for int() with base 10: ''`
- `answer.isdigit()` (with `not`) filters non-numeric text before the conversion, so `abc` never
  reaches `int()`
- Once the loop guarantees a valid `n`, the guards *after* it disappear: validation moved from
  "check afterwards" to "only let good data in"

## Where we stopped

**Day 4, third session — 2026-10-19, afternoon.** Exercises 01–13 are done. Stage 5 (lists and
dicts) is under way. Next session starts here:

- [ ] `14_unique.py` — remove duplicates from a list while keeping the original order. Pairs
  nicely with the list work from 13 and introduces membership testing (`in`, `not in`).
- Then `15_frequency.py` — count how many times each word appears (the first dict).

**Resolved:** `11_palindrome.py` now has one active version (the second, two-pointer version);
the other is kept commented out on purpose.

Tools already learned: `input`, `print`, f-strings, `int`/`float`, `round`, `len`,
`if / elif / else`, `and` / `or`, comparison operators, `for` + `range`, `while` + `break`,
`\n`, `%` (modulo), `isdigit`, `import random` + `random.randint`, string indexing,
iteration, `.lower()` / `.strip()` / `.split()`, slicing, `append` / `join`, two pointers,
flags, and the accumulator and counter patterns.

**Exercise 14 — unique (remove duplicates, keep the order)**

- `in` / `not in` ask a yes/no question about membership and return `True` / `False`. On a list they compare whole items; on a string they look for a piece of text: `"app" in fruits` is `False`, `"app" in "apple"` is `True`
- A list accumulator starts as `[]` (like `0` for sums and `""` for text). It goes before the loop — inside, it is emptied every round, with no error
- Unique-list algorithm: `if n not in unique: unique.append(n)`. The question is about `unique`, never about the original list — the original always contains the item, so nothing would ever be added
- `append` changes the list in place and returns `None`: `unique = unique.append(n)` replaces the list with `None` and crashes next round with `AttributeError`
- `isdigit()` asks "are all characters digits?" (`""` is `False`). `"-5"` and `"3.5"` fail it, because `-` and `.` are not digits — it accepts only non-negative whole numbers
- A check needs an `if`: `number.isdigit() , numbers.append(...)` with a comma is two separate actions — the result of the check is thrown away (dead code again, as in exercises 10 and 12) and `append` always runs. The check must also use the loop variable (`item`), not a name that does not exist (`NameError`)
- `int()` changes equality: `"01"`, `"1"` and `"001"` are three different strings but all become `1` — converting first and removing duplicates after gives a different answer from the other order
- `input()` has to be inside `while True:` — outside, the variable never changes and the same result repeats forever (infinite loop; `Ctrl+C` stops it). A guard that ends in `break` needs no `else` after it
- Two valid ways to handle a bad item: skip it with a message that shows the real item (`f"skipping: {item}"`, not fixed text), or stop everything with a flag. A flag is only needed for the second, and a flag line at the same indentation as the `if` runs for every item
- Compute once, then use the name: `removed = len(numbers) - len(unique)` and `if removed == 1:` — not the same subtraction repeated in every condition. It comes after the loop that builds `unique`, and uses `numbers`, not `raw`: skipped invalid items are not removed duplicates
- Singular/plural once more, with three cases: 0 gets its own message ("No duplicates"), 1 is singular, 2 or more is plural
- The test shapes that mattered: `1 2 x 2` (a bad item between good ones), `-5 3` and `3.5 2` (the limits of `isdigit`), and an empty line
- Style: 4 spaces per indent level, spaces around `==`; Shift+Alt+F formats the file in VS Code

**Exercise 15 — word frequency (first dict)**

- A dict maps keys to values: `counts = {}`, `counts["apple"] = 1`, read with `counts["apple"]`. A missing key is `KeyError: 'cherry'`, like `IndexError` for lists. `in` checks the keys: `"cherry" in counts`
- Updating is the accumulator pattern with a key: `counts[word] = counts[word] + 1` reads the old value and writes the new one
- Counting algorithm: `if word in counts:` add 1, `else:` first sighting, `counts[word] = 1`. The first-time value is a number — the count so far — not the word (`= word`, later `"the" + 1` is a `TypeError`) and not the dict itself (`= counts`, later `dict + 1` is a `TypeError`). When unsure, trace `the cat the` by hand instead of guessing
- `for word in counts:` walks the keys; `counts[word]` is the value. Keys come in the order of first appearance
- A loop takes its items from whatever comes after `in`: `for word in counts:` over an empty dict runs zero rounds, so `word` never exists (`NameError`). Counting loops over the list `words`; printing loops over the dict `counts`. A `print` outside every loop runs once and shows only the last word
- A line ending in `:` needs an indented body (`IndentationError`, before even one line runs), and `else` must line up exactly with its `if`
- `split(x)` and `strip(x)` are different tools: `split(".,!?")` cuts only where that whole 5-character text appears (almost never); `strip(".,!?")` removes any of those characters from the start and end of one word and leaves the middle alone (`don't`). `strip` works on a single word, after `split()`
- `"".split(",")` is `['']`, not `[]`. Only `split()` with no argument gives an empty list for empty text — the guard `len(words) == 0` relies on it
- `word.strip(...)` returns a new string — it has to be stored (`word = word.strip(...)`) or it is thrown away
- Clean the data once, at the start, before the keys are built: `.lower()` before `.split()` (`.lower()` is a string method, so `.split().lower()` is an `AttributeError`) and `strip` inside the counting loop, before the `if`. Cleaning only inside the `print` changes the display and not the counts: `Hello, hello!!` still made two keys. To show the original case, keep the original text (exercise 11)
- The test that exposed it was a word repeated with different punctuation; `the cat, the dog!` passed even with the bug. Test shapes, not just values
- Champion with a dict: `best_word = ""`, `best_count = 0`, `if counts[word] > best_count:` then update both. `0` is a safe start because every count is at least 1 (in exercise 13 numbers could be negative). The champion needs its own name — `word` is overwritten every round (exercise 7). `>` keeps the first word on a tie, `>=` the last
- Where a variable is created depends on which loop it must survive: `counts = {}` before the `for` loop (survives its rounds) but inside `while True:` (fresh for every sentence); `input` inside `while True:` (it must repeat)
- Edge case: `!!!` strips to `""`, an empty key. `if word == "": continue` skips it

## Where we stopped

**2026-11-05. Exercises 01–15 are done. Stage 5 (lists and dicts) is under way. Next:**

 16 — the dict method `.get()` (turns the if/else counter into one line), then a small phone book: add names and look them up.

New tools: `in` / `not in`, dict basics (`{}`, `d[key]`, `KeyError`, looping over keys), `strip(chars)`.
