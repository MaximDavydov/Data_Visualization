import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(num_points=5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('dark_background')
    # plt.style.use('classic')
    # Ф-ия figsize управляет размером окна, dpi - разрешение экрана
    fix, ax = plt.subplots(figsize=(15, 7), dpi=103)
    point_numbers = range(rw.num_point)

    #zorder - номер фона по списку
    ax.plot(rw.x_values, rw.y_values, linewidth=3, zorder=1)

    # edgecolor - цвет края точек, учитывается в теме
    # с - по каким точкам будет задаваться цвет
    # ax.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.PuOr, edgecolor='none')
    # zorder - на передний план


    # Emphasize the first and last points.
    ax.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=100, zorder=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100, zorder=2)


    # Remove the axes.
    # Удаление оси с графиков - методы ax.get_x(y)axis переводят флаг видимости
    ax.get_xaxis().set_visible(True)
    ax.get_yaxis().set_visible(True)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break