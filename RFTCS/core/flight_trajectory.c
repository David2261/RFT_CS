#include "trajectory.h"


int main()
{
	int speed = 29000;
	float sine = api_double_angle_sine();
	float fr = api_flight_range(sine, speed);
	float ft = api_flight_time(speed);
	if (ft < 1 || fr < 1)
	{
		printf("Ошибка в вычислениях!!!\n");
	}
	else
	{
		printf("Дальность полета = %.2f\n Время полета = %.2f\n", fr, ft);
	}
	return 0;
}


float api_double_angle_sine()
{
	/* Синус двойного угла */
	float num = FPV;
	float x = 2 * sin(num) * cos(num);
	x = (x < 0) ? -x : x;
	return x;
}


float api_flight_range(float sine, int speed)
{
	/* Дальность полета */
	float G = ACCELERATION_FREE_FALL;
	return (pow(speed, 2.0) * sine) / (2 * G);
}


float api_flight_time(int speed)
{
	float G = ACCELERATION_FREE_FALL;
	float A = FPV;

	return ((2 * speed * sin(A)) / G);
}
