from .bot import get_rows_format_2
from .utils import render

url = "http://www.sca.isr.umich.edu/files/tbciccice.csv"


def Components():
    return render(
        url,
        ("Current", "Expected"),
        "Components",
        "Components of the Index of Consumer Sentiment",
        get_rows_format_2,
    )
