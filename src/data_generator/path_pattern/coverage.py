import numpy as np
from scipy.spatial import distance
from .pattern_base import PatternBase
from utils import xyz_to_view, view_to_pose_batch


class Coverage(PatternBase):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.view_list = None

    def get_view_list(self):
        view_list = self.fibonacci_spiral_hemisphere()
        self.view_list = iter(view_list)

    def plan_next_view(self):
        return next(self.view_list)

    # https://github.com/matt77hias/fibpy/blob/master/src/sampling.py
    def fibonacci_spiral_hemisphere(self, mode=0):
        samples_num = self.budget
        n = 2 * samples_num
        rn = range(samples_num, n)

        shift = 1.0 if mode == 0 else n * np.random.random()

        ga = np.pi * (3.0 - np.sqrt(5.0))
        offset = 1.0 / samples_num

        view_samples = np.zeros((samples_num, 2))
        j = 0
        for i in rn:
            phi = ga * ((i + shift) % n)
            cos_phi = np.cos(phi)
            sin_phi = np.sin(phi)
            cos_theta = ((i + 0.5) * offset) - 1.0
            sin_theta = np.sqrt(1.0 - cos_theta * cos_theta)
            xyz = self.radius * np.array(
                [cos_phi * sin_theta, sin_phi * sin_theta, cos_theta]
            )
            view = xyz_to_view(xyz, self.radius)

            if view[0] < self.phi_min:
                view[0] = self.phi_min
            view_samples[j, :] = view

            j += 1
        return view_samples

    def get_camera_view_direction(self, poses):
        view_direction = poses[..., :3, 0]
        view_direction = view_direction / np.linalg.norm(view_direction)
        return view_direction

    def reorder_list(self, view_list):
        pose_list = view_to_pose_batch(view_list, self.radius)
        view_direction = self.get_camera_view_direction(pose_list)

        step = len(view_list)
        view_index_list = range(step)
        visited_index_list = list(np.random.choice(view_index_list, 2))

        for i in range(step - 2):
            remain_index_list = list(set(view_index_list) - set(visited_index_list))
            cos_distance_list = []
            for idx in remain_index_list:
                cos_dist = 0.0
                for image_idx in visited_index_list:
                    cos_dist += distance.cosine(
                        view_direction[idx], view_direction[image_idx]
                    )
                cos_distance_list.append(cos_dist)
            new_ref_index = remain_index_list[np.argmax(cos_distance_list)]
            visited_index_list.append(new_ref_index)

        self.view_list = view_list[visited_index_list]
