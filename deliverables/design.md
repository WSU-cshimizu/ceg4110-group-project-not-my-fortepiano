# Design Specification

1. The system shall have inputs

   1. The inputs shall be in the forms of a mouse, touchscreen, or keyboard input
      Using one or more of these inputs to click or touch certain areas of the GUI shall trigger an event in the front end corresponding to that area of the GUI.
     

2. The system shall have a frontend

   1. The frontend shall have a menu that allows the user to select between "free-play", "survival", "play song", and "see high scores" modes
      This shall be a drop-down menu from the title screen, so the user may select which mode to play in.
   2. The frontend shall have a piano-style keyboard GUI
      In order to properly simulate a piano, the interface should like a piano's keyboard.
   3. The frontend shall have a popup for adding a name to save a high score at the end of a round of "survival" mode
      The frontend shall display the user's current score as determined by the backend, and shall prompt the user to enter their initials if their score
      exceeds the high scores stored previously in the backend.
     

4. The system shall have a backend

   1. The backend of the system shall have logical components.
      1. The logical components of the system shall have logic to allow the user to play individual piano notes
         The notes will be acquired from a MIDI file and the each piano key will correspond to its proper note. 
      2. The logical components of the system shall have logic to transform piano logic into piano sounds
         The backend shall send the sound of the note chosen by the user to the frontend to play through the audio system on the user's device.
   2. The backend of the system shall have database components.
      1. The system shall have a database for songs
         These songs will be broken down into notes that the front end will display to the user. The backend shall keep track of the number of notes the user plays that
         correctly correspond to the notes of the song, and determine the user's score based on the this.
      3. The system shall have a database for top scores and associated names
         The backend shall store the three highest scores along with those users' initials and display them when "see high scores" is selected from the menu.
