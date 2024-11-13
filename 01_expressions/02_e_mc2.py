def energy():
    C = 299792458  # speed of light in m/s

    mass = float(input("Enter kilos of mass: "))

    energy = mass * C**2

    print(f"\nm = {mass} kg")
    print(f"C = {C} m/s")
    print(f"{energy} joules of energy!")

energy()