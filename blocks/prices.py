# ruff: noqa: F405, F403

import csv
import requests

from io import StringIO
from fasthtml.common import *

from blocks.utils import generate_chart


def Prices():
    url = "http://www.sca.isr.umich.edu/files/tbcpx1px5.csv"
    response = requests.get(url)
    rows = []

    csv_reader = csv.reader(StringIO(response.text))
    for row in csv_reader:
        try:
            month, year, _, current, _, expected, *_ = row
            assert year.isdigit()
            float(current)
            float(expected)
            data = (
                month,
                year,
                f"{float(current):,.1f}",
                f"{float(expected):,.1f}",
            )
            rows.append(data)

        except (AssertionError, ValueError):
            print("Invalid data:", row)

    chart = Div(generate_chart(rows, "Next Year", "Next 5 Years"), cls="wlv-chart")

    card = Card(
        Pre(rows),
        style="display: none",
        header="Expected Change in Prices",
        footer=A(url, href=url),
    )

    toggle = """
        const el = document.querySelector('#Prices article');
        el.style.display = el.style.display === 'none' ? 'block' : 'none';
    """

    return Div(card, chart, On(code=toggle), id="Prices", cls="wlv-container")
