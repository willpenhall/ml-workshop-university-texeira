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