"""
Title: main code file
Author: Braeden Dirksen
Date: oct 10
"""

from functions import *

print("""
                             ___
                            /   |
                           /__  |
                             |  |
                             |  |
                             |  |
                           __|  |__
                          |________|
       |--
       |   \                     
       |____\                           
       |                                
       |                               
_______|___|''''''''''|  o     o 
        |  |..........|\              o
        |________|      \\                o      
------------------------/~~~~~~~~~~~~~~~~~~~o~~~~~~~~  

""")



print("""


                            ________
                           /  __    |        
                          |__|  |   |
                               /   /
                             /   /
                           /   /____
                          |_________|     
                            

       |--                                                  --|  
       |   \                        o                     /   |          
       |____\               o               o            /____|  
       |         .'\   o                         o            |          
       |       .'  .\                                         |          
_______|____.'   .'____                            __o________|__________     
        |   '. .'|     \                          /                      |
   0    |________|  0   \                        /   0     0      0     0|
------------------------/~~~~~~~~~~~~~~~~~~~~~~~~\-----------------------|
""")

print("""


                             ________                           
                            /  ___   |
                           |__/   |  |
                                __|  |
                               |__   |  
                            __    |  |            
                           |  \___|  |   
                            \________|

       |--                                                    
       |   \                        o                                       
       |____\               o               o                           
       |         .'\   o                         o        --|                       
       |       .'  .\                                    /__|                          
_______|____.'   .'____                             o       |            
        |   '. .'|     \                                    |                    
   0    |________|  0   \                            /o-----|-----|
                         \                          /             |      
-------------------------/~~~~~~~~~~~~~~~~~~~~~~~~~~\-------------|                    
""")












### code starts here ###
print("which scenario do you want to do? ")
scen = convint(inputs())
if scen == 1:
        print("what is the speed of the cannon ball as it leaves the cannon?")
        speed = convint(inputs())
        print("how far above the water is the cannon?")
        height = convint(inputs())
        print("the distance the cannon ball went is", scen1calc(speed, height))
elif scen == 2:
        print("what is the speed of the cannon ball as it leaves the cannon?")
        speed = convint(inputs())
        print("what is the angle of the cannon from the horizontal?")
        angle = convint(inputs())
else:
        print("what is the angle of the cannon from the horizontal?")
        angle = convint(inputs())
        print("how much taller is ur ship then the other ship?")
        height = convint(inputs())
        print("what is the speed of the cannon ball as it leaves the cannon?")
        speed = convint(inputs())
        print("the distance the cannon ball travels would be", scen3calc(speed, angle, height))
