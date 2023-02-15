from distutils.core import setup, Extension

some_module = Extension(
	"api_distance_N_step",
	source="core/flight_simulation.c"
)

setup(
	name="RFTCS_Core",
	version="1.0.1",
	description="Extend core on the C code",
	author="Bulat",
	ext_modules=[
		Extension()
	]
)
