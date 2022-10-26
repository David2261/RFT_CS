#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "constant.h"
#include "settings.h"


float double_angle_sine();
float flight_range(float, int);
float flight_time(int);

int main() {
	int speed = 29000, FLAG = 0;
	float sine = double_angle_sine();
	float fr = flight_range(sine, speed), ft;
	if (fr < 1) FLAG = 1;
	if (FLAG == 0) {
		ft = flight_time(speed);
		if (ft < 1) FLAG = 1;
		if (FLAG == 1) {
			printf("Ошибка в вычислениях!!!\n");
		} else {
			printf("Дальность полета = %f\n Время полета = %f\n", fr, ft);
		}
	}
	return 0;
}

float double_angle_sine() {
	/* Синус двойного угла */
	float num = FPV;
	return 2 * sinh(num) * cosh(num);
}

float flight_range(float sine, int speed) {
	/* Дальность полета */
	float G = ACCELERATION_FREE_FALL;
	return (pow(speed, 2) * sine) / (2 * G);
}

float flight_time(int speed) {
	float G = ACCELERATION_FREE_FALL;
	float A = FPV;

	return ((2 * speed * sinh(A)) / G);
}


