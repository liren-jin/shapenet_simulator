from .uniform import Uniform
from .random import Random
from .coverage import Coverage


def get_path(cfg):
    path_pattern = cfg["path_pattern"]

    if path_pattern == "uniform":
        return Uniform(cfg)
    elif path_pattern == "random":
        return Random(cfg)
    elif path_pattern == "coverage":
        return Coverage(cfg)
