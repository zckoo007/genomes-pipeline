#!/usr/bin/env python3

import os
import shutil
import argparse
import sys

NAME_MANY_GENOMES = "many_genomes"
NAME_ONE_GENOME = "one_genome"
NAME_MASH = "mash_folder"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Moves clusters according the number of genomes")
    parser.add_argument("-i", "--input", dest="input_folder", help="drep_split out folder", required=True)

    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        if not os.path.exists(NAME_MANY_GENOMES):
            os.makedirs(NAME_MANY_GENOMES)
        if not os.path.exists(NAME_ONE_GENOME):
            os.makedirs(NAME_ONE_GENOME)
        if not os.path.exists(NAME_MASH):
            os.makedirs(NAME_MASH)

        drep_clusters = args.input_folder
        clusters = os.listdir(drep_clusters)
        for cluster in clusters:
            genomes = os.listdir(os.path.join(drep_clusters, cluster))
            number_of_genomes = sum([1 for i in genomes if len(i.split('.fa')) > 1])
            if number_of_genomes > 1:
                for genome in genomes:
                    shutil.copy(os.path.join(drep_clusters, cluster, genome), os.path.join(NAME_MANY_GENOMES, cluster, genome))
                mashes = [i for i in genomes if len(i.split('mash.tsv')) > 1]
                if len(mashes) > 0:
                    mash = mashes[0]
                    shutil.copy(os.path.join(drep_clusters, cluster, mash), os.path.join(NAME_MASH, mash))
            if number_of_genomes == 1:
                for
                shutil.copy(os.path.join(drep_clusters, cluster), os.path.join(NAME_ONE_GENOME, cluster))

