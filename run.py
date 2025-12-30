from config.domain import domain
from config.fluid_properties import fluid
from config.boundary_conditions import boundary_conditions
from methods.solver import solve_cavity
from graphics.plot_fields import plot_velocity_field


def main():
    results = solve_cavity(domain, fluid, boundary_conditions)
    plot_velocity_field(results)


if __name__ == "__main__":
    main()