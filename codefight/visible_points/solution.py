#!/usr/bin/env python

from math import degrees, atan2


def visiblePoints(points):
    ''' Caterpillar method over the sorted list of angles '''
    npoints = len(points)

    # exit fast on corner cases
    if npoints <= 1: return npoints

    angles = sorted(map(to_angle, points))

    head = 0
    max_len = cur_len = 1

    for tail in xrange(npoints):
        while cur_len <= npoints and (angles[head] - angles[tail]) % 360 <= 45:
            max_len = max(cur_len, max_len)
            head = (head + 1) % npoints
            cur_len += 1
        cur_len -= 1
    return max_len


def to_angle(point):
    x, y = point[0], point[1]
    return degrees(atan2(y, x)) % 360

