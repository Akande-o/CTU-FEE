def combine_dict(d1, d2):
    comb_d = dict(d1)
    for key in d2.keys():
        if key in comb_d:
            comb_d[key] += d2[key]
        else:
            comb_d[key] = d2[key]
    return comb_d
if __name__ == "__main__":
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}
    print(combine_dict(d1, d2))
 