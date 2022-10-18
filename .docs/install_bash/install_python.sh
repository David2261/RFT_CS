#! /bin/bash
cd ~

sudo apt update && sudo apt upgrade

echo 'Обновление прошло успешно!!!'

num=1

while [ $num -gt 4 ]
do
	echo num
	num=$[ $num + 1 ]
	sleep 1
done


sudo apt install wget build-essential libncursesw5-dev libssl-dev \
libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

echo 'Добавление среды для python прошло успешно!!!'

wget https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tgz

tar xzf Python-3.10.2.tgz

echo 'Установка python успешно!!!'

cd Python-3.10.2

./configure --enable-optimizations
make altinstall
make -j 2
sudo make install
echo 'Помолимся вместе со мной, чтобы всё было чики-пуки!!!'
sleep 1

python3.10 -V
pip3.10 -V

echo 'Поздравляю вас python установлен и уже работает, и pip тоже :)'