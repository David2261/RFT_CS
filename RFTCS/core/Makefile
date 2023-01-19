.PHONY: all trajectory run_trajectory clean

GG = gcc
GC = -Wall -Werror -Wextra

DIR_OUT=bin

FT = flight_trajectory.c
FO = flight_trajectory.o

all: trajectory
# -shared -Wl,-soname,adder -o adder.so -fPIC
trajectory: $(FT)
	$(GG) $(GC) -fPIC -shared -o Trajectory.so $(FT) -lm
	$(MAKE) run_trajectory


run_trajectory: $(FO)
	mv Trajectory.so ./$(DIR_OUT)/Trajectory.so
# 	mv $(FO) ./$(DIR_OUT)/$(FO)

clean:
	rm -rf $(DIR_OUT)/*
	rm -f ./*.o && rm -f ./*.so
