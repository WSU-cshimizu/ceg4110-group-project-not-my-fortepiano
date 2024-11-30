### Requirements

1. The system shall contain a Survival mode
   1. The system shall have an option to select Survival Mode
2. The system shall allow the user to input their score into the leaderboard for Survival mode
   1. The system shall contain a way to accept scores
   2. The system shall contain a leaderboard for Survival scores
3. The system shall have a leaderboard that contains scores
   1. The system shall have a database to hold scores
   2. The system shall have functionality to retrieve scores
4. The system shall have a leaderboard that shows all highscores
   1. The system shall show scores for Play Music mode
   2. The system shall show scores for Survival mode
5. The system shall contain a Free Play mode
6. The system shall contain a menu selection for Free Play mode
7. The system shall have a song selection menu
   1. The system shall have a database of all songs
   2. The system shall have functionality to retrieve songs
8. The system shall allow the user to input their score into the leaderboard for Play Music mode
9. The system shall have functionality to play a song again in Play Music
   1. The system shall redirect the user to the leaderboard to show score ranking
   2. The system shall have functionality to return to play another song
10. The system shall display the users score after finishing or terminating song

### Build Requirements
- The system shall be programmed in the languages Python, HTML, CSS, Javascript, and SQL.

### GUI Requirements

- The system shall have inputs

   - The inputs shall be in the forms of a mouse, touchscreen, or keyboard input

- The system shall have a frontend

   - The frontend shall have a menu that allows the user to select between "free-play", "survival", "play song", and "see high scores" modes
   - The frontend shall have a piano-style keyboard GUI
   - The frontend shall have a popup for adding a name to save a high score at the end of a round of "survival" mode


### Backend Requirements
- The system shall have a backend

   - The backend of the system shall have logical components.
      - The logical components of the system shall have logic to allow the user to play individual piano notes
      - The logical components of the system shall have logic to transform piano logic into piano sounds
   - The backend of the system shall have database components.
      - The system shall have a database for songs
      - The system shall have a database for top scores and associated names
