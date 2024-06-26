import argparse
import os
from ccivr.__init__ import __version__

def get_path():
    
    parser = argparse.ArgumentParser(
        description='Extracts cisNats from data of gene sets.'
        )

    parser.add_argument('input',
        help='the path of the CSV file to read'
        )

    parser.add_argument('-o', '--output',
        help=
            'the path of the directory to save results, '
            'if not specified, files would be stored in the same location as input file.'
        )

    parser.add_argument('-v', '--version', action='version',
        version=__version__,
        help='show the version number and exit'
        )

    args = parser.parse_args()

    input_file = os.path.abspath(args.input)
    
    if args.output:
        output_dir = os.path.abspath(args.output)
    else:
        output_dir = os.path.dirname(input_file)

    class Paths:
        def __init__(self,input,output:list):
            self.input = input
            self.output = output

    paths = Paths(
        input = input_file, 
        output = output_dir
        )

    return paths
