#include "simulation.h"

int main()
{
	return 0;
}

float api_distance_N_step(float fuel_flow, int step, float init_distance)
{
	float length = init_distance - step * fuel_flow;
	return length;
}

float api_tg_Beta(float speed, int radius, float init_radius)
{
	float V = (speed * init_radius) / radius;
	V = (0 < V) ? V : -V;
	float beta = V / (2 * sqrt(V));
	return V;
}

float api_elliptical_range(float speed, float radius, float init_radius)
{
	float Beta = api_tg_Beta(speed, radius, init_radius);
	float length = 2 * radius * arctan(Beta);
	return length;
}

float api_mass_rocket(int mass_empty, int mass_fuel)
{
	float mass = (float)mass_empty + mass_fuel;
	return mass;
}

float api_amount_gas_released(int mass, float molar_mass)
{
	float amount = (float)mass / molar_mass;
	return amount;
}

float api_overpressure(float flow, int burn_temp, float molar_mass, float gas_const)
{
	float H = (float)burn_temp * gas_const * molar_mass;
	float OP = H / flow;
	return OP;
}

float api_thrust_force(float pressure, float cross_section_area)
{
	return pressure * cross_section_area;
}

float api_impuls(float thrustF, int time)
{
	return thrustF * time;
}

float api_height_force(float height, float heightStage, float numberStages)
{
	return height + heightStage * numberStages;
}

// CylindricalCavity
float api_cylindrical_cavity(float init_distance, float step, float burnFuel)
{
	return init_distance + step * burnFuel;
}

float api_volume_cylindrical_cavity(float R_n, float distance)
{
	double degree = 2.00;
	return ((float)M_PI * pow(R_n, degree) * distance);
}

float api_aerodynamic_pressure(float speed, float density)
{
	double degree = 2.00;
	return (density * pow(speed, degree)) / 2;
}

float api_aerodynamic_drag(float pressure, float cross_section_area)
{
	return pressure * cross_section_area * cross_section_area;
}

float api_gravitation_losses(float free_fall, float FPV)
{
	return sin(FPV) * free_fall;
}

float api_control_losses(float TVV, float thrustF, float mass)
{
	float angel = 1 - cos(TVV);
	return (thrustF / mass) * angel;
}

// Speed
float api_resultant_force(float thrustF, float gravLost, float mass, float G)
{
	return thrustF * gravLost - mass * G;
}

float api_rocket_acceleration(float restF, float mass)
{
	return restF / mass;
}

float api_rocket_speed(float speed_0, float boost, int time)
{
	float clock = (float)time;
	return speed_0 + boost * clock;
}
