import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim

def mse(a, b):
    return np.mean((a.astype(np.float32) - b.astype(np.float32)) ** 2)

def ssim_score(a, b):
    gray_a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    gray_b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    return ssim(gray_a, gray_b)