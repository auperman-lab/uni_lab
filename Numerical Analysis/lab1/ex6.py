from PIL import Image
import numpy as np


def transform(image, degree, scalex, scaley):
    scale = np.array([[scalex, 0], [0, scaley]])
    data = np.array(image)
    h, w, _ = data.shape
    h2, w2 = h // 2, w // 2
    wr, hr = np.max(np.abs(scale @ rotM(degree) @ np.array([[-w2, w2, w2], [h2, h2, -h2]])), axis=1).astype(int)

    data2 = np.zeros((hr*2, wr*2, 3))

    yr, xr = np.indices((hr*2, wr*2))
    yr, xr = yr.flatten(), xr.flatten()

    yrc, xrc = yr - hr, xr - wr
    xc, yc = (rotM(-degree) @ (np.linalg.inv(scale) @ np.row_stack((xrc, yrc)))).astype(int)

    x, y = xc + w2, yc + h2
    include = np.logical_and(np.abs(xc) < w2, np.abs(yc) < h2)

    data2[yr[include], xr[include]] = data[y[include], x[include]]
    data2 = np.uint8(data2)
    return Image.fromarray(data2)


def rotM(degree):
    theta = np.radians(degree)

    c, s = np.cos(theta), np.sin(theta)

    return np.array([[c, -s], [s, c]])


img = Image.open('/Users/nmacrii/Desktop/doomguy in van gogh style.png')


img2 = transform(img, 40, 5, 5)

img2.show()
