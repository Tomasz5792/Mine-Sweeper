

#import
import random

#variables
minefield_input = []
number_of_mines = 10
minefield_lengh = 6
minefield_height = 5


def create_minefield(minefield_input, minefield_lengh, minefield_height):               #create empty minefeild

    #variables
    minefield_input = []        #to reset minefield_input

    minefield_input = [["-"]*minefield_lengh for x in range(minefield_height)]  #list comprehension because a while loop didn't work.  I think because it copied the same lengh list height times.

    return minefield_input

def view_minefield(minefield_input):                                                    #veiw minefeild
    for lengh in minefield_input:
        for height in lengh:
            print(f"{height:<3}",end="")
        print("")
    
def add_mines(minefield_input, number_of_mines, minefield_lengh, minefield_height):     #add mines to minefield
    
    #variables
    mines_added = 0
    
    while mines_added < number_of_mines:

        if any("-" in sublist for sublist in minefield_input) == True:       #while minefield_input still has a space for a mine, doesnt error if you add more mines than spaces.

            lengh = random.randint(0,minefield_lengh-1)
            height = random.randint(0,minefield_height-1)

            if minefield_input[height][lengh] == "-":
                minefield_input[height][lengh] = "#"

                mines_added = mines_added + 1

        else:
            mines_added = mines_added + 1

    return minefield_input
    
def add_numbers(minefield_input, minefield_lengh, minefield_height):                    #add numbers to minefield

    for height in range(0, minefield_height):
        for lengh in range(0, minefield_lengh):
            
            if minefield_input[height][lengh] == "-":
                minefield_input[height][lengh] = 0

            if minefield_input[height][lengh] == "#":
                pass

            else:
                if height > 0 and minefield_input[height-1][lengh] == "#":                                      #mine above
                    minefield_input[height][lengh] = minefield_input[height][lengh] + 1 
                
                if height < minefield_height-1 and minefield_input[height+1][lengh] == "#":                     #mine below
                    minefield_input[height][lengh] = minefield_input[height][lengh] + 1

                if lengh > 0 and minefield_input[height][lengh-1] == "#":                                       #mine left
                    minefield_input[height][lengh] = minefield_input[height][lengh] + 1 
                
                if lengh < minefield_lengh-1 and minefield_input[height][lengh+1] == "#":                       #mine right
                    minefield_input[height][lengh] = minefield_input[height][lengh] + 1
                
                if height > 0 and lengh > 0 and minefield_input[height-1][lengh-1] == "#":                      #mine top left
                    minefield_input[height][lengh] = minefield_input[height][lengh] + 1

                if height > 0 and lengh < minefield_lengh-1 and minefield_input[height-1][lengh+1] == "#":      #mine top right
                    minefield_input[height][lengh] = minefield_input[height][lengh] + 1

                if height < minefield_height-1 and lengh > 0 and minefield_input[height+1][lengh-1] == "#":     #mine bottom left
                    minefield_input[height][lengh] = minefield_input[height][lengh] + 1

                if height < minefield_height-1 and lengh < minefield_lengh-1 and minefield_input[height+1][lengh+1] == "#":     #mine bottom right
                    minefield_input[height][lengh] = minefield_input[height][lengh] + 1
    
    return minefield_input


minefield_input = create_minefield(minefield_input, minefield_lengh, minefield_height)  #create empty minefeild

minefield_input = add_mines(minefield_input, number_of_mines, minefield_lengh, minefield_height)    #add mines to minefeild

print("Input")
view_minefield(minefield_input)                                                         #print input minefield

minefield_input = add_numbers(minefield_input, minefield_lengh, minefield_height)       #add numbers to minefield

print("")
print("Output")
view_minefield(minefield_input)                                                         #print output minefield
