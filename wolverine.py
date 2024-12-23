# ruff: noqa: F405, F403

import csv
import requests
import pandas as pd
import altair as alt

from io import StringIO
from fasthtml.common import *
from fh_altair import altair2fasthtml


def generate_chart(rows):
    months_years = [f"{row[0]} {row[1]}" for row in rows]
    current_values = [float(row[2]) for row in rows]
    expected_values = [float(row[3]) for row in rows]

    pltr = pd.DataFrame({"x": months_years, "y": current_values})
    chart = (
        alt.Chart(pltr)
        .mark_line()
        .encode(y="y", x=alt.X("x", sort=None))
        .properties(width=400, height=200)
    )

    pltr["expected"] = expected_values

    chart += (
        alt.Chart(pltr)
        .mark_line(color="red")
        .encode(y="expected", x=alt.X("x", sort=None))
    )
    return altair2fasthtml(chart)


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
            print(data)

        except (AssertionError, ValueError):
            print("Invalid data:", row)

    chart = Div(generate_chart(rows), cls="wlv-chart")

    card = Card(
        Pre(rows),
        style="display: none",
        header="Components of the Index of Consumer Sentiment",
        footer=A(url, href=url),
    )

    toggle = """
        const el = document.querySelector('#Components article');
        el.style.display = el.style.display === 'none' ? 'block' : 'none';
    """

    return Div(card, chart, On(code=toggle), id="Components"),


def Wolverine():
    title = "Michigan Consumer Sentiment Index"
    return Titled(title), Components()
