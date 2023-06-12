import rospy
import os
import sys

# add src folder as top level import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import yaml
import argparse
from planner import get_planner
from datetime import datetime


def main():
    args = parse_args()
    rospy.init_node(args.planner_type)

    # find planner configuration file
    planner_cfg_path = os.path.join(
        "planning/config", f"{args.planner_type}_planner.yaml"
    )
    assert os.path.exists(planner_cfg_path)
    with open(planner_cfg_path, "r") as config_file:
        planner_cfg = yaml.safe_load(config_file)
    planner_cfg.update(args.__dict__)
    planner_cfg["experiment_id"] = datetime.now().strftime("%d-%m-%Y-%H-%M")
    nbv_planner = get_planner(planner_cfg)

    while not rospy.is_shutdown():
        nbv_planner.start()
        rospy.spin()


def parse_args():
    parser = argparse.ArgumentParser()

    # mandatory arguments
    parser.add_argument(
        "--planner_type", "-P", type=str, required=True, help="planner_type"
    )
    # arguments with default values
    parser.add_argument(
        "--record_path",
        type=str,
        default="records",
        help="output directory path",
    )
    parser.add_argument(
        "--planning_budget",
        "-BG",
        type=int,
        default=20,
        help="maximal measurments for the mission",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cuda",
        help="config file path",
    )
    parser.add_argument(
        "--gpu_id",
        type=str,
        default="0",
        help="gpu to use, space delimited",
    )
    parser.add_argument(
        "--initial_view",
        type=list,
        default=[0, 0],
        help="prefixed initial camera view angle",
    )
    parser.add_argument(
        "--random_initial",
        action="store_true",
        help="use random inital camera pose",
    )
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
