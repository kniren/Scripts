#!/usr/bin/python -tt
f = open("/sys/class/power_supply/BAT0/charge_full")
q = open("/sys/class/power_supply/BAT0/charge_now")
CFULL = int(f.readline())
CNOW = int(q.readline())
PERC = ('{0:.0f}'.format(CNOW*100/CFULL))
print(PERC)
