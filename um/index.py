from .bot import get_rows_format_1
from .utils import render

url = "http://www.sca.isr.umich.edu/files/tbcics.csv"


def Index():
    return render(
        url,
        ("Index",),
        "Index",
        "The Index of Consumer Sentiment",
        get_rows_format_1,
    )
