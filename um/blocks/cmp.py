from ..bot import get_rows_format_2
from ..wrap import wrap
from ..utils import render
from . import block


url = "http://www.sca.isr.umich.edu/files/tbciccice.csv"


def components_block(rt):

    path = "/components"

    @rt(path)
    def get():
        return wrap(*Components())

    return block(path, "components", "UM Components")


def Components():
    return render(
        url,
        ("Current", "Expected"),
        "Components",
        "Components of the Index of Consumer Sentiment",
        get_rows_format_2,
    )
