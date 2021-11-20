from vunit import VUnit
from . import prompt, create, add

vunit = VUnit.from_argv()

# Structural
todo = [
    add.files,
    create.vhdl_ls_config,
    create.hdl_checker_config,
    prompt.multiple_tests_with_gui,
]

[f(vunit) for f in todo]

vunit.main() 
