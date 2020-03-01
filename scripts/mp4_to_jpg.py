import os
import argparse
import subprocess
from pathlib import Path
import ffmpeg

def mp4_to_jpg(filename, dir, mode):
    print('Starting MP4 processing...')
    file = Path(filename).stem
    image = ffmpeg.input(filename)
    image2 = ffmpeg.output(image, os.path.join(dir, file + '_%dimage.jpg'))
    ffmpeg.run(image2)

    if (mode == 'a'):
        input = ffmpeg.input(filename)
        output_file = os.path.join(dir, file + '.srt')
        output = ffmpeg.output(input, output_file, map='0:2', y='-y')
        ffmpeg.run(output)
    else:
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert MP4s into JPGs')
    parser.add_argument('-i', '--input_file', type=str, required=True, help='MP4 filepath')
    parser.add_argument('-o', '--output_dir', type=str, required=True, help='Output directory')
    parser.add_argument('-m', '--mode', type=str, default=False, help='Set mode to \'a\' to create SRT file')
    args = parser.parse_args()

    mp4_to_jpg(args.input_file, args.output_dir, args.mode)