Here is the Python function implemented in a markdown style code block:

```python
def noprofit_noloss(sell_price, cost_price):
    """
    Function to check whether the given amount has no profit and no loss
    """
    if sell_price > cost_price:
        return False
    else:
        return True
```

You can use this function to check whether a given amount has no profit and no loss. If the sell price is greater than the cost price, it means there is a profit, so the function will return `False`. If the sell price is less than or equal to the cost price, it means there is no profit or loss, so the function will return `True`.
