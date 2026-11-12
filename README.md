# ml-workshop-university-texeira
Workshop for EGR 444 - OmegaConf / Hydra - University Texeira

# Run in Google Colab (no install needed)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willpenhall/ml-workshop-university-texeira/blob/main/stock_workshop/workshop_colab.ipynb)

Open the notebook and run the cells in section 0 first (or Runtime → Run all). It installs omegaconf and hydra-core and writes every config file, `engine.py` and `run.py` into Colab, so nothing needs to be uploaded.

`workshop_colab.ipynb` is generated from the repo files. After editing anything in `conf/`, `engine.py`, `run.py` or `workshop.ipynb`, regenerate it from inside `stock_workshop`:
```
python build_colab.py
```

# Open venv
py -3.12 -m venv .venv \
.venv\Scripts\Activate.ps1
# Install omegacongf and hydra-core
python -m pip install omegaconf hydra-core
# Run to check versions
python -c "import omegaconf, hydra; print(omegaconf.__version__, hydra.__version__)"
python -c "import engine; print(len(engine.simulate_prices(100, 0.08, 0.25, 252, 42)))"

# Test Runs
python run.py strategy.fast_window=5 backtest.commission=0.002   # change values\
python run.py market=tsla                                        # swap a whole group option\
python run.py +backtest.note=trial1                              # + adds a key that does not exist\
python run.py strategy.fast_window=50                            # trips the fast < slow check\
python run.py --cfg job                                          # print the config, do not run main()

# Multirun Sweep
python run.py -m market=aapl,msft,tsla # run using three different market.yaml's \
python run.py -m strategy.fast_window=5,10,20 # sweep through three different fast window options \
python run.py -m market=aapl,tsla strategy.fast_window=5,20 # grid sweep through two different parameters 
