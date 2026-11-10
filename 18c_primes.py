# If no divisor is found up to the square root, none will be found thereafter either.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_up_to(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


while True:
    text = input("Enter a N (Press enter to exit): ")
    if text == "":
        print("Alright, python had been stopped. goodbye.")
        break

    if not text.isdigit():
        print("Invalid input. Please enter a whole number (0 or more).")
        continue

    number = int(text)
    prime = primes_up_to(number)

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

    if len(prime) == 0:
        print("There are no prime number up to", number)
    elif len(prime) == 1:
        print("Prime number up to", number, "is:")
        print(prime)
    else:
        print("Prime numbers up to", number, "are:")
        print(prime)
