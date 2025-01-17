"""
Defines all functions used in hybracter
"""

import gzip
from Bio import SeqIO
import sys
import os


# define functions
# get long reads
def get_input_lr_fastqs(wildcards):
    return dictReads[wildcards.sample]["LR"]


# get min chrom length (define chrom size)
def getMinChromLength(wildcards):
    return dictReads[wildcards.sample]["MinChromLength"]


def get_input_r1(wildcards):
    return dictReads[wildcards.sample]["R1"]


def get_input_r2(wildcards):
    return dictReads[wildcards.sample]["R2"]


### host removal


def is_fasta_file(file_path):
    """
    Check if a file is in FASTA or FASTA.gz format.

    Args:
        file_path (str): The path to the file to be checked.
    Returns:
        bool: True if the file is in FASTA or FASTA.gz format, False otherwise.
    """
    try:
        with gzip.open(file_path, "rt") as handle:
            records = list(SeqIO.parse(handle, "fasta"))
            return len(records) > 0
    except (IOError, ValueError):
        # Handle exceptions for non-existent or non-FASTA files
        return False


def check_host():
    """
    checks the  HOST for removing contaminants
    """
    if config.args.contaminants == "none":
        CONTAM = "none"
    elif config.args.contaminants == "lambda":
        CONTAM = os.path.join(dir.contaminant_genomes, "lambda.fasta")
    else:  # check it is a FASTA
        # check the provided host is a fasta or fasta.gz
        if is_fasta_file(config.args.contaminants):
            CONTAM = config.args.contaminants
        else:
            sys.exit(
                f"You have provided a host genome file {config.args.contaminants} that is not a FASTA file."
            )
    return CONTAM


## database checks


def check_db(database_dir):
    """
    database_dir = path to database directory
    taken and adapted from hecatomb https://github.com/shandley/hecatomb/blob/main/hecatomb/snakemake/workflow/rules/preflight/validate.smk
    returns nothing (will sys.exit if it fails)
    """

    db_files = ["plsdb.msh", "plsdb.tsv"]

    # Check for Database files
    dbFail = False
    for f in db_files:
        dbFile = os.path.join(database_dir, f)
        if not os.path.isfile(dbFile):
            dbFail = True
            sys.stderr.write(f" ERROR: missing database file {dbFile}\n")
    if dbFail:
        sys.stderr.write(
            "\n"
            "    FATAL: One or more database files is missing.\n"
            "    Please run 'hybracter install' to download and install the missing database files.\n"
            "\n"
        )
        sys.exit(1)
