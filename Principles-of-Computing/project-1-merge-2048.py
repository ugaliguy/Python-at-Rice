"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = []
    merge_line = []
    merged = False
    indx2 = 0

    for indx1 in range(len(line)):
        new_line.append(0)
        
    for indx1 in range(len(line)):
        if (line[indx1] != 0):
            new_line[indx2] = line[indx1]
            indx2 += 1

    for indx1 in range(len(line) - 1):
        if(new_line[indx1] != 0):
            if ((new_line[indx1] == new_line[indx1+1]) and (merged == False)):
                merge_line.append(2*new_line[indx1])
                merged = True
            elif ((new_line[indx1] != new_line[indx1+1]) and (merged == False)):     
                merge_line.append(new_line[indx1])
            elif (merged == True):
                merged = False
        else:
            merged = True

    if ((new_line[-1] != 0) and (merged == False)):
        merge_line.append(new_line[-1]) 
    
    while (len(merge_line) < len(line)):
        merge_line.append(0)

    return merge_line

