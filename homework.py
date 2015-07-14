#Course: PFAB Homework #01
#Date: 20150714
#Student:  Will Guest
#
#filename: homework.py
#
#_____Code starts below this line_____
 
import math
 
first = "Will"
last = "Guest"
age = 55
print " "
print first, last, age
 
sideA = 12.55
sideB = 17.85
sideC = math.sqrt((sideA * sideA) + (sideB * sideB))
print ""
print "Side C would be equal to", sideC ,"!"
 
operand1 = 95
operand2 = 64.5
 
print ""
print "95 + 64.5 = ", operand1 + operand2
print "95 - 64.5 = ", operand1 - operand2
print "95 x 64.5 = ", operand1 * operand2
print "95 / 64.5 = ", operand1 / operand2
print "95% of 65.5 = ", .95 * operand2
 
print ""
print "(...But I was told there would be no math!)"
 
#My implementation is the best because, well, just *because*.  Seriously, though, it's an effective choice because if (for example) one of the operands' value 
#were to change, my code would run "as-is" (that is, correctly, without error, and with no changes being made). 
#It would be a really good idea to include the "import math" command in the lesson.  Kind of a big omission there, but Mr. Google likes me, so, not so terrible.
