# What’s New in the 3\.0\.0\.9477 Release of 14 May 2025

> **Note**: Images omitted — refer to original DOCX for figures.


__Data:__

\- No changes\.

__Content__:  Basically, all of the standalone scenarios were touched again\.

\- Removing "__Tutorial 12__" on NBC\.  It will just be a write\-up, not a scenario now\.

\- "__Tutorial 9 Air Support Opereations__" had a typo in it and has been renamed to fix it\.

\- "__Huenfeld Bridges__" updated again by Jim to include WLR and associated arty unit\.

\- "__A Final Push__", "__US3 Campaign__", and "__Pursuit__" updated by the Editors\. "__A Final Push__" also has the BP warnings that refer to now\-removed Forces fixed\.

\- "__Once More Unto The Breach__" and "__Quietly Flows the Donau__" updated by Gary\. We are making sure we are using the latest\.

\- The existing "__Fulda__" map has been updated with a lot more place names now\.

\- The three scenarios that use the Fulda Map have been updated with the new details\. "__Return to Fulda__", "__Link Up__", and "__Rude Awakening__"\.

\- Revised update to "__The First Dance__"\. Charles has been striving to balance the scenario and thinks he is close\.

\- "__Tutorials 7 to 11__": JohnO \- Here are the files with the updated mission briefing\. There will be another update as soon as I get feedback from Charles on Tutorial 10: Air Assault and Tutorial 11: Military Convoy\. Once I get the feedback from Charles, I will update the files one last time\.

\- "__Kampfgruppe Becker__" and "__The Battle of the Nations__" no longer would load and play as games\.  This is due to a very recent tightening of internal validation standards\. Sorry about that\.  The result was that these 2 scenarios would not load, and perhaps 20 other standalones now manifested problems that needed to be addressed\.  This has been fixed for all except for "__Armageddons Dawn__", "__The Long Night__" and "__Cross Checking__" which are not to be played yet\. This does not affect game play, just the internal data ordering of the scenario files themselves\. Rob needs another day to do the same fixes for the campaign scenarios, so please don't expect those to work right now\. They are not being tested yet, but I'm just mentioning it\.

__Code:__

\- We recently improved the time estimation routine that supplies time estimates to future waypoints\.  In this build, we fix PatchPathTiming so it is robust against invalid/empty paths \(as in the Overture scenario, where WP cannot move everywhere due to bridges being absent\)

\- Assault order: removed posture bonus that depended on having spotted units\. We have a better mechanism to delay the visible posture change during preparation\. \(William, r9469\)

\- Fix crash in ScenEd BP Mission edit where we tried to edit the wrong mission and it caused a crash in the SOP editor\. \(Kevin, 9471\)

\- Fix SOP preset ordering to always put HQ, Recce, and Engineer presets on top in lists that hold multiple presets \(right click set SOP and SOP manager preset dropdown\) \(Kevin, r9471\)  


__Documents:__

\- \\Documents\\WhatsNew\\WhatsNew\.pdf is now being updated with these commit notes so that there is a single reference available for all of them\.

\- \\Documents\\\_Beta Users\\FC SOP Explained v4\.pdf has been updated with the contents of an overview written by Kevin\.

