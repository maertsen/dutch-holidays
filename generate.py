#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name		generate.py
Description	...
Author		Pander <pander@users.sourceforge.net>
License		...

0.1 2013-05-10	Pander <pander@users.sourceforge.net>
Initial release
"""

import os

kalender = open('NederlandseFeestdagen.ics', 'w')
calendar = open('DutchHolidays.ics', 'w')

calendar_header= open('calendar-header.txt', 'r')
for line in calendar_header.readlines():
    kalender.write(line)
    calendar.write(line.replace('NederlandseFeestdagen', 'DutchHolidays'))

holiday_header = ''
event_header= open('event-header.txt', 'r')
for line in event_header.readlines():
    holiday_header += line

holiday_footer = ''
event_footer= open('event-footer.txt', 'r')
for line in event_footer.readlines():
    holiday_footer += line

directory = 'scripted-holidays'
for holiday_file in sorted(os.listdir(directory)):
    if holiday_file.endswith(".txt"):
        holiday = open(directory+ '/' + holiday_file,'r')
        (naam, name) = holiday_file[:-4].split('_')
        kalender.write(holiday_header.strip()+naam+'\n')
        calendar.write(holiday_header.strip()+naam+' ('+name+')\n')
        for line in holiday.readlines():
            kalender.write(line)
            calendar.write(line)
        kalender.write(holiday_footer)
        calendar.write(holiday_footer)

calendar_footer= open('calendar-footer.txt', 'r')
for line in calendar_footer.readlines():
    kalender.write(line)
    calendar.write(line)