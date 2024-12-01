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

### Testing Requirements
Test-1. Mode Selection
Test 1.1: Verify that the user can select between Survival Mode, Play Music Mode, Free Play Mode, and View High Scores from the main menu.
Test 1.2: Ensure that each mode properly loads its respective gameplay functionality upon selection.

Test-2. Gameplay Functionality
• Survival Mode
Test 2.1: Verify that Survival Mode starts as expected when selected from the menu.
Test 2.2: Test the game logic in Survival Mode to ensure the player's progress is tracked correctly.
Test 2.3: Ensure the player's score is calculated correctly based on performance in Survival Mode.
Test 2.4: Validate that the system compares the player's score to existing high scores and prompts for name input if the score qualifies.
Test 2.5: Confirm that when the game ends, the user can input their name and the score is added to the leaderboard.
Test 2.6: Verify that the player can return to the main menu after the game ends.
• Play Music Mode
Test 2.7: Verify that Play Music Mode loads the correct song selection menu.
Test 2.8: Ensure the user can select and play a song in Play Music Mode.
Test 2.9: Validate that the system calculates a score based on the player's performance and accuracy.
Test 2.10: Ensure the player is able to replay the song or return to the menu after completing the song.
Test 2.11: Confirm that the leaderboard properly displays high scores for Play Music Mode.
• Free Play Mode
Test 2.12: Verify that Free Play Mode starts when selected and does not track scores.
Test 2.13: Ensure the user can play freely without scoring and can quit the mode to return to the main menu.

Test-3. Score and Leaderboard Functionality
Test 3.1: Verify that the leaderboard displays high scores correctly for Survival Mode and Play Music Mode.
Test 3.2: Ensure that scores for both modes are stored in the database and are persistent across sessions.
Test 3.3: Test the leaderboard to confirm that new high scores correctly overwrite previous scores if they surpass them.
Test 3.4: Ensure that players can view the leaderboard after playing any mode.

Test-4. Database and Data Persistence
Test 4.1: Verify that the database is storing high scores, song data, and user names correctly.
Test 4.2: Test data retrieval functionality to ensure high scores and song information can be accessed and displayed correctly.
Test 4.3: Ensure that database connections are stable and that data is preserved between gameplay sessions.

Test-5. User Interface (UI) and Frontend Functionality
Test 5.1: Verify that the piano-style keyboard GUI is displayed correctly in all modes where it is used.
Test 5.2: Ensure that the menu is intuitive and allows users to navigate between Survival Mode, Play Music Mode, and Free Play Mode.
Test 5.3: Validate that the score input popup for adding a name to the leaderboard appears at the end of Survival Mode and Play Music Mode if the player achieves a high score.
Test 5.4: Test the keyboard, mouse, and touchscreen inputs to ensure that all input methods work across devices and platforms.

test-6. Error Handling
Test 6.1: Ensure that the game gracefully handles invalid inputs, such as invalid names for the leaderboard or unexpected key presses during gameplay.
Test 6.2: Validate that the game does not crash if the database fails to connect or retrieve data.
Test 6.3: Verify that if the system encounters an error during gameplay, it displays a user-friendly error message and handles the error without crashing.

Test-7. Endgame and Session Flow
Test 7.1: Confirm that the user is redirected to the main menu after completing any mode (Survival, Play Music, or Free Play).
Test 7.2: Ensure the user can return to the main menu and select a new mode without issues.
Test 7.3: Test that the user can exit the game entirely from the main menu or during gameplay.

Test-8. Compatibility and Performance
Test 8.1: Verify that the game performs consistently across different platforms.
Test 8.2: Ensure the game runs smoothly on different browsers and devices with minimal lag or performance issues.

Test-9. Regression Testing
Test 9.1: After any updates, verify that all features (leaderboards, scoring, gameplay modes) work as expected and that no new bugs have been introduced.
Test 9.2: Ensure that previous functionalities (such as menu navigation and gameplay) are unaffected by new features added to the game.

Test-10. Usability and User Experience (UX)
Test 10.1: Ensure that the game is easy to navigate, with clear instructions and an intuitive interface.
Test 10.2: Test the responsiveness and accessibility of the game, making sure that it's usable by players with various abilities.
