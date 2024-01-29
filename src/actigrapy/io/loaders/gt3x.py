"""Loader for the .gt3x file format."""

import os

import pygt3x.reader

from actigrapy.common.data_model import InputData


def load(
    path: str | os.PathLike[str],
) -> InputData:
    """Load actigraphy data from .gt3x file."""
    with pygt3x.reader.FileReader(str(path)) as reader:
        df = reader.to_pandas()
    return df