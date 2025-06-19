# What’s New in the 2\.1\.5\.9335 Release of 13 Apr 2025

> **Note**: Images omitted — refer to original DOCX for figures.


__NEW__: The Matrix beta test is going to be done via Steam\.  This blew up our SVN\-based testing, so I have added a new file "IsNotSteamMode\.txt" to just the SVN builds and NOT the Steam build\.  If this file is present, then the game will NOT launch in Steam mode when otherwise it would now try to\.  \(Rename this new file to something else and it will try and fail unless you actually have Steam running and a Steam virtual serial number\.\)  For the SVN\-based testers, the best plan is to copy your "serialreg\.txt" from your Matrix\-installed copy of FCSS over into your beta game folder\.  It will then just run until the Cold War game release\.  Without this serialreg\.txt file the game will revert now to the internal drop dead date which is currently 31 May 2025, and will be extended from time to time until the game ships\.

__Modules__\.  At long last I am introducing "Cold War" as its own module\.  There are a lot of file changes so bear with me\.  Regular beta testers will see the 'new' Cold War and will find 10 campaigns and 60 standalone scenarios\.  All your saved games are still in the old folders though\.  All of your work in progress, test files, and saved games/campaigns are still where they started under \\FCCS\\Saved\\ and \\FCSS\\Saved\\\.

__Content:__

\- Tutorial 7 Engineer Operations is now finished by JohnO\.  This is confusing because Pro and Commercial engineering scope is quite different\.  We will circle back around and figure this out in the next week or two\.

\- Tutorial 9 Air Support Operations by JohnO is now up to date\.  I don't think its done, just not as out of date as before\.

\- Tutorial 10 Air Assault Operations \- ditto\.

\- UK1 campaign: corrections by the author made to the each Mission Briefings start time and duration\.

__Code:__

\- Scenario selection: indicate the day parts \(day, dawn, night, dusk\) covered in the scenario duration\. \(William, r9333\)

\- FPSS\-5963: Switch from using Survey Monkey for beta user feedback survey to just Google Forms instead\.  It is MUCH easier for us to use this survey info this way\.

__Documents:__

\- adding \\Documents\\Beta Users\\OTS Beta Intro 2025\.docx

