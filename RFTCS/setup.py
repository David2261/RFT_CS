from distutils.core import setup, Extension


setup(
	name="RFTCS_Core",
	version="1.0.1",
	description="Extend core on the C code",
	author="Bulat",
	ext_modules=[
		Extension("core_api", ["core/bind.c", "core/api.c"])
	]
)
