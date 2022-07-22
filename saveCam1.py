import os
import time
# handling CONFIGURATION file for BOX setting
file = "/home/pi/Downloads/*.mp4"
FILENAME = "/home/pi/Videos/CompressedVideo/"


def video_compressor(file, FILENAME):
    # OUTPUTFILE=f'{APP_FOLDER_SERVICE_PATH}/{FILENAME}'
    os.system(f"ffmpeg -i {file} -vcodec h264 -crf 35 -b:v 2097k -acodec aac {FILENAME}")
    # os.system(f"rm- rf {file}")
    # os.system(f"cp {OUTPUTFILE} {file}")
    time.sleep(2)
    print("old deleted")


video_compressor(file, FILENAME)
