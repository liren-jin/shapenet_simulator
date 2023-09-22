import rospy
import os
import yaml
import argparse
import subprocess
from path_pattern import get_path
from tqdm import tqdm
import time
import signal


def main():
    args = parse_args()
    scene_num = args.scene_num
    scene_id_list = range(scene_num)
    scene_path = args.scene_path

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

    for i in range(scene_num):
        scene_id = scene_id_list[i]
        scene_id = f"{scene_id:03d}"
        cmd_simulator = (
            f"ign gazebo -r -s headless-rendering {scene_path}/scene{scene_id}.sdf"
        )

        process_simulator = subprocess.Popen("exec " + cmd_simulator, shell=True)
        print("start p1")

        time.sleep(5)
        path_cfg["experiment_id"] = scene_id
        path_generator = get_path(path_cfg)

        print(f"---------- start recording scene{scene_id} ----------\n")
        path_generator.start()
        print(f"---------- finish recording scene{scene_id} ----------\n")

        process_simulator.kill()
        process_simulator.wait()
        # process_simulator.terminate()
        # process_simulator.wait()
        # os.killpg(os.getpgid(process_simulator.pid), signal.SIGTERM)
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
        "--scene_num",
        "-S",
        type=int,
        required=True,
        help="number of scenes used",
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
