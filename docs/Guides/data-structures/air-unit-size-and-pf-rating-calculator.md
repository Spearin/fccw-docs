# Air Unit Size and PF Rating Calculator

> **Note**: Images omitted — refer to original DOCX for figures.


As noted earlier in this document\. The Size and PF rating for Air Units is derived from some input parameters and some calculations to put both factors into values that work within the game engine\. You can use this table one of two ways\. The first is to see if your platform is already on the list of over 600 aircraft, drones, and helicopters on our existing list \(We will be adding more entries over time of course\)\. Alternately, you can add more entries into the spreadsheet by supplying a few key parameters as noted below\.

> **Note**: Image omitted — refer to original DOCX for figures.



## Adding More Data

- Go to the bottom of the table and add in a new row by dragging the table corner marker \(in the bottom left side of the table\) down to add in new rows\.
- In the Air Unit ID field, add the name of the platform you wish to add\.
- In the Empty Wt LBs field, enter the empty weight of the platform in pounds \(US\)\.
- In the Engine/Exhaust Ports field, enter the number of engines/power plants on the platform\. Also include additional VTOL exhaust ports \(For example, the Harrier has a 4\-port system but no main power plant exhaust so a value of 4 will be used\)\. 
!!! note

    __ For any Glider based platform you must enter “1” in the Engines field for the calculations to work\. The Glider functionality will be resolved by the platform AIRGL SU Type\.


- In the Trans field, place a “y” if the platform is a transport of some kind and “n” if it is not\. A transport is defined as any platform that carries internal cargo beyond its operating crew\. So, a Mi\-24 Hind is a transport \(carries troops\), but a Mi\-28 Havoc is not\.
- In the Engine Type field, place “r” is the primary engine system is a Rotor, “p” if it is a Propeller, and “j” if it is a Jet/Rocket”\. 
!!! note

    __ for a Glider enter “p” so the program calculates properly\.

!!! note

    __ In cases of a hybrid engine setup, choose Jet over Rotor and Propeller, or choose Rotor over Propeller\.


- A value for the Final PF Rating and the Final Size with be shown in the last two fields\. Transfer these results to the Units Data sheet for the platform you added\.
- You may wish to sort the table by the Air Unit ID once you have recorded the new entries\.
!!! warning

    *__*There are calculations hidden between column G and O in the spreadsheet\. If you want to change or experiment on matching up the Sizes and PFs in a different way you are free to edit things\. Make a backup first\.


