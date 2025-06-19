# What’s New in the 3\.0\.0\.9562 Release of 3 June 2025

> **Note**: Images omitted — refer to original DOCX for figures.


__Data:__

\- No changes\.

__Content:__

\- "__Overture__" updated by Charles on 29 May

\- “__Huenfeld Bridges__” Please include this update \(final OoB updates and spelling corrections\)

__Code:__

\- FPSS\-5404, 5743: The game sometimes runs out of Windows __GDI resources__ and asks the player to restart it or crash\. \->  Reduce GDI usage by making unit counter fragment bitmaps use the TMemoryBackend\. \(William, r9559, r9562\)  This results in a dramatic reduction in GDI objects in use in William’s testing\.

\- FPSS\-6022 Add explanations about overrun failing/succeeding to __radio log messages__ for attacker\. \(Will, r9550\)

\- FPSS\-6042: Fixed unit holding in River\. they now repath if they try to enter water but they already lost their amphib capabilities \(from losses for example\)\. \(Will, r9555\)

\- FPSS\-6066: __PBEM and PBEM\+\+__ games throw an Assertion Error at the end of VCR replay\.  \(Wentzel & Anderson\)  It took half a day to trace this down but I think we have this fixed now\.

\- FPSS\-6120, 6150: fixes to user editing via Unit Dashboard and unit waypoints, preventing crashes: \(William, r9560\)\.  So:

\-\- when selecting an order in Unit Dashboard, ensure the corresponding unit is selected, and corresponding unit waypoints are displayed

\-\- don't allow simultaneous editing from two or more Uni tDashboards\. 

\-\- offer a hint in the Unit Dashboard orders pop\-up menu when pending edits in another dashboard block editing in this dashboard\.

\-Other improvements:

\-\- when barrage waypoints are plotted inside minimum range or outside maximum range, state so explicitly to the player, removing confusion \(Joergen\)

\-\- in Unit Dashboard's orders list, show the number of rounds being fired \(Joergen\)

\-\- make the OnArrival orders form pop\-up closer to the current mouse position\.

\- FPSS\-6154: improve __radio log messages__ when command transfers \(HQ falls out\), adding message the log of the unit becoming new HQ\. \(William, r9549\)

\- FPSS\-6158: __Direct Path UI__: fix checked/enabled states in waypoint pop\-up menu, move Direct Path to last spot in the row, as it will be an infrequent choice\. \(William, r9556\)

\- FPSS\-6167: introduce a 0 minutes workaround for players to plan future Resupply orders that will resupply up to 100% in minimal time \(marcbellizi\) \(William, r9561\)

