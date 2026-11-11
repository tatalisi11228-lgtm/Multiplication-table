def sieve(n):
    if n < 2:
        return []

    flags = [True] * (n + 1)
    flags[0] = False
    flags[1] = False

    for i in range(2, int(n**0.5) + 1):
        if flags[i]:
            for j in range(i*i, n + 1, i):
                flags[j] = False

    primes = []
    for i in range(2, n + 1):
        if flags[i]:
            primes.append(i)
    return primes


while True:
    text = input("> Enter a N (Press enter to exit): ")
    if text == "":
        print("Alright, python had been stopped. Goodbye.")
        break
    if not text.isdigit():
        print("Not valid, please enter a number.")
        continue

    number = int(text)
    primes = sieve(number)

    if number in primes:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
    if len(primes) == 0:
        print(f"There are no prime numbers up to {number}.")
    elif len(primes) == 1:
        print(f"Prime number up to {number} is:")
        print(primes)
    else:
        print(f"Prime numbers up to {number} are:")
        print(primes)
