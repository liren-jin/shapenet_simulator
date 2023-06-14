import argparse
import yaml
import random
import numpy as np
from sdf_template import *

MIN_NUM = 5
MAX_NUM = 10
SDF_TEMPLATE = {
    5: sdf_5obj,
    6: sdf_6obj,
    7: sdf_7obj,
    8: sdf_8obj,
    9: sdf_9obj,
    10: sdf_10obj,
}
CATEGPRY = ["car", "chair", "table", "mug"]
LABEL = {"car": 1, "chair": 2, "table": 3, "mug": 4}


def main():
    args = parse_args()

    with open(args.config_path, "r") as cfg_file:
        scene_cfg = yaml.safe_load(cfg_file)

    scene_property = generate_property(args.obj_num, scene_cfg)
    if args.random_num:
        obj_num = np.random.randint(MIN_NUM, MAX_NUM)
    else:
        obj_num = args.obj_num

    sdf_template = SDF_TEMPLATE[args.obj_num]
    sdf_string = sdf_template.format(**scene_property)

    with open("new_scene.sdf", "w") as sdf_file:
        sdf_file.write(sdf_string)


def generate_property(num, cfg):
    category_list = []
    model_list = []
    label_list = []
    x_list = []
    y_list = []
    z_list = []
    yaw_list = []

    for i in range(num):
        category = random.choice(CATEGPRY)
        category_list.append(category)
        obj_num = cfg[category]
        model_list.append(f"{category}{random.choice(range(obj_num))}")
        label_list.append(LABEL[category])
        x_list.append(np.random.uniform(cfg["min_x"], cfg["max_x"]))
        y_list.append(np.random.uniform(cfg["min_y"], cfg["max_y"]))
        z_list.append(np.random.uniform(cfg["min_z"], cfg["max_z"]))
        yaw_list.append(np.random.uniform(-3.1415, 3.1415))

    scene_property = {
        "category": category_list,
        "model": model_list,
        "label": label_list,
        "x": x_list,
        "y": y_list,
        "z": z_list,
        "yaw": yaw_list,
    }
    return scene_property


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
        "--random_num",
        action="store_true",
        help="random number of object in the scene",
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
