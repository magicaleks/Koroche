import random
import uuid


def make_uuid() -> str:
    return str(uuid.uuid4())


def make_alias(length: int, only_numbers: bool = False) -> str:
    """Making alias for oneway short link

    * length > 4

    """

    if only_numbers:
        min_lvl = 10 ** (length - 1)
        ret = random.randint(min_lvl, min_lvl * 10 - 1)
        return str(ret)

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    result = ""
    for i in range(length):
        result += random.choice(alphabet)

    return result
