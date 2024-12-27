import csv
import requests

from io import StringIO

from fasthtml.common import A, Card, Pre

from blocks.utils import generate_chart


def Index():
    url = "http://www.sca.isr.umich.edu/files/tbcics.csv"
    response = requests.get(url)
    rows = []

    csv_reader = csv.reader(StringIO(response.text))
    for row in csv_reader:
        try:
            month, year, _, _, index, *_ = row
            assert year.isdigit()
            float(index)
            data = (
                month,
                year,
                f"{float(index):,.1f}",
            )
            rows.append(data)
            print(data)

        except (AssertionError, ValueError):
            print("Invalid data:", row)

    chart = generate_chart(rows, "Index")

    card = Card(
        Pre(rows),
        style="display: none",
        header="The Index of Consumer Sentiment",
        footer=A(url, href=url),
    )

    return "Index", card, chart
