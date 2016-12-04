#! /usr/bin/env python3

import time

t_format = "%d/%m/%Y_%H:%M"

def main():

    fin = open('output.db.txt', 'r')
    fout = open ('anal.out.txt', 'w')
    data = []

    for l in fin.readlines():
        e = l.split('\t')
        data.append(( int(e[0]), int(e[1]) ))

    dep = []
    (n_prev, t_prev) = data[0]         # previous number of post
    for t in data[1:]:
        dn, dt = t[0] - n_prev, t[1] - t_prev
        speed = dn/dt
        fout.write("{}\t{}\t{}\n".format(t[1],
                                         time.strftime(t_format,
                                                       time.gmtime(t[1])),
                                         speed))

if __name__ == "__main__":
    main()

# set timefmt "%d/%m/%Y_%H:%M"
# set xdata time
# plot "anal.out.txt" using 2:3 with lines
