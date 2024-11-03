import csv
import pandas as pd

def newScoreFile(songName): #I am making these as functions so hopefully they can be easily reused/integrated
    emptyScore = {'score': [0, 0, 0],
                  'name': [" ", " ", " "]}
    newScoreDF = pd.DataFrame(emptyScore)
    newScoreDF.to_csv(songName + "score.csv", index=True)
    
def resetSongs():
    songData = {'songTitle':["Mary Had a Little Lamb", "Down by the station"],
                'musicFile':["Mary Had a Little Lamb.mid", "Down by the station.mid"],
                'scoreFile':["MHLLscore.csv", "DBSscore.csv"]
                }
    songFrame = pd.DataFrame(songData)
    songFrame.to_csv("songs.csv", index=False)

def resetScores():
    songScore1 = newScoreFile("MHLL")
    songScore2 = newScoreFile("DBS")
    survScore = newScoreFile("surv")
    
    
#resetSongs() #initial call to create songs.csv
#resetScores() #initial call to create scores csv files
 
#function(s) to access and change current song's score.csv
    #access songs.csv
    #find correct song's row
    #get the score csv
    #bring the score csv into a dataframe
    #compare top 3 scores with user's current score
    #nested ifs:
    #if current score > 1st place score, shift 2nd place to 3rd place, 1st place to 2nd place, prompt user for initials and replace 1st place score
    #if current score > 2nd place score or current score = 1st place, shift 2nd place to 3rd place, prompt user for initials and replace 2nd place score
    #if current score > 3rd place score or current score = 2nd place, prompt user for initials and replace 3rd place score
    #only need to maintain/display top 3 scores

#function(s) to access and change survscore.csv 
    #access survival score csv
    #bring the csv into a dataframe
    #compare top 3 scores with user's current score
    #nested ifs:
    #if current score > 1st place score, shift 2nd place to 3rd place, 1st place to 2nd place, prompt user for initials and replace 1st place score
    #if current score > 2nd place score or current score = 1st place, shift 2nd place to 3rd place, prompt user for initials and replace 2nd place score
    #if current score > 3rd place score or current score = 2nd place, prompt user for initials and replace 3rd place score
    #only need to maintain/display top 3 scores
def loadSurvScore(score):
    currentScores = pd.read_csv("survscore.csv")
    if (score > currentScores[[0]].iloc[[0]]):
        currentScores.iloc[[2]] = currentScores.iloc[[1]]
        currentScores.iloc[[1]] = currentScores.iloc[[0]]
        currentScores[0].iloc[[0]] = score
        #input initials into name location
        initials = input("Enter your initials: ")
        currentScores[0].iloc[[1]] = initials
    else:
        if(score == currentScores[[0]].iloc[[0]] or score > currentScores[[0]].iloc[[1]]):
            currentScores[[2]] = currentScores.iloc[[1]]
            currentScores[[1]].iloc = score
            #input initials into name location
            initials = input("Enter your initials: ")
            currentScores[0].iloc[[1]] = initials
        else:
            if (score == currentScores[[0]].iloc[[1]] or score > currentScores[[0]].iloc[[2]]):
                currentScores[[2]].iloc[[0]] = score
                #input initials into name location
                initials = input("Enter your initials: ")
                currentScores[0].iloc[[1]] = initials
    print(currentScores)
    currentScores.to_csv("survscore.csv", index=True)