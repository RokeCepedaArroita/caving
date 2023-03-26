def ascent_time(rope_length, n_cavers, n_rebelays=0, ascent_speed=7, transition_time=2):
    ''' Ascent or descent simulator: calculates the time it would take for a party of cavers
        to ascend or descend a rope with a number of equally spaced rebelays.

        Parameters:
        rope_length (float): the total length of the rope in meters
        n_cavers (int): the number of cavers in the group
        n_rebelays (int): number of rebelays. 0 means that no rebelays are set up (i.e., the full length is climbed)
        ascent_speed (float, optional): the ascent or descent speed in meters per minute (default is 7 for ascent, 70 is suggested for descent)
        transition_time (float, optional): the time it takes for a caver to transition from one rebelay to the next in minutes (default is 2)

        Returns:
        total_time (float): the total time taken by the group to complete the ascent or descent        '''

    # Check input
    if not isinstance(n_cavers, int) or n_cavers < 1:
        raise ValueError('n_cavers must be an integer of at least 1')

    # Calculate length of each rebelay section
    if n_rebelays > 0:
        section_length = rope_length / (n_rebelays + 1)
    else:
        section_length = rope_length

    # Calculate time for each caver to ascend one section and transition to next section
    section_time = (section_length / ascent_speed) + transition_time

    # Calculate time for the first caver to ascend entire length of rope
    leader_time = section_time * (n_rebelays + 1)

    # Add one additional section for every other caver in the group
    total_time = leader_time + section_time * (n_cavers - 1)

    # Return total time in minutes
    return total_time
