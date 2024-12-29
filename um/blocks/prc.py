from ..bot import get_rows_format_2
from ..wrap import wrap
from ..utils import render
from . import block

url = "http://www.sca.isr.umich.edu/files/tbcpx1px5.csv"


def prices_block(rt):

    path = "/prices"

    @rt(path)
    def get():
        return wrap(*Prices())

    return block(path, "prices", "UM Prices")


def Prices():
    return render(
        url,
        ("Next Year", "Next 5 Years"),
        "Prices",
        "Expected Change in Prices",
        get_rows_format_2,
    )
