from .bot import get_rows_format_2
from .utils import render

url = "http://www.sca.isr.umich.edu/files/tbcpx1px5.csv"


def Prices():
    return render(
        url,
        ("Next Year", "Next 5 Years"),
        "Prices",
        "Expected Change in Prices",
        get_rows_format_2,
    )
