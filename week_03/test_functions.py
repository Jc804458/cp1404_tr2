def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32.0

def is_even(number):
    return number % 2 == 0



def main():
    f_degree = (celsius_to_fahrenheit(21))
    print(f"{f_degree:.1f}")
    print(f"{is_even(15)}")
    number = 5
    print(f"{number}^2= {sqaure(number)}")
# start the program:


def sqaure (number):
    """square the number"""
    return number ** 2


main()
