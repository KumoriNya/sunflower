# sunflower
Full stack developing the website for SunflowerAI

TODOs:
1. Development - Connection with whisper server
2. General
    1. Feature - Making sure when caption text corrects itself (from the server), update the displayed caption text as well
    2. Feature - Add functionality to know when the event stops to disconnect the websocket (Is this required?)
    3. Feature - Reconnect to the server when connection is unexpectedly shut down
    4. Fix - Instead of chopping the caption by the unit of a word, update the caption by sentences (Upon displaying new sentence, remove the oldest displaying sentence) Potential solution: asking the server to include a message of "Sentence finished" to let the web know. Also instead of delivering one word at a time, deliver the whole on-going sentence instead, and the frontend adjust displayment accordingly.

3. Host UI
    1. Feature - Keep only the most recent sentences (1 ~ 3?)
    2. Feature - Make the caption 'flow' over somewhere on the page? Potential improvement: drag + resize by user.

4. Audience UI



Also:
Styling - Add styling (logo, font, theme colours, responsivity for mobile devices)
Feature?- Test generating QR code that leads to a url, and guarantee one for the final demo url
Feature - Integration of slides: enable uploading a powerpoint file (and potentially a link to google slides) and display caption on the slides as well
Deployment - Check if webflow allows appending extra webpages. If not, see if firebase allows customised domain name. If not, explore how to deploy websites to specific domain name.