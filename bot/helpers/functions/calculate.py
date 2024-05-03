from typing import Union


def calculate_number(number: Union[int, float]) -> str:
    """
    ### calculate_number
    params:
    * number - required to decompose into percentages.
    """
    result = []

    for i in range(5, 100, 5):
        value = number - (number * (i / 100))
        is_last = True if i == 95 else False

        result.append(f'{"└" if is_last else "├"} {i}% — <code>{round(value, 2)}</code> ₽')

    result = '\n'.join(result)

    return f'{number} 💰\n{result}'
