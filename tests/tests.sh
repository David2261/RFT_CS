#!/bin/bash
# File for run tests

echo "core(1) | display(2) | setup(3) | main(4)";
read context_id;

if [[ $context_id -eq 1 ]] || [[ $context_id -eq "core" ]]; then
		pytest core;
		echo "flake8 fails: "
		flake8 --count core;
	elif [[ $context_id -eq 2 ]] || [[ $context_id -eq "display" ]]; then
		pytest display;
		echo "flake8 fails: "
		flake8 --count display;
	elif [[ $context_id -eq 3 ]] || [[ $context_id -eq "setup" ]]; then
		pytest setup;
		echo "flake8 fails: "
		flake8 --count setup;
	elif [[ $context_id -eq 4 ]] || [[ $context_id -eq "main" ]]; then
		pytest test_main.py
		echo "flake8 fails: "
		flake8 --count test_main.py
	else
		echo "Fail context!!!"
fi