# %%
# =============================================================================
# 1. IMPORT LIBRARIES & SETUP
# =============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
sns.set_style("whitegrid")

print("✅ Libraries loaded")

# %%
# =============================================================================
# 2. LOAD DATASETS (Update filenames if needed)
# =============================================================================
SOCIAL_FILE = "isoc_ci_ac_i__custom_21498829_linear_2_0.csv"
ECOMMERCE_FILE = "isoc_ec_ib20__custom_ecommerce.csv"  # Update with your actual filename

print(f"📁 Loading: {SOCIAL_FILE}")
sm = pd.read_csv(SOCIAL_FILE)

print(f"📁 Loading: {ECOMMERCE_FILE}")
ec = pd.read_csv(ECOMMERCE_FILE)

print(f"\n✅ Loaded: Social Media ({sm.shape}), E-commerce ({ec.shape})")
# %%
