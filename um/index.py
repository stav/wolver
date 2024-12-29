# ruff: noqa: F405, F403, F811
from fasthtml.common import *

from .bot import get_rows_format_1
from .utils import render, wrap

url = "http://www.sca.isr.umich.edu/files/tbcics.csv"

close_index = "document.getElementById('wlv-index').innerHTML = ''; document.getElementById('wlv-index-close').style.display = 'none';"
open_index = (
    "document.getElementById('wlv-index-close').style.display = 'inline-block';"
)


def index(rt):

    @rt("/index")
    def get():
        return wrap(*Index())

    return (
        Card(
            Div(id="wlv-index"),
            cls="wlv-container",
            header=Div(
                Button(
                    "Index",
                    hx_get="/index",
                    hx_target="#wlv-index",
                    hx_trigger="click",
                    onclick=open_index,
                ),
                Button(
                    "X",
                    id="wlv-index-close",
                    cls="wlv-close",
                    onclick=close_index,
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
