import csv
import requests

from io import StringIO

from fasthtml.common import A, Card, Pre

from blocks.utils import generate_chart


def Components():
    url = "http://www.sca.isr.umich.edu/files/tbciccice.csv"
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

    chart = generate_chart(rows, "Current", "Expected")

    card = Card(
        Pre(rows),
        style="display: none",
        header="Components of the Index of Consumer Sentiment",
        footer=A(url, href=url),
    )

    return "Components", card, chart
