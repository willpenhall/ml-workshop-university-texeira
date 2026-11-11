# ml-workshop-university-texeira
Workshop for EGR 444 - OmegaConf / Hydra - University Texeira

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
