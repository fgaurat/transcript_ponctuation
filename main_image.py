#!/usr/bin/env python
import sys
import os
import cv2
import pafy
import random


# pip install opencv-python
# pip install pafy
# pip install youtube-dl==2020.12.2

def main():
    num = 5
    url="https://www.youtube.com/watch?v=_hdoLkGgPxM"
    video = pafy.new(url)
    print(f"{video.title=}")
    print(f"{video.duration=}")
    # print(f"{video.description=}")
    best  = video.getbest()

    capture = cv2.VideoCapture(best.url)
    length = int(capture.get(cv2. CAP_PROP_FRAME_COUNT))
    img_positions = []
    for i in range(num):
        v0 = int(length / num * i)
        v1 = int(length / num * (i+1))
        r = random.randint(v0,v1)
        img_positions.append(r)

    for img_position in img_positions:
        capture.set(cv2.CAP_PROP_POS_FRAMES, img_position)
        ret, frame = capture.read()
        if ret:
            cv2.imwrite(f"img_{img_position}.png", frame)
            print(f"img_{img_position}.png OK")
        else:
            print("error")
            break

    capture.release()
if __name__ == '__main__':
    main()