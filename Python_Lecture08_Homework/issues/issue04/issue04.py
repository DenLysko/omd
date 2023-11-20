from typing import List, Tuple
import pytest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError("expected at least 1 arguments, got 0")

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f"{{0:0{len(uniq_categories)}b}}"

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


@pytest.mark.parametrize(
    "coding_array,result",
    [
        (["0", "1", "2"], [("0", [0, 0, 1]), ("1", [0, 1, 0]), ("2", [1, 0, 0])]),
        (
            ["q", "w", "e"],
            [("q", [0, 0, 1]), ("w", [0, 1, 0]), ("e", [1, 0, 0])],
        ),
    ],
)
def test_sigle_character_string(coding_array, result):
    assert fit_transform(coding_array) == result


def test_words():
    assert fit_transform(["word", "second word", "third word", "word"]) == [
        ("word", [0, 0, 1]),
        ("second word", [0, 1, 0]),
        ("third word", [1, 0, 0]),
        ("word", [0, 0, 1]),
    ]


def test_empty_string():
    with pytest.raises(TypeError):
        fit_transform()


if __name__ == "__main__":
    from pprint import pprint

    cities = ["Moscow", "New York", "Moscow", "London"]
    exp_transformed_cities = [
        ("Moscow", [0, 0, 1]),
        ("New York", [0, 1, 0]),
        ("Moscow", [0, 0, 1]),
        ("London", [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    pprint(transformed_cities)
    assert transformed_cities == exp_transformed_cities
