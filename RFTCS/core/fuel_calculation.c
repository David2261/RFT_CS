#include "fuel.h"
#include <time.h>

int main()
{
	double time_spent = 0.0;
	clock_t begin = clock();

	float Me = 524.0, Mf = 579.0, Isp = 4200.0, speed = 450.0;
	float freeFall = 9.8;
	float natLog = api_natural_logarithm(Mf, Me);
	float euler = api_euler(freeFall, speed, Isp);
	float totalSpeed = api_total_speed(freeFall, Isp, natLog);
	float totalOil = api_total_oil(Me, euler);
	printf("Total Speed: %.2f\nTotal Oil: %.2f\n", totalSpeed, totalOil);
	
	clock_t end = clock();
	time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
	printf("%f\n", time_spent);
	return 0;
	/*
	Total Speed: 45480.23
	Total Oil: 5.76
	time: 0.000267
	*/
}

float api_natural_logarithm(float massFuel, float massEmpty)
{
	float res = massFuel / massEmpty;
	return res;
}

float api_euler(float freeFall, float speed, float Isp)
{
	return exp(speed / (Isp * freeFall));
}

float api_total_speed(float freeFall, float Isp, float natLog)
{
	return freeFall * Isp * natLog;
}

float api_total_oil(float massEmpty, float euler)
{
	return massEmpty * (euler - 1);
}
