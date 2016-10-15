#!/usr/bin/env python
import sys


# FIXME: Runtime error
def sieve_range(start, end):
    uncrossed = [True] * (end + 1)
    uncrossed[0] = uncrossed[1] = False
    for p in xrange(2, end + 1):
        if p * p > end:
            break
        if uncrossed[p]:
            for i in xrange(p**2, end + 1, p):
                uncrossed[i] = False

    for num in xrange(start, end + 1):
        if uncrossed[num]:
            print num


if __name__ == "__main__":
    no_of_tcs = int(sys.stdin.readline())
    for tc in xrange(no_of_tcs):
        # TODO: Could find max of all tc ranges, find all the primes from
        # 2 - max, then all the other tcs are subsets of that. No need to redo???
        m, n = sys.stdin.readline().split()
        sieve_range(int(m), int(n))
        print ""
