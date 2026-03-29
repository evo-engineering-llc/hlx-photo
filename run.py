import os
import cv2

from core.hlx import hlx_reconstruct
from utils.corrupt import corrupt_center
from utils.metrics import mse, ssim_score

# config
config = {
    "freq_strength": 0.25
}

INPUT_DIR = "examples"
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):

    if not filename.lower().endswith((".jpg", ".png", ".jpeg")):
        continue

    path = os.path.join(INPUT_DIR, filename)

    print(f"\nProcessing: {filename}")

    original = cv2.imread(path)

    if original is None:
        print("❌ Failed to load")
        continue

    corrupted, region = corrupt_center(original)

    reconstructed = hlx_reconstruct(original, corrupted, region, config)

    # metrics
    m = mse(original, reconstructed)
    s = ssim_score(original, reconstructed)

    print(f"✔ MSE: {m:.2f} | SSIM: {s:.4f}")

    # save outputs
    base = filename.split(".")[0]

    cv2.imwrite(os.path.join(OUTPUT_DIR, f"{base}_original.jpg"), original)
    cv2.imwrite(os.path.join(OUTPUT_DIR, f"{base}_corrupted.jpg"), corrupted)
    cv2.imwrite(os.path.join(OUTPUT_DIR, f"{base}_reconstructed.jpg"), reconstructed)

print("\n🔥 DONE")