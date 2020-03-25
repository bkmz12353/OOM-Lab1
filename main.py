import numpy as np
import matplotlib.pyplot as plt


def x(t):
    return ((iv * m * np.cos(phi_rad)) / wa) * (1 - np.exp(-(wa * t) / m))


def y(t):
    return ((m * (iv * np.sin(phi_rad) * wa + m * g)) / pow(wa, 2)) * (1 - np.exp((-wa * t) / m)) - ((m * g * t) / wa)


g = 9.8
print("Имеются заданные плотности материалов:")

materials = {
    "Аллюминий": 2700,
    "Сталь": 7800,
    "Платина": 21460
}

material_number = 1

for key, value in materials.items():
    print(material_number, "-", key, value)
    material_number += 1

print("\nВыберите материал или введите 0 для ручного ввода плотности: ", end="")

material_number = int(input())

if material_number != 0:
    rho = list(materials.values())[material_number - 1]
else:
    rho = int(input("Введите плотность: "))

iv = int(input("Введите начальную скорость: "))  # initial velocity
r = float(input("Введите радиус шара: ").replace(",", "."))
phi = int(input("Введите угол вылета: "))

# iv = 30
# r = 0.02
# phi = 45
# rho = 7800

phi_rad = phi * np.pi / 180
m = (4 / 3) * rho * np.pi * pow(r, 3)
wa = 0.4  # windage

x_data = []
y_data = []
t = 0

while y(t / 1000) >= 0:
    x_data.append(x(t / 1000))
    y_data.append(y(t / 1000))
    t += 1

print("\nВремя полета (с) =", t / 1000)
print("Дальность полёта (м) =", round(x(t), 2))

plt.style.use("dark_background")
plt.plot(x_data, y_data, color="w")
plt.xlabel("Дальность (м)")
plt.ylabel("Высота (м)")
params = np.round([iv, m, phi], 2)
plt.title("Начальная скорость = {}. Масса = {}. Угол вылета = {} ".format(*params))

plt.show()
