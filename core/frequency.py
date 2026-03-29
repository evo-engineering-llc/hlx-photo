import numpy as np
import cv2

def frequency_match_local(original, reconstructed, region, strength=0.25):

    x, y, w, h = region
    result = reconstructed.copy().astype(np.float32)

    mask = np.zeros(original.shape[:2], dtype=np.float32)
    mask[y:y+h, x:x+w] = 1

    mask = cv2.GaussianBlur(mask, (61, 61), 0)
    mask = mask / np.max(mask)
    mask = mask[..., None]

    for c in range(3):

        f_orig = np.fft.fft2(original[:, :, c])
        f_rec = np.fft.fft2(reconstructed[:, :, c])

        mag_orig = np.abs(f_orig)
        mag_rec = np.abs(f_rec)
        phase_rec = np.angle(f_rec)

        mag_new = mag_rec + strength * (mag_orig - mag_rec)

        f_new = mag_new * np.exp(1j * phase_rec)
        channel = np.fft.ifft2(f_new).real

        result[:, :, c] = (
            (1 - mask[:, :, 0]) * result[:, :, c] +
            mask[:, :, 0] * channel
        )

    return np.clip(result, 0, 255).astype(np.uint8)