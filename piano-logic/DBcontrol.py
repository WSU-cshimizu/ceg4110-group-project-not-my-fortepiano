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

#function(s) to access and change survscore.csv