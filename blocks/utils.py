import pandas as pd
import altair as alt

from fh_altair import altair2fasthtml


def generate_chart(rows, y1, y2):
    months_years = [f"{row[0]} {row[1]}" for row in rows]
    current_values = [float(row[2]) for row in rows]
    expected_values = [float(row[3]) for row in rows]

    pltr = pd.DataFrame({"x": months_years})

    pltr[y1] = current_values
    chart = (
        alt.Chart(pltr)
        .mark_line()
        .encode(y=y1, x=alt.X("x", sort=None))
        .properties(width=400, height=200)
    )

    pltr[y2] = expected_values
    chart += (
        alt.Chart(pltr).mark_line(color="red").encode(y=y2, x=alt.X("x", sort=None))
    )
    return altair2fasthtml(chart)
