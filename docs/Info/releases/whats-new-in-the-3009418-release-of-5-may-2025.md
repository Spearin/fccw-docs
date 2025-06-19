# What’s New in the 3\.0\.0\.9418 Release of 5 May 2025

> **Note**: Images omitted — refer to original DOCX for figures.


__Data:__

\- Housekeeping\.  Each game module \(FCSS, FCCS, FCCW2\) was an independent module that either shared files in a common location or duplicated them all locally\.  Neither was as efficient as hoped\.  I have now created the GameModule 'Alias' for three internal folders: data, maps and sils\.  I've changed FCCS, FCSS, and FCCW2 to use these aliases to point to the files in FCCW and I can now delete about 6,000 files using perhaps 2 GB of disk space in total\.  The trick was to remove just the SVN\-versioned files but NOT any locally created or edited content that was \*\*not versioned\*\* in SVN\.  Your stuff like saved games and test scenarios and new maps\.  This has now been figured out and tested ok\.  Fresh new SVN downloads will now fetch far fewer files and proceed much more quickly again\.  Also, when we update sils, maps and national data files there will be far fewer, ideally only one, copy to update each time\.  Happy days for Rob\. Note that this does NOT apply to the Steam distro \- it is totally slimmed down already and has no duplicate files\.  


__Content:__

\- standalone "__The First Dance__" has had a slight change made to the scenario description by Charles\.

\- Standalone "__Huenfeld Bridges__" fixed SOP and typo in Mission Briefing by Charles\.

\- update “__The Ordeal of the 4th Lancers__” with updated Soest map, and with correct 4de Lancers Regiment badge\. \(William, r9412\)

\- FPSS\-6032: spottability problems in Soest map\.  Rework spottability computations to include additional units present in same location, as these would restrict access to best concealed/covered positions\. Tweak map values for urban terrain, and update Soest\.fp10 values\. \(William, r412\)

\- Charles updated the Setup areas and Revised SOPs for "__Finale__" scenario\.  \(Charles, r9414\)

\- "__Go West Young Man__" updated by Charles for SOPs, previous changes were lost?  


__Code:__

\- PBEM\+\+\.  New Matrix BETA serial numbers for Cold War have been hardwired into the "Beta 1" and "Beta 2" shortcut buttons now so that PBEM\+\+ can be tested for Cold War game\.

\- SOP: Improve SOP Manager Scope help dialog box\.  \(Kevin, r9404\)

\- Fix memory leak when the player starts plotting a path/barrage/etc\. and then cancels plotting\. \(William, r9407\)

\- FPSS\-6002: ScenEd: validate the deployment hexes in the BPs too\. \(Charles\) Iterate through every battleplan and flag any units that are Undeployed in the Validation Notes\.

\- FPSS\-6027: fix some AD systems such as Tunguska's not engaging helo's with SAMs because of weapon/ammo mix\-up in shot generation \(Gary\)\. \(William, r9405\)

\- Fix a rare crash in TMilUnit\.UpdateOrdersTiming\(\) where integer \- TDateTime \(seconds in float fraction\) conversion creates a difference/problem\.  Occurred in US1\-SN4 Percutio, when Soviet armor attempts to re\-path after hitting mines\. \(William, r9413\)

\- FPSS\-6034: We weren't creating terminal orders \(hold, screen, etc\.\) for impromptu unload \(Unload issued from right click menu\)\. This was only a problem if the unit didn't already have a dropoff set in the original TT plan \(or if we started the scenario embarked\)\. Now we do\.  \(Kevin, r9417\)

__Documents:__

\- \\Documents\\WhatsNew\\WhatsNew\.pdf is now being updated with these commit notes so that there is a single reference available for all of them\.

