import pytest
from project.py import get_stock_info, get_stock_price, get_stock_history, plot_stock_graph

# Example symbols for testing
symbol = 'AAPL'

def test_get_stock_info():
    info = get_stock_info(symbol)
    assert isinstance(info, dict)
    assert 'symbol' in info

def test_get_stock_price():
    price = get_stock_price(symbol)
    assert isinstance(price, float)
    assert price > 0

def test_get_stock_history():
    history = get_stock_history(symbol)
    assert not history.empty

def test_plot_stock_graph():
    image_stream = plot_stock_graph(symbol)
    assert image_stream