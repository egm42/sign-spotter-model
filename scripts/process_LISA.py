import argparse
import pandas as pd
import os

def process(input_dir, output_dir, sign_list):
    df = pd.read_csv(os.path.join(input_dir, 'allAnnotations.csv'), sep=',|;')
    print(sign_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rearrange LISA dataset')
    parser.add_argument('-d', '--input_dir', type=str, required=False, help='LISA parent directory')
    parser.add_argument('-o', '--output_dir', type=str, required=True, help='Output directory')
    args = parser.parse_args()

    sign_list = ['addedLane', 'curveLeft', 'curveRight', 'dip', 'doNotEnter', 'keepRight', 'laneEnds', 'merge', 'noLeftTurn', 'noRightTurn', 'pedestrianCrossing', 'rightLaneMustTurn', 'school', 'schoolSpeedLimit25', 'signalAhead', 'slow', 'speedLimit15', 'speedLimit25', 'speedLimit30', 'speedLimit35', 'speedLimit40', 'speedLimit45', 'speedLimit50', 'speedLimit55', 'speedLimit65', 'stop', 'stopAhead', 'yield']

    process(args.input_dir, args.output_dir, sign_list)