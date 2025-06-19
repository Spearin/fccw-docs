# What’s New in the 3\.0\.0\.9437 Release of 8 May 2025

> **Note**: Images omitted — refer to original DOCX for figures.


__Data:__

\- Data and art update\. Fixes for bad helo guns\. Better color for the Brits\. Latest placeholder splash art elements\. \(JRS, r9435\)  All CW national data files have been touched and therefore all scenarios have been refreshed\.

__Content:__

\-  Updates for "__Hammer Falls__", "__Quietly Flows the Donau__", and "__Once More Unto The Breach__" from the Editors\.

\- Also, __"A Second Dance__" and "__The First Dance__" by the Editors\.  Corrected a typo in The First Dance that a player noticed\.

\- "__Race to the Fulda__" regressed to having an RU549 platform in "SPA/68 FA MRR" instead of the RU547 that we replaced it with\.  RU549 no longer exists in the Soviet national data file\. \(Rob, r9437\)

\- __Tutorials 7 and 8__ updated by JohnO after feedback from GaryC

\- all scenarios have been refreshed due to the national data file updates

__Code:__

\- FPSS\-5934: Fail more gracefully when loading an unfinished scenario file\.  It now displays the error message \(which is useful to the devs only\) and then shows a second one that the scenario is unplayable for some reason\.  It goes back to the Setup main screen instead of throwing an exception now\.

\- FPSS\-5987: Scenario Welcome window says improved positions cannot be moved in setup, which is incorrect\.  This dialog has now been fixed\.

\- FPSS\-6044: fixed an incorrect check to see if we were about to move into the hex we're already in\. \(Kevin, r9431\)

