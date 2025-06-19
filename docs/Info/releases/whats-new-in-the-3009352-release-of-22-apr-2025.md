# What’s New in the 3\.0\.0\.9352 Release of 22 Apr 2025

> **Note**: Images omitted — refer to original DOCX for figures.

!!! note

    The game version has rolled from "2\.1\.5\.x" to "3\.0\.0\.x" in anticipation of the CW beta testing and release\.


__Data:__  
\- All Cold War data files have been updated with 1\) Fixed Formation structure calls, 2\) added ad\-hoc ground transport formations for TT use, 3\) added WLR formations, Added Parked truck and jeep to units and to FARPs to help kill the moving FARP issues\. I have a few other items to circle back on from inputs from Fred and others, but those can wait a bit for me to deal with docs and bug reports\. \(Jim\)

__Content:__  
\- All scenarios were rebuilt late on 21 Apr 2025 to use the latest data files\.

\- All scenario metadata files \(\*\.blr\) have been updated to start with better default Scenario Complexity and Scenario Unit Totals/Size values\.  
  
\- Fix Eiterfeld map\. \(William\)  
  
\- Update five scenarios using the updated Eiterfeld map \(Desperation, Huenfeld Bridges, Race to the Fulda, The First Dance, The Three Sisters\)\.  
  
\- Fixed scenario info and briefings for "Desperation" and "The First Dance"\.  
  
\- Fixed BP problems in "Desperation" and "Race to the Fulda"\.  
  
\- "Go West Young Man" author added an Arty Bty  
  
\- "Eyes Ears and Teeth" touched to update based on feedback by author  
  
\- "The Ordeal of the 4th Lancers" typos fixed by author\.  
  
\- "Pursuit" updated by the author from feedback received\.  
  
\- "USSR2\-SN4 All That Glitters" updated by the author from SM feedback  
  
\- "Race to the Fulda" updated by Rob to replace sole instance of Soviet RU549 recon BRM with a RU547 recon BRM to fix data integrity error\.  
  
\- Tutorials 8 to 11 are now marked as "Tutorials" for scenario selection filtering purposes\.

__Code:__  
\- Steam play\. The contents of \\FCCW\\Data\\, \\Sils\\ and \\Bin\\ all need to be copied to \\Documents\\Games too if the main Steam \\Commons is in \\Program Files \(x86\)  
  
\- UI polish: Use an illustrated message for waypoint placement/editing errors\. \(William, r9339\)  
  
\- Crash fix to GetVisibleOrders\(\), as it is called before unit locations are definitive \- crash in EG1\-SN1 Liberation Begins campaign\. \(William, r9340\)  
  
\- PBEM\+\+ Issue Challenge and Cancel Challenge buttons disappeared at 125% font size \(Kevin\) Fixed by Rob  
  
\- FPSS\-5623: The final waypoint of a TT mission will now be freely moved to instead of moving as a formation\. This way, transports will go to the target hex instead of spreading around it\. Useful for things like returning to a carrier\. \(Kevin, r9342\)  
  
\- Also, a bunch of formatting/whitespace/code standard changes\.  
  
\- Also, a change in when we consider a TT plan in progress\. Shouldn't really change anything, I changed this investigating another thing that got fixed differently anyway, but bringing this in should add some resiliency\. \(Change in uPlayers\.pas\)  
  
Withdraw and Helo R&R Bug Fixes: \(Will, r9349\)  
\- Fixed an issue where helos would interrupt an emergency withdrawal to resupply at FARP causing strange behaviour \(FPSS\-5941, FPSS\-5915\)  
\- Fixed some issues where units were withdrawing when they should not be able to \(FPSS\-5962\)  
  
\- FPSS\-5974: All or most CW scenarios now have 'XS' and 'Easy' filter values embedded in the BLR files\. Yes, the internal value for TotalUnits was 0 in most cases and this led to the minimal XS and Easy values\. More intelligent defaults have now been provided\. Scenario authors can still override them and will\.  
  
\- Exception logging destination mailbox has changed to "[Support@OnTargetSimulations\.com](mailto:Support@OnTargetSimulations.com)" from Rob's personal one\. It is forwarded \(currently\) to Rob's mailbox behind the scenes\.  
  
\- FPSS\-5977: Cannot focus a disabled or invisible window in Dashboard\. This has to be a timing issue of some sort, so the calling routine was rewritten to delay the call just slightly\. Under review to see if it happens again\.

__Documents:__  
\- Andrew updated the \\\_Beta Users\\"OTS Beta Intro 2025\.docx"  
\- adding in \\\_Contributors\\FPC Campaigns User Notes\.docx"

