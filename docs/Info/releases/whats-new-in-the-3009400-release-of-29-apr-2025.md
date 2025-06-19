# What’s New in the 3\.0\.0\.9400 Release of 29 Apr 2025

> **Note**: Images omitted — refer to original DOCX for figures.


__Data:__

\- No changes\.

__Content:__

\- A brand new standalone scenario just came in\.  "__Schlacht bei Diemelstadt" __features Poland tangling with West\-German forces\.  Authored by Fred Schwarz\. \(R9390\)

\- Charles did a final sweep of scenarios and touched SOPs\.  Hopefully, this is the last bulk sweep\!

\-\- all the Campaign scenarios for: FR1, UK1, US3, USSR1 and USSR2 were reviewed and updated as necessary\.

\-\- 31 standalone scenarios: __A Brief Moment in Time, A Final Push, A Second Dance, A Time to Dance, Air and Land, Beaning the Beamers, Breakaway, Chance Encounter, Desperation, Eyes Ears and Teeth, Falling From The Sky, First Clash, Flying Scotsmen, For Queen and Country, Go West Young Man, Hammer Falls, High Sticking, It Begins, Lesson of War, Link Up, Meeting in Arolsen, Pursuit, Race to the Fulda, Return to Fulda, Rude Awakening, Steel Rain, The Battle of The Nations, The Fisrt Dance, The Ride of the 12th Cuirassier, The Screen, __and__ The Three Sisters__\.

Not updated: Huenfeld Bridges\.

\- Just to be sure, all FCCW scenarios \(standalone and campaign\) have been data\-refreshed again so that they are guaranteed to have the absolute latest national data values\.

__Code:__

\- FPSS\-5977 \- game crashes with the message that it cannot 'focus a control or window'\.  We thought this was fixed but if you mash the function keys F4/5/6 together you can still force it\.  Trying a new way of being more careful and discriminating now\.

\- FPSS\-6012 \- Rework the white space in the Scenario Selection screen to make the layout seem a little less jarring\. \(Jim\)\.  A new variation is included here for feedback\. \(Rob, r9391\) Layout Improvement in Setup Game Difficulty Screen\.  Incorporate William's suggestions\. \(r9398\)

\- Setup, Campaign Selection: Selecting a national flag would list any campaigns that had that nation as an opposing force and not just a friendly force\.  This was intentional, but it looked odd, so we have filtered out the campaigns where the selected nationality is an OpFor\.  For example, selecting the 'American' flag no longer shows the EG3 East German campaign as an American choice\.  Thanks to Jorgen and Jim for explaining this\. \(Rob, r9393\)\.

\- SOP presets: fix IFV SOP presets 'Screen & Fight', 'March' to use 'Carriers when Empty Support Passengers' so the IFVs contribute to spotting and fighting\. \(Zumwalt\_446\)\. \(William, r9392\)\.

\- Turn off the Survey mechanism for anything other than Cold War scenarios right now

\- FCSS\-6021: fix Barrage orders editing: rename Start Time to Time of Impact, fix handling of Time of Impact changes

\- Fix Options/Show Unit Counter Halo menu remaining enabled during turn resolution\.

\- Upgrade standard game save confirmations to illustrated messages with leader badge\.

__Documents:__

\- \\Documents\\WhatsNew\\WhatsNew\.pdf is now being updated with these commit notes so that there is a single reference available for all of them\.

