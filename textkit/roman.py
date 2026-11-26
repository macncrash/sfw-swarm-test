_NUMERALS = (
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
)


def to_roman(n):
    """Roman numerals for 1..3999; ValueError otherwise."""
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 3999:
        raise ValueError(f"to_roman: need an integer in 1..3999, got {n!r}")
    out = []
    for value, numeral in _NUMERALS:
        count, n = divmod(n, value)
        out.append(numeral * count)
    return ''.join(out)
