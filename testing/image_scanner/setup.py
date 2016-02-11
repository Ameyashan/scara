import sys
from cx_Freeze import setup, Executable
setup(
    name="GUI PROGRAM",
    version="0.1",
    description="MyEXE",
    executables=[Executable("main_caller.py", base="Win64GUI")],
    )
