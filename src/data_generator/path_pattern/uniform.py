from .pattern_base import PatternBase
from utils import uniform_sampling
import numpy as np


class Uniform(PatternBase):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.view_list = None

    def get_view_list(self):
        view_list = np.empty((self.budget, 2))

        for i in range(self.budget):
            view_list[i] = uniform_sampling(self.radius, self.phi_min)

        self.view_list = iter(view_list)

    def plan_next_view(self):
        return next(self.view_list)
