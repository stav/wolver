from fasthtml.common import A, Card, Pre

from .utils import generate_chart
from .bot import get_rows_format_2

url = "http://www.sca.isr.umich.edu/files/tbciccice.csv"


def Components():
    rows = list(get_rows_format_2(url))

    chart = generate_chart(rows, "Current", "Expected")

    card = Card(
        Pre(rows),
        style="display: none",
        header="Components of the Index of Consumer Sentiment",
        footer=A(url, href=url),
    )

    return "Components", card, chart
