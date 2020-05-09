import json
import argparse

import os
import sys
#sys.path.insert(0, "")

# local modules
import config
import pipeline


parser = argparse.ArgumentParser()


parser.add_argument(
    "-file_index",
    type=int,
    default=0, 
    help="get the file from a list using indicies")

parser.add_argument(
    "-min_length",
    type=int,
    default=3, 
    help="minimum length of token to be considered")

parser.add_argument(
    "-window",
    type=int,
    default=2,
    help="window of the token around the keyword")

args = parser.parse_args()

files = os.listdir(path=config.ROOT_DIR)


def execute(idx):
    for f in files:
        path = os.path.join(config.ROOT_DIR, f)

    def return_seq():
        with open(path, mode='r', encoding='utf-8') as f:
            data = json.load(f)
            for i, d in enumerate(data['body']):
                tok_list = pipeline.remove_stopwords(d)
                seq = pipeline.tok_sequence(tok_list, args.min_length, args.window)    

                print(seq)

    return_seq()


if __name__ == "__main__":
    execute(args.file_index)

