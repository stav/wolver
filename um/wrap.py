from fasthtml.common import Div, On


def wrap(title, card, chart):
    toggle = f"""
        const el = document.querySelector("#{title} article");
        el.style.display = el.style.display === 'none' ? 'block' : 'none';
    """

    return Div(
        card,
        chart,
        On(code=toggle),
        id=title,
    )
