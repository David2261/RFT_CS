#! /bin/bash
poetry completions bash >> ~/.bash_completion

echo $PWD

echo 'Если это вам не подходит нажмите break, потому что дальше идет установка среды для проекта'
sleep 5


poetry install

source .venv/bin/activate

poetry tree -list


