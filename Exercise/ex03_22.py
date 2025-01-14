# Exercise 3.22
for i in range(2):
    value = int(input('Enter an integer (-1 to break): '))
    print('You entered:', value)
    
    if value == -1:
        break
else:
    print('The loop terminated without executing the break')

## if we enter -1 it break stament will be executed and loop is terminated.
## if we enter any other value, the loop continues to the next iteration. 
## After the for loop has completed all its iterations, the else clause is executed. 

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
