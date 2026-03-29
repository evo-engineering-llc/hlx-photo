import cv2

def restore_color(original, reconstructed):
    orig_lab = cv2.cvtColor(original, cv2.COLOR_BGR2LAB)
    recon_lab = cv2.cvtColor(reconstructed, cv2.COLOR_BGR2LAB)

    recon_lab[:, :, 1] = orig_lab[:, :, 1]
    recon_lab[:, :, 2] = orig_lab[:, :, 2]

    return cv2.cvtColor(recon_lab, cv2.COLOR_LAB2BGR)