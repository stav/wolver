# ruff: noqa: F405, F403, F811
from fasthtml.common import *
from fh_altair import altair_headers

from blocks import Index, Components, Prices, wrap
from style import styles

app, rt = fast_app(live=True, debug=True, hdrs=[styles, altair_headers])

close_index = "document.getElementById('wlv-index').innerHTML = ''; document.getElementById('wlv-index-close').style.display = 'none';"
open_index = (
    "document.getElementById('wlv-index-close').style.display = 'inline-block';"
)


@rt()
def index():
    return (
        Titled(
            "Michigan Consumer Sentiment Index",
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
        ),
    )


@rt("/index")
def get():
    return wrap(*Index())


serve()
