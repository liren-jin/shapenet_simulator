import numpy as np
from .pattern_base import PatternBase
from utils import random_view


class Random(PatternBase):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.num_candidates = cfg["num_candidates"]
        self.view_change = cfg["view_change"]

    def plan_next_view(self):
        view_list = np.empty((self.num_candidates, 2))

        for i in range(self.num_candidates):
            view_list[i] = random_view(
                self.current_pose[:3, 3],
                self.radius,
                self.phi_min,
                min_view_change=0.2,
                max_view_change=self.view_change,
            )

        next_index = np.random.choice(len(view_list))
        next_view = view_list[next_index]
        return next_view
