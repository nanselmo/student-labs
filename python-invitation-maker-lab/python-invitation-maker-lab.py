
### Challenge 1 (using str.replace):
#Ron plans to have his party on May 18th, 1997 (Sunday).
#In `invitation.py` use chained str.replaces to customize the invitation
#Remember to use puts to output your solution to the screen.


percy_invitation = "The family of Percy Weasley proudly invite you to their graduation commencement on Saturday the 22nd of May 1993. Festivities will be held at The Burrow. See you then!"

ron_invitation= percy_invitation.replace("Saturday the 22nd of May 1993","Sunday the 18th of May 1997")

print ron_invitation

### Challenge 2 (using string interpolation):
#It's 1998 and time for Ginny's graduation.
#Ron wants to help his little sis out. Instead of using str.replace,
#let's use string interpolation to change the content of the invitation.
#Now that you know what string interpolation is, assign the following content from Percys invitation to variables in ginnys invitation

#1. name, 'Percy'
#2. the day, 'Saturday'
#3. the date, '22nd'
#4. the year, '1993'


#Now that we have Percy's information, it's time to change the
#value of these variables to reflect Ginny's info.
#Ginny plans to have her party on May 17th, 1998 (Sunday).

#Use string interpoloation and the variables you
#just created to customize Percy's invitation for Ginny.
#As in Challenge 1, you'll want to use puts to print out your
#solution to the screen.

name= "Ginny"
date="17th of May"
year="1998"
day= "Sunday"

ginny_invitation = "The family of %s Weasley proudly invite you to their graduation commencement on %s %s %s. Festivities will be held at The Burrow. See you then!" % (name, day, date, year)

print ginny_invitation
