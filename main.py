from fasthtml.common import serve, fast_app
from fh_altair import altair_headers

from wolverine import Wolverine
from style import styles

app, rt = fast_app(live=True, debug=True, hdrs=[styles, altair_headers])


@rt
def index():
    return Wolverine()


serve()
