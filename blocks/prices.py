from fasthtml.common import A, Card, Pre

from .utils import generate_chart
from .bot import get_rows_format_2

url = "http://www.sca.isr.umich.edu/files/tbcpx1px5.csv"


def Prices():
    rows = list(get_rows_format_2(url))

    chart = generate_chart(rows, "Next Year", "Next 5 Years")

    card = Card(
        Pre(rows),
        style="display: none",
        header="Expected Change in Prices",
        footer=A(url, href=url),
    )

    return "Prices", card, chart
