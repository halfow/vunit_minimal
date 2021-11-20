"""
Add files, config, parameters etc.

TODO: a wrapper function should probably be used to make 
      it easy to import for stuff like "deep" regression.
"""
from vunit import VUnit
from pathlib import Path

def files(vunit: VUnit) -> None:
    root = Path(__file__).parent.parent
    lib = vunit.add_library(root.name)
    lib.add_source_files(root / "*/*.vhd")
