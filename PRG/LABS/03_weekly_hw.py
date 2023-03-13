def compute_time_diff(h1, m1, h2, m2):
    ''' Returns the values of hours and minutes of the time difference

    Parameters:
        h1 - the value in hours of the first time
        m1 - the value in minutes of the first time
        h2 - the value in hours of the second time
        m2 - the value in minutes of the second time
    Returns:
        hour - the value of the time diff in hours
        min - the value of the time diff in minutes
    '''
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    if t1 > t2:          # in the case when t1 is larger than t2
        t = t1 - t2
    else:                # in the case when t2 is greater than t1
        t = t2 - t1
    hour = t // 60
    min = t % 60
    return hour, min

if __name__ == "__main__":
    h, m = compute_time_diff(13, 20, 15, 10)
    print(h, m)
