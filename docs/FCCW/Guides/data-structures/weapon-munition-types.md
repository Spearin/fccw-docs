# Weapon Munition Types

> **Note**: Images omitted — refer to original DOCX for figures.


A munition is defined as a single type of round or burst from a gun tube\-based weapon such as a tank gun or mortar tube\. Items like ATGMs and most small arms are well enough covered in the standard Systems \(Weapons\) tab in the data spreadsheets\. 

This new tab of information requires adding weapon data from the systems tab to the new munitions tab\. Then breaking that information up into unique rounds of ammo based on the various penetration values and Characteristics seen in that weapon system data\.

From there, the unit’s weapon list needs updated to show the rounds used and the total number of rounds \(or bursts\) carried on the platform\. The weapons list can be a mix of weapon systems that have munitions or not\. See Section 18\.24 above for details on how to annotate munition load outs for weapon systems\.
!!! note

    __ Mistakes in the formatting of the Weapon System and it ammo loadout or munition information can cause the game to crash or have unwanted effects on combat\.


##  The Munition Types Tab

> **Note**: Image omitted — refer to original DOCX for figures.



The Munition Types Tab is similar to and uses the values, calculations, and shared characteristic of the Systems \(Weapons\) tab and the information from Section 10 Systems applies to this table for the columns outlined in Red above and zoomed in below in Section 11\.2\. The columns outlined in the blue box are new entries that have definitions seen below in Section 11\.3\.

## Columns Based on Systems Values

> **Note**: Image omitted — refer to original DOCX for figures.



The major difference for these columns compared to the Systems tab is the values apply to only one type of munition type like AP or HEAT round\.

With this new tab, users can craft any number of rounds used by a weapon system that has “projectile” munitions\. 

For example, you could create data for three 120mm AP rounds\. Each can have different values for ranges, penetration, or Characteristics\. 

If a munition type does not use one or any of the values for SA Value, AP Pen, or HEAT Pen, place a zero \(0\) in the field\. 

Be sure to only apply those Characteristics that apply to the type of round/munition being designed\. This is different from the Systems tab where the older data covers all munition cases and is parsed out internally in the code for capability\.

## Columns for the Munition Types

> **Note**: Image omitted — refer to original DOCX for figures.



These new columns have the following definitions\.

### AmmoTypeID

The AmmoTypeID must be a unique name that must start with the Weapon ID \(WpnID\) of the Weapon from the Systems Tab\. In the information above, the weapon ID is FGN1 that is a 105mm M101A1 field gun\. After the WpnID add an underscore and then add any alpha numeric name or code\. This could be “AP”, “AP1”, “XM896”, “bob42”, etc\.

Adding a “\!” in front of the AmmoTypeID will cause this munition to NOT be loaded in the game\. This is helpful for munitions with non\-implemented code or effect\.

### WpnID

This must be the unique WEAPTAG value of the particular weapon as seen in the Systems Tab\.

In the image above, the WpnID is “FGN1” from the Systems tag\.

### Name

This is the name of the munition type\. This can be any alpha\-numeric identifier\. Try to keep the name to 24 characters to be visible in the Ammo dialogs in game\.

In the image above we just used the name of the Weapon System\. A better name may have been “105mm AP Round” for the first entry\.

### Description

This describes the basic Type of Munition and is used in the Ammo dialogs found in game\. This should be a basic description of the function of the round\.

In the image above the first munition type is an “Armor Piercing” round\.

### Type

These codes tell the code how to apply the round when fired\. Codes in Italic are provisional and may be added later\.

> **Note**: Image omitted — refer to original DOCX for figures.



These codes must be typed in as shown to function in the game\.
!!! note

    __ New custom types will not function in game and require coding to work\. Contact the developers if new items are required\.


## Setting Up Munition Types

The following image shows how to add defined Munition types in the Units Tab in the Integrated Weapons List with other weapons\.

> **Note**: Image omitted — refer to original DOCX for figures.



### Munition Type Entry

Any number of weapon systems can be added to a unit, and they can be a mix of regular weapons from the systems tab or Munition Type weapons that are further defined by round type in the Munition Types Tab\.

Here are the rules to follow to format a valid Integrated Weapons List:

- Each Weapon System or Full Munitions entry MUST be separated by a comma and single space\. 
- Weapon Systems are denoted by a WEAPTAG, then “\*”, and then the number of rounds/bursts for the weapon\. In the data excerpt above, these Weapon Systems are entries like “VSW7\*120”, “ATGM\*13”, or “AAA11\*90”\.
- A Munitions based Weapon entry has the following format\. 
	- Starts with just the WEAPTAG value and then a “: ”\.
	- Then any number of defined munition types by AmmoTypeID then ”\*” and then the number of rounds
	- Each Munition Type MUST be separated by a ”; ”\.
	- The last or only Munition Type must be followed by a comma if another weapon entry follows\.

