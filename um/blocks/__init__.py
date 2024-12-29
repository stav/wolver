from fasthtml.common import Button, Card, Div


def block(path, id, title):

    close_trigger = f"document.getElementById('wlv-{id}').innerHTML = ''; document.getElementById('wlv-{id}-close').style.display = 'none';"
    open_trigger = f"document.getElementById('wlv-{id}-close').style.display = 'inline-block';"

    return (

        Card(
            Div(id=f"wlv-{id}"),
            cls="wlv-container",
            header=Div(
                Button(
                    title,
                    hx_get=path,
                    hx_target=f"#wlv-{id}",
                    hx_trigger="click",
                    onclick=open_trigger,
                ),
                Button(
                    "X",
                    id=f"wlv-{id}-close",
                    cls="wlv-close",
                    onclick=close_trigger,
                ),
            ),
        ),
    )
