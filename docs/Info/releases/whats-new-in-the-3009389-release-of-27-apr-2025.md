# What’s New in the 3\.0\.0\.9389 Release of 27 Apr 2025

> **Note**: Images omitted — refer to original DOCX for figures.


__Data:__

\- FPSS\-6011: fix the sil image for BMD1KSH and update all the Soviet Cold War national data files to use it\. \(Jim\) 

__Content:__

\- Add Camp Lee, and two exercise areas to Bad Neustadt am Saale map labels\. \(William, r9376\)

\- Fix scenario 'blurbs' to again contain an indication across which parts of the day the scenario plays out\. \(William, r9377\)

\- Support pretty tables in scenario selection, scenario description, and briefing \(developed using Tutorial 07 \- Engineer Operations\)\. \(William, r9381\)

\- Adding more leader badges \(5 x British, 1 x Belgium\) \(William, r9387\)

\- CW splash: upgrade the main splash screen with separate title, background, and main art, so it scales with various resolutions\. Also updated the "little splash" with a properly scaled version \(so the graphic isn't distorted when displaying\)\. \(William, r9388\)

\- REFRESH ALL scenario data to use the modified Soviet national data files\. \(Rob\)

__Code:__

\- FPSS\-5432: Fixed barrage orders that were without a matching combat event during auto\-testing, William\.  \(Will, r9385\)

\- FPSS\-5623: Tactical Transport: terminal point of TT plans now has all of the transports going to it instead of using the formation spread\. \(Kevin, r9389\)

\- FPSS\-5781: Fixed artillery does not ‘Rest and Resupply’ if ordered \(Gary C\)\. \(Will, r9384\)

\- FPSS\-5957: Set alternative file paths for Steam correctly for Commercial users\.  This was getting mixed up with the Matrix installs to "\\Program Files \(x86\)\\"\.  They are very similar conditions, but not identical, so it had to be teased out\.  The goal is to make sure that the various read/write data files and supporting bin files are copied to the new location BEFORE the game needs to read them\.  It was doing it after, and so the first game launch gave very puzzling errors\. \(Rob\)

\- FPSS\-5976: fix problem with waypoints remaining on the map after a rubber band selection that does not yield any selected unit\.  And fix old overlays problem in the process\.

\- FPSS\-5981: SOP Manager display issues with a 150% font\.  Two of the labels crowded too closely together, and the right edge of the three darker shape boxes was being clipped\.  All now fixed\.  \(Rob\)

\- FPSS\-5982: Game throws exception when exiting while in F11 full screen mode\. \(Rob\)

\- FPSS\-5984: Fix corner case in plotting movement orders, where we did not allow moves to the alternative line\-of\-sight location when initiated from OOB\.

\- FPSS\-6000: FPSS\-5998: fix crash in VCR replay \(we should not generate professional log entries during VCR replay\)

\- FPSS\-6010: Fix weird dropdown menu placement in F11 full screen mode \(by removing redundant menu placement code\) \(Jim\) \(William, r9374\)

\- FPSS\-6010: In F11 full screen mode, display the game caption info \(game version and scenario info\) on the right side of menu bar, if space permits \(William, r9375\)

\- FPSS\-6013: The standard Windows MessageDlg user messages are shown in the \*\*screen center\*\* only and with really big displays this may no longer be anywhere near where the game is running\.  It looks bizarre\.  These messages are now always put over the very approximate center of the \*\*game center\*\* \(the main form window\) and not the overall screen center\.  \(Rob\)

\- Unit counter hints: get rid of yellow warning color on pale yellow background and get rid of bullets if we cannot indent the listed items\.

__Documents:__

\- \\Documents\\WhatsNew\\WhatsNew\.pdf is now being updated with these commit notes so that there is a single reference available for all of them\.

