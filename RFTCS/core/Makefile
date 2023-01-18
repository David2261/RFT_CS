.PHONY: all trajectory run_trajectory clean

GG = gcc
GC = -Wall -Werror -Wextra

DIR_OUT=bin

FT = flight_trajectory.c
FO = flight_trajectory.o

all: trajectory

trajectory: $(FT)
	$(GG) -c $(GC) $(FT)
	$(GG) -o Trajectory $(FO) -lm
	$(MAKE) run_trajectory


run_trajectory: $(FO)
	mv Trajectory ./$(DIR_OUT)/Trajectory

clean:
	rm -rf $(DIR_OUT)/*
