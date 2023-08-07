from distutils.core import setup, Extension


setup(
	name="RFTCS_Core",
	version="1.0.1",
	description="Extend core on the C code",
	author="Bulat",
	ext_modules=[
		Extension("API_das", ["api.c"]),
		Extension("API_FR", ["api.c"]),
	]
)
