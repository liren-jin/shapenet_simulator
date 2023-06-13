import argparse
import yaml
import random
import numpy as np

from sdf_template.obj5_template import SDF_TEMPLATE as sdf_5obj
from sdf_template.obj6_template import SDF_TEMPLATE as sdf_6obj
from sdf_template.obj7_template import SDF_TEMPLATE as sdf_7obj

SDF_TEMPLATE = {5: sdf_5obj, 6: sdf_6obj, 7: sdf_7obj}
CATEGPRY = ["car", "chair", "table", "bed"]
LABEL = {"car": 1, "chair": 2, "table": 3, "bed": 4}


def main():
    args = parse_args()

    with open(args.config_path, "r") as cfg_file:
        scene_cfg = yaml.safe_load(cfg_file)

    scene_property = generate_property(args.obj_num, scene_cfg)
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

    for i in range(num):
        category = random.choice(CATEGPRY)
        category_list.append(category)
        obj_num = cfg[category]
        model_list.append(f"{category}{np.random.randint(obj_num)}")
        label_list.append(LABEL[category])
        x_list.append(np.random.uniform(cfg["min_x"], cfg["max_x"]))
        y_list.append(np.random.uniform(cfg["min_y"], cfg["max_y"]))
        z_list.append(np.random.uniform(cfg["min_z"], cfg["max_z"]))

    scene_property = {
        "category": category_list,
        "model": model_list,
        "label": label_list,
        "x": x_list,
        "y": y_list,
        "z": z_list,
    }
    return scene_property


def parse_args():
    parser = argparse.ArgumentParser()

    # mandatory arguments
    parser.add_argument(
        "--obj_num",
        "-N",
        type=int,
        required=True,
        help="define number of objects in the scene",
    )
    # arguments with default values
    parser.add_argument(
        "--record_path",
        type=str,
        default="records",
        help="output directory path",
    )
    parser.add_argument(
        "--config_path",
        type=str,
        default="scene_cfg.yaml",
        help="scene configuration file",
    )
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
