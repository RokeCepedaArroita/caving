from ascent_time import ascent_time
from optimum_rebelay import optimum_rebelay, optimum_rebelay_both_ways


def plot_ascent_times(rope_length, n_cavers, ascent_speed=7, transition_time=2, max_number_rebelays=100):
    """
    Plots the ascent times as a function of the length of a section (i.e., the rebelay length).

    Parameters:
    rope_length (float): the total length of the rope in meters
    n_cavers (int): the number of cavers in the group
    ascent_speed (float, optional): the ascent speed in meters per minute (default is 7)
    transition_time (float, optional): the time it takes for a caver to transition from one rebelay to the next in minutes (default is 2)
    max_number_rebelays (int, optional): the maximum number of rebelays to compute (default is 100)

    Example usage:
    plot_ascent_times(rope_length=100, n_cavers=4, ascent_speed=7, transition_time=2)
    """

    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.interpolate import interp1d

    # Set the range of rebelay numbers to iterate over
    n_rebelays_range = range(0, max_number_rebelays)

    # Iterate over the range of rebelay numbers and calculate ascent times
    ascent_times = []
    rebelay_lengths = []
    for n_rebelays in n_rebelays_range:
        rebelay_length = rope_length / (n_rebelays + 1)
        rebelay_lengths.append(rebelay_length)
        time = ascent_time(rope_length, n_cavers, n_rebelays, ascent_speed, transition_time)
        ascent_times.append(time)

    # Find the minimum ascent time and the corresponding rebelay length using cubic interpolation
    f = interp1d(rebelay_lengths, ascent_times, kind='cubic')
    x_new = np.linspace(min(rebelay_lengths), max(rebelay_lengths), num=1000, endpoint=True)
    y_new = f(x_new)
    optimum_rebelay_length = round(x_new[np.argmin(y_new)], 1)

    # Plot the ascent times vs. the length of each rebelay section
    fig, ax = plt.subplots()
    ax.plot(rebelay_lengths, ascent_times)
    ax.set_xlabel('Rebelay length (meters)')
    ax.set_ylabel('Ascent time (minutes)')
    ax.set_title('Ascent time vs. Rebelay length')
    ax.set_ylim([0.9*np.min(ascent_times), ascent_times[0]])
    ax.set_xlim([0, rope_length])
    ax.axvline(x=optimum_rebelay_length, color='r', linestyle='--', label='Optimum rebelay length: {:.1f} meters'.format(optimum_rebelay_length))
    ax.legend()

    # Add a text box with the caver group size
    textstr = f'Caver group size: {n_cavers}'
    props = dict(boxstyle='round', facecolor='white', alpha=0.8)
    plt.text(0.7, 0.95, textstr, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=props)

    # Show
    plt.show()




def plot_optimum_rebelay_length_both_ways(rope_length, max_cavers, ascent_speed=7, descent_speed=70, transition_time=2, max_rebelays=100):
    """
    Plots the optimum rebelay length as a function of the number of cavers for ascent, descent and both ways.

    Parameters:
    rope_length (float): the total length of the rope in meters
    max_cavers (int): the maximum number of cavers in the group
    ascent_speed (float, optional): the ascent speed in meters per minute (default is 7)
    descent_speed (float, optional): the descent speed in meters per minute (default is 70)
    transition_time (float, optional): the time it takes for a caver to transition from one rebelay to the next in minutes (default is 2)
    max_rebelays (int, optional): the maximum number of rebelays to compute (default is 100)

    Example usage:
    plot_optimum_rebelay_length_both_ways(rope_length=80, max_cavers=8, transition_time=2, max_rebelays=100)
    """

    import matplotlib.pyplot as plt
    import numpy as np

    # Compute ascent

    # Set the range of cavers and iterate over them to find the optimum rebelay length for each group size
    cavers_range = range(1, max_cavers+1)
    optimum_rebelay_lengths = []
    for n_cavers in cavers_range:
        optimum_rebelay_length = optimum_rebelay(rope_length, n_cavers, ascent_speed, transition_time, max_rebelays)
        optimum_rebelay_lengths.append(optimum_rebelay_length)
    # Plot the optimum rebelay length vs. the number of cavers
    fig, ax = plt.subplots()
    sc1 = ax.scatter(cavers_range, optimum_rebelay_lengths, color='#FF0000', marker='^', label='Ascent')


    # Compute both

    # Set the range of cavers and iterate over them to find the optimum rebelay length for each group size
    cavers_range = range(1, max_cavers+1)
    optimum_rebelay_lengths = []
    for n_cavers in cavers_range:
        optimum_rebelay_length = optimum_rebelay_both_ways(rope_length, n_cavers, ascent_speed, descent_speed, transition_time=2, max_number_rebelays=100)
        optimum_rebelay_lengths.append(optimum_rebelay_length)
    # Plot the optimum rebelay length vs. the number of cavers
    sc2 = ax.scatter(cavers_range, optimum_rebelay_lengths, color='#000000', marker='d', label='Both')


    # Compute descent

    # Set the range of cavers and iterate over them to find the optimum rebelay length for each group size
    cavers_range = range(1, max_cavers+1)
    optimum_rebelay_lengths = []
    for n_cavers in cavers_range:
        optimum_rebelay_length = optimum_rebelay(rope_length, n_cavers, descent_speed, transition_time, max_rebelays)
        optimum_rebelay_lengths.append(optimum_rebelay_length)
    # Plot the optimum rebelay length vs. the number of cavers
    sc2 = ax.scatter(cavers_range, optimum_rebelay_lengths, color='#0037FF', marker='v', label='Descent')


    # Complete the figure
    ax.set_xlabel('Number of cavers')
    ax.set_ylabel('Best rebelay length (m)')
    ax.set_ylim([0, rope_length])
    ax.set_title(f'Rope Length = {rope_length} m')
    plt.legend()
    ax.grid(True, linestyle='--')
    plt.show()


plot_optimum_rebelay_length_both_ways(rope_length=80, max_cavers=8, transition_time=2, max_rebelays=100)
