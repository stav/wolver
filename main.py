from fasthtml.common import fast_app, Titled, serve
from fh_altair import altair_headers

import um
from style import styles

app, rt = fast_app(live=True, debug=True, hdrs=[styles, altair_headers])


@rt
def index():
    return (
        Titled(
            "The Mighty Index of Indexes",
            um.index(rt),
        ),
    )


serve()
