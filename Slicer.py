from PIL import Image
import os
from os import listdir

def slice_image(image_path, patch_size, padding, offset):
  """
  Slices an image into patches with specified size, padding, and offset.

  Args:
      image_path: Path to the image file.
      patch_size: Size of each patch (width and height).
      padding: Number of pixels to pad around each patch.
      offset: Number of pixels to offset between patches.

  Returns:
      A list of image patches as PIL Image objects.
  """

  # Open the image
  image = Image.open(image_path)

  # Get image dimensions
  width, height = image.size

  # Calculate the number of patches horizontally and vertically
  num_patches_x = (width + 2 * padding - offset) // (patch_size + offset)
  num_patches_y = (height + 2 * padding - offset) // (patch_size + offset)

  patches = []
  for y in range(num_patches_y):
    for x in range(num_patches_x):
      # Calculate starting coordinates with offset and padding
      start_x = x * (patch_size + offset) - padding
      start_y = y * (patch_size + offset) - padding

      # Ensure coordinates are within image bounds
      end_x = min(start_x + patch_size + 2 * padding, width)
      end_y = min(start_y + patch_size + 2 * padding, height)

      # Extract the patch with padding
      patch = image.crop((start_x, start_y, end_x, end_y))

      patches.append(patch)

  return patches


if not os.path.exists(os.getcwd() + "\\in"):
  os.makedirs(os.getcwd() + "\\in")

if not os.path.exists(os.getcwd() + "\\res"):
  os.makedirs(os.getcwd() + "\\res")

for images in os.listdir(os.getcwd() + "\\in"):
  if (images.endswith(".png")):
    print(os.getcwd() + "\\in\\" + images)
    patches = slice_image("in\\" + images,180,0,0)
    for i, patch in enumerate(patches):
      patch.save(f"res/{images}_{i}.png")
