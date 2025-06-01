"""
Visualization tools for results
"""
import matplotlib.pyplot as plt

def plot_ndvi_timeseries(dates, values):
    """Create time series plot"""
    plt.figure(figsize=(10,5))
    plt.plot(dates, values)
    plt.title("NDVI Time Series")
    plt.savefig("output/ndvi_plot.png")
