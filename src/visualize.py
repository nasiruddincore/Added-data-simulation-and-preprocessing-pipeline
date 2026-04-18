import matplotlib.pyplot as plt
import numpy as np

def plot_inventory_full(forecast, rop, safety_stock, on_hand, order_qty):
    days = np.arange(len(forecast))

    plt.figure(figsize=(12,6))

    # Forecast demand
    plt.plot(days, forecast, label="Forecast Demand", marker='x')

    # Current stock line
    plt.axhline(y=on_hand, linestyle='--', label="Current Stock")

    # Reorder point
    plt.axhline(y=rop, linestyle='--', label="Reorder Point (ROP)")

    # Safety stock
    plt.axhline(y=safety_stock, linestyle='--', label="Safety Stock")

    # After order stock level
    new_stock = on_hand + order_qty
    plt.axhline(y=new_stock, linestyle='--', label="Stock After Order")

    # Highlight stockout risk area
    plt.fill_between(days, 0, safety_stock, alpha=0.1, label="Stockout Risk Zone")

    # Highlight overstock zone
    plt.fill_between(days, rop, new_stock, alpha=0.1, label="Overstock Zone")

    plt.title("Inventory Optimization Visualization")
    plt.xlabel("Future Days")
    plt.ylabel("Units")

    plt.legend()
    plt.grid(True)

    # Save image
    plt.savefig("outputs/full_inventory_visualization.png")

    plt.show()