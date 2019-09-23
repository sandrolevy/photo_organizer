import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("photo_organizer.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)




setup(
    name = "Photo Organizer",
    version = "1.0",
    description = "Simple Photo Organizer write in Python",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
