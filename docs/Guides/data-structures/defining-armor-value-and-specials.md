# Defining Armor Value and Specials

> **Note**: Images omitted — refer to original DOCX for figures.


Based on the value\(s\) obtained in Section 18\.25\.3 above either a Hull PF or a Turret PF and associated Hull PF was generated\. In the case of a pure hull design the Hull PF rating was entered in the data sheet\. If a turret was present on the AVF platform the Turret PF rating was entered in the data sheet\. This is a very basic kinetic resistance value, and we use several Characteristics to account for the other more advanced aspects of armor coverage\. The following sections will cover these additional aspects\.

## Hull to Turret Ratio \(HTR\)

The HTR Characteristics are located in the Defensive Abilities listing and are defined in the following table\. This code allows the game engine to calculate a PF for the hull based on the Turret PF and this code\.

__Code__

__Unit Special Description__

__Notes__

HTR1

Hull to Turret Ratio, Type 1

Ratio is 1\.40 for Hull PF / Turret PF rating, \+50% to PF adjustment for hull hits

To determine which value to use, calculate Hull PF / Turret PF and consult the range in the Notes Field\. If the value falls into the range of HTR4 \(near 1\.0\) you do not need to add this special to the Defenses List of the unit\. 

## Advanced Composite Armour \(ACA\)

The ACA Characteristics are in the Defensive Protection listing and are defined in the following table\. This code allows the game engine to augment the PF rating against HEAT based rounds based on location \(hull or turret\) and aspect \(Front, Side, Rear, and Top\)\.
!!! note

    __ You can assign more than one of these codes in the Defenses List of a unit if there is a variable level of coverage based on location and aspect\.


__Code__

__Unit Special Description__

__Notes__

ACAH1

Advanced Composite Armour \(Effectiveness 1\)

2\.0 ratio Hull, Aspect Coded \(F/S/R/T\)

ACAT1

Advanced Composite Armour \(Effectiveness 1\)

2\.0 ratio Turret, Aspect Coded \(F/S/R/T\)

To determine which value to use, a calculation of the ratio of the HEAT resistance to Kinetic resistance for the location and aspect needs to be done and then compared to the table to get the correct basic ACA code\. To complete an ACA code, add the Aspect Letters after the 1\-5 effectiveness value\. 

For example, if you have an “ACAH3” \(hull ACA with a ratio between 1\.5 and 1\.75\) and it covers front and side only the full code will be “ACAH3FS”\. 

## Explosive Reactive Armour \(ERA\)

The ERA Characteristics are located in the Defensive Protection listing and are defined in the following table\. This code allows the game engine to augment the HEAT or Kinetic AP penetration value of an incoming round based on location \(hull or turret\) and aspect \(Front, Side, Rear, and Top\)\. You can also use these codes for NERA protection as well\.
!!! note

    __ You can assign more than one of these codes in the Defenses List of a unit if there is a variable level of coverage based on location and aspect\.


__Code__

__Unit Special Description__

__Notes__

ERAH1

ERA \- Hull, Type 1, Aspect \(Front/Side/Rear/Top\)

Explosive reactive armor, early type, CE only \- Kontakt\-1, Hull, Aspect Coded \(F/S/R/T\)

ERAH2

ERA \- Hull, Type 2, Aspect \(Front/Side/Rear/Top\)

Explosive reactive armor, early type, CE only \- Kontakt\-3, Hull, Aspect Coded \(F/S/R/T\)

__Code__

__Unit Special Description__

__Notes__

ERAH3

ERA \- Hull, Type 3, Aspect \(Front/Side/Rear/Top\)

Explosive reactive armor, late type, CE/KE \- Kontakt\-5 \(85\+\), Hull, Aspect Coded \(F/S/R/T\)

ERAH4

ERA \- Hull, Type 4, Aspect \(Front/Side/Rear/Top\)

Explosive reactive armor, late type, CE/KE \- Relikt \(06\+\), Hull, Aspect Coded \(F/S/R/T\)

ERAT1

ERA \- Turret, Type 1, Aspect \(Front/Side/Rear/Top\)

Explosive reactive armor, early type, CE only \- Kontakt\-1, Turret, Aspect Coded \(F/S/R/T\)

ERAT2

ERA \- Turret, Type 2, Aspect \(Front/Side/Rear/Top\)

Explosive reactive armor, early type, CE only \- Kontakt\-3, Hull, Aspect Coded \(F/S/R/T\)

ERAT3

ERA \- Turret, Type 3, Aspect \(Front/Side/Rear/Top\)

Explosive reactive armor, late type, CE/KE \- Kontakt\-5 \(85\+\), Turret, Aspect Coded \(F/S/R/T\)

ERAT4

ERA \- Turret, Type 4, Aspect \(Front/Side/Rear/Top\)

Explosive reactive armor, late type, CE/KE \- Relikt \(06\+\), Turret, Aspect Coded \(F/S/R/T\)

In order to determine which value to use, select the type that best matches the performance of the listed types for the location \(hull or turret\) and aspect\. To complete an ERA code, add the Aspect Letters after the 1\-4 effectiveness value\. 

For example, if you have an “ERAH4” \(hull ERA with a performance like Relikt\) and it covers front and side only the full code will be “ERAH4FS”\. 

## HEAT Resistant Armour \(HRA\)

The HRA Characteristics are located in the Defensive Protection listing and are defined in the following table\. This code allows the game engine to augment the HEAT PF value of the armor for systems with enhanced HEAT protection versus a lighter kinetic protection \(hull or turret\) and aspect \(Front, Side, Rear, and Top\)\. This type of armor is mainly found on IFVs and APCs\.
!!! note

    You can assign more than one of these codes in the Defenses List of a unit if there is a variable level of coverage based on location and aspect\.


__Code__

__Unit Special Description__

__Notes__

HRAH1

HEAT Resistant Armor\-Hull, Type 1, Aspect \(F/S/R/T\) 

Reduced HEAT \- >3 and 6 and 9 and 12 and 15 ratio \(C/K\), Hull, Aspect Coded \(F/S/R/T\)

HRAT1

HEAT Resistant Armor\-Turret, Type 1, Aspect \(F/S/R/T\) 

Reduced HEAT \- >3 and 6 and 9 and 12 and 15 ratio \(C/K\), Turret, Aspect Coded \(F/S/R/T\)

To determine which value to use, a calculation of the ratio of the HEAT resistance to Kinetic resistance for the location and aspect needs to be done and then compared to the table to get the correct basic HRA code\. To complete an HRA code, add the Aspect Letters after the 1\-5 effectiveness value\. 

For example, if you have an “HRAT3” \(turret HRA with a ratio between 9\.0 and 12\.0\) and it covers front, side, and top, the full code will be “HRAT3FST”\. 

## Skirt Armour \(SKT\)

The SKT Characteristics are located in the Defensive Protection listing and are defined in the following table\. This code allows the game engine to augment the HEAT or Kinetic AP penetration value of an incoming round based on location \(hull or turret\) and considered to be Side and Rear only aspects\. 
!!! note

    __ You can assign more than one of these codes in the Defenses List of a unit if there is a variable level of coverage based on skirt type and location of coverage\.


__Code__

__Unit Special Description__

__Notes__

SKTHL

Armoured Skirt Hull sLats

used for slat style skirts that degrade AP and HEAT weapons

SKTHP

Armoured Skirt Hull Plate

used for plate style skirts that degrade AP and HEAT weapons

SKTHS

Armoured Skirt Hull Spaced

used for spaced plate style skirts that degrade AP and HEAT weapons

SKTHW

Armoured Skirt Hull Wire

used for wire style skirts that degrade AP and HEAT weapons

SKTTL

Armoured Skirt Turret sLats

used for slat style skirts that degrade AP and HEAT weapons

SKTTP

Armoured Skirt Turret Plate

used for plate style skirts that degrade AP and HEAT weapons

SKTTS

Armoured Skirt Turret Spaced

used for spaced plate style skirts that degrade AP and HEAT weapons

SKTTW

Armoured Skirt Turret Wire

used for wire style skirts that degrade AP and HEAT weapons

To determine which value to use, select the type of skirt that best represents the setup on the unit\. 

## Values for Side and Top/Rear

There are two internal global values used in the game\. For a side aspect shot the basic PF value is multiplied to 0\.46 and for the top and rear time 0\.21\. Both numbers are based on looking at many post WW2 tanks and these were the majority breakpoints for those aspects\.

