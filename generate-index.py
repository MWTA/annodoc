#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import re


def get_default_header():
    return (
        "---\n"
        "layout: entry\n"
        "title: Sample CoNLL-U Annotations\n"
        "---\n"
        "For testing purposes only. Don't mind the lack of better comparison\n"
        "visualisation..."
    )


def main(root_dir):
    print(f'CREATING index.md on "{root_dir}"')
    fnames = sorted(os.listdir(root_dir))
    fnames = filter(lambda e: e.endswith('.md') and e != 'index.md', fnames)
    index_md_path = os.path.join(root_dir, 'index.md')
    with open(index_md_path, 'w') as fd:
        fd.write(get_default_header() + '\n\n')

        for e in fnames:
            fname = re.sub('.conll.md$', '', e)
            fd.write(f'[{fname}]({fname}.conll.html)\n\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('ROOT_DIR', help="The path to the parser's root dir")
    args = parser.parse_args()

    main(args.ROOT_DIR)
