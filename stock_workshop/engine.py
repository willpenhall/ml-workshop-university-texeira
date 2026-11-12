"""Tiny backtest engine for the config workshop. Standard library only."""
import math
import random


def simulate_prices(start_price, annual_drift, annual_vol, days, seed):
    """Geometric random walk: one simulated closing price per trading day."""
    rng = random.Random(seed)
    dt = 1 / 252
    prices = [float(start_price)]
    for _ in range(days):
        shock = rng.gauss(0, 1)
        growth = (annual_drift - 0.5 * annual_vol ** 2) * dt + annual_vol * math.sqrt(dt) * shock
        prices.append(prices[-1] * math.exp(growth))
    return prices


def sma(prices, window, i):
    """Simple moving average of the last `window` prices ending at index i."""
    return sum(prices[i - window + 1 : i + 1]) / window


def run_backtest(prices, fast_window, slow_window, initial_cash, commission):
    """Moving-average crossover: all in when fast > slow, all cash when fast < slow."""
    cash = float(initial_cash)
    shares = 0.0
    equity_curve = []
    for i, price in enumerate(prices):
        if i >= slow_window - 1:
            fast = sma(prices, fast_window, i)
            slow = sma(prices, slow_window, i)
            if fast > slow and shares == 0:
                shares = cash * (1 - commission) / price
                cash = 0.0
            elif fast < slow and shares > 0:
                cash = shares * price * (1 - commission)
                shares = 0.0
        equity_curve.append(cash + shares * price)
    return equity_curve


def total_return(equity_curve):
    return equity_curve[-1] / equity_curve[0] - 1


def max_drawdown(equity_curve):
    peak = equity_curve[0]
    worst = 0.0
    for value in equity_curve:
        peak = max(peak, value)
        worst = min(worst, value / peak - 1)
    return worst


METRICS = {"total_return": total_return, "max_drawdown": max_drawdown}