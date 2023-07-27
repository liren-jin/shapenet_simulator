import argparse
import yaml
import random
import numpy as np
from sdf_template import *

MIN_NUM = 5
MAX_NUM = 15
# CATEGPRY = ["car", "chair", "table", "mug", "ship", "sofa"]
CATEGPRY = ["car", "chair", "table", "sofa"]
LABEL = {"car": 1, "chair": 2, "table": 3, "mug": 4, "ship": 5, "sofa": 6}


def main():
    args = parse_args()

    with open(args.config_path, "r") as cfg_file:
        scene_cfg = yaml.safe_load(cfg_file)

    with open(args.metadata_path, "r") as metadata_file:
        metadata = yaml.safe_load(metadata_file)

    if args.random_num:
        obj_num = np.random.randint(MIN_NUM, MAX_NUM)
    else:
        obj_num = args.obj_num

    model_setup = include_models(obj_num, scene_cfg, metadata)
    scene_property = {
        "model_setup": model_setup,
        "resolution": scene_cfg["resolution"],
        "fov": scene_cfg["fov"],
        "rgbd_topic": scene_cfg["rgbd_topic"],
        "semantic_topic": scene_cfg["semantic_topic"],
    }
    scene_sdf_string = scene_sdf_template.format(**scene_property)

    with open("new_scene.sdf", "w") as sdf_file:
        sdf_file.write(scene_sdf_string)


def include_models(num, cfg, metadata):
    total_include_string = ""

    for i in range(num):
        category = random.choice(CATEGPRY)
        model = random.choice(metadata[category])
        label = LABEL[category]
        x = np.random.uniform(cfg["min_x"], cfg["max_x"])
        y = np.random.uniform(cfg["min_y"], cfg["max_y"])
        z = np.random.uniform(cfg["min_z"], cfg["max_z"])
        yaw = np.random.uniform(-3.1415, 3.1415)
        model_property = {
            "category": category,
            "model": model,
            "label": label,
            "x": x,
            "y": y,
            "z": z,
            "yaw": yaw,
            "index": i + 1,
        }
        model_include_string = include_template.format(**model_property)
        total_include_string += model_include_string

    return total_include_string


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--obj_num",
        "-N",
        type=int,
        default=5,
        help="define number of objects in the scene",
    )
    parser.add_argument(
        "--record_path",
        type=str,
        default="records",
        help="output directory path",
    )
    parser.add_argument(
        "--config_path",
        type=str,
        default="cfg/scene_cfg.yaml",
        help="scene configuration file",
    )
    parser.add_argument(
        "--metadata_path",
        type=str,
        default="models/metadata.yaml",
        help="metadata file",
    )
    parser.add_argument(
        "--random_num",
        action="store_true",
        help="random number of object in the scene",
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
