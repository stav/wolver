import pandas as pd
import altair as alt

from fh_altair import altair2fasthtml


def generate_chart(rows, y1, y2=None):
    months_years = [f"{row[0]} {row[1]}" for row in rows]
    y1_values = [float(row[2]) for row in rows]

    data = pd.DataFrame({"x": months_years})

    data[y1] = y1_values
    chart = (
        alt.Chart(data)
        .mark_line()
        .encode(y=y1, x=alt.X("x", sort=None, title="Month"))
        .properties(width=400, height=200)
    )

    if y2:
        y2_values = [float(row[3]) for row in rows]
        data[y2] = y2_values
        chart += (
            alt.Chart(data).mark_line(color="red").encode(y=y2, x=alt.X("x", sort=None))
        )

    return altair2fasthtml(chart)
