# ruff: noqa: F405, F403, F811
from fasthtml.common import *

from .bot import get_rows_format_2
from .wrap import wrap
from .utils import render

url = "http://www.sca.isr.umich.edu/files/tbciccice.csv"

close_trigger = "document.getElementById('wlv-components').innerHTML = ''; document.getElementById('wlv-components-close').style.display = 'none';"
open_trigger = (
    "document.getElementById('wlv-components-close').style.display = 'inline-block';"
)


def components_block(rt):

    @rt("/components")
    def get():
        return wrap(*Components())

    return (
        Card(
            Div(id="wlv-components"),
            cls="wlv-container",
            header=Div(
                Button(
                    "UM Components",
                    hx_get="/components",
                    hx_target="#wlv-components",
                    hx_trigger="click",
                    onclick=open_trigger,
                ),
                Button(
                    "X",
                    id="wlv-components-close",
                    cls="wlv-close",
                    onclick=close_trigger,
                ),
            ),
        ),
    )


def Components():
    return render(
        url,
        ("Current", "Expected"),
        "Components",
        "Components of the Index of Consumer Sentiment",
        get_rows_format_2,
    )
