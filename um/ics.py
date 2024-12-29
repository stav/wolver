# ruff: noqa: F405, F403, F811
from fasthtml.common import *

from .bot import get_rows_format_1
from .wrap import wrap
from .utils import render

url = "http://www.sca.isr.umich.edu/files/tbcics.csv"

close_trigger = "document.getElementById('wlv-index').innerHTML = ''; document.getElementById('wlv-index-close').style.display = 'none';"
open_trigger = (
    "document.getElementById('wlv-index-close').style.display = 'inline-block';"
)


def index_block(rt):

    @rt("/index")
    def get():
        return wrap(*Index())

    return (
        Card(
            Div(id="wlv-index"),
            cls="wlv-container",
            header=Div(
                Button(
                    "UM Index",
                    hx_get="/index",
                    hx_target="#wlv-index",
                    hx_trigger="click",
                    onclick=open_trigger,
                ),
                Button(
                    "X",
                    id="wlv-index-close",
                    cls="wlv-close",
                    onclick=close_trigger,
                ),
            ),
        ),
    )


def Index():
    return render(
        url,
        ("Index",),
        "Index",
        "The Index of Consumer Sentiment",
        get_rows_format_1,
    )
