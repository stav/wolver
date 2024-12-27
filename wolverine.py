from fasthtml.common import Titled

from blocks import Index, Components, Prices, wrap


def Wolverine():
    title = "Michigan Consumer Sentiment Index"
    return Titled(
        title,
        wrap(*Index()),
        wrap(*Components()),
        wrap(*Prices()),
    )
