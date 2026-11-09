Python Practice — Hamid

A graded exercise track, starting from zero. You write the code; the reviewer runs it, checks the logic, and explains what to improve.

How this works
Read the task in the file's header comment.
Write your solution below the # your code here line.
Run it: python <filename>.py
Tell me what happened — including the exact error, if there is one.

Rules: don't look up a full solution before trying. Getting it wrong, then finding out why, is the entire point. Ask for a hint instead of an answer.

Track
Stage 1 — Input, variables, arithmetic
 01_temperature.py — Celsius to Fahrenheit converter ✅
 02_madlib.py — fill-in-the-blank story ✅
 03_bill_split.py — split a bill with tip ✅
Stage 2 — Conditionals (if / elif / else)
 04_grade.py — turn a score into a letter grade ✅
 05_leap_year.py — is this year a leap year? ✅
 06_largest.py — largest of three numbers ✅
Stage 3 — Loops (for / while)
 07_times_table.py — print a multiplication table ✅
 08_average.py — average N numbers read from input ✅
 09_guess_game.py — number guessing game ✅
Stage 4 — Strings
 10_reverse.py — reverse a string ✅
 11_palindrome.py — palindrome checker ✅
 12_word_count.py — count words in a sentence ✅
Stage 5 — Lists and dicts
 13_max_no_builtin.py — find the maximum without max() ✅
 14_unique.py — remove duplicates, keep order ✅
 15_frequency.py — count each word's occurrences ✅
 16 — phone book (dict: add and look up) ✅
 17_get.py — .get(): one-line counter and safe lookup ✅
Stage 6 — Functions
 18_calculator.py — a menu-driven calculator, with functions ✅
 18b_refactor.py — the word counter from 17, rewritten as functions ✅
 Not placed yet: print primes up to N
Stage 7 — Files and structure
 19_save_load.py — write data to a file, read it back
 20_todo.py — a small to-do list app that persists
Concepts covered so far

Exercise 01 — temperature converter

input("...") — asks the user for text and returns it as a string
float(...) — converts a string into a decimal number
print(...) — displays output
f-strings — f"{value}" drops a value into text
Variables and = assignment
TypeError: unsupported operand type(s) for /: 'str' and 'int' — what happens when you do arithmetic on text instead of converting it first
Reading a traceback: bottom line = cause, arrow ^ = the guilty variable

Exercise 02 — mad libs story

Storing several input() results in separate variables
When NOT to convert: text stays text when you only want to place it in a sentence
f-strings with the same variable used more than once
\n — the newline character, for breaking one string across lines
One print = one line of output

Exercise 03 — split a bill with tip

int(...) vs float(...) — whole numbers vs decimals, and why it matters
round(value, n) — rounding for money output
Several inputs feeding several calculations
Naming matters: a variable named tip_amount that holds a percentage hides a real bug behind a believable-looking line of code
ZeroDivisionError — dividing by zero
ValueError — float("abc") when the user types text
A silent bug: float() accepts 3.5 people and returns a nonsense answer, while int() refuses it — catching mistakes instead of hiding them
Always test with several different inputs, not just one

Exercise 04 — score to letter grade

if / elif / else — one ladder, checked top to bottom: the first True branch wins and every branch after it is skipped
elif continues the same ladder; a fresh if starts an independent one — which is why two separate ifs can both fire for the same input
Indentation is the block: a branch with no indented body is an IndentationError
else takes no condition — else: score < 60: is a SyntaxError
Direction matters: >= 90 means "90 and above"; <= 90 means the opposite
Text typed by the user stays text: "100" < "90" is True, because two strings compare character by character instead of by value
Placement is logic: a range guard (score < 0 or score > 100) only works as the first rung — put it later and half of it is unreachable dead code
or — "either of these two bad cases is enough"
A branch that prints nothing is a silent bug: no output, no error, and the program just ends. Worse than a crash, and the reason we test many inputs

Exercise 05 — leap year

% gives the remainder, not the quotient: 2024 % 4 == 0 means "divisible by 4"
year % 100 != 0 — "not divisible by 100"
int() for a year (a whole number), float() for a score — pick by what the value means
f-strings put the variable inside the text: f"{year} is a leap year". Two string literals written next to each other glue together instead: 'year'"is a leap year" prints the literal word yearis a leap year — not the variable
Nested exceptions ("divisible by 4, except 100, except 400") must be checked most specific first: 400 → 100 → 4 → else
Branches placed after a broader condition are unreachable dead code: once % 4 == 0 is checked, neither % 100 == 0 nor % 400 == 0 can ever be true below it
A ladder with no final else can fall off the end and print nothing at all — the silent bug again. Every input should produce some output
ValueError — int("abc") when the user types text instead of a number

Exercise 06 — largest of three

Each branch asks one question about one candidate: a >= b and a >= c — "is a at least as big as both others?" A chain like a >= b and b >= c instead describes the ordering of b and c, and misses every case where a is largest but b < c
and joins two conditions that must both be true
>= instead of > handles ties: with plain >, the input (5, 5, 3) fell through to the else branch and announced that 3 was the largest
The last else needs no condition: if neither a nor b is the largest, it has to be c
Test shapes, not just values. (12,45,7), (45,12,7) and (7,12,45) all hid the same bug, because in each of them the stray conditions happened to hold. The missing shape was "a is the largest, but b < c"

Exercise 07 — multiplication table (first loop)

for i in range(1, 11): — run the body once for every number in the range
range(a, b) excludes b: range(1, 11) counts 1…10. This off-by-one is one of the most common mistakes in programming
The loop variable is a box that gets a new value every round — never reuse a name that already holds something you still need. i first held the user's number; the loop overwrote it and the number was gone (the output was just 1…10)
The loop body is indented, exactly like an if body. A line at the outer indentation runs only once, not once per round
f-strings can hold a whole calculation, not just a variable: f"{number} x {i} = {number * i}"
int() here, because the sample output shows 7, not 7.0
A stray character can hide inside a name: دnumber is legal Python (Unicode letters are allowed in identifiers), so it runs fine while looking like a typo — it only bites later, when you type the name differently somewhere else

Exercise 08 — average of N numbers (first accumulator)

The accumulator pattern: an empty box before the loop, add to it inside, use the result after the loop
Zero, because it is the identity for addition (0 + x = x). A product would start at 1
The box must be before the loop: put it inside and it is reset every round — the total ends up holding only the last number, with no error at all (a silent bug)
The box also has to exist first, because total = total + x reads the old value before writing the new one. Without total = 0 the first round is a NameError
input() inside the loop is the whole point of the loop: one line, asked n times
int() for the count ("how many"), float() for the values (quantities)
The counter and the reading need two names: i is the round number, x holds the number
An if alone does not stop a program — it only chooses. To guard n == 0 the whole computation has to sit in the else of the guard
ZeroDivisionError — what n = 0 hits on total / n
round(average, 2) keeps the output readable: 2.33 instead of 2.3333333333333335
First-round trick (the challenge): for a maximum or minimum there is no neutral starting value — largest = 0 breaks on negative numbers. So round one is special: if i == 1: seeds both boxes with the first number, and the comparisons start at round two

Exercise 09 — guess the number (first while)

while repeats until a condition turns false; for repeats a known number of times
Python checks the condition before every round: true → run the body, then check again; false → leave the loop
Nothing that should stay fixed may be created inside the loop: with secret = random.randint(...) in the body, every round gets a new secret and the game is unwinnable — and there is no error message, only an unwinnable game
import random belongs at the top of the file, once
random.randint(1, 100) includes both ends — unlike range
while True: + break needs no fake starting value. The alternative condition while guess != secret: does need guess = 0 before the loop, because the condition is checked before the first round
Something inside the loop must move the condition towards false, otherwise: infinite loop
Binary search: guess the middle and every wrong guess throws away half of what is left. 100 numbers need at most 7 guesses (log2 100 ≈ 6.6), against 50 on average for 1, 2, 3, 4…

Exercise 10 — reverse a string (Stage 4 begins)

A string is a sequence: index from 0, and negative indices count from the end (word[0], word[5], word[-1]), with len(word) for the length
IndexError: string index out of range — asking for a character that is not there
for char in word: walks the characters directly — no range, no counter needed
A text accumulator starts as the empty string "", not 0 (0 + "a" is a TypeError)
Order matters here, unlike addition: result = char + result prepends (reverses), while result = result + char appends (the string comes back unchanged)
An indented print inside the loop fires once per round — a great debug window, but the final answer wants one line after the loop
len is a function: len(word). Square brackets are for indexing (word[0]), so len[word] gives TypeError: 'builtin_function_or_method' object is not subscriptable
A line whose result is neither printed nor stored is dead code — len(word) alone does nothing
The challenge: split() turns a sentence into a list of words, a nested loop reverses each word, parts.append(rev) collects them, " ".join(parts) glues them back

Exercise 11 — palindrome checker (two ways)

A palindrome compares equal to its own reverse: build the reverse and use == on strings
== on strings compares character by character, so case matters: "L" != "l". .lower() normalises before comparing — keep the original for display, compare the cleaned one
str.lower() / .upper() are methods: attached to the string with a dot, unlike len(word) which is a function taking the string as an argument
The two-pointer method needs no second string: left starts at 0, right at len(word) - 1, compare, then move both inward (left + 1, right - 1) until they meet
right counts down. Writing right = right + 1 walks off the end of the string → IndexError: string index out of range
A flag (is_palindrome = True) can hold a boolean and be set to False inside the loop
Two pointers stop at the first mismatch (1 step for hello), while the reverse method always does the whole word (5 steps) — faster, but the reverse method reads more simply
A guard for the empty input (if word == "":) keeps the program from announcing that "nothing" is a palindrome
Testing only non-palindromes hid a real bug: with hello the mismatch broke out before the broken line ever ran. Palindrome shapes were the missing test

Exercise 12 — count the words (Stage 4 complete)

split() returns a list of words and len(list) says how many — counting a sentence is two calls
Counting by hand is the same counter as before: count = 0 before the loop, count + 1 inside. len is simply that loop, already written for you
len counts items: len(sentence) is characters, len(sentence.split()) is words
split() with no argument collapses runs of whitespace, so "I  am" still gives two words — and "   ".split() gives [], i.e. zero words
A line whose result is neither printed nor stored is dead code (len(sentence) alone). This appeared a second time — the same mistake as len(word) in exercise 10. Worth watching for
Naming: after split() the variable holds a list of words, not a sentence. words says what it is
Singular/plural again: 1 word but 4 words, and 0 words takes the plural
An empty sentence gets its own message instead of "0 words" — the guard pattern, once more
The three challenges in one pass: longest word with longest = "" (length 0 is the neutral starting value for a length comparison, and it is safe when the list is empty), the letter count with letters = letters + len(word), and the average after the loop. Inside the loop the division ran every round and the intermediate values were meaningless (0.75, 2.0, 3.25)

Exercise 13 — max without max() (Stage 5 begins)

A list holds many values under one name: numbers = [], then numbers.append(x) per item
Indexing works just like strings: numbers[0], numbers[-1], len(numbers); a loop with for num in numbers: walks the items
Current-champion algorithm: start with largest = numbers[0], then if num > largest: largest = num for the rest
Start from numbers[0], never 0 — with negative numbers 0 would win while not even being in the list (-5, -1, -3 → the answer is -1)
Comparing a number against the list is a TypeError: '>' not supported between instances of 'float' and 'list'. The comparison is always against largest
Two passes are normal: first collect, then analyse. Keeping the list lets you get max, min, sum and average afterwards; a running max inside the reading loop throws that ability away
Re-prompt loop: while True: + continue while the input is invalid + break when it is good. A plain if cannot guard code that crashes inside the same expression — int(input()) dies before any check on the next line
int('') → ValueError: invalid literal for int() with base 10: ''
answer.isdigit() (with not) filters non-numeric text before the conversion, so abc never reaches int()
Once the loop guarantees a valid n, the guards after it disappear: validation moved from "check afterwards" to "only let good data in"
Where we stopped

Day 4, third session — 2026-10-19, afternoon. Exercises 01–13 are done. Stage 5 (lists and dicts) is under way. Next session starts here:

 14_unique.py — remove duplicates from a list while keeping the original order. Pairs nicely with the list work from 13 and introduces membership testing (in, not in).
Then 15_frequency.py — count how many times each word appears (the first dict).

Resolved: 11_palindrome.py now has one active version (the second, two-pointer version); the other is kept commented out on purpose.

Tools already learned: input, print, f-strings, int/float, round, len, if / elif / else, and / or, comparison operators, for + range, while + break, \n, % (modulo), isdigit, import random + random.randint, string indexing, iteration, .lower() / .strip() / .split(), slicing, append / join, two pointers, flags, and the accumulator and counter patterns.

Exercise 14 — unique (remove duplicates, keep the order)

in / not in ask a yes/no question about membership and return True / False. On a list they compare whole items; on a string they look for a piece of text: "app" in fruits is False, "app" in "apple" is True
A list accumulator starts as [] (like 0 for sums and "" for text). It goes before the loop — inside, it is emptied every round, with no error
Unique-list algorithm: if n not in unique: unique.append(n). The question is about unique, never about the original list — the original always contains the item, so nothing would ever be added
append changes the list in place and returns None: unique = unique.append(n) replaces the list with None and crashes next round with AttributeError
isdigit() asks "are all characters digits?" ("" is False). "-5" and "3.5" fail it, because - and . are not digits — it accepts only non-negative whole numbers
A check needs an if: number.isdigit() , numbers.append(...) with a comma is two separate actions — the result of the check is thrown away (dead code again, as in exercises 10 and 12) and append always runs. The check must also use the loop variable (item), not a name that does not exist (NameError)
int() changes equality: "01", "1" and "001" are three different strings but all become 1 — converting first and removing duplicates after gives a different answer from the other order
input() has to be inside while True: — outside, the variable never changes and the same result repeats forever (infinite loop; Ctrl+C stops it). A guard that ends in break needs no else after it
Two valid ways to handle a bad item: skip it with a message that shows the real item (f"skipping: {item}", not fixed text), or stop everything with a flag. A flag is only needed for the second, and a flag line at the same indentation as the if runs for every item
Compute once, then use the name: removed = len(numbers) - len(unique) and if removed == 1: — not the same subtraction repeated in every condition. It comes after the loop that builds unique, and uses numbers, not raw: skipped invalid items are not removed duplicates
Singular/plural once more, with three cases: 0 gets its own message ("No duplicates"), 1 is singular, 2 or more is plural
The test shapes that mattered: 1 2 x 2 (a bad item between good ones), -5 3 and 3.5 2 (the limits of isdigit), and an empty line
Style: 4 spaces per indent level, spaces around ==; Shift+Alt+F formats the file in VS Code

Exercise 15 — word frequency (first dict)

A dict maps keys to values: counts = {}, counts["apple"] = 1, read with counts["apple"]. A missing key is KeyError: 'cherry', like IndexError for lists. in checks the keys: "cherry" in counts
Updating is the accumulator pattern with a key: counts[word] = counts[word] + 1 reads the old value and writes the new one
Counting algorithm: if word in counts: add 1, else: first sighting, counts[word] = 1. The first-time value is a number — the count so far — not the word (= word, later "the" + 1 is a TypeError) and not the dict itself (= counts, later dict + 1 is a TypeError). When unsure, trace the cat the by hand instead of guessing
for word in counts: walks the keys; counts[word] is the value. Keys come in the order of first appearance
A loop takes its items from whatever comes after in: for word in counts: over an empty dict runs zero rounds, so word never exists (NameError). Counting loops over the list words; printing loops over the dict counts. A print outside every loop runs once and shows only the last word
A line ending in : needs an indented body (IndentationError, before even one line runs), and else must line up exactly with its if
split(x) and strip(x) are different tools: split(".,!?") cuts only where that whole 5-character text appears (almost never); strip(".,!?") removes any of those characters from the start and end of one word and leaves the middle alone (don't). strip works on a single word, after split()
"".split(",") is [''], not []. Only split() with no argument gives an empty list for empty text — the guard len(words) == 0 relies on it
word.strip(...) returns a new string — it has to be stored (word = word.strip(...)) or it is thrown away
Clean the data once, at the start, before the keys are built: .lower() before .split() (.lower() is a string method, so .split().lower() is an AttributeError) and strip inside the counting loop, before the if. Cleaning only inside the print changes the display and not the counts: Hello, hello!! still made two keys. To show the original case, keep the original text (exercise 11)
The test that exposed it was a word repeated with different punctuation; the cat, the dog! passed even with the bug. Test shapes, not just values
Champion with a dict: best_word = "", best_count = 0, if counts[word] > best_count: then update both. 0 is a safe start because every count is at least 1 (in exercise 13 numbers could be negative). The champion needs its own name — word is overwritten every round (exercise 7). > keeps the first word on a tie, >= the last
Where a variable is created depends on which loop it must survive: counts = {} before the for loop (survives its rounds) but inside while True: (fresh for every sentence); input inside while True: (it must repeat)
Edge case: !!! strips to "", an empty key. if word == "": continue skips it

Exercise 16 — phone book (dict: add and look up)

{} is an empty dict, [] an empty list. An empty set is set(), because {} alone is always a dict
Adding and updating share one line: contacts[name] = number adds a new key, or replaces the value if the key already exists — a repeated name silently overwrites the old number
Assignment replaces, it never adds: contacts_lists = name followed by contacts_lists = number leaves only the number. A dict grows only through d[key] = value
The dict is created before the loop (contacts = {}). contacts_lists = [] inside while True: was emptied every round, with no error (exercise 8 again)
input(...).split() returns a list, not a string — the prompt even printed ['ali']:. Cleaning one name is .strip().lower()
The stop check comes right after the first input: asking for the number first means Enter on the name still asks for a number before the program stops
for name, number in contacts.items(): — .items() gives (key, value) pairs and unpacking splits each pair into two names. for name, number in contacts_name: over a list of strings is a ValueError, because a string cannot be unpacked into two names
if search in contacts: checks the keys; contacts[search] reads the value. Reading a missing key is KeyError: 'reza', so the in check comes first. The other case is a plain else, not elif not ...
An empty dict counts as False: if not contacts: catches Enter on the very first prompt — continue after the message, and break once at least one contact exists
A message is not a stop: print("No number entered") without continue still runs the next line, and the contact is saved with an empty number — a silent bug (exercise 4 again). .strip() makes a line of spaces count as empty
Re-asking until the input is valid: while not number: with the same input once before the loop and once inside it, or while True: + break. The same pattern validates y/n: while add not in ("y", "n"):
continue goes back to the start of the nearest enclosing loop. For an invalid y/n that was the search loop, so the program asked "Who are you searching for?" again instead of repeating the add question. To repeat one question, give it its own small loop; a break after that loop still leaves the outer one
The search stage needs its own loop: leftover name and number from the adding loop hold only the last contact, not what the user is looking for now
A program with two jobs becomes two loops: stage one adds contacts, stage two searches. The contacts live only while the program runs — saving them to a file is Stage 7
The tests that mattered: Enter on the very first prompt, a name with no number, Ali and ali (one key after cleaning), a missing name followed by y, n and something else (x), and an empty number after y
Style: 4 spaces per indent level everywhere (8 spaces inside one branch ran, but looked like a different block), a typo check on the messages (again, haven't added), and one name per job (name was reused by a later loop)
Where we stopped

2026-11-07. Exercises 01–16 are done. Stage 5 (lists and dicts) is under way. Next:

17 — the dict method .get() (turns the if/else counter from 15 into one line, and is the safe alternative to KeyError when reading a key that may be missing).

New tools: d[key] = value (add or replace), .items() with unpacking, in on dict keys, if not contacts: for an empty dict, while x not in (...) for validation, set().

Exercise 17 — .get() (one-line counter and safe lookup)

d.get(key) reads a value like d[key], but a missing key gives None instead of KeyError. d.get(key, default) gives the default instead of None. ages["reza"] crashes, ages.get("reza") prints None, ages.get("reza", 0) prints 0
.get takes two separate pieces, the key and then the default, split by a comma and both outside any quotes. .get("reza, 0") is ONE text — a 7-character key that is not in the dict — so it printed None instead of 0, with no error
A key alone is not a default: counts.get(0) looks for a key named 0 and gives None. The key comes first, the default second
A line whose result is neither printed nor stored is dead code: counts.get("the", 0) on its own shows nothing (the same mistake as in exercises 10, 12 and 14)
Quotes decide what is looked up: .get("the", 0) always looks up the literal text the, so every search showed the count of the. .get(word, 0) looks up whatever is inside the variable. Only a test with a word that is not there (bird) exposed it
Reusing the same kind of quote inside an f-string (f"{counts.get("the", 0)}") only works on Python 3.12+. With a variable and no quotes the problem does not exist
The one-line counter: counts[word] = counts.get(word, 0) + 1. .get gives "the count so far" (0 for a new word, the real count otherwise) and + 1 stores the new count. The four lines of if word in counts / else from exercise 15 become one
[] reads, .get reads safely: counts[word.strip()] on an empty dict is a KeyError. Cleaning is word = word.strip(...), stored, on its own line before the counting line
.strip() with empty () removes only whitespace; the punctuation has to go inside, as one text
Same mistake as in exercise 15: split(",.!/?:") cuts only where that whole text appears, so "The cat, the dog!" stayed ONE word (the cat, the dog: 1). split() with no argument, then strip(...) on each word
Which one to use: counts[word] when the key is certain (the printing loop — the keys come from counts itself), counts.get(word, 0) when it may be missing (the counting line and the search)
Clean the search the same way as the data (.lower().strip(...)): "hello?" finds hello. Use the same characters in both strips, or the lookup misses

The empty check

The guard has to look at the result of the cleaning, not at the raw input. if not words: passed for !!!, because split() gave ['!!!'], a full list. The word only becomes empty after strip, inside the loop. Nothing was counted, nothing was printed, and the program still asked "Which word?" (a silent bug, exercise 4 again)
The check goes after the counting loop and tests counts: if not counts:. One test catches !!!, an empty line and a line of spaces. With no words the loop runs zero rounds and counts stays {}
Moving code means deleting the old copy. The counting loop was copied above the if, but the old one stayed inside the else, so every word was counted twice (the: 4, cat: 2, dog: 2) — no error, only doubled numbers (a silent bug, exercise 8 again)
while True: with a break only in the empty branch asked the questions again and again (an infinite loop). One sentence and one question need no loop
if word: counting does the same as if not word: continue, in fewer lines

Challenge — count the letters of one word

for letter in word: walks the characters (exercise 10); the counting line is the same one-liner with letter as the key. Its own dict gets its own name, letters, not counts
A line that is never used is noise: counts = {} was created and never touched
if letter: inside a loop over characters is always true, because a character is never empty. The question "was anything counted?" belongs to the result, after the loop: if not letters:
A print inside the counting loop shows running totals (b: 1, a: 1, n: 1, a: 2, n: 2, a: 3), not the final counts. The final answer wants its own loop after counting (exercise 10). An empty check inside the loop never runs either: an empty word means zero rounds, so no message and no error. Counting and printing are two jobs, so two loops, with the check between them
isdigit() asks "is this a digit?". Used with continue it skipped the digits and left spaces and commas in. isalpha() asks "is this a letter?": if letter.isalpha(): counts only letters, so "ban ana", "a,b,a" and "a1b2a" all come out clean. strip only trims the two ends of a text, never the middle
The test shapes that mattered: !!! (a full list before cleaning, an empty dict after), The cat, the dog! (showed the doubled count), a word that is not there (bird, exposed .get("the", 0)), an empty line and a line of spaces, Hello, hello!! HELLO (one key, hello: 3), banana and Banana, ban ana, a,b,a and a1b2a
Style: 8 spaces inside one branch again (it ran, but looked like a different block). Shift+Alt+F formats the file in VS Code

Where we stopped

2026-11-09. Exercises 01–17 are done, challenge included. Stage 5 (lists and dicts) is under way. Next:

18 — not chosen yet. The track list at the top still has the original names for 16–18 (16 became the phone book, 17 became .get()), so the first step next session is to decide: continue with Stage 6 (functions) from 18_calculator.py, or one more dict exercise first.

New tools: d.get(key) and d.get(key, default), the one-line counter counts[word] = counts.get(word, 0) + 1, the empty check on the result after the loop (if not counts:), str.isalpha(), for letter in word: to count characters.

Exercise 18 — menu-driven calculator (Stage 6 begins: functions)

def add(a, b): defines a function. The indented body does nothing until the function is called: result = add(2, 3). Defining and calling are two different steps
Parameters (a, b) are names that receive the values passed in the call. They are the function's own boxes: the a and b inside the function are separate from any a and b in the main program
return hands a value back so it can be stored (result = add(a, b)); print only shows it and returns nothing. A function that prints cannot be reused for anything else, so the calculation functions only calculate, and input / print stay in the main program
Definitions go once at the top of the file, outside the loop. Defined inside the while loop or inside an if branch they are rebuilt every round: it runs, but it is the wrong place
A guard in the caller is not a safe function: the zero check in the main program protects that one call, while divide(5, 0) on its own still crashes with ZeroDivisionError. The guard belongs inside the function: if b == 0: return None
None means "no value". The caller asks if result is None: (error message) else: (the equation). Use is None, not == 0 — 0 is a valid answer (divide(0, 5))
A check that can never fail is dead code: if result is not None: was always true while divide never returned None (the same family as the dead branches in exercise 5)
elif choice == "5": after if choice == "5": break can never run, and anything written after a break in the same block is skipped. The goodbye message goes before the break
A forgotten result = add(a, b) is a silent bug: print shows the result of the previous round, and on the very first round a NameError. Test 3 and then 1
IndentationError: an indent that matches no outer level (an 8 under a 12 under a 4) stops the whole file before any line runs, so even the menu never appears. 4 spaces per level; Shift+Alt+F formats the file
Typing a name like choice or name in VS Code can add a stray import at the top (from secrets import choice, from unicodedata import name). Esc closes the suggestion list; delete the line
The test shapes that mattered: 3 then 1, a zero divisor from the menu and divide(5, 0) called directly, 5 as the very first choice, 7 and abc, negative numbers, decimals

Challenge — ask_number(prompt)

A parameter can be text: the function receives the question and returns a number. Two float(input(...)) lines became two calls of one function: ask_number("Enter first number: ")
Reading numbers in one place means a later check for abc changes one function, not every call
float() already ignores spaces at both ends, so float(" 3 ") works and .strip() inside is not needed
choice stays text and does not go through ask_number: it is compared with "1" to "5", not calculated with
number1 and number2 say more than a and b. Parentheses in the output keep negatives readable: (-6.0) / (3.0)
A challenge is added on top of the finished version, one change at a time. Rewriting the file dropped the four functions and put the calculations back inline: the program still worked, but the exercise itself went a step back
Final shape: five definitions at the top, then one loop that only calls them. Tests that passed: 3 then 1, a zero divisor from the menu, divide(5, 0) called directly (None), divide(0, 5) (0.0), 5 first, 7, abc, negatives, decimals

Where we stopped

2026-11-09. Exercises 01–18 are done, challenge included. Stage 6 (functions) is under way. The final calculator has five definitions at the top (add, subtract, multiply, divide, ask_number) and a loop that only calls them; divide returns None for b == 0 and is safe on its own. Next:

Decide the next step: the two exercises that were not placed (rewrite an earlier exercise as functions, print primes up to N) or Stage 7 (files: 19_save_load.py). The first one is the natural next move, because it practises the same def / return pattern on code that already exists.

New tools: def, parameters and return, calling a function, return None and is None, a function with a text parameter (ask_number), the exit message before break.

Exercise 18b — the word counter rewritten with functions (refactoring)

Refactoring means the same behaviour with a new structure: one job per function (clean, count_words, most_common), and the main part only asks, calls and prints. Nothing is counted or cleaned outside the functions
Data flows from function to function: clean(text) gives a list, count_words(words) gives a dict, most_common(counts) gives (word, count). The output of one is the input of the next: count_words(clean(sentence))
Everything a function needs comes in through its parameters. A loop over the outer variable sentence inside clean ignored the text that was passed in, so clean("Hello. hello!!") did not test what was written
A function that calls itself by accident never ends: word = clean(word) inside clean gave RecursionError: maximum recursion depth exceeded. Cleaning one word is word.strip(...)
One job per function: counting lines inside clean mixed two jobs. A line like counts[word] = counts = {} .words.append(word) is evaluated on the right first and fails with AttributeError: 'dict' object has no attribute 'words'
The box (words = [], counts = {}) is created INSIDE the function, so every call starts fresh, and return comes after the loop, level with the for
Order of string methods: text.lower().split() — lower() is a string method, so text.split().lower() is AttributeError: 'list' object has no attribute 'lower'. text.strip() where split() belongs makes the loop walk characters, not words. split() already ignores spaces at both ends
Test every function alone before wiring them together. clean(clean(x)) hands a list to a function that expects text
A function that passed its tests is not touched while the next one is written: clean was broken three times by edits made for other reasons
Returning two values: return best_word, best_count, and best_word, best_count = most_common(counts) unpacks them — the same unpacking as for name, number in contacts.items()
Champion start: best_word = None, best_count = 0. An empty dict runs zero rounds and returns (None, 0) with no separate if; > keeps the first word on a tie
The empty check stays on the result: if not counts: catches !!!, an empty line and a line of spaces
Refactoring must keep the behaviour: the first version dropped the Which word? search from exercise 17. A rewrite is checked against the original, feature by feature
The searched word is cleaned the same way as the data (.lower().strip(...)) and read with counts.get(search, 0), so hello?, HELLO and bird (0) all work
The test shapes that mattered: !!!, an empty line, a line of spaces, Hello, hello!! HELLO, The cat, the dog!, a tie (a b), a single word, and a search for hello?, HELLO, bird, an empty word and !!!
Style: two blank lines between functions (PEP 8); Shift+Alt+F formats the file

Where we stopped

2026-11-09. Exercises 01–18 and 18b are done. Stage 6 (functions) is under way: a menu calculator with five functions, and the word counter split into three functions plus a main part. Next:

Decide between the last unplaced exercise (print primes up to N, where a function like is_prime(n) that answers yes or no is the natural shape) and Stage 7 (files: 19_save_load.py).

New tools: functions that take and return lists and dicts, chaining functions (count_words(clean(sentence))), returning two values and unpacking them, RecursionError, the rule "parameters in, return out", one job per function.
