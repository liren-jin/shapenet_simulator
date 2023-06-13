import numpy as np
import os
import trimesh
import argparse
from sdf_template.model_sdf_template import (
    MODEL_SDF_TEMPLATE,
    MODEL_CONFIG_TEMPLATE,
)

AUTHOR = "Liren Jin"
EMAIL = "ljin@uni-bonn.de"


def main():
    args = parse_args()
    root_dir = os.path.join(os.getcwd(), "models")
    category_list = os.listdir(root_dir)
    for category in category_list:
        category_root_dir = os.path.join(root_dir, category)
        model_list = os.listdir(category_root_dir)

        for model in model_list:
            model_root_dir = os.path.join(category_root_dir, model)
            mesh_file_path = os.path.join(
                model_root_dir, "models", "model_normalized.obj"
            )
            mesh = trimesh.load_mesh(mesh_file_path)

            mass = mesh.volume * 1.0  # 1.0 is the default density
            print(mass)
            # center_mass= mesh.center_mass.tolist()
            inertia = mesh.moment_inertia.tolist()
            print(inertia)
            scale = args.model_scale * [1, 1, 1]

            model_property = {
                "category": category,
                "model_name": model,
                "mass": mass,
                "inertia": inertia,
                "scale": scale,
            }
            config_property = {"model_name": model, "author": AUTHOR, "email": EMAIL}

            sdf_string = MODEL_SDF_TEMPLATE.format(**model_property)
            with open(f"{model_root_dir}/model.sdf", "w") as sdf_file:
                sdf_file.write(sdf_string)

            cfg_string = MODEL_CONFIG_TEMPLATE.format(**config_property)
            with open(f"{model_root_dir}/model.config", "w") as cfg_file:
                cfg_file.write(cfg_string)


def parse_args():
    parser = argparse.ArgumentParser()
    # arguments with default values
    parser.add_argument(
        "--model_scale",
        type=int,
        default=1,
        help="scale of the model",
    )
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
