from standpoint import TexFormatter, omikuji


def test_omikuji() -> None:
    assert isinstance(omikuji(), str)


def test_tex_formatter() -> None:
    formatter = TexFormatter()
    assert "3.14" in formatter.format_data(3.14)
