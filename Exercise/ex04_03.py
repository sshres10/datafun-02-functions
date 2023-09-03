# Exercise 4.3
def cube(x):
    """Calculate the cube of x."""
    x ** 3

print('The cube of 2 is', cube(2))

## The problem is it does not return any value. If a function doesn't have a return satement, it returns none by default 

def cube(x):
    """Calculate the cube of x."""
    return x ** 3

print('The cube of 2 is', cube(2))


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
