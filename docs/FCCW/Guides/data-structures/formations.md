# Formations

> **Note**: Images omitted — refer to original DOCX for figures.


This is where the whole process comes together\. The Formations Tab is where you assemble the units and formations used in the scenario editor to build your orders of battle\.

> **Note**: Image omitted — refer to original DOCX for figures.



## Description \(Format Use\)

> **Note**: Image omitted — refer to original DOCX for figures.

This field has several uses for providing OOB formation names, names for formation elements, cues for node indenture, visible separators between main and subgroups of formations and elements, and identifiers or names for major groups in the formation spreadsheet table\. 

All these elements are used to provide the layout of selectable formations and elements of formation in the game’s scenario editor\. These primary types are as follows:

### Major Formation Identifiers

Found in the chevron brackets” ” These are major formation group names that form major OOB elements like “” or “” or "" and “ **Note**: Image omitted — refer to original DOCX for figures.

To put together an OOB, the names and use of the node indent symbols “>”, “>>”, and “>>>” allow the Scenario Editor to generate an indented list based on the indents and the names\. The above Motor Rifle Battalion is comprised of a “>”Battalion HQ, “>”Motor Rifle Company, “>”Mortar Battery, “>”Anti\-Tank Platton, “>”AA Section, and “>” Attached Tank Company\. The Anti\-Tank Platoon has a third level breakdown with the “>>” noted platoon element entries\.

## Code

This __MUST__ be a unique identifier for each formation element in the formations table that has information in the Composition Field of the table\. It can be an alphanumeric construction with symbols but no spaces\. These tags are used in formation compositions, so keeping them short, but identifiable is helpful\.

These Codes are also used in formation compositions to build larger formation groups\.

### Indented Node Code

The ability to control the level of indenture of the collapsible nodes in the OOB section of the Scenario Editor has been added\. This improves both the grouping and readability of the data\. Eight levels of indenture are usable, and they are “ **Note**: Image omitted — refer to original DOCX for figures.



Next is an image of how that structure appears in the game’s Scenario Editor\.

> **Note**: Image omitted — refer to original DOCX for figures.



## Tag

These are alphanumeric names that appear as part of a unit’s identification in\-game\. Such as “4/A/2\-5 Cav”\. These names can be renamed in the scenario editor if they do not auto generate in a way that works for your scenario\. There are two special codes you can use\. 

- %C/ \- This will provide an incrementing capitol letter\. This is good for adding the Company Identifier for most NATO style units such as the “A/” in the example above\.
- %d/ \- This with provide and incrementing number starting at “1” and is good for most NATO Platoon Identifiers\. This would be the “4/” in the example above\.

Reviewing the various data file entries will give you a sense of what can be done\. These unit identifiers should be as short as practical to be seen on a counter\. The full name will appear in other information sources/panels \(like the Subunit Inspector and Staff Reports\) in full\.

## Composition

The Composition entry is used to generate the various orders of battle for a given nation’s forces\. There are two types of Composition constructs: Units and Formations\. 

To build a Unit Composition, you will need to use the CompID of a particular unit and then a “\*” symbol with the count of those units \(if there is only a single unit, the “\*1” can be omitted\)\. 

To build a Formation Composition, you will need to use the Code in column two of a particular formation element and then a “\*” symbol with the count of those formation elements \(if there is only a single Code, the “\*1” can be omitted\)\. 
!!! warning

    __You cannot mix CompIDs and Codes in the same line or it will crash the game\. Data Validation will catch most of these errors when used\.


> **Note**: Image omitted — refer to original DOCX for figures.



## Role

The Role identifier is a set value that describes the overall use of the particular formation element and is used by the game’s AI to control behavior\. Refer to Section 10 above, for a list of all valid Roles\.

## Unit Size

This is the NATO size symbol corresponding to the size of the formation element in the row, not the overall size of the whole formation\. These symbols will show up on the counters in\-game\. 
!!! note

    __ For a Platoon, it is three periods and not an ellipse\. Excel is extremely helpful in turning three periods into an ellipse for you\. This will not work in the game and will get flagged in the Validation Program\. To change this behavior, go into Excel’s Options, Proofing, click AutoCorrect Options, scroll the Replace Text as you type window and find the three periods replaced with the ellipse and Delete that entry\. You are good to go now\.


## Is HQ Of

If your formation row entry is an HQ structure, you will then need to assign a NATO size symbol for the size of the formation it commands \(not the size of the unit itself, which is covered in the Size field\)\.

## BPT Default

These codes are used by the game engine to set various AI parameters and behaviors based on the composition of the formation this code is used on\. A list of valid codes can be found in Section 11 above\.
!!! note

    __ This feature is currently under implementation and the full effect may not be present in game code, but the Data Validation Program has the current list of codes and can detect bad or unneeded codes in the formation table\.


## Task Force Type

These codes are used by the Scenario Editor to filter out certain mission types of units\. This allows the user to zero in on certain formations they need to add to the scenario\. Valid Task Force Types can be found in Section 9 above\. Task Force Types should be used on all formations you want to group and the Formation Identifiers and separators to keep the look and information clear\.

You can assign more than one filter to a row if they are comma\- delimited\. This allows for certain formations to appear in multiple Task Force Types\. Check the supplied data files to see examples of Task Force Type use\.
!!! note

    __ This feature is not currently active in the game, and we may at some point remove it\.


## Formation Format Best Practices

