.PHONY: all trajectory run_trajectory clean

GG = gcc
GC = -Wall -Werror -Wextra

FT = flight_trajectory.c constant.h settings.h

all: trajectory

trajectory: $(FT)
	$(GG) $(GC) $(FT) -lm Trajectory
	$(MAKE) run_trajectory


run_trajectory: Trajectory
	./Trajectory

clean:
	rm -f -r *.o
	rm -f -r *.dch

