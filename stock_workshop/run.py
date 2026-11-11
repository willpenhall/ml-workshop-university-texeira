import hydra
from omegaconf import DictConfig, OmegaConf

from engine import METRICS, run_backtest, simulate_prices


@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))

    # A schema checks types, not relationships between values:
    assert cfg.strategy.fast_window < cfg.strategy.slow_window, \
        "fast_window must be smaller than slow_window"

    m, s, b = cfg.market, cfg.strategy, cfg.backtest
    prices = simulate_prices(m.start_price, m.annual_drift, m.annual_vol, m.days, m.seed)
    curve = run_backtest(prices, s.fast_window, s.slow_window, b.initial_cash, b.commission)

    results = ", ".join(f"{name}={METRICS[name](curve):+.1%}" for name in b.metrics)
    print(f"RESULT {m.ticker} sma {s.fast_window}/{s.slow_window}: {results} | final ${curve[-1]:,.0f}")


if __name__ == "__main__":
    main()