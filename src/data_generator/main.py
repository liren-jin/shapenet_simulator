import rospy
import os
import yaml
import argparse
from datetime import datetime
from path_pattern import get_path


def main():
    args = parse_args()
    rospy.init_node(args.path_pattern)

    path_cfg_path = os.path.join("config", f"{args.path_pattern}.yaml")
    assert os.path.exists(path_cfg_path)
    with open(path_cfg_path, "r") as config_file:
        path_cfg = yaml.safe_load(config_file)
    path_cfg.update(args.__dict__)
    path_cfg["experiment_id"] = datetime.now().strftime("%d-%m-%Y-%H-%M")
    path_generator = get_path(path_cfg)

    print("---------- start recording ----------\n")
    path_generator.start()
    print("---------- finish recording ----------\n")


def parse_args():
    parser = argparse.ArgumentParser()

    # mandatory arguments
    parser.add_argument(
        "--path_pattern",
        "-P",
        type=str,
        required=True,
        help="path pattern to record data",
    )
    # arguments with default values
    parser.add_argument(
        "--record_path",
        "-R",
        type=str,
        default="records",
        help="output root directory path",
    )
    parser.add_argument(
        "--budget",
        "-BG",
        type=int,
        default=20,
        help="maximal measurments for the mission",
    )
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
