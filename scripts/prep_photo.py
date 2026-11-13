"""
Prepare the photo for clean ASCII conversion:
  1. remove the background (rembg) so the subject is isolated
  2. bilateral-smooth away the texture while keeping drawn lines/features sharp
  3. stretch tones so skin lands near bright and hair/lines/shadows stay dark
  4. darken the line work (difference-of-gaussians ridges)
  5. composite onto white and crop square around the subject

Output: source-prepped.png (grayscale), consumed by make_ascii_svg.py.

    python scripts/prep_photo.py <input.jpg/png> [output.png]
"""
import os
import sys

import cv2
import numpy as np
from PIL import Image
from rembg import remove, new_session

HERE = os.path.dirname(os.path.abspath(__file__))
INP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "source-photo.jpg")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "source-prepped.png")

LINE_WEIGHT = 0.6     # how hard drawn lines are pushed toward black

print(f"Loading input photo from: {INP}")
src_img = Image.open(INP)
# If image is very large, downscale slightly for fast and accurate rembg
max_dim = 1600
if max(src_img.size) > max_dim:
    ratio = max_dim / max(src_img.size)
    src_img = src_img.resize((int(src_img.width * ratio), int(src_img.height * ratio)), Image.LANCZOS)

# 1. cut out the subject
print("Removing background with rembg (u2netp)...")
session = new_session("u2netp")
cut = remove(src_img.convert("RGBA"), session=session)
rgb = np.array(cut.convert("RGB"))
alpha = np.array(cut.split()[-1])                 # 0 = background
gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

# 2. smooth texture, keep edges
print("Smoothing skin texture and enhancing edges...")
smooth = gray
for _ in range(3):
    smooth = cv2.bilateralFilter(smooth, 9, 40, 9)

# 3. tone stretch over the subject only
subject_pixels = smooth[alpha > 128]
if len(subject_pixels) > 0:
    lo, hi = np.percentile(subject_pixels, [2, 92])
    tone = np.clip((smooth.astype(np.float32) - lo) / max(1e-5, (hi - lo)), 0, 1)
else:
    tone = smooth.astype(np.float32) / 255.0

# 4. dark-on-light ridges -> darken
fine = cv2.GaussianBlur(smooth, (0, 0), 1.5).astype(np.float32)
coarse = cv2.GaussianBlur(smooth, (0, 0), 6).astype(np.float32)
lines = np.clip((coarse - fine) / 40.0, 0, 1)
out = np.clip(tone - LINE_WEIGHT * lines, 0, 1) * 255

# 5. paste onto white (feathered a hair to avoid a halo), square crop
mask = cv2.GaussianBlur(alpha.astype(np.float32) / 255.0, (0, 0), 1.0)
out = out * mask + 255.0 * (1.0 - mask)

ys, xs = np.where(alpha > 20)
if len(xs) > 0 and len(ys) > 0:
    # Focus primarily on head/upper torso for a portrait look
    head_y_min = ys.min()
    # Calculate a nice portrait crop
    box_w = xs.max() - xs.min()
    box_h = ys.max() - ys.min()
    side = int(max(box_w, min(box_h, box_w * 1.3)) + 60)
    
    cx = (xs.min() + xs.max()) // 2
    # Bias cy towards the upper half (face)
    cy = int(head_y_min + side * 0.45)
    
    canvas = np.full((side, side), 255, np.uint8)
    x0, y0 = cx - side // 2, cy - side // 2
    sx0, sy0 = max(x0, 0), max(y0, 0)
    sx1, sy1 = min(x0 + side, out.shape[1]), min(y0 + side, out.shape[0])
    
    canvas[sy0 - y0:sy1 - y0, sx0 - x0:sx1 - x0] = out[sy0:sy1, sx0:sx1].astype(np.uint8)
    final_img = Image.fromarray(canvas, mode="L")
else:
    final_img = Image.fromarray(out.astype(np.uint8), mode="L")

final_img.save(OUT)
print("wrote", OUT, final_img.size)
