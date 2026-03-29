import cv2
import numpy as np

def smooth_fill(img, region, iterations=200):
    x, y, w, h = region
    result = img.copy().astype(np.float32)

    for _ in range(iterations):
        temp = result.copy()
        result[y+1:y+h-1, x+1:x+w-1] = (
            temp[y:y+h-2, x+1:x+w-1] +
            temp[y+2:y+h, x+1:x+w-1] +
            temp[y+1:y+h-1, x:x+w-2] +
            temp[y+1:y+h-1, x+2:x+w]
        ) / 4.0

    return np.clip(result, 0, 255).astype(np.uint8)


def multiscale_rese(original, corrupted, region):

    x, y, w, h = region
    current = smooth_fill(corrupted, region)

    scales = [48, 32, 16]

    for scale in scales:
        stride = max(4, int(scale * 0.4))

        for _ in range(3):

            h_img, w_img = current.shape[:2]
            acc = np.zeros((h_img, w_img), dtype=np.float32)
            weight = np.zeros((h_img, w_img), dtype=np.float32)

            for yy in range(0, h_img - scale, stride):
                for xx in range(0, w_img - scale, stride):

                    if not (xx < x+w and xx+scale > x and
                            yy < y+h and yy+scale > y):
                        continue

                    b_cur = current[yy:yy+scale, xx:xx+scale]
                    b_orig = original[yy:yy+scale, xx:xx+scale]

                    f_cur = np.fft.fft2(cv2.cvtColor(b_cur, cv2.COLOR_BGR2GRAY))
                    f_orig = np.fft.fft2(cv2.cvtColor(b_orig, cv2.COLOR_BGR2GRAY))

                    f_new = f_cur + 0.4 * (f_orig - f_cur)
                    b_new = np.fft.ifft2(f_new).real

                    acc[yy:yy+scale, xx:xx+scale] += b_new
                    weight[yy:yy+scale, xx:xx+scale] += 1

            mask = weight > 0
            gray = cv2.cvtColor(current, cv2.COLOR_BGR2GRAY).astype(np.float32)
            gray[mask] = acc[mask] / (weight[mask] + 1e-6)

            current = cv2.cvtColor(
                np.clip(gray, 0, 255).astype(np.uint8),
                cv2.COLOR_GRAY2BGR
            )

    return current