# What’s New in the 3\.0\.0\.9460 Release of 11 May 2025

> **Note**: Images omitted — refer to original DOCX for figures.


__Data:__

\- No changes\.

__Content:__

\- __Tutorial 10__ revised again by author on 9 May @ 3 p\.m\.

\- __Tutorial 12__ on NBC weapons has been canceled in favor of a simple write\-up\.

\- "__Link Up__" has been updated by the Editors on 10 May\.

\- Counter Battery vis weapons locating radar \("WLR"\) has been added by Jim to five of the scenarios in Wave 3: “__Huenfeld Bridges__”, “__Kampfgruppe Becker”,__ “__Race to the Fulda__”, “__Return to Fulda__”, and “__The Battle of the Nations__”\.  This replaces the previous CB fire driven by a dice roll\.  Documentation to follow shortly\.

__Code:__

\- Unit Dashboard handling dead units: do not generate new orders if the unit inspected has none\. Just handle 0\-order units\.  \(William, r9453\)

\- FPSS\-6061: fix AD systems not engaging CAS units appearing in the same hex \(substitute effective AD range for those cases\)\.

Also fix effective steps calculations in all AttackX routines, likely yielding increased readiness loss from the attack for the defender\.

\- FPSS\-6064: Soviet 82mm Vasilek mortar does not have a mortar preset in SOP\.  It was being classed as a light utility vehicle instead of a mortar unit\.  Fixed by Kevin in r9457\.

\- FPSS\-6065: ScenEd: saving a scenario sometimes gives a quadruple "Copy Fail" message\.  A slightly mangled path name was involved and is now fixed\.

\- Fix corner case where a weapon locating radar \("WLR"\) would detect projectiles from an off\-map battery at an on\-map location\.

\- FPSS\-6068: fix bad newline in dialog and upgrade the dialog to an illustrated message while we're at it\. \(William, r9459\)

