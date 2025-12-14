import random
import numpy as np

def set_seed(seed):
    """Sets all random seeds for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
