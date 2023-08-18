import numpy as np
import os
from PIL import Image
import glob

data_rootdir = "records/uniform"


###### hard coded only for this simulator #####
###### for sanity check of the semantic label #####
def check_overlap(image, label, anno_map):
    image = image.reshape(-1, 3)
    label = label.reshape(-1)
    background_mask = label == 0
    bg_pixel = background_mask.sum()

    white_pixel_anno = np.all(anno_map == np.array([255, 255, 255]), axis=-1)
    if white_pixel_anno.sum() != bg_pixel:
        return "wrong"

    background_pixel = image[background_mask]
    white_pixel_img = np.all(background_pixel == np.array([243, 243, 243]), axis=-1)
    white_pixel_num = white_pixel_img.sum()

    if abs(white_pixel_num - bg_pixel) > 50:
        print(white_pixel_num - bg_pixel)
        return "wrong"


if __name__ == "__main__":
    assert os.path.exists(data_rootdir)
    scene_list = [
        c
        for c in os.listdir(data_rootdir)
        if os.path.isdir(os.path.join(data_rootdir, c))
    ]
    scene_path = [os.path.join(data_rootdir, scene) for scene in scene_list]
    for scene in scene_path:
        image_files = []
        anno_files = []
        anno_map_files = []
        image_path = os.path.join(scene, "images")
        anno_path = os.path.join(scene, "semantics")
        scene_images = [
            x
            for x in glob.glob(os.path.join(image_path, "*"))
            if (x.endswith(".jpg") or x.endswith(".png"))
        ]
        scene_images.sort()
        scene_annos = [
            x for x in glob.glob(os.path.join(anno_path, "*")) if (x.endswith("npy"))
        ]
        scene_annos_map = [
            x for x in glob.glob(os.path.join(anno_path, "*")) if (x.endswith("png"))
        ]
        scene_images.sort()
        scene_annos.sort()
        scene_annos_map.sort()

        image_files = scene_images
        anno_files = scene_annos
        anno_map_files = scene_annos_map

        for idx in range(len(image_files)):
            path_to_current_img = image_files[idx]
            img_pil = np.array(Image.open(path_to_current_img))
            path_to_current_anno_map = anno_map_files[idx]
            anno_pil = np.array(Image.open(path_to_current_anno_map))
            path_to_current_anno = anno_files[idx]
            anno = np.load(path_to_current_anno)
            res = check_overlap(img_pil, anno, anno_pil)
            if res == "wrong":
                print(image_files[idx])
                break
