#!/usr/bin/env python
import sys
import os
import cv2
import pafy
import random
import argparse

# pip install opencv-python
# pip install pafy
# pip install youtube-dl==2020.12.2

def main(url, num,image_prefix,image_extension):
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
            file_name = f"{image_prefix}{img_position}.{image_extension}"
            cv2.imwrite(file_name, frame)
            print(f"{file_name} OK")
        else:
            print("error")
            break

    capture.release()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get some images from youtube video')
    parser.add_argument('url', type=str, help='Youtube video url')
    parser.add_argument('num', type=int, help='Number of images to get')
    parser.add_argument('image_prefix', type=str, default="img_",help='File name prefix for images')
    parser.add_argument('image_extension', type=str, default="png",help='File name extension for images')

    args = parser.parse_args()

    main(args.url, args.num,args.image_prefix,args.image_extension)