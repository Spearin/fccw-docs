# What’s New in the 3\.0\.0\.9547 Release of 28 May 2025

> **Note**: Images omitted — refer to original DOCX for figures.


__Data:__

\- "25 May Data update\. Some minor data clean\-ups\. US FARPs may need to be updated if there is an error with duplicate SUTag IDs\. Other nations checked out okay\. Other nations had some filters on still so those got fixed up\. Did everyone to be safe\. Scenarios need not be refreshed\." Jim\.

\- "CW 80s Canada\.xls" updated to amalgamate a single recon mortar unit with its HQ so that it will perform better\.

__Content:__

\- FPSS\-6104: fix “__EG1\-SN4 Valley of the Damned__”, “__EG1\-SN5 For the Fatherland__” and “__US1\-SN3 Iron Rangers__” campaign scenario BPs which had Hold or Screen BP missions without \*\*explicit objective locations\*\*\. \(William, r9511\)

\- __Tutorials 7 to 11__ updated by the author multiple times\.  These are very close to done now and we are looking for beta feedback now under Andrew’s direction\.  The docx version of FM03 Tutorial Operations has been added to the \\\\Documents\\FMs\\ folder so that everyone can follow along with the latest doc version\.

\- __USSR2\-SN1__, "Arty/4/1/79 Bde" renamed to "Arty 1/4/1/79 Bde" for consistency

\- FPSS\-6032: __Spottability__ problems \- re\-process all 81 Cold War maps to slightly reduce concealment in urban terrain \(as done earlier for Soest\)\.  \(William, r9528\)

\- __All scenarios reprocessed__ to use the updated map data from FPSS\-6032\.

\- FPSS\-6135: fix a bunch of problems in the __Melsungen__ map, refresh the “__USSR\-SN1 Red Hammer__” campaign scenario\. \(William, r9530\)

\- FPSS\-6130: Re\-fix __US Mech mortar units__ \(svn9506\) so they are a plain mortar platoon, not a company HQ unit\. Rob fixed 13 standalone and 11 campaign scenarios for this\.

\- "__A Brief Moment in Time__" had a single mortar unit amalgamated into its HQ by Rob\.

\- “__The Heilbronn Gambit__” updated by Charles late 27 May

__Code:__

\- FPSS\-6005: Will's new __direct movement path__ implementation \(but not hooked up to the UI\)\. Implemented across all modules\. \(Will, r9528\)

\- FPSS\-6117: Add __Direct Path SOP__ option to various UI elements\.

\- FPSS\-6081: Fix bug preventing picking up passengers from working if the transport had to travel to them\.  \(Kevin, r9510\)

\- FPSS\-6099: Make slightly more descriptive __scenario blurb__, removing guesswork for new players\. \(William, r9523\)

\- FPSS\-6108: __SOP__ \- Change text of Relocate When: "__Never__" to be "__Stance Only__"\.  This is intended to remove the apparent conflict in directives between the Stance and Relocate When settings\. \(Kevin, r9517\)  

\- FPSS\-6112: __SOP__: Add selection inversion buttons to the SOP Manager to bulk select/deselect multiple units\. \(Kevin, r9520\)

\- FPSS\-6113: __SOP__: Temporarily block out the 'SOP Paste' buttons to see if anyone has issues before I remove the code\.  This is part of the latest SOP simplification drive and this feature is going because there are alternatives \(the SOP Presets\) that are easier to use\. \(Kevin, r9521\)

\- __SOP__: Add additional close\-range and march AD presets to SAM units\. Also changed the ordering of presets to be more consistent\. Also removed a couple of generic presets from a couple of units since we add generics to everyone anyway\. \(Kevin, r9513\)

\- Change __SOP Manager__ to attempt to preserve the Scope when changing which unit is being looked at\. It now preserves the selection of default or terminal order if selected, otherwise attempts to do the same order \#\. \(Kevin, r9532\)

\- FPSS\-6117: Add __Direct Path SOP__ option to various UI elements\.

\- __SOP__: Recce Screen & Fight now has carriers supporting

\- __SOP__: APC Dismounted Attack now has carriers hiding instead

\- __SOP__: In Preset short descriptions change carriers hiding being described as \`hide in rear\` instead of \`support from rear\` to help differentiate from carriers in support

\- FPSS\-6116, 6102: If you __'bulk rename'__ a group of units then any unit that does not get renamed gets undeployed in all BPs instead\.  This was a problem with bulk renaming especially and was a very annoying bug we did not tie into bulk renaming specifically so we could not find it\.  

\- FPSS\-6119: Fix erratic time estimates for movement when unit was on the move in the UnitDashboard\.  UnitDashboard: describe the active order as having \_started\_, not as \_starting\_\.

\- JIRA\-6126: fix CalcMaxEffectiveRangeInM calculation to ignore out\-of\-ammo weapons, providing a better range outline in overlays \(Zumwalt\_446\)\. Also cleaned up how to determine if a unit is/has become unarmed\. \(William, r9519\)

\- FPSS\-6132: Fix ampersand not correctly displayed in Unit Dashboard title and ScenEd force roster, for Andrew's Argyll and Sutherland Highlanders\. \(William, r9531\)

\- Remove a couple of redundant orders consistency checks \(they were already executed by the DoOrder\) \(Kevin, r9510\)

\- FPSS\-6131: Saving a previously saved Scenario in the Editor under a \*\*new name\*\* causes a quadruple "File copy operation" failure\.  Fixed\.

\- FPSS\-6140: update TMilUnit's __unarmed status__ explicitly when initializing the unit and set UnitAmmoPc accordingly\.

\- FPSS\-6132: correctly escape & character in forms dealing with unit/force names: ScenEd Change Force Name \- Andrew

\- FPSS\-6140: update TMilUnit's unarmed status explicitly when initializing the unit, and set UnitAmmoPc accordingly\. Also fix unarmed units showing 'red' status when created in ScenEd \- Charles

\- Bump game version to 432, in order to reuse an obsolete TWaypoint datetime field for tracking the start of order execution\.

__Documents:__

\- The docx version of FM03 Tutorial Operations has been added to the \\\\Documents\\FMs\\ folder so that everyone can follow along with the 5 tutorials\.

\- \\\\Documents\\\_Beta Testers\\ now contains a write\-up of what the key Unit orders are supposed to represent\.  There has been a lot of confusion recently and it isn’t helping that we are changing what Assault means quite a bit in response to your feedback\.  The document will explain current ideas in detail and will be put into the main game docs at a suitable time\.

