.PHONY: all trajectory run_trajectory clean

GG = gcc
GC = -Wall -Werror -Wextra

DIR_OUT=bin

# Trajectory
FT = flight_trajectory.c
FO = flight_trajectory.o
FS = Trajectory.so
# Simulation
ST = flight_simulation.c
SO = flight_simulation.o
SS = Simulation.so
# Fuel
FuT = fuel_calculation.c
FuO = fuel_calculation.o
FuS = Fuel.so

all: trajectory
# -shared -Wl,-soname,adder -o adder.so -fPIC
# Main function for create CDLL
trajectory: $(FT)
	$(GG) $(GC) -fPIC -shared -o $(FS) $(FT) -lm
	$(GG) $(GC) -fPIC -shared -o $(SS) $(ST) -lm
	$(GG) $(GC) -fPIC -shared -o $(FuS) $(FuT) -lm
	$(MAKE) run_trajectory

# Separate function for debugging
flight_trajectory: $(FT)
	$(GG) $(GC) -c $(FT) -lm
	$(GG) -o trajectory $(FO)

# Separate function for debugging
flight_simulation: $(ST)
	$(GG) $(GC) -c $(ST) -lm
	$(GG) -o simulation $(SO) -lm

# Separate function for debugging
fuel_calculation: $(FuT):
	$(GG) $(GC) -c $(FuT) -lm
	$(GG) -o fuel $(FuO) -lm

run_trajectory: $(FO)
	mv $(FS) ./$(DIR_OUT)/$(FS)
	mv $(SS) ./$(DIR_OUT)/$(SS)
	mv $(FuS) ./$(DIR_OUT)/$(FuS)

clean:
	rm -rf $(DIR_OUT)/*
	rm -f ./*.o && rm -f ./*.so
