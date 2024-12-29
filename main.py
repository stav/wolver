# ruff: noqa: F405, F403, F811
from fasthtml.common import *
from fh_altair import altair_headers

from blocks import Index, Components, Prices, wrap
from style import styles

app, rt = fast_app(live=True, debug=True, hdrs=[styles, altair_headers])


@rt()
def index():
    return Titled(
        "Michigan Consumer Sentiment Index",
        Card(
            Div(id="wlv-index"),
            cls="wlv-container",
            header=Div(
                Button(
                    "Index",
                    hx_get="/index",
                    hx_target="#wlv-index",
                    onclick="document.querySelector('#wlv-index').style.display = 'block'; document.querySelector('#wlv-close-index').style.display = 'inline-block';",
                ),
                Button(
                    "X",
                    id="wlv-close-index",
                    cls="wlv-close",
                    onclick="document.querySelector('#wlv-index').style.display = 'none'; document.querySelector('#wlv-close-index').style.display = 'none';",
                ),
            ),
        ),
    )


@rt("/index")
def get():
    return wrap(*Index())


serve()
