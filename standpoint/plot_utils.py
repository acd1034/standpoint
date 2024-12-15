from matplotlib.ticker import ScalarFormatter


class TexFormatter(ScalarFormatter):
    def __call__(self, x: float, pos: int | None = None) -> str:
        base = super().__call__(x, pos)
        return base.replace(r"\mathdefault", "")

    def get_offset(self) -> str:
        base = super().get_offset()
        return base.replace(r"\mathdefault", "")
