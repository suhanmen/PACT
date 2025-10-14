"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""



def noprofit_noloss(selling_price, cost_price):
    return selling_price == cost_price

assert noprofit_noloss(1500, 1200) == False
