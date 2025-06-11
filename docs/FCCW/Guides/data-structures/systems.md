# Systems

> **Note**: Images omitted — refer to original DOCX for figures.


The Systems tab is where each specific weapon or system \(Precision Guided Munition, Tank Gun, and Anti\-Tank Guided Missile\) is defined for a number of characteristics\.

## WEAPTAG

The WEAPTAG is an alphanumeric entry that must be a unique identifier for each entry\. Our basic format is the weapon type character code \(See Section 6 above\) and then an integer value to create values like “ATGM4”, or “ISW8”\. 
!!! warning

    *__*Once you set these values for a dataset and use it in the scenario editor, any edits, or reorders of the WEAPTAGs that break the initial WEAPTAG\-Weapon relationship will cause existing scenarios to load bad data if you update a scenario’s data with a corrupted dataset with remapped WEAPTAGs\. If you need to add more weapons between entries \(for data consistency/appearance\), you should add to the code with additional alphanumeric characters\. For example, if you had “ATGM3” and “ATGM4” in your list and wanted to add in two more variants, you can add rows to the spreadsheet in between them and use WEAPTAGs like “ATGM3A” and “ATGM3B”\. You could also add a new value greater than the largest weapon type the WEAPTAG list\.


## Name

This is the given identification of a specific weapon or system used by its nation\. For example, “AGM\-114K Hellfire II”, “9M330 Tor”, “120mm L11A5”, etc\.

## NATO Designation

This is a weapon’s or system’s specific NATO designation, if one exists\. For example, “SA\-15 Gauntlet” for the “\(9M330 Tor”\)\. This field is included to allow for most OpFor hardware of Russian origin to carry its given NATO designated code and name\. It can also be used for alternate names used by countries for other countries’ hardware\.

## Description

This is a short description explaining the Weapon’s function/type\. For example, “Auto Cannon”, “Medium Tank Cannon”, etc\. This description is displayed in the Sub\-Unit Inspector and in several other information panels when weapon information is shown\. 

## Type

This is the weapons type and listed in Section 6 above as the Type Tag\. Examples are “ATGM”, “ISW”, and “AGM”\.

## Role

Weapon Role codes are used in the game engine to help the AI determine use versus targets\. Weapons can have more than one role\. In those cases, a comma delimited list in the Weapons Role field is required\.

Role

Description

AA

Anti\-All: Affects all types

AD

Air Defense: Target Airborne Threats

AP

Anti\-Personnel: Target Ground Troops

AT

Anti\-Tank: Target Land Based Threats

The current list of Role based on Weapon Type Tag Follows:

Type Tag

New Description

Role

AAA

Anti\-Aircraft Gun

AD,AP

ACN

Aircraft Cannon

AT,AP,AD

AGL

Automatic Grenade Launcher

AP,AT

AMG

Aircraft Machine Gun

AP,AT,AD

ARK

Air Launched Rocket

AT,AP

ATK

Anti\-Tank Gun 

AT

AUCN

Auto Cannon

AT,AP,AD

FGN

Artillery Gun

AP,AT

ISW

Infantry Support Weapon

AP

MGN

Machine Gun

AP

Type Tag

__New Description__

__Role__

MTR

Mortar

AP,AT

RKT

Rocket

AP,AT

RPG

Rocket Propelled Grenade

AT

SMA

Light Small Arms

AP

TGN

Light Tank Cannon

AT,AP

VSW

Vehicle Support Weapon

AP,AT

ACM

Cluster Munition

AT,AP

AIB

Iron Bomb

AP,AT

EXP

Explosive Device

AP,AT

FLM

Flame Weapon

AP,AT

AARM

Anti\-Radiation Missile

AL

AGM

Guided Missile

AP,AT,AL

ATGM

Anti\-Tank Guided Missile

AT,AL

SAM

Surface to Air Missile

AD

BIOW

Biological Weapon

AP

CWN

Chemical Warhead Non\-Persistent

AP,AT,AL

CWP

Chemical Warhead Persistent

AP,AT,AL

NCW

Nuclear Warhead \(kT\)

AA

## Accuracy

Weapon accuracy comes in two types, Guided/Smart Weapons with their own means to engage a target \(these will have one or more Guidance List Characteristic \(see Section 5\.2 above\) or a basic accuracy related to the type of weapon system in use \(primarily gun\-based systems\)\.

### Guided/Smart Weapons

The accuracy for weapon systems like AARM, AGM, ATGM, NCW, RKT \(guided\), or SAM\. The range is 0 to 20 and each point of value is worth 5%\. Set this value to at or near the weapons rated accuracy for use against its standard target type\. Other weapon related characteristics and enemy systems will adjust this base accuracy in combat\.

### Non\-Guided Weapons

For all of the other non\-guided weapons use the value found in the table below for the type of weapon and in some cases size/caliber to get the basic accuracy number\. These weapons will factor in fire control, crew capability and other effects to determine a final hit probability in combat\.

__Type__

__Description__

__Accuracy__

__AAA__

Anti\-Aircraft Gun >= 12\.7mm

4

__AAA__

Anti\-Aircraft Gun  **Note**: Image omitted — refer to original DOCX for figures.



### Capabilities List

These Shared Characteristic Codes for Weapons\-Capabilities can be found in Section 5\.2 above\. If your weapon or system has any of the Capabilities found in the lists, you add them to a comma delimited list in the Capabilities List spreadsheet field\.

### Defenses List

These Shared Characteristic Codes for Weapons\-Defenses can be found in Section 5\.2 above\. If your weapon or system has any of the Defenses found in the lists, you add them to a comma delimited list in the Defenses List spreadsheet field\.

### Guidance List

These Shared Characteristic Codes for Weapons\-Guidance can be found in Section 5\.2 above\. If your weapon or system has any of the Guidance systems found in the lists, you add them to a comma delimited list in the Guidance List spreadsheet field\. You may have more than one guidance system on the weapon\.

## Sound Effect

Each weapon has an associated sound effect when it is fired/used\. These “\*\.WAV” files are based on weapon type as noted in the table below\. You can add in your own weapon sound effects and that information is covered in the Game Engine Modification document\.

> **Note**: Image omitted — refer to original DOCX for figures.



