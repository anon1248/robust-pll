""" Configurations. """

from glob import glob
from typing import Dict, Tuple

# Dataset kind
DATASET_KIND = {
    "rl": 0,
    "mnistlike": 1,
}

# Augmentation type
AUG_TYPE = {
    "rl": 0,
    "instance-dependent": 1,
}

# Data splits
SPLIT_IDX = {
    "train": 0,
    "test": 1,
    "holdout": 2,
}

# Data
SELECTED_DATASETS: Dict[str, Tuple[int, str]] = {
    # Real-world datasets
    "bird-song": (0, "rl"),
    "lost": (1, "rl"),
    "mir-flickr": (2, "rl"),
    "msrc-v2": (3, "rl"),
    "soccer": (4, "rl"),
    "yahoo-news": (5, "rl"),
    # MNIST datasets
    "mnist": (6, "mnistlike"),
    "fmnist": (7, "mnistlike"),
    "kmnist": (8, "mnistlike"),
    "notmnist": (9, "mnistlike"),
}

# All real-world datasets
REAL_WORLD_DATA = list(sorted(
    glob("external/realworld-datasets/*.mat")
))
REAL_WORLD_DATA_LABELS = [
    path.split("/")[-1].split(".")[0] for path in REAL_WORLD_DATA
]
REAL_WORLD_LABEL_TO_PATH = dict(zip(REAL_WORLD_DATA_LABELS, REAL_WORLD_DATA))