#!/bin/bash
# File for run tests

echo "core(1) | display(2)";
read context_id;

if [[ $context_id -eq 1 ]] || [[ $context_id -eq "core" ]]; then
		echo "pytest fails: "
		pytest rocket_flight_simulation;
		pytest rocket_flight_trajectory;
		pytest rocket_fuel_calculation;
		echo "flake8 fails: "
		flake8 --count rocket_flight_simulation;
		flake8 --count rocket_flight_trajectory;
		flake8 --count rocket_fuel_calculation;
	elif [[ $context_id -eq 2 ]] || [[ $context_id -eq "display" ]]; then
		pytest display;
		echo "flake8 fails: "
		flake8 --count display;
	else
		echo "Fail context!!!"
fi