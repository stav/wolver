from ..bot import get_rows_format_1
from ..wrap import wrap
from ..utils import render
from . import block

url = "http://www.sca.isr.umich.edu/files/tbcics.csv"


def index_block(rt):

    path = "/index"

    @rt(path)
    def get():
        return wrap(*Index())

    return block(path, "index", "UM Index")


def Index():
    return render(
        url,
        ("Index",),
        "Index",
        "The Index of Consumer Sentiment",
        get_rows_format_1,
    )
