from fasthtml.common import A, Card, Pre

from .utils import generate_chart
from .bot import get_rows_format_1

url = "http://www.sca.isr.umich.edu/files/tbcics.csv"


def Index():
    rows = list(get_rows_format_1(url))

    chart = generate_chart(rows, "Index")

    card = Card(
        Pre(rows),
        style="display: none",
        header="The Index of Consumer Sentiment",
        footer=A(url, href=url),
    )

    return "Index", card, chart
