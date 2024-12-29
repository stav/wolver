# ruff: noqa: F405, F403, F811
from fasthtml.common import *

from .bot import get_rows_format_2
from .wrap import wrap
from .utils import render

url = "http://www.sca.isr.umich.edu/files/tbcpx1px5.csv"

close_trigger = "document.getElementById('wlv-prices').innerHTML = ''; document.getElementById('wlv-prices-close').style.display = 'none';"
open_trigger = (
    "document.getElementById('wlv-prices-close').style.display = 'inline-block';"
)


def prices_block(rt):

    @rt("/prices")
    def get():
        return wrap(*Prices())

    return (
        Card(
            Div(id="wlv-prices"),
            cls="wlv-container",
            header=Div(
                Button(
                    "UM Prices",
                    hx_get="/prices",
                    hx_target="#wlv-prices",
                    hx_trigger="click",
                    onclick=open_trigger,
                ),
                Button(
                    "X",
                    id="wlv-prices-close",
                    cls="wlv-close",
                    onclick=close_trigger,
                ),
            ),
        ),
    )


def Prices():
    return render(
        url,
        ("Next Year", "Next 5 Years"),
        "Prices",
        "Expected Change in Prices",
        get_rows_format_2,
    )
