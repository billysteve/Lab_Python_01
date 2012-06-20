#A PROGRAM TO CALCULATE THE DAY OF THE WEEK A DATE FELL OR WILL FALL
import math

"""A = the month of the year
   B = the day of the month
   C = the year of the cemtury
   D = the century
   """
print"enter any date: "
print" Enter the month 1-12 where march = 1,........febuary =12: "
A = raw_input("Month ")
A = int(A)
B=raw_input("Day? ")
B = int(B)
year = raw_input("Year? ")

D=year[-4:-2]
D = int(D)
C=year[-2:]
C= int(C)

#computing the day of the week
if (A == 11 or A == 12): 
 C = C-1
 W = (13*A-1)/5
 X = C/4
 Y = D/4
 Z = W+X+Y+B+C-2*D
 R = Z%7
else:
  W = (13*A-1)/5
  X = C/4
  Y = D/4
  Z = W+X+Y+B+C-2*D
  R = Z%7
#outputing the day of the week
if R < 0: R = R + 7
if R == 0: print "Sunday "
if R == 1: print "Monday "
if R == 2: print "Tuesday "
if R == 3: print "Wednesday "
if R == 4: print "Thursday "
if R == 5: print "Friday "
if R == 6: print "Saturday "


