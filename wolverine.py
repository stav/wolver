from fasthtml.common import Titled

from blocks import Index, Components, Prices


def Wolverine():
    title = "Michigan Consumer Sentiment Index"
    return Titled(
        title,
        Index(),
        Components(),
        Prices(),
    )
