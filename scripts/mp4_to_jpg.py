import os
import argparse
import subprocess
from pathlib import Path
import ffmpeg

def mp4_to_jpg(filename, dir, mode):
    print('Starting for file: %s' % filename)
    file = Path(filename).stem
    image = ffmpeg.input(filename)
    image2 = ffmpeg.output(image, os.path.join(dir, file + '_%d_image.jpg'))
    ffmpeg.run(image2)

    if (mode == 'srt'):
        input = ffmpeg.input(filename)
        output_file = os.path.join(dir, file + '.srt')
        output = ffmpeg.output(input, output_file, map='0:2', y='-y')
        ffmpeg.run(output)
    else:
        pass

def process_directory(input_dir, output_dir):
    for filepath in Path(input_dir).glob('**/*'):
        mp4_to_jpg(filepath, output_dir, 'srt')
    print('Finished processing')

def remove_audio(input_dir, output_dir):
    for filepath in Path(input_dir).glob('**/*'):
        output_file = os.path.join(output_dir, filepath.name)
        subprocess.call(['ffmpeg', '-i', filepath, '-c', 'copy', '-an', output_file])
    print('Finished processing')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert MP4s into JPGs')
    parser.add_argument('-i', '--input_file', type=str, required=False, help='MP4 filepath')
    parser.add_argument('-d', '--input_dir', type=str, required=False, help='Input directory')
    parser.add_argument('-o', '--output_dir', type=str, required=True, help='Output directory')
    parser.add_argument('-m', '--mode', type=str, required=False, help='Set mode to \'srt\' to create SRT file')
    parser.add_argument('-a', '--audio', type=str, required=False, help='Set audio flag to \'remove\' to remove audio track from input files')
    args = parser.parse_args()

    if(args.input_file):
        print('Processing file: ')
        mp4_to_jpg(args.input_file, args.output_dir, args.mode)
    elif(args.audio):
        print('Removing audio tracks')
        remove_audio(args.input_dir, args.output_dir)
    elif(args.input_dir):
        print('Processing directory: ')
        process_directory(args.input_dir, args.output_dir)