import cv2
import os

INPUT_DIR = "outputs"
OUTPUT_DIR = "outputs"

for filename in os.listdir(INPUT_DIR):

    if "_original" not in filename:
        continue

    base = filename.replace("_original.jpg", "")

    original_path = os.path.join(INPUT_DIR, f"{base}_original.jpg")
    recon_path = os.path.join(INPUT_DIR, f"{base}_reconstructed.jpg")

    if not os.path.exists(recon_path):
        continue

    original = cv2.imread(original_path)
    reconstructed = cv2.imread(recon_path)

    diff = cv2.absdiff(original, reconstructed)

    cv2.imwrite(os.path.join(OUTPUT_DIR, f"{base}_diff.jpg"), diff)

print("🔥 Diff generation complete")