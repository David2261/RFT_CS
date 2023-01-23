#!/bin/bash

declare -a files=(
"../tests/__logs__/main.log"
"../tests/__logs__/error.log"
"../RFTCS/__logs__/main.log"
"../RFTCS/__logs__/error.log"
)

# Check size, if more than 1 byte > clean
for i in "${files[@]}"
do 
	if [wc -c "${files[@]}"]
	then
		echo -n "" > "${files[@]}"
	fi
done
