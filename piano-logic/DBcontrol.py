import csv
import pandas as pd

def newScoreFile(songName): #I am making these as functions so hopefully they can be easily reused/integrated
    emptyScore = {'score': [],
                  'name': []}
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
    
    
resetSongs()
resetScores()
 
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