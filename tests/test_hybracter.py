import os
import shutil
import subprocess
import unittest
from pathlib import Path

import pytest

__author__ = "George Bouras"
__copyright__ = "Copyright 2023, Hybracter"
__license__ = "MIT"
__type__ = "Test Script"
__maintainer__ = "George Bouras"
__email__ = "george.bouras@adelaide.edu.au"

# test data
test_data_path = Path("hybracter/test_data")
db_dir: Path = "plassembler_db"


@pytest.fixture(scope="session")
def tmp_dir(tmpdir_factory):
    return tmpdir_factory.mktemp("tmp")


threads = 2


def remove_directory(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)


def exec_command(cmnd, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
    """executes shell command and returns stdout if completes exit code 0
    Parameters
    ----------
    cmnd : str
      shell command to be executed
    stdout, stderr : streams
      Default value (PIPE) intercepts process output, setting to None
      blocks this."""

    proc = subprocess.Popen(cmnd, shell=True, stdout=stdout, stderr=stderr)
    out, err = proc.communicate()
    if proc.returncode != 0:
        raise RuntimeError(f"FAILED: {cmnd}\n{err}")
    return out.decode("utf8") if out is not None else None


def test_hybracter_t_hybrid():
    """hybracter test-hybrid"""
    outdir: Path = "test_hybracter_output"
    cmd = f"hybracter test-hybrid --threads {threads} --output {outdir}"
    exec_command(cmd)
    remove_directory(outdir)


def test_hybracter_t_hybrid_no_medaka():
    """hybracter test-hybrid no medaka"""
    outdir: Path = "test_hybracter_output"
    cmd = f"hybracter test-hybrid --threads {threads} --output {outdir} --no_medaka"
    exec_command(cmd)
    remove_directory(outdir)


def test_hybracter_t_hybrid_no_pypolca():
    """hybracter test-hybrid no pypolca"""
    outdir: Path = "test_hybracter_output"
    cmd = f"hybracter test-hybrid --threads {threads} --output {outdir} --no_pypolca"
    exec_command(cmd)
    remove_directory(outdir)


def test_hybracter_t_long():
    """hybracter test-long"""
    outdir: Path = "test_hybracter_output"
    cmd = f"hybracter test-long --threads {threads} --output {outdir}"
    exec_command(cmd)
    remove_directory(outdir)


def test_hybracter_t_long_no_medaka():
    """hybracter test-long no medaka"""
    outdir: Path = "test_hybracter_output"
    cmd = f"hybracter test-long --threads {threads} --output {outdir} --no_medaka"
    exec_command(cmd)
    remove_directory(outdir)


def test_hybracter_install():
    """test hybracter install and install dirs for later tests"""
    cmd = f"hybracter install  --databases {db_dir}"
    exec_command(cmd)


"""
test with csv
"""


def test_hybracter_hybrid_csv():
    """test hybracter hybrid default"""
    outdir: Path = "test_hybracter_output"
    input_csv: Path = test_data_path / "test_hybrid_input.csv"
    cmd = f"hybracter hybrid --input {input_csv} --threads {threads} --output {outdir} --databases {db_dir}"
    exec_command(cmd)
    remove_directory(outdir)


def test_hybracter_no_pypolca_no_medaka():
    """test hybracter hybrid no pypolca and no medaka"""
    outdir: Path = "test_hybracter_output"
    input_csv: Path = test_data_path / "test_hybrid_input.csv"
    cmd = f"hybracter hybrid --input {input_csv} --threads {threads} --output {outdir} --no_pypolca --databases {db_dir} --no_medaka "
    exec_command(cmd)
    remove_directory(outdir)


def test_hybracter_no_medaka():
    """test hybracter hybrid no medaka"""
    outdir: Path = "test_hybracter_output"
    input_csv: Path = test_data_path / "test_hybrid_input.csv"
    cmd = f"hybracter hybrid --input {input_csv} --threads {threads} --output {outdir} --databases {db_dir} --no_medaka"
    exec_command(cmd)
    remove_directory(outdir)


def test_hybracter_no_pypolca():
    """test hybracter hybrid no pypolca"""
    outdir: Path = "test_hybracter_output"
    input_csv: Path = test_data_path / "test_hybrid_input.csv"
    cmd = f"hybracter hybrid --input {input_csv} --threads {threads} --output {outdir} --no_pypolca --databases {db_dir} "
    exec_command(cmd)
    remove_directory(outdir)


"""
long
"""


def test_hybracter_long():
    """test hybracter long"""
    outdir: Path = "test_hybracter_output"
    input_csv: Path = test_data_path / "test_long_input.csv"
    cmd = f"hybracter long --input {input_csv} --threads {threads} --output {outdir} --databases {db_dir}"
    exec_command(cmd)
    remove_directory(outdir)


def test_hybracter_long_no_medaka():
    """test hybracter long"""
    outdir: Path = "test_hybracter_output"
    input_csv: Path = test_data_path / "test_long_input.csv"
    cmd = f"hybracter long --input {input_csv} --threads {threads} --output {outdir} --databases {db_dir} --no_medaka"
    exec_command(cmd)
    remove_directory(outdir)


"""
single
"""


def test_hybracter_hybrid_single():
    """test hybracter hybrid single"""
    outdir: Path = "test_hybracter_output_hybr_single"
    longreads: Path = test_data_path / "Fastqs/test_long_reads.fastq.gz"
    reads1: Path = test_data_path / "Fastqs/test_short_reads_R1.fastq.gz"
    reads2: Path = test_data_path / "Fastqs/test_short_reads_R2.fastq.gz"
    cmd = f"hybracter hybrid-single -l {longreads} -1 {reads1} -2 {reads2} -c 50000 -s Sample1 --threads {threads} --output {outdir} --databases {db_dir}"
    exec_command(cmd)
    remove_directory(outdir)


def test_hybracter_hybrid_single_no_medaka():
    """test hybracter hybrid single no medaka"""
    outdir: Path = "test_hybracter_output_hybr_single"
    longreads: Path = test_data_path / "Fastqs/test_long_reads.fastq.gz"
    reads1: Path = test_data_path / "Fastqs/test_short_reads_R1.fastq.gz"
    reads2: Path = test_data_path / "Fastqs/test_short_reads_R2.fastq.gz"
    cmd = f"hybracter hybrid-single -l {longreads} -1 {reads1} -2 {reads2} -c 50000 -s Sample1 --threads {threads} --output {outdir} --databases {db_dir} --no_medaka"
    exec_command(cmd)
    remove_directory(outdir)


@pytest.mark.dependency(depends=["test_hybracter_install"])
def test_hybracter_long_single():
    """test hybracter long"""
    outdir: Path = "test_hybracter_output_long_single"
    longreads: Path = test_data_path / "Fastqs/test_long_reads.fastq.gz"
    cmd = f"hybracter long-single -l {longreads} -c 50000 -s Sample1  --threads {threads} --output {outdir} --databases {db_dir}"
    exec_command(cmd)
    remove_directory(outdir)


def test_hybracter_long_single_no_medaka():
    """test hybracter long no medaka"""
    outdir: Path = "test_hybracter_output_long_single"
    longreads: Path = test_data_path / "Fastqs/test_long_reads.fastq.gz"
    cmd = f"hybracter long-single -l {longreads} -c 50000 -s Sample1  --threads {threads} --output {outdir} --databases {db_dir} --no_medaka"
    exec_command(cmd)
    remove_directory(outdir)


"""
custom db
"""


def test_hybracter_dnaapler_custom_db():
    """test hybracter hybrid-single with custom_db"""
    outdir: Path = "test_hybracter_output_custom_db"
    longreads: Path = test_data_path / "Fastqs/test_long_reads.fastq.gz"
    reads1: Path = test_data_path / "Fastqs/test_short_reads_R1.fastq.gz"
    reads2: Path = test_data_path / "Fastqs/test_short_reads_R2.fastq.gz"
    dnaapler_custom_db: Path = test_data_path / "dnaapler_custom_db/dnaA.faa"
    cmd = f"hybracter hybrid-single -l {longreads} -1 {reads1} -2 {reads2} -c 50000 -s Sample1 --threads {threads} --output {outdir} --databases {db_dir} --dnaapler_custom_db {dnaapler_custom_db}"
    exec_command(cmd)
    remove_directory(outdir)


def test_citation():
    """test hybracter citation"""
    cmd = "hybracter citation"
    exec_command(cmd)


def test_version():
    """test hybracter version"""
    cmd = "hybracter version"
    exec_command(cmd)


class errors(unittest.TestCase):
    def test_no_db(self):
        """test hybracter with no db"""
        with self.assertRaises(RuntimeError):
            outdir: Path = "test_hybracter_output"
            empty_db: Path = "tests/empty_db"
            cmd = f"hybracter test-hybrid --threads {threads} --output {outdir} --database {empty_db} --no_pypolca"
            exec_command(cmd)
            remove_directory(outdir)


# cleanup
remove_directory(db_dir)
