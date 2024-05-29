from PIL import Image
import os
from os import listdir

def slice(image_path, patch_width, patch_height, padding, offset):
  """
  Slices an image into patches with specified size, padding, and offset.

  Args:
      image_path: Path to the image file.
      patch_width: Width of each patch
      patch_height: Height of each patch, if negative then is set to width
      padding: Number of pixels to pad around each patch.
      offset: Number of pixels to offset between patches.

  Returns:
      A list of tuples in the format of (image patche as PIL Image objects, x, y).
  """

  if(patch_height < 0):
    patch_height = patch_width

  # Open the image
  image = Image.open(image_path)

  # Get image dimensions
  width, height = image.size

  # Calculate the number of patches horizontally and vertically
  num_patches_x = (width + 2 * padding - offset) // (patch_width + offset)
  num_patches_y = (height + 2 * padding - offset) // (patch_height + offset)

  patches = []
  for y in range(num_patches_y):
    for x in range(num_patches_x):
      # Calculate starting coordinates with offset and padding
      start_x = x * (patch_width + offset) - padding
      start_y = y * (patch_height + offset) - padding

      # Ensure coordinates are within image bounds
      end_x = min(start_x + patch_width + 2 * padding, width)
      end_y = min(start_y + patch_height + 2 * padding, height)

      # Extract the patch with padding
      patch = image.crop((start_x, start_y, end_x, end_y))

      patches.append((patch,x,y))

  return patches

