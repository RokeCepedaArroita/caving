from ascent_time import ascent_time


def optimum_rebelay(rope_length, n_cavers, ascent_speed=7, transition_time=2, max_number_rebelays=100):
    """
    Finds the optimum rebelay length that minimizes the ascent OR descent time.

    Unique parameters:
    max_number_rebelays (int, optional): the maximum number of rebelays to compute (default is 100)

    Returns:
    optimum_rebelay_length (float): the optimum rebelay length in meters that minimizes the ascent time
    """

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

    return optimum_rebelay_length



def optimum_rebelay_both_ways(rope_length, n_cavers, ascent_speed=7, descent_speed=70, transition_time=2, max_number_rebelays=100):
    """
    Finds the optimum rebelay length that minimizes the COMBINED descent and ascent time.

    Unique parameters:
    max_number_rebelays (int, optional): the maximum number of rebelays to compute (default is 100)

    Returns:
    optimum_rebelay_length (float): the optimum rebelay length in meters that minimizes the ascent time
    """

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
        time_up = ascent_time(rope_length, n_cavers, n_rebelays, ascent_speed, transition_time)
        time_down = ascent_time(rope_length, n_cavers, n_rebelays, descent_speed, transition_time)

        ascent_times.append(time_up+time_down)

    # Find the minimum ascent time and the corresponding rebelay length using cubic interpolation
    f = interp1d(rebelay_lengths, ascent_times, kind='cubic')
    x_new = np.linspace(min(rebelay_lengths), max(rebelay_lengths), num=1000, endpoint=True)
    y_new = f(x_new)
    optimum_rebelay_length = round(x_new[np.argmin(y_new)], 1)

    return optimum_rebelay_length
