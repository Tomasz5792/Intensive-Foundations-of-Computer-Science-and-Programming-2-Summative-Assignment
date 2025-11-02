#how to do docstring

def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.

    Raises:
        ValueError: If a or b are not integers.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")
    return a + b


print(add_numbers(1,2))

isinstance()

#multi output docstring

from typing import Union

def add_numbers(a: int, b: int, as_string: bool = False) -> Union[int, str]:
    """
    Adds two numbers together and optionally returns the result as a string.

    Args:
        a (int): The first number.
        b (int): The second number.
        as_string (bool): If True, returns the sum as a string. Default is False.

    Returns:
        Union[int, str]: The sum of the two numbers, as an integer or string.

    Raises:
        ValueError: If a or b are not integers.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")
    
    result = a + b
    return str(result) if as_string else result
