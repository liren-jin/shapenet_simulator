import numpy as np
import os
import yaml
import trimesh
import pyrender
import argparse
from template import *
from constants import *

AUTHOR = "Liren Jin"
EMAIL = "ljin@uni-bonn.de"


def main():
    args = parse_args()
    root_dir = os.path.join(os.getcwd(), "models")

    # category_list = [
    #     c for c in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, c))
    # ]
    category_list = CATEGPRY
    print("available categories:", category_list)
    metadata = {}

    for category in category_list:
        category_root_dir = os.path.join(root_dir, category)
        model_list = os.listdir(category_root_dir)
        metadata.update({category: model_list})

        for model in model_list:
            print(f"generating {category}/{model} sdf file")

            model_root_dir = os.path.join(category_root_dir, model)
            mesh_file_path = os.path.join(
                model_root_dir, "models", "model_normalized.obj"
            )
            mesh = trimesh.load(mesh_file_path, force="mesh", process=False)
            collision_mesh = trimesh.convex.convex_hull(mesh)
            collision_mesh = collision_mesh.simplify_quadric_decimation(200)
            _ = collision_mesh.export(f"{model_root_dir}/collision.stl")
            _ = collision_mesh.export(
                f"{model_root_dir}/collision.obj"
            )  # for visualization in meshlab

            mesh = pyrender.Mesh.from_trimesh(collision_mesh)
            bbox_size = mesh.extents
            origin = mesh.centroid
            mass = 100.0  # default mass of all models
            inertia = cal_inertia(bbox_size, mass)
            inertia = np.abs(inertia)

            if args.random_scale:
                scale_factor = np.random.uniform(1, 2)
                scale = scale_factor * np.array([1.0, 1.0, 1.0])
            else:
                scale = args.fix_model_scale * np.array([1.0, 1.0, 1.0])

            if category == "airplane":
                scale = 1.5 * scale

            model_property = {
                "label": LABEL[category],
                "model_name": model,
                "origin": origin,
                "mass": mass,
                "inertia": inertia,
                "bounding_box": bbox_size,
                "scale": scale,
            }
            config_property = {
                "category": category,
                "model_name": model,
                "author": AUTHOR,
                "email": EMAIL,
            }

            if args.simple_collision:
                template = model_sdf_template_simple
            else:
                template = model_sdf_template

            sdf_string = template.format(**model_property)
            with open(f"{model_root_dir}/model.sdf", "w") as sdf_file:
                sdf_file.write(sdf_string)

            cfg_string = model_config_template.format(**config_property)
            with open(f"{model_root_dir}/model.config", "w") as cfg_file:
                cfg_file.write(cfg_string)

    print("----------write metadata file----------")
    with open(f"{root_dir}/metadata.yaml", "w") as metadata_file:
        yaml.dump(metadata, metadata_file)


def cal_inertia(bbox_size, mass):
    inertia = []  # izz, iyy, izz
    k = mass / 12
    inertia.append(k * (bbox_size[1] ** 2 + bbox_size[2] ** 2))
    inertia.append(k * (bbox_size[0] ** 2 + bbox_size[2] ** 2))
    inertia.append(k * (bbox_size[0] ** 2 + bbox_size[1] ** 2))
    return inertia


def parse_args():
    parser = argparse.ArgumentParser()
    # arguments with default values
    parser.add_argument(
        "--fix_model_scale",
        type=float,
        default=0.8,
        help="scale of the model",
    )

    parser.add_argument(
        "--random_scale",
        action="store_true",
        help="use random scale of the model",
    )

    parser.add_argument(
        "--simple_collision",
        action="store_true",
        help="use bbox as collision geometry to speed up simulation",
    )
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
