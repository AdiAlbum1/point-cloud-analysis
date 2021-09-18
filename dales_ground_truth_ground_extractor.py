import argparse

import laspy

from dales_aux.dales_classes import DalesClasses

def parse_input_arguments():
    # Create the parser
    my_parser = argparse.ArgumentParser(description='Extract DALES dataset LAS file\'s ground truth ground points')

    # add argparse argumnets
    my_parser.add_argument('-i', '--input', type=str, help='path to input LAS file',
                           default='dales_las/train/5080_54435.las')
    my_parser.add_argument('-o', '--output', type=str, help='path to output LAS file',
                           default='ground.las')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    input_las, output_las = args.input, args.output

    return input_las, output_las


if __name__ == "__main__":
    input_las_path, output_las_path = parse_input_arguments()

    las = laspy.read(input_las_path)
    las.points = las.points[las.classification == DalesClasses.GROUND.value]
    las.write(output_las_path)