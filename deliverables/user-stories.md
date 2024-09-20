# User Story Compendium

## User Stories

As a gamer, I want to be able to play survival mode and save my scores into a leaderboard, so I can see my progress as I get better.

As a competitive gamer, I want to be challenged by other survival mode players' high scores, even if I cannot beat their scores.

As an aspiring musician, I want to be able to select and use the Free Play mode to experiment with writing my own music.

As a competitive musician, I want to be able to play a provided song and get a high score so I can compete for the best score.

As a musician, when I play a song in the song mode and don’t get a high score, I want to receive feedback so I can understand how to improve and try again.

## Developer Stories

As a developer, I want to have a GUI that is user friendly, sleek, and fully functionable.

As a developer, I want the interface to work with mouse, touchscreen, and QWERTY keyboard, so that the user may play our piano simulator on different devices.

As a developer, I want to be able to use a MIDI library to play piano notes, so I don't have to implement a piano player from scratch.

As a developer, I want to create a timing and scoring system so I can properly assign high scores to users.

As a Developer, I want to test framework to verify functionality, validate score tracking for high and low scores, and ensure smooth transitions with proper feedback across survival mode, song, and free play modes.

## Tester Story

As a tester, I want to ensure the functionality of the three game modes (survival, song, and free play) and the five "happy path" scenarios that we have come up with, and correct any errors that may lead to a "sad path."

The five "happy paths" are:

     1. user selects survival mode -> user plays survival mode -> user gets high score -> user enters their name to the leaderboard -> user is returned to menu. 
     2. user selects survival mode -> user plays survival mode -> user does not get high score -> user is returned to menu. 
     3. user selects song mode -> user plays song -> user gets high score - user enters their name to the leaderboard -> user is returned to menu. 
     4. user selects song mode -> user plays song -> user does not get high score -> user is returned to menu. 
     5. user selects free play mode -> user plays freely -> user quits free play mode -> user is returned to menu. 
