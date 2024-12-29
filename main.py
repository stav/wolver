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
                        Div(
                            "Index",
                            hx_get="/first-endpoint",
                            hx_target="#first-target",
                            hx_trigger="click",
                        ),
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
                    # Button("Click me", id="multi-action-button"),
                    Div(id="first-target"),
                    # Div(id="second-target"),
                ),
            ),
            # Script(
            #     """
            #     console.log('index', htmx);
            #     document.getElementById('multi-action-button').addEventListener('click', function() {
            #     htmx.ajax('GET', '/first-endpoint', { target: '#first-target' });
            #     htmx.ajax('GET', '/second-endpoint', { target: '#second-target' });
            # });
            #     """
            # ),
        ),
    )


@rt("/index")
def get():
    return wrap(*Index())


@rt("/first-endpoint")
def get():
    return Div("First endpoint")


@rt("/second-endpoint")
def get():
    return Div("Second endpoint")


serve()
