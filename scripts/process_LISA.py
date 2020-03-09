import argparse
import pandas as pd
import os
import pathlib
import shutil
import xml.etree.cElementTree as ET
import cv2

def process(input_dir, output_dir, sign_list):
    df = pd.read_csv(os.path.join(input_dir, 'allAnnotations.csv'), sep=',|;')
    
    # Renamed columns to remove spaces and make all lowercase
    columns = ['filename', 'annotation_tag', 'upper_left_corner_x', 'upper_left_corner_y', 'lower_right_corner_x', 'lower_right_corner_y']
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df_filtered = df.filter(items=columns)
    df_filtered = df_filtered[df_filtered['annotation_tag'].isin(sign_list)]

    for row in df_filtered.itertuples():
        im_path = os.path.join(input_dir, row.filename)
        # print("Processing: ", im_path)
        shutil.copy(im_path, output_dir)
        im = cv2.imread(im_path)
        h, w, c = im.shape
        xml_file = os.path.join(output_dir, pathlib.Path(row.filename).stem + '.xml')

        if(os.path.isfile(xml_file)):
            root = ET.parse(xml_file).getroot()
            obj = ET.SubElement(root, "object")
            ET.SubElement(obj, "name").text = row.annotation_tag

            # Determine what these tags mean
            ET.SubElement(obj, "pose").text = "Unspecified"
            ET.SubElement(obj, "truncated").text = "1"
            ET.SubElement(obj, "difficult").text = "0"

            box = ET.SubElement(obj, "bndbox")
            ET.SubElement(box, "xmin").text = str(row.upper_left_corner_x)
            ET.SubElement(box, "ymin").text = str(row.upper_left_corner_y)
            ET.SubElement(box, "xmax").text = str(row.lower_right_corner_x)
            ET.SubElement(box, "ymax").text = str(row.lower_right_corner_y)
            tree = ET.ElementTree(root)
            tree.write(xml_file)
        else:
            root = ET.Element("annotation")
            ET.SubElement(root, "folder").text = output_dir
            ET.SubElement(root, "filename").text = os.path.basename(row.filename)
            ET.SubElement(root, "path").text = str(pathlib.Path(row.filename).absolute())
            source = ET.SubElement(root, "source")
            ET.SubElement(source, "database").text = "Unknown"
            size = ET.SubElement(root, "size")
            ET.SubElement(size, "width").text = str(w)
            ET.SubElement(size, "height").text = str(h)
            ET.SubElement(size, "depth").text = str(c)
            ET.SubElement(root, "segmented").text = "0"
            obj = ET.SubElement(root, "object")
            ET.SubElement(obj, "name").text = row.annotation_tag

            # Determine what these tags mean
            ET.SubElement(obj, "pose").text = "Unspecified"
            ET.SubElement(obj, "truncated").text = "1"
            ET.SubElement(obj, "difficult").text = "0"

            box = ET.SubElement(obj, "bndbox")
            ET.SubElement(box, "xmin").text = str(row.upper_left_corner_x)
            ET.SubElement(box, "ymin").text = str(row.upper_left_corner_y)
            ET.SubElement(box, "xmax").text = str(row.lower_right_corner_x)
            ET.SubElement(box, "ymax").text = str(row.lower_right_corner_y)
            tree = ET.ElementTree(root)
            tree.write(xml_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rearrange LISA dataset')
    parser.add_argument('-d', '--input_dir', type=str, required=False, help='LISA parent directory')
    parser.add_argument('-o', '--output_dir', type=str, required=True, help='Output directory')
    args = parser.parse_args()

    sign_list = ['addedLane', 'curveLeft', 'curveRight', 'dip', 'doNotEnter', 'keepRight', 'laneEnds', 'merge', 'noLeftTurn', 'noRightTurn', 'pedestrianCrossing', 'rightLaneMustTurn', 'school', 'schoolSpeedLimit25', 'signalAhead', 'slow', 'speedLimit15', 'speedLimit25', 'speedLimit30', 'speedLimit35', 'speedLimit40', 'speedLimit45', 'speedLimit50', 'speedLimit55', 'speedLimit65', 'stop', 'stopAhead', 'yield']

    process(args.input_dir, args.output_dir, sign_list)