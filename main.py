def fizzbuzz(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    if num <= 0:
        raise ValueError("Input must be a positive integer.")
    if num % 3 != 0 and num % 5 != 0:
        raise ValueError("Number must be a multiple of 3 or 5.")

    if num % 3 == 0 and num % 5 != 0:
        return "fizz"
    if num % 5 == 0 and num % 3 != 0:
        return "buzz"
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
