# Systems

The Systems tab is where each specific weapon or system (Precision Guided Munition, Tank Gun, and Anti-Tank Guided Missile) is defined for a number of characteristics.

## WEAPTAG

The WEAPTAG is an alphanumeric entry that must be a unique identifier for each entry. Our basic format is the weapon type character code (See Section 6 above) and then an integer value to create values like “ATGM4”, or “ISW8”.

!!! warning
    Once you set these values for a dataset and use it in the scenario editor, any edits, or reorders of the WEAPTAGs that break the initial WEAPTAG-Weapon relationship will cause existing scenarios to load bad data if you update a scenario’s data with a corrupted dataset with remapped WEAPTAGs. If you need to add more weapons between entries (for data consistency/appearance), you should add to the code with additional alphanumeric characters. For example, if you had “ATGM3” and “ATGM4” in your list and wanted to add in two more variants, you can add rows to the spreadsheet in between them and use WEAPTAGs like “ATGM3A” and “ATGM3B”. You could also add a new value greater than the largest weapon type the WEAPTAG list.

## Name

This is the given identification of a specific weapon or system used by its nation. For example, “AGM-114K Hellfire II”, “9M330 Tor”, “120mm L11A5”, etc.

## NATO Designation

This is a weapon’s or system’s specific NATO designation, if one exists. For example, “SA-15 Gauntlet” for the “(9M330 Tor”). This field is included to allow for most OpFor hardware of Russian origin to carry its given NATO designated code and name. It can also be used for alternate names used by countries for other countries’ hardware.

## Description

This is a short description explaining the Weapon’s function/type. For example, “Auto Cannon”, “Medium Tank Cannon”, etc. This description is displayed in the Sub-Unit Inspector and in several other information panels when weapon information is shown.

## Type

| **Type Tag** | **New Description** | **Role** |
|--------------|---------------------|----------|
| **AAA**   | Anti-Aircraft Gun | AD,AP |
| **ACN**   | Aircraft Cannon | AT,AP,AD |
| **AGL**   | Automatic Grenade Launcher | AP,AT |
| **AMG**   | Aircraft Machine Gun | AP,AT,AD |
| **ARK**   | Air Launched Rocket | AT,AP |
| **ATK**   | Anti-Tank Gun | AT |
| **AUCN**  | Auto Cannon | AT,AP,AD |
| **FGN**   | Artillery Gun | AP,AT |
| **ISW**   | Infantry Support Weapon | AP |
| **MGN**   | Machine Gun | AP |
| **MTR**   | Mortar | AP,AT |
| **RKT**   | Rocket | AP,AT |
| **RPG**   | Rocket Propelled Grenade | AT |
| **SMA**   | Light Small Arms | AP |
| **TGN**   | Light Tank Cannon | AT,AP |
| **VSW**   | Vehicle Support Weapon | AP,AT |
| **ACM**   | Cluster Munition | AT,AP |
| **AIB**   | Iron Bomb | AP,AT |
| **EXP**   | Explosive Device | AP,AT |
| **FLM**   | Flame Weapon | AP,AT |
| **AARM**  | Anti-Radiation Missile | AL |
| **AGM**   | Guided Missile | AP,AT,AL |
| **ATGM**  | Anti-Tank Guided Missile | AT,AL |
| **SAM**   | Surface to Air Missile | AD |
| **BIOW**  | Biological Weapon | AP |
| **CWN**   | Chemical Warhead Non-Persistent | AP,AT,AL |
| **CWP**   | Chemical Warhead Persistent | AP,AT,AL |
| **NCW**   | Nuclear Warhead (kT) | AA |

This is the weapons type and listed in Section 6 above as the Type Tag. Examples are “ATGM”, “ISW”, and “AGM”.

## Role

Weapon Role codes are used in the game engine to help the AI determine use versus targets. Weapons can have more than one role. In those cases, a comma delimited list in the Weapons Role field is required.

| **Role** | **Description** |
|----------|-----------------|
| **AA** | Anti-All: Affects all types |
| **AD** | Air Defense: Target Airborne Threats |
| **AP** | Anti-Personnel: Target Ground Troops |
| **AT** | Anti-Tank: Target Land Based Threats |

The current list of Role based on Weapon Type Tag Follows:

## Accuracy

Weapon accuracy comes in two types, Guided/Smart Weapons with their own means to engage a target (these will have one or more Guidance List Characteristic (see Section 5.2 above) or a basic accuracy related to the type of weapon system in use (primarily gun-based systems).

### Guided/Smart Weapons

The accuracy for weapon systems like AARM, AGM, ATGM, NCW, RKT (guided), or SAM. The range is 0 to 20 and each point of value is worth 5%. Set this value to at or near the weapons rated accuracy for use against its standard target type. Other weapon related characteristics and enemy systems will adjust this base accuracy in combat.

### Non-Guided Weapons

For all of the other non-guided weapons use the value found in the table below for the type of weapon and in some cases size/caliber to get the basic accuracy number. These weapons will factor in fire control, crew capability and other effects to determine a final hit probability in combat.

| **Type** | **Description** | **Accuracy** |
|----------|-----------------|--------------|
| **AAA**  | Anti-Aircraft Gun ≥ 12.7mm | 4 |
| **AAA**  | Anti-Aircraft Gun < 12.7mm | 3 |
| **ACM**  | Cluster Munition | 5 |
| **ACN**  | Aircraft Cannon | 6 |
| **AGL**  | Automatic Grenade Launcher | 4 |
| **AIB**  | Iron Bomb (Air launched, free fall) | 1 |
| **AMG**  | Aircraft Machine Gun | 5 |
| **ARK**  | Air Launched Rocket(s) | 5 |
| **ATG**  | Anti-Tank Gun (Recoilless Rifles) | 2 |
| **AUCN** | Chain Gun | 6 |
| **EXP**  | Explosive Device (Grenade, IED) | 5 |
| **FGN**  | Artillery Gun (All sizes) | 1 |
| **FLM**  | Flame Weapon | 5 |
| **ISW**  | Infantry Support Weapon | 3 |
| **MGN**  | Machine Gun | 3 |
| **MTR**  | Mortar (All Sizes) | 1 |
| **RKT**  | Unguided Ground Launched Rockets | 1 |
| **RPG**  | Rocket Propelled Grenade | 2 |
| **SMA**  | Medium Small Arms (Assault Rifles) | 3 |
| **SMA**  | Light Small Arms (Rifles, SMGs) | 2 |
| **SMA**  | Light Small Arms (Pistols) | 1 |
| **SMA**  | Small Arms (Sniper Rifles) | 10 |
| **TGN**  | Tank Cannon – Smoothbore per 2500m of Range | 1 |
| **TGN**  | Tank Cannon – Rifled per 2500m of Range | 2 |
| **VSW**  | Vehicle Support Weapon | 3 |

## Range

This is the maximum range of the weapon system in meters.

## Effective Range

Depending on weapon type, the Effective range is calculated by taking the maximum range in meters times the Range Multiplier. This range is used in combat calculations as a factor for hit percentage and also the base point for the weapons AP penetration calculated in Section 19.12 below.

| **Weapon Type(s)** | **Range Multiplier** |
|--------------------|----------------------|
| AAA, AMG, AUCN, FGN, ISW, MGN, MTR, SMA (not Sniper), TGN, VSW | 0.33 |
| ACN, AGL, AIB, ARK, EXP, FLM, RKT (Unguided), RPG, SMA (Sniper only) | 0.5 |
| ACM | 0.7 |
| AARM, AGM, ATGM, NCW, RKT (Guided), SAM | 1 |

## Min Range

Certain weapon systems have a minimum range which must be traveled or is unreachable. Primarily this will affect artillery systems, ATGMs, SAMs, and some PGMs. IF there is no minimum range restriction set the value in this field to 0.

## SA Value

SA or Small Arms value is a relative measure of small high-speed projectiles from a gun, machine gun or other ballistic firing weapon system or from blast fragmentation warheads on artillery shells or missile warheads (ATGMs, SAMs, and Rockets). The following charts show the calculated SA value for the various types of weapons that have this value. The size if the bore size of the barrel or diameter of the shell in millimeters.

### SA Value for Artillery Guns

Use these values for tube artillery based on the shell size in millimeters. If the size is not on the table, you can use the formula below to calculate the value. Values are rounded to the nearest 0.25.

**SA Value = Tube Size in mm \* 0.04338 + 3.35746 – then round to the closest 0.25**

| **HE: Arty Guns** | **SA** |
|-------------------|--------|
| 0   | 0 |
| 40  | 5 |
| 50  | 5.5 |
| 60  | 6 |
| 81  | 6.75 |
| 82  | 7 |
| 105 | 8 |
| 120 | 8.5 |
| 122 | 8.75 |
| 130 | 9 |
| 152 | 10 |
| 155 | 10 |
| 160 | 10.25 |
| 175 | 11 |
| 203 | 12.25 |
| 227 | 13.25 |
| 240 | 13.75 |
| 300 | 16.25 |

### SA Value for Mortars

Use these values for mortars based on the shell size in millimeters. If the size is not on the table, you can use the formula below to calculate the value. Values are rounded to the nearest 0.25.

**SA Value = Tube Size in mm \* 0.0414 + 1.1122 – then round to the closest 0.25**

| **HE: Arty Guns** | **SA** |
|-------------------|--------|
| 0   | 0 |
| 40  | 5 |
| 50  | 5.5 |
| 60  | 6 |
| 81  | 6.75 |
| 82  | 7 |
| 105 | 8 |
| 120 | 8.5 |
| 122 | 8.75 |
| 130 | 9 |
| 152 | 10 |
| 155 | 10 |
| 160 | 10.25 |
| 175 | 11 |
| 203 | 12.25 |
| 227 | 13.25 |
| 240 | 13.75 |
| 300 | 16.25 |

### SA Value for Rockets

Use these values for rockets based on the size in millimeters of the rocket diameter. If the size is not on the table, you can use the formula in the header cell after the dash to calculate the value. If the rocket is a Fuel Air Explosive type (FAE), use the FAE column.

| **HE: Rockets – mm/15** | **SA** | **FAE** |
|-------------------------|--------|---------|
| 0   | 0  | 0   |
| 40  | 3  | 10  |
| 50  | 3  | 13  |
| 60  | 4  | 15  |
| 81  | 5  | 20  |
| 82  | 5  | 21  |
| 105 | 7  | 26  |
| 120 | 8  | 30  |
| 122 | 8  | 31  |
| 130 | 9  | 33  |
| 152 | 10 | 38  |
| 155 | 10 | 39  |
| 160 | 11 | 40  |
| 175 | 12 | 44  |
| 203 | 14 | 51  |
| 227 | 15 | 57  |
| 240 | 16 | 60  |
| 300 | 20 | 75  |
| 400 | 27 | 100 |
| 750 | 50 | 188 |

### SA Value for Small Arms

Use these values for small arms and anti-aircraft guns based on round size in millimeters. If the size is not on the table, you can use the formula in the header cell after the dash to calculate the value. If the gun system has multiple barrels, use the modifier at the bottom of the table to adjust the SA value to get a final data value.

| **Small Arms/AAG – 0.0915mm + 0.6393** | **SA** |
|----------------------------------------|--------|
| 0     | 0  |
| 4     | 1  |
| 5     | 1  |
| 7.62  | 1  |
| 9     | 1  |
| 12.7  | 2  |
| 14    | 2  |
| 20    | 2  |
| 25    | 3  |
| 30    | 3  |
| 35    | 4  |
| 40    | 4  |
| 50    | 5  |
| 60    | 6  |
| 80    | 8  |
| 105   | 10 |
| 120   | 12 |
| 125   | 12 |
| **2 to 3 barrels = +1 to SA** |        |
| **4 to 6 barrels = +2 to SA** |        |

### SA Value for Tank HE Rounds

Use these values for tank HE rounds based on the shell size in millimeters. If the size is not on the table, you can use the formula in the header cell after the dash to calculate the value.

| **HE: TGNs – mm/20-1** | **SA** |
|------------------------|--------|
| 0     | 0  |
| 40    | 1  |
| 50    | 2  |
| 60    | 2  |
| 81    | 3  |
| 82    | 3  |
| 105   | 4  |
| 120   | 5  |
| 122   | 5  |
| 130   | 6  |
| 152   | 7  |
| 155   | 7  |
| 165   | 7  |
| 175   | 8  |
| 203   | 9  |
| 227   | 10 |
| 240   | 11 |
| 300   | 14 |

## AP Pen

The AP Pen value represents the best AP round for a given weapon system and is calculated by taking the weapon’s penetration value in millimeters of RHA at effective range (may vary with a weapon but roughly a range equal to muzzle velocity) divided by 10. This value assumes long rod penetrators for tank guns and AP type rounds for other kinetic weapon systems. The penetration value will be increased or decreased by an in-game engine calculation based on actual range to target.

## HEAT Pen

The HEAT Pen value represents the best HEAT round for a given weapon system and is calculated by taking the weapon’s penetration value in millimeters of RHA divided by 10. HEAT values do not change over range. Do not degrade or decrement the full value of the HEAT penetration for any special conditions (top attack, tandem or triple warheads, standoff probes, etc.), those items will be accounted for in the various Characteristics lists in Section 5.2 above.

## Weapon Lists

There are three columns in the data file devoted to lists of parameters. They deal with Abilities, Defenses, and Equipment Platform Characteristics. As you can see from the image below, these lists are sparsely populated and very type dependent.

### Capabilities List

These Shared Characteristic Codes for Weapons-Capabilities can be found in Section 5.2 above. If your weapon or system has any of the Capabilities found in the lists, you add them to a comma delimited list in the Capabilities List spreadsheet field.

### Defenses List

These Shared Characteristic Codes for Weapons-Defenses can be found in Section 5.2 above. If your weapon or system has any of the Defenses found in the lists, you add them to a comma delimited list in the Defenses List spreadsheet field.

### Guidance List

These Shared Characteristic Codes for Weapons-Guidance can be found in Section 5.2 above. If your weapon or system has any of the Guidance systems found in the lists, you add them to a comma delimited list in the Guidance List spreadsheet field. You may have more than one guidance system on the weapon.

## Sound Effect

Each weapon has an associated sound effect when it is fired/used. These “\*.WAV” files are based on weapon type as noted in the table below. You can add in your own weapon sound effects and that information is covered in the Game Engine Modification document.