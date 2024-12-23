from standpoint import TexFormatter, omikuji
from standpoint.math import divmod as my_divmod


def test_omikuji() -> None:
    assert isinstance(omikuji(), str)


def test_tex_formatter() -> None:
    formatter = TexFormatter()
    assert "3.14" in formatter.format_data(3.14)


def test_divmod() -> None:
    assert my_divmod(7, 3) == (2, 1)
