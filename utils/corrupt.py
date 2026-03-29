import numpy as np

def corrupt_center(img, size=150):
    h, w, _ = img.shape
    x = w // 2 - size // 2
    y = h // 2 - size // 2

    corrupted = img.copy()
    corrupted[y:y+size, x:x+size] = 0

    return corrupted, (x, y, size, size)


def corrupt_multi(img, n=5, size=80):
    corrupted = img.copy()
    h, w, _ = img.shape

    for _ in range(n):
        x = np.random.randint(0, w-size)
        y = np.random.randint(0, h-size)
        corrupted[y:y+size, x:x+size] = 0

    return corrupted