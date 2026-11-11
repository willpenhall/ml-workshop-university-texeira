from dataclasses import dataclass
from omegaconf import OmegaConf

market = OmegaConf.load("conf/market/aapl.yaml")
strategy = OmegaConf.load("conf/strategy/sma_crossover.yaml")
backtest = OmegaConf.load("conf/backtest/default.yaml")

cfg = OmegaConf.create({"market": market, "strategy": strategy, "backtest": backtest})
print(OmegaConf.to_yaml(cfg))
print(cfg.market.ticker, cfg.strategy.fast_window)

override = OmegaConf.from_dotlist(["strategy.fast_window=5", "backtest.commission=0.002"])
cfg = OmegaConf.merge(cfg, override)
print(cfg.strategy.fast_window, cfg.backtest.commission)   # 5 0.002

@dataclass
class StrategyConfig:
    name: str
    fast_window: int
    slow_window: int

schema = OmegaConf.structured(StrategyConfig)
checked = OmegaConf.merge(schema, strategy)                # passes
print(checked.slow_window)                                 # 30

# Break it on purpose, one line at a time (each raises, so run them separately):
OmegaConf.merge(schema, {"fast_window": "quick"})          # ValidationError: not an int
OmegaConf.merge(schema, {"fast_windw": 5})                 # ConfigKeyError: typo caught