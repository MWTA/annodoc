#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import re


def get_raw_text(conll_filepath):
    rawtext = ''
    with open(conll_filepath) as fd:
        rawtext = fd.read().strip()

    return rawtext


def get_default_header():
    return (
        "---\n"
        "layout: entry\n"
        "title: Sample CoNLL-U Annotations\n"
        "---\n"
        "For testing purposes only. Don't mind the lack of better comparison\n"
        "visualisation..."
    )


def main(dirpath):
    fnames = [e for e in os.listdir(dirpath) if e.endswith('.conll')]

    for fname in fnames:
        fpath = os.path.join(dirpath, fname)
        print(f'PROCESSING {fpath}')
        rawtext = get_raw_text(fpath)
        text = re.sub(r'\n\n', r'\n\n~~~\n\n~~~ conllu\n', rawtext)
        text = '~~~ conllu\n' + text + '\n\n~~~\n'

        with open(fpath + '.md', 'w') as fd:
            header_text = get_default_header()
            fd.write(header_text + '\n\n')
            fd.write(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'ROOT_DIR', help="The path to the dataset's root directory")
    args = parser.parse_args()
    main(args.ROOT_DIR)
