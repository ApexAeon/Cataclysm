import os
os.environ['TCL_LIBRARY'] = "D:\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "D:\\Python36-32\\tcl\\tk8.6"
import cx_Freeze

executables = [cx_Freeze.Executable("./Cataclysm-SRC/scripts/frame.py")]

cx_Freeze.setup(
    name="Cataclysm",
    options={"build_exe": {"packages":["pygame"],"include_files":[]}},
    executables=executables
    )
