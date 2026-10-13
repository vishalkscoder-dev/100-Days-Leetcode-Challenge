import subprocess
subprocess.run("cls", shell=True)


def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_length = min(ax2, bx2) - max(ax1, bx1)
    overlap_width = min(ay2, by2) - max(ay1, by1)

    if overlap_length > 0 and overlap_width > 0:
        overlap_area = overlap_length * overlap_width
    else:
        overlap_area = 0

    return area1 + area2 - overlap_area

ax1 = -3
ay1 = 0

ax2 = 3
ay2 = 4

bx1 = 0
by1 = -1

bx2 = 9
by2 = 2

print(computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))