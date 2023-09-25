import rospy
import os
import yaml
import argparse
import subprocess
from path_pattern import get_path
import time
import glob


def main():
    args = parse_args()
    scene_path = args.scene_path

    print(scene_path)
    scene_file_list = [
        x for x in glob.glob(os.path.join(scene_path, "*")) if x.endswith(".sdf")
    ]
    print(scene_file_list)

    rospy.init_node(args.path_pattern)

    path_cfg_path = os.path.join(
        "src/data_generator", "config", f"{args.path_pattern}.yaml"
    )
    assert os.path.exists(path_cfg_path)
    with open(path_cfg_path, "r") as config_file:
        path_cfg = yaml.safe_load(config_file)
    path_cfg.update(args.__dict__)

    cmd_bridge = ["roslaunch", "simulator", "ros_bridge.launch"]
    process_bridge = subprocess.Popen(cmd_bridge)

    for scene_file in scene_file_list:
        cmd_simulator = f"ign gazebo -r -s headless-rendering {scene_file}"

        process_simulator = subprocess.Popen("exec " + cmd_simulator, shell=True)
        print("start simulator")

        time.sleep(5)
        scene_id = os.path.split(scene_file)[1].rsplit(".", maxsplit=1)[0]
        print(scene_id)
        path_cfg["experiment_id"] = scene_id
        path_generator = get_path(path_cfg)

        print(f"---------- start recording scene{scene_id} ----------\n")
        path_generator.start()
        print(f"---------- finish recording scene{scene_id} ----------\n")

        process_simulator.kill()
        process_simulator.wait()
        time.sleep(5)

    process_bridge.terminate()
    process_bridge.wait()


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

    parser.add_argument(
        "--scene_path",
        type=str,
        required=True,
        help="scene sdf directory path",
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
