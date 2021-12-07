def best_match(goals1, goals2):
    goalDiff = 0
    closestGoal = 0
    closestIndex = 0
    goalDiffRatio = 0

    for count in range(len(goals1)):

    # check for closest score

        goalDiff = goals2[count] - goals1[count]
        
        #Set first as highest
        if(count == 0):
            goalDiffRatio = goals2[count] / (goals2[count] + goals1[count])
            closestGoal = goalDiff
        
        else:
            #if previous closest score is bigger than current save it
            if(goalDiff > closestGoal):

                closestGoal = goalDiff
                goalDiffRatio = goals2[count] / (goals2[count] + goals1[count])
                closestIndex = count

            #if previous and current are same check for highest goal2 to goal 1 ratio(For goal2 highest score)
            elif(goalDiff == closestGoal):
                if(goals2[count] / (goals2[count] + goals1[count]) > goalDiffRatio and goals2[count] / (goals2[count] + goals1[count]) != 0):

                    closestGoal = goalDiff
                    goalDiffRatio = goals2[count] / (goals2[count] + goals1[count])
                    closestIndex = count
                    
    return closestIndex


print(best_match([18, 6, 11, 2, 16, 13, 15, 16], [9, 0, 3, 0, 7, 10, 5, 8]))
