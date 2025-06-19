# What’s New in the 3\.0\.0\.9509 Release of 21 May 2025

> **Note**: Images omitted — refer to original DOCX for figures.


Based on player feedback, we are concentrating on improvements to Assault orders, and also to SOP\. We have made a minor national data file update that required all scenarios to be refreshed again\.

__Data:__

- All of the Cold War national data files have been updated again\.  The changes relate primarily to artillery formations\.  In particular, some US mechanized infantry and cavalry formations had four to six company mortars with their own HQ that did not routinely support their formation\.  By merging the HQ unit with the mortar unit, the mortars should now work to support the rest of the group as expected\.
- Part of this change was to add in artillery observers, especially for Warsaw Pact forces, where the artillery itself is likely to be off\-map, but unit observers are on the map to call in fire\.  We used to assume they existed, but now we can model them explicitly going forward\.
- A few artillery types could fire nuclear munitions, and we had those listed in the data sheets\.  This opened a can of worms we would rather leave shut\.  Going forward, there will be no nuclear munitions for artillery pieces, and for scenarios with the nuclear option, surface\-to\-surface missiles will be provided to launch nuclear Strikes\.  This is the old treatment, and we are consciously returning to it\.

__Content:__

\- Sorry, but at this time, the following scenarios are not playable due to broken battleplans:

1. Armageddon’s Dawn 
2. Cross Checking
3. The entire Canadian CA1 campaign
\- In "__An Autobahn Too Far__", the WG “PzArtBtl 305" was set to off\-map but not actually given an off\-map location\.  Fixed by Rob\.

\- "__It Begins__", "__Steel Rain__", "__First Clash__", "__Link Up__", and "__Eyes Ears and Teeth__" SOP for Recon Stay and Fight preset was changed by Charles\.  In the Preset "Recon Screen and Fight" it has the "Carriers When Empty" SOP set for "Hide Nearby" when it should be "Support Passengers"\. Because of this, the Carriers don't fight\. Recon units with IFVs will need their carriers’ firepower\.

\- "__Beaning the Beamers__" minor spelling corrections by Gary on 20 May\.

\- All of the standalone and campaign scenarios have been data refreshed to use the latest national data files provided by Jim\.

\- No fewer than 26 scenarios had or potentially had a problem with mortar support described above and have been fixed by merging the mortar HQ into the mortar unit itself\.  25 of these were US and one was Belgian\.  These are the affected scenarios:

1. A Final Push – Done, 1 unit
2. A Second Dance – Done, 2 units
3. Alamo at Soest – Done, 1 unit
4. First Clash – Done, 1 unit
5. Hammer Falls – wave 3, Done, 1 unit
6. Hunting in the Woods – Done, 1 unit
7. Link Up – wave 5, Done, 2 units
8. Meeting in Arolsen – BE, Done, 1 unit
9. Overture – Done, 1 unit
10. Regulars Forward – Done, 1 unit
11. Return to Fulda – wave 3, Done, 1 unit
12. Seek\-Fix\-Destroy – wave 6, Done, 1 unit
13. Soviet Main Attack Force – wave 6, Done, 3 units
14. Steel Rain – Done, 2 units
15. The Heilbronn Gambit – Done, 2 units
16. EG1\-SN2 – Done, 1 unit
17. US1\-SN2 – Done, 1 unit, no BPs
18. US1\-SN3 – Done, 2 units, no BPs
19. US1\-SN4 – Done, 2 units, no BPs
20. US1\-SN5 – Done, 2 units, no BPs
21. US3\-SN1 – wave 5 – Done, 1 unit, no BPs
22. US3\-SN2 – wave 5 – Done, 1 unit, no BPs
23. US3\-SN3 – wave 5 – Done, 1 unit, no BPs
24. US3\-SN4 – wave 5 – Done, 1 unit, no BPs
25. USSR1\-SN5 – Done, 1 unit
26. USSR2\-SN3 – Done, 2 units  
__Code:__

\- FPSS\-6079: tweak __Assault__ to be a more aggressive move: \(William, r9494\)

\-\- Increase the ground speed of Assault to be between that of Move Hasty and Move Deliberate\.

\-\- Shorten the Preparation delay from 30 minutes to 15 \- similar to Move Deliberate \(National Injects\)

\-\- Assault units now have the ability to exit a hex while leaving known hostile stragglers behind\. Move Deliberate does not have this ability\.

\- FPSS\-5985: further improve __estimates for path travel times__ \(look at order type for each waypoint\) \(William, r9487\)

\- FPSS\-6106: __SOP__\.  Change: Have the currently selected Unit in the SOP Manager synchronize to the currently selected unit elsewhere\.  Now if you have the SOP Manager up for Unit A and then click on Unit B on the map, the SOP Manager will switch from Unit A to B, just the same as the Dashboard does\.  This ought to greatly reduce confusion when editing\.   
!!! note

    if there were SOP edits in progress at the time of the switch, they will be saved if “Automatically Apply Currently Settings When Scope Changes” is checked and will be discarded if it is not\.  We could use feedback on whether we should continue this way, or pop up a confirmation dialog instead to keep or discard changes\.  This is more conspicuous but potentially much more laborious\.


\- __SOP__: fix check for 'Relocate while spotted' to consider solely known hostile units and recently lost hostile contacts\. \(William, r9503\)

\- Fix the last preset in __SOP Manager__ to be selectable now\.  Add preset targeting low\-level HQs to help them not leave their subordinates behind\.  Make HQ, Recce, and Engi presets appear first\.  \(Kevin, r9476\)

\- __Overrun__ tweaks: ignore in\-transport steps, don't abort if a friendly unit is withdrawing, consider all enemy units in combat\. \(William, r9494\)

\- FPSS\-6105: A regular engineer unit could move to a hex with an improved position but was not allowed to give it a terminal order to demolish it\.  It offered to remove an obstacle in error instead\.  This has been fixed and a terminal order to demolish an IP in the destination hex is now offered and works\.

\- FPSS\-6039: One tester \(Ernie Weisbrot\) consistently has problems loading saved games from the Steam build but not from the SVN build\.  We have added debugging code to try to understand why if it happens again\.

\- FPSS\-6086: Sometimes, when loading a file, there is a missing "\\" delimiter in the path name\.  Fixed in about 8 places now\.  It was not a common problem but it could happen if a path was edited manually\. \(Andrew\)

\- Fix incorrect off\-map location checks \(resulting in off\-map locations that were on the map\)\.   This will trigger scenario validation errors for scenarios that feature incorrect off\-map locations \(Battle of Nations being one\)\. \(William, r9488\)

\- Fix the pathfinding problem where amphibious unit wouldn't choose to cross a wet hex side\. \(Will, r9489\)

\- The Battleplan Validator function was reporting if a BP had a Force, which in turn had no Missions at all\.  This is not necessarily an error but is useful to know at this stage\.  There is now an internal global flag compiled in that will suppress this message if False, and it is now set to False to reduce clutter in the reports\.  It can be re\-enabled at any time on request to Rob\.

