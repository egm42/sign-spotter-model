import os
import argparse
import subprocess

def mp4_to_jpg(filepath, dir, mode):
    print('Starting MP4 processing...')
    if(mode):
        print('Basic Mode')
    else:
        print('Advanced Mode')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert MP4s into JPGs')
    parser.add_argument('-i', '--input_file', type=str, required=True, help='MP4 filepath')
    parser.add_argument('-o', '--output_dir', type=str, required=True, help='Output directory')
    parser.add_argument('-b', '--basic', type=bool, nargs='?', const=True, default=False, help='Toogle to True to only extract JPGs')
    args = parser.parse_args()

    mp4_to_jpg(args.input_file, args.output_dir, args.basic)