from main import fizzbuzz

while True:
    user_input = input("Enter a number: ")
    try:
        num = int(user_input)
        if num <= 0:
            raise ValueError("Number must be greater than 0.")
        if num % 3 != 0 and num % 5 != 0:
            raise ValueError("Number is not a multiple of 3 or 5.")
        print(fizzbuzz(num))
        break
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
