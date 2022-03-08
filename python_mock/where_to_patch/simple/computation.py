from python_mock.where_to_patch.simple.magic_number import get_magic_number


def compute(n: int) -> int:
    magic_number = get_magic_number()
    return magic_number + n
