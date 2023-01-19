#ifndef SIMULATION_H_
#define SIMULATION_H_

#include "main_extend.h"
float api_distance_N_step(float, int, float);
float api_tg_Beta(float, int, float);
float api_elliptical_range(float, float, float);
float api_mass_rocket(int, int);
float api_amount_gas_released(int, float);
float api_overpressure(float, int, float, float);
float api_thrust_force(float, float);
float api_impuls(float, int);
float api_height_force(float, float, float);
// CylindricalCavity
float api_cylindrical_cavity(float, float, float);
float api_volume_cylindrical_cavity(float, float);
// Resistance
float api_aerodynamic_pressure(float, float);
float api_aerodynamic_drag(float, float);
float api_gravitation_losses(float, float);
float api_control_losses(float, float, float);
// Speed
float api_resultant_force(float, float, float);
float api_rocket_acceleration(float, float);
float api_rocket_speed(float, float, float);

#endif // SIMULATION_H_
