from fasthtml.common import serve, fast_app, Titled
from fh_altair import altair_headers

from blocks import Index, Components, Prices, wrap
from style import styles

app, rt = fast_app(live=True, debug=True, hdrs=[styles, altair_headers])


@rt
def index():
    return Titled(
        "Michigan Consumer Sentiment Index",
        wrap(*Index()),
        wrap(*Components()),
        wrap(*Prices()),
    )


serve()
