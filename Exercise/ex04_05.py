# Exercise 4.5

def seconds_since_midnight(hour, minute, second):
    hour_in_seconds = hour * 3600
    minute_in_seconds = minute * 60
    return hour_in_seconds + minute_in_seconds + second

print('the total calc is', seconds_since_midnight(13, 30, 45))

""" we define the seconds_since_midnight function. 
Then, we call the function with the arguments 13, 30, and 45, representing the time 1:30:45 PM."""

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
