"""MOve identical images into different folders based on Lighting levels"""
import shutil
import os

# separate images in instance directories base don suffix id
# 0001_GT_SRGB_034.png
# 0001_NOISY_SRGB_034.png
image_instance_path = "/u2/users/piz693/SIDD-small/SRGB/train/Data"
target_instance_path = "/u2/users/piz693/SIDD-small/SRGB/train/separated"
os.makedirs(target_instance_path, exist_ok=True)

instance_dirs =[path for path in os.listdir(image_instance_path) if os.path.isdir(os.path.join(image_instance_path, path))] 


for instance in instance_dirs:
    for root, dirs, files in os.walk(os.path.join(image_instance_path, instance)):
        for filename in files:
            suffix_id = filename.split("_")[-1][:3]
            new_dir = instance + f"_{suffix_id}"
            print(filename, suffix_id, new_dir)
            os.makedirs(os.path.join(target_instance_path, new_dir), exist_ok=True)
            if filename.lower().endswith(f"{suffix_id}.png"):
                # move
                label = "noisy.png" if "NOISY" in filename else "clean.png"
                shutil.copy2(
                    image_instance_path + "/" + instance + "/" + filename, 
                    target_instance_path + "/" + new_dir + "/" + label
                )

"""Visualize crops on original images"""

dim = 256
shape = img.shape
horizontal_patches = shape[1] // dim
vertical_patches = shape[0] // dim
patch_id = 0
print("SHAPE",shape)
print("HORIZONTAL AND VERTICAL PATCH NUMBERS",horizontal_patches, vertical_patches)

figure, ax = plt.subplots()
ax.imshow(img)
#   :                +------------------+
#   :                |                  |
#   :              height               |
#   :                |                  |
#   :               (xy)---- width -----+
for vert_i in range(vertical_patches):
    for hor_i in range(horizontal_patches):
        # print(dim * hor_i, dim * (hor_i+1))
        # print(dim * vert_i, dim * (vert_i+1))
        rect = plt.Rectangle(
        xy=(
            dim * hor_i, 
            dim * vert_i
        ),
        height = dim,
        width=dim,
        fill=False,
        color="black"
        )
        ax.add_patch(rect)