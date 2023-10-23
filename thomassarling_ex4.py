import numpy as np
import matplotlib.pyplot as plt


class GravitationalBody:
    mass: float = None
    position: tuple[int, int] = None
    surface_radius: int = None

    def __init__(self, mass: float, position: tuple[int, int], surface_radius: int):
        self.mass = mass
        self.position = position
        self.surface_radius = surface_radius


# all the planets and the moon ( alligned )
EARTH = GravitationalBody(5.972e24, (0, 0), 6_378_000)
MOON = GravitationalBody(7.34767309e22, (384_000_000, 0), 1_737_400)
SUN = GravitationalBody(2e30, (-1.5e11, 0), 696_340_000)
JUPITER = GravitationalBody(1.898e27, (628_730_000_000, 5), 69_911_000)
SATURN = GravitationalBody(5.68319e26, (1_275_000_000_000, 0), 58_232_000)
URANUS = GravitationalBody(8.68103e25, (2_723_950_000_000, 0), 25_362_000)
NEPTUNE = GravitationalBody(1.024e26, (4_351_400_000_000, 0), 24_622_000)
VENUS = GravitationalBody(4.86732e24, (-41_400_000_000, 0), 6_052_000)
MARS = GravitationalBody(6.41693e23, (78_340_000_000, 0), 3_390_000)
MERCURY = GravitationalBody(3.30104e23, (-91_691_000_000, 0), 2_440_000)

bodies = {
    "Earth": EARTH,
    "Moon": MOON,
    "Sun": SUN,
    "Jupiter": JUPITER,
    "Saturn": SATURN,
    "Uranus": URANUS,
    "Neptune": NEPTUNE,
    "Venus": VENUS,
    "Mars": MARS,
    "Mercury": MERCURY
}

# energy


def energy(x, y, vx, vy, body1: GravitationalBody, body2: GravitationalBody = None):
    G = 6.67428e-11

    numerator1 = -G*body1.mass

    denominator1 = get_distance((x, y), body1.position)

    if body2 is not None:
        numerator2 = -G*body2.mass
        denominator2 = get_distance((x, y), body2.position)
    else:
        numerator2 = 0
        denominator2 = 1
    PE = (numerator1/denominator1)+(numerator2/denominator2)
    KE = (1/2)*((vx)**2+(vy)**2)

    return PE+KE


def get_radius(position: tuple[int, int]) -> int:
    x = position[0]
    y = position[1]
    return np.sqrt(x ** 2 + y ** 2)


def get_distance(pos1: tuple[int, int], pos2: tuple[int, int]):
    x_dist = pos1[0] - pos2[0]
    y_dist = pos1[1] - pos2[1]
    return np.sqrt(x_dist ** 2 + y_dist ** 2)


def f_3(x, y, body1: GravitationalBody, body2: GravitationalBody = None):
    G = 6.67428e-11

    r = get_radius((x, y))

    #r1 = get_radius(body1.position)

    scalar1 = (x - body1.position[0])
    numerator1 = body1.mass * -G
    denominator1 = (get_distance((x, y), body1.position)) ** 3
    value1 = scalar1 * numerator1 / denominator1

    value2 = 0
    if body2 is not None:
        #r2 = get_radius(body2.position)
        scalar2 = (x - body2.position[0])
        numerator2 = body2.mass * -G
        denominator2 = (get_distance((x, y), body2.position)) ** 3
        value2 = scalar2 * numerator2 / denominator2

    return value1 + value2


def f_4(x, y, body1: GravitationalBody, body2: GravitationalBody = None):
    G = 6.67428e-11

    r = get_radius((x, y))

    r1 = get_radius(body1.position)

    scalar1 = (y - body1.position[1])
    numerator1 = body1.mass * -G
    denominator1 = (get_distance((x, y), body1.position)) ** 3
    value1 = scalar1 * numerator1 / denominator1

    value2 = 0
    if body2 is not None:
        r2 = get_radius(body2.position)
        scalar2 = (y - body2.position[1])
        numerator2 = body2.mass * -G
        denominator2 = (get_distance((x, y), body2.position)) ** 3
        value2 = scalar2 * numerator2 / denominator2

    return value1 + value2


def RK4(x0, y0, vx0, vy0, h, N, body1: GravitationalBody, body2: GravitationalBody = None):

    y = np.zeros(N, dtype=float)
    vx = np.zeros(N, dtype=float)
    vy = np.zeros(N, dtype=float)
    x = np.zeros(N, dtype=float)
    t = np.zeros(N, dtype=float)
    e = np.zeros(N, dtype=float)

    x[0], y[0], vx[0], vy[0] = x0, y0, vx0, vy0

    for i in range(0, N - 1):
        # collison
        if get_distance((x[i], y[i]), body1.position) <= body1.surface_radius or \
                (body2 is not None and get_distance((x[i], y[i]), body2.position) <= body2.surface_radius):
            if i == 0:
                vx[i] = 0
                vy[i] = 0
               # e[i] = energy(x[i], y[i], vx[i], vy[i], body1, body2)
            if i < N - 1:

                t[i + 1] = t[i] + h
                x[i + 1] = x[i]
                y[i + 1] = y[i]
                vx[i + 1] = 0.0
                vy[i + 1] = 0.0
                e[i+1] = energy(x[i], y[i], vx[i], vy[i], body1, body2)
            print("Collision!")
            print("time of Collision:")
            print(t[i])
            break
        # rugakutta
        t[i + 1] = t[i] + h
        e[i] = energy(x[i], y[i], vx[i], vy[i], body1, body2)
        k1x = vx[i]
        k1y = vy[i]
        k1vx = f_3(x[i], y[i], body1, body2)
        k1vy = f_4(x[i], y[i], body1, body2)

        k2x = vx[i] + k1vx * (h / 2)
        k2y = vy[i] + k1vy * (h / 2)
        k2vx = f_3(x[i] + ((h / 2) * k1x), y[i] +
                   ((h / 2) * k1y), body1, body2)
        k2vy = f_4(x[i] + ((h / 2) * k1x), y[i] +
                   ((h / 2) * k1y), body1, body2)

        k3x = vx[i] + k2vx * (h / 2)
        k3y = vy[i] + k2vy * (h / 2)
        k3vx = f_3(x[i] + ((h / 2) * k2x), y[i] +
                   ((h / 2) * k2y), body1, body2)
        k3vy = f_4(x[i] + ((h / 2) * k2x), y[i] +
                   ((h / 2) * k2y), body1, body2)

        k4x = vx[i] + k3vx * (h)
        k4y = vy[i] + k3vy * (h)
        k4vx = f_3(x[i] + ((h) * k3x), y[i] + (h * k3y), body1, body2)
        k4vy = f_4(x[i] + ((h) * k3x), y[i] + (h * k3y), body1, body2)

        x[i + 1] = (x[i] + (h / 6) * (k1x + 2 * k2x + 2 * k3x + k4x))
        y[i + 1] = (y[i] + (h / 6) * (k1y + 2 * k2y + 2 * k3y + k4y))
        vx[i + 1] = vx[i] + (h / 6) * (k1vx + 2 * k2vx + 2 * k3vx + k4vx)
        vy[i + 1] = vy[i] + (h / 6) * (k1vy + 2 * k2vy + 2 * k3vy + k4vy)
    #e[-1] = energy(x[-1], y[-1], vx[-1], vy[-1], body1, body2)
    return x, y, vx, vy, e, t


def info():
    print("Welcome to the 2 body rocket path sim \n")
    print("We use the ruga-kutta4 Methods to approximate the path \n")
    print("all the bodies are on 0 y \n")
    print("I decided not to use the z axis but it is reasonably easy done \n")
    print("manhattan distance vs Euclidean distance was thought a tiny bit about \n")
    print("the bodies do not orbit due to the fact this is really complex for the coder and the computer \n ")
    print("animation would be much better than this static plot and is something i want to include \n")
    print("\n now we will talke about the options: 2,models the space station, however the space station does course corrections we will not \n")
    print("\n option 3: this shows the moon fly by photography mission ")
    print("\n option 4: this lets you pick what you want to do, its janky but cool ")
    print("\n option 4 lets your create comets etc ")
    print("\n i have allowed energy consevation to show")
    print("\n  ")


def space_station():
    print("Space Station")
    print("Space Station values are y=420_000 ABOVE EARTH , vy or vx=7.70*1000")
    x, y, vx, vy, e, t = RK4(0, 420_000+6_378_000, 7.70*1000,
                             0, 1, 100_00, EARTH)
    plt.xlabel("x_postion(m)")
    plt.ylabel("y_postion(m)")
    plt.plot(x, y)

    #body1 = plt.Circle(EARTH.position, EARTH.surface_radius)
    #fig, ax = plt.subplots()
    # ax.add_patch(body1)
    plt.show()


def moon_and_back():
    print("Moon and Back")
    #body1mass = input("...")
    # by trial and error this is a moon fly by with near by earth return
    x, y, vx, vy, e, t = RK4(-6.8e6, 0, 0, -10720, 30, 100_000, EARTH, MOON)
    #x, y, vx, vy = RK4(0, 8_000_000, 15000, 1500, 0.5, 150000, EARTH, MOON)

    body1 = plt.Circle(EARTH.position, EARTH.surface_radius)
    body2 = plt.Circle(MOON.position, MOON.surface_radius)
    fig, ax = plt.subplots()
    plt.xlabel("x_postion(m)")
    plt.ylabel("y_postion(m)")
    ax.add_patch(body1)  # add where moon and earth is
    ax.add_patch(body2)

    plt.plot(x, y)
    plt.show()

    # plt.plot(t, e)  # enegry agaisnt time
    # plt.show()


def rk4_option():
    # lets you pick values for rk4 , messy
    while True:
        try:
            x = float(
                input("Enter the initial x position of the rocket relative to first body : \n"))
            break
        except ValueError:
            print("Invalid input! Please enter a valid float.\n")
    while True:
        try:
            y = float(
                input("Enter the initial y position of the rocket relative to first body: \n"))
            break
        except ValueError:
            print("Invalid input! Please enter a valid float.\n")
    while True:
        try:
            vx = float(input("Enter the initial x velocity of the rocket: \n"))
            break
        except ValueError:
            print("Invalid input! Please enter a valid float.\n")
    while True:
        try:
            vy = float(input("Enter the initial y velocity of the rocket: \n"))
            break
        except ValueError:
            print("Invalid input! Please enter a valid float.\n")
    return x, y, vx, vy


def pick_your_bodies():
    print("now you will pick from a list")

    gravity_sources = {
        "Earth": EARTH,
        "Moon": MOON,
        "Sun": SUN,
        "Jupiter": JUPITER,
        "Saturn": SATURN,
        "Uranus": URANUS,
        "Neptune": NEPTUNE,
        "Venus": VENUS,
        "Mars": MARS,
        "Mercury": MERCURY

    }
# lists creating options
    print("Select the first gravity source:")
    for i, source in enumerate(gravity_sources):
        print(f"{i+1}. {source}")
    while True:
        try:
            source1_idx = int(
                input("Enter the index of the first gravity source: ")) - 1
            body1 = gravity_sources[list(gravity_sources.keys())[source1_idx]]
            break
        except (ValueError, IndexError):
            print("Invalid input! Please enter a valid index.\n")

    print("Select the second gravity source:")
    available_sources = [source for i, source in enumerate(
        gravity_sources) if i != source1_idx]+["NONE"]
    for i, source in enumerate(available_sources):
        print(f"{i+1}. {source}")
    while True:
        try:
            source2_idx = int(
                input("Enter the index of the second gravity source: ")) - 1
            if source2_idx == 9:
                body2 = None
            else:
                body2 = gravity_sources[available_sources[source2_idx]]
            break
        except (ValueError, IndexError):
            print("Invalid input! Please enter a valid index.\n")
    x, y, vx, vy = rk4_option()
    return x, y, vx, vy, body1, body2


def menu(choices: list[str]) -> int:
    for idx, choice in enumerate(choices):
        idx += 1
        idx = str(idx)
        while len(idx) < len(str(len(choices))):
            idx = "0" + idx
        print(f"{idx}) {choice}")
    while True:
        response = input("Choice: ")
        try:
            response = int(response)
            if 1 <= response <= len(choices):
                return response
        except ValueError:
            continue


# menu
choice_ = menu([
    "Info",
    "Space Station",
    "Moon and Back",
    "Pick your bodies"
])
if choice_ == 1:
    info()
elif choice_ == 2:
    space_station()
elif choice_ == 3:
    moon_and_back()
elif choice_ == 4:

    x, y, vx, vy, body1, body2 = pick_your_bodies()
    x, y, vx, vy, _, _ = RK4(
        body1.position[0]+x, body1.position[1]-y, vx, vy, 0.5, 200_000, body1, body2)
    # change h,N for time of calculation
    plt.xlabel("x_postion(m)")
    plt.ylabel("y_postion(m)")
    plot_body1 = plt.Circle(
        body1.position, body1.surface_radius,)
    if body2 is not None:
        plot_body2 = plt.Circle(
            body2.position, body2.surface_radius,)

    fig, ax = plt.subplots()
    ax.add_patch(plot_body1)
    if body2 is not None:
        ax.add_patch(plot_body2)

    ax.plot(x, y)
    print("enjoy your path")
    print("if you want to run thecode for long , reduce h and or increase t . smaller h makes it less accurate though")
    plt.show()
