def format_time(time):

    """
    Function to format time

    :param time: time in seconds

    :return: tuple:  (time, time unit)
    """

    if 0.0001 < time < 1:
        return time * 1000, 'ms'

    elif time < 0.0001:
        return time * 1000000, 'us'

    else:
        return time, 's'
