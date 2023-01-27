import pytest

from src.convert import convert_string


def test_check():
    assert convert_string('1', '2', '3', '4',) == str(1, 2, 3, 4)


if __name__ == '__main__':
    pytest.main()
