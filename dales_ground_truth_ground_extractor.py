import argparse

import laspy
from dales_classes import DalesClasses

if __name__ == "__main__":
    # Create the parser
    my_parser = argparse.ArgumentParser(description='Extract DALES dataset LAS file\'s ground truth ground points')

    my_parser.add_argument('-i', '--input', type=str, help='path to input LAS file',
                           default='dales_las/train/5080_54435.las')
    my_parser.add_argument('-o', '--output', type=str, help='path to output LAS file',
                           default='ground.las')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    input_las_path = args.input
    output_las_path = args.output

    las = laspy.read(input_las_path)
    las.points = las.points[las.classification == DalesClasses.GROUND.value]
    las.write(output_las_path)