import os
import time
# handling CONFIGURATION file for BOX setting
file = "your current file to compress"
FILENAME = "file compressed "


def video_compressor(file, FILENAME):
    os.system(f"ffmpeg -i {file} -vcodec h264 -crf 35 -b:v 2097k -acodec aac {FILENAME}")
    time.sleep(2)
    print("old deleted")


video_compressor(file, FILENAME)
