import csv
import pandas as pd

def newScoreFile(songName): #function to make an "empty" score file
    emptyScore = {'score': [0, 0, 0],
                  'name': [' ', ' ', ' ']}
    newScoreDF = pd.DataFrame(emptyScore)
    newScoreDF.to_csv(songName + 'score.csv', index=False)
    
def resetSongs(): #function to relate song titles, their midi files, and their score files
    songData = {'songTitle':['Mary Had a Little Lamb', 'Down by the station'],
                'musicFile':['Mary Had a Little Lamb.mid', 'Down by the station.mid'],
                'scoreFile':['MHLLscore.csv', 'DBSscore.csv']
                }
    songFrame = pd.DataFrame(songData)
    songFrame.to_csv('songs.csv', index=False)

def resetScores(): #function to make new score files for the different songs and modes; this is rudimentary and can be called to remake all files with scores set to 0.
    songScore1 = newScoreFile('MHLL')
    songScore2 = newScoreFile('DBS')
    survScore = newScoreFile('surv')
    
#resetSongs() #initial call to create songs.csv; comment out when game is in use!
#resetScores() #initial call to create scores csv files; comment out when game is in use!

#functions to access and change current song's score.csv
def findSongScore(currentSong):
    #open songs.csv
    songDir = pd.read_csv('songs.csv')
    #find the song by its name
    #find the score file in that row
    #return the score file's name so we have a parameter to pass to loadSongScore()
    return(songDir[songDir['songTitle'] == currentSong]['scoreFile'].values[0])
    
    #get the score csv
def loadSongScore(scoreFile, score):
    #bring the score csv into a dataframe
    currentScores = pd.read_csv(scoreFile)
    #compare top 3 scores with user's current score
    #nested ifs:
    if (score > currentScores.iloc[0, 0]):
        #if current score > 1st place score, shift 2nd place to 3rd place, 1st place to 2nd place, prompt user for initials and replace 1st place score
        currentScores.iloc[2, 0] = currentScores.iloc[1, 0]
        currentScores.iloc[2, 1] = currentScores.iloc[1, 1]
        currentScores.iloc[1, 0] = currentScores.iloc[0, 0]
        currentScores.iloc[1, 1] = currentScores.iloc[0, 1]
        currentScores.iloc[0, 0] = score
        #input initials into name location
        initials = input("Enter your initials: ")
        currentScores.iloc[0, 1] = initials
    else:
        if(score == currentScores.iloc[0, 0] or score > currentScores.iloc[1, 0]):
            #if current score > 2nd place score or current score = 1st place, shift 2nd place to 3rd place, prompt user for initials and replace 2nd place score
            currentScores.iloc[2, 0] = currentScores.iloc[1, 0]
            currentScores.iloc[2, 1] = currentScores.iloc[1, 1]
            currentScores.iloc[1, 0]= score
            #input initials into name location
            initials = input("Enter your initials: ")
            currentScores.iloc[1, 1] = initials
        else:
            if (score == currentScores.iloc[1, 0] or score > currentScores.iloc[2, 0]):
                #if current score > 3rd place score or current score = 2nd place, prompt user for initials and replace 3rd place score
                currentScores.iloc[2, 0] = score
                #input initials into name location
                initials = input("Enter your initials: ")
                currentScores.iloc[2, 1] = initials
    #only need to maintain/display top 3 scores
    print(currentScores)
    currentScores.to_csv(scoreFile, index=False)

#function to access and change survscore.csv 
def loadSurvScore(score):
    #access survival score csv
    #bring the csv into a dataframe
    currentScores = pd.read_csv('survscore.csv')
    #compare top 3 scores with user's current score
    #nested ifs:
    if (score > currentScores.iloc[0, 0]):
        #if current score > 1st place score, shift 2nd place to 3rd place, 1st place to 2nd place, prompt user for initials and replace 1st place score
        currentScores.iloc[2, 0] = currentScores.iloc[1, 0]
        currentScores.iloc[2, 1] = currentScores.iloc[1, 1]
        currentScores.iloc[1, 0] = currentScores.iloc[0, 0]
        currentScores.iloc[1, 1] = currentScores.iloc[0, 1]
        currentScores.iloc[0, 0] = score
        #input initials into name location
        initials = input("Enter your initials: ")
        currentScores.iloc[0, 1] = initials
    else:
        if(score == currentScores.iloc[0, 0] or score > currentScores.iloc[1, 0]):
            #if current score > 2nd place score or current score = 1st place, shift 2nd place to 3rd place, prompt user for initials and replace 2nd place score
            currentScores.iloc[2, 0] = currentScores.iloc[1, 0]
            currentScores.iloc[2, 1] = currentScores.iloc[1, 1]
            currentScores.iloc[1, 0]= score
            #input initials into name location
            initials = input("Enter your initials: ")
            currentScores.iloc[1, 1] = initials
        else:
            if (score == currentScores.iloc[1, 0] or score > currentScores.iloc[2, 0]):
                #if current score > 3rd place score or current score = 2nd place, prompt user for initials and replace 3rd place score
                currentScores.iloc[2, 0] = score
                #input initials into name location
                initials = input("Enter your initials: ")
                currentScores.iloc[2, 1] = initials
    #only need to maintain/display top 3 scores
    print(currentScores)
    currentScores.to_csv('survscore.csv', index=False)
    
#function to find music file based on song title
def findMusicFile(songName):
    #open songs.csv
    songDir = pd.read_csv('songs.csv')
    #find the song by its name
    #find the music file in that row
    #return that music file's name
    return(songDir[songDir['songTitle'] == songName]['musicFile'].values[0])

#function to find song title based on music file
def findSongTitle(songFile):
    #open songs.csv
    songDir = pd.read_csv('songs.csv')
    #find the song by its music file
    #find the name in that row
    #return the song title associated with the music file
    return(songDir[songDir['musicFile'] == songFile]['songTitle'].values[0])

#testing function calls;  comment out when game is in use!
#loadSurvScore(1000)
#loadSurvScore(500)
#print(findSongScore("Mary Had a Little Lamb"))
#loadSongScore(findSongScore("Mary Had a Little Lamb"), 1000)