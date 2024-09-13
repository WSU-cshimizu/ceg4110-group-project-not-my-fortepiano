# Project Overview Proposal
## Not My Fortepiano

### Why an online piano?
We want to build a browser-based piano game because we feel that it is a void that might be able to be filled. While there are a number of app-equivalent games, not many are browser-based. More importantly, most of them do not offer a [Guitar Hero](https://en.wikipedia.org/wiki/Guitar_Hero)-style of gameplay. The game will include a sandbox mode, an interactive timing-based skill mode, and a follow-along mode.  Users will be able to select between many formats of gameplay, from casual to more in-depth, competitive styles, allowing nearly everyone to have an interest in the game.

### Components
1. **Piano Front-end**
   - A front-end design that allows users to interact with the game. This does not include any of the actual connections, which will be handled via JavaScript. This is just the HTML/CSS layout for the piano, and will not be a full piano, but will include generic integration for future expansion.
2. **Piano Logic (Sandbox Mode)**
   - Will run in JavaScript on the user client. This will be the actual event handler and communicator for the different game modes. Its functions will include making sounds and knowing which key has been pressed.
3. **Timing-based**
   - Will also run in JavaScript on the user client. This mode will introduce pseudo-random key selections with a time limit, requiring the user to click a certain key within a certain number of seconds. This mode will keep a score and properly handle incorrect key presses.
4. **Follow-along**
   - Will also run in Javascript on the user client. This mode will have a specified set of sheet music for users to follow along with, allowing them to replicate popular songs. This mode will include a generic array-like storage system, allowing for future expansion.
5. **Follow-along Music Creation**
   - Will have a number of example follow-along songs for users to play. This mode will include keystrokes in-order along with a potential timing recommendation.

### Integration
The piano front-end will communicate with the sandbox mode logic, which will determine which key has been pressed. This will allow the sandbox mode to properly play piano sounds. This logic will be used for the timing-based and follow-along systems. The timing based system will be a Guitar Hero-style game mode, showing in the front-end which key needs to be pressed and deduct from the user's score for timing delays. The timing-based mode will not be connected to sheet music and will be more like a Bop-It/Guitar Hero mix. The follow-along mode will show sheet music to play, using parts of the timing-based system to cue which keys to press along with a timing recommendation.

### Language
The piano will use HTML/CSS for the front-end and JavaScript for handling the event-detection. We are using HTML/CSS for the front-end because it is the most widely used browser-based design language. In addition to this, nearly everyone in our group has experience with it. We are using JavaScript because it is lightweight, we do not need any back-end connections to store data, and because everyone in our group has experience with it as well. If we decided to add back-end integration in the future, JavaScript allows us to do this seamlessly with AJAX. JavaScript will also work well for event-handling, especially with its DOM support for HTML.

### Life Cycle and Methodology
For our project, we plan on following an Agile process. Most of the members in our group have experience dealing with Agile, and we feel that it will allow us to complete the project. If we are unable to totally integrate all parts, this allows for us to at least deliver some product with less features instead of a product that is only half-working. We will also implement a Scrum methodology, allowing for us to give very defined goals for a particular period (hopefully weekly) and to examine where we are at.
