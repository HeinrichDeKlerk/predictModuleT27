def five_num_summary(items):
    '''
    This function takes one argument. a list of numbers and computes the five number summary on that list.
    that means it calculates the max, min, median, first quartile, and third quartile and returns a dictionary
    with those values.

        '''

    for num in items:
        s_list = sorted(items)
        n_max = np.max(s_list)
        n_med = np.median(s_list)       
        n_q1 = np.percentile(s_list, 25)
        n_min = np.min(s_list)
        n_q3 = np.percentile(s_list, 75)
        
        D = { "max":n_max, "median":n_med, "min":n_min, "q1":n_q1, "q3":n_q3}
    return D
