import numpy as np

def simulate(mass, thrust, burn_time):
    g = 9.81
    rho = 1.225   # air density
    Cd = 0.75     # drag coefficient (estimate)
    A = 0.01      # cross-sectional area (m^2)

    dt = 0.01
    t = 0

    velocity = 0
    height = 0
    max_height = 0

    while height >= 0:
        if t < burn_time:
            force = thrust
        else:
            force = 0

        drag = 0.5 * Cd * rho * A * velocity**2 * np.sign(velocity)

        net_force = force - (mass * g) - drag
        acceleration = net_force / mass

        velocity += acceleration * dt
        height += velocity * dt

        if height > max_height:
            max_height = height

        t += dt

        if t > 60:
            break

    return max_height


# quick test
if __name__ == "__main__":
    print("Test 1 (baseline):", simulate(1.5, 50, 2))
    print("Test 2 (more thrust):", simulate(1.5, 80, 2))
    print("Test 3 (more mass):", simulate(3.0, 50, 2))
    