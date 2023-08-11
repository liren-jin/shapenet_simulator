import argparse
import yaml
from template import *
from constants import *


def main():
    args = parse_args()

    with open(args.config_path, "r") as cfg_file:
        scene_cfg = yaml.safe_load(cfg_file)
    scene_property = {
        "resolution": scene_cfg["resolution"],
        "update_rate": scene_cfg["update_rate"],
        "fov": scene_cfg["fov"],
        "rgbd_topic": scene_cfg["rgbd_topic"],
        "semantic_topic": scene_cfg["semantic_topic"],
        "background_color": scene_cfg["background_color"],
        "ambient_light": scene_cfg["ambient_light"],
    }
    scene_sdf_string = scene_sdf_template.format(**scene_property)

    with open("scene_base.sdf", "w") as sdf_file:
        sdf_file.write(scene_sdf_string)


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--config_path",
        type=str,
        default="cfg/scene_cfg.yaml",
        help="scene configuration file",
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
