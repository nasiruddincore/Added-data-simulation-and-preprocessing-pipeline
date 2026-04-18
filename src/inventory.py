import numpy as np
from scipy.stats import norm

def inventory_calc(forecast, on_hand, lead_time):
    z = norm.ppf(0.95)
    mu = sum(forecast[:lead_time])
    sigma = np.std(forecast)
    safety_stock = z * sigma
    rop = mu + safety_stock
    order_qty = max(0, rop - on_hand)

    return {
    "safety_stock": round(float(safety_stock), 2),
    "reorder_point": round(float(rop), 2),
    "order_qty": round(float(order_qty), 2)
}