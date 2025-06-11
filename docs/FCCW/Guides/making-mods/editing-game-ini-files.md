# Editing Game INI Files

> **Note**: Images omitted — refer to original DOCX for figures.


The game has several INI files that store certain information used by the game to track options, setting, colors, line widths, and a host of other functions\. In some cases, changing these may be easier than doing them in\-game or may be helpful to change colors or transparency of overlays to colors the player finds easier to work with\. While these files are easy to open and edit in a text editor, as the following warning notes, you can break the game\. 
!!! note

    __ We will not be defining every value seen in the ini files in this document\. The entries are, for the most part, self\-explanatory\. We will note what each files covers and which ones not to mess with if you want your game to work right\.

!!! warning

    __Making incorrect entries or incorrect formats \(text instead of an integer, can cause the game to crash and be almost impossible to find\. If you are not comfortable editing ini files don’t mess with them\. If you are, make backups and use them if things crash\.

!!! warning

    __These files WILL get overridden by updates when there are changes or new values added to the game by the development team\. If you really want your changes, please make copies and note what information you have changed, so you can update the file\(s\) when needed\.


## List of INI Files

Here is a listing and explanation of what is found in each INI file\.

- flashpoint\.ini – This INI file covers the majority of the games options and player settings\. In some cases, changing settings may be faster here than in the games dialogs, but the dialogs are less risky as typing errors can crash the game\.
- Line\-of\-Fire\-Animations\.ini – This INI file holds the parameters used to render the various weapon firing effects\. This file might be worth making changes depending on how you like the look of the default firing animations\. Easy things to adjust here are line thickness and color or projectile size and colors\.
- log\_settings\.ini – This INI file is used to track the setting found in the radio log\. Highly recommended to not edit this file unless you really know what you are doing and want to make changes\.
- overlays\.ini – This INI file sets all the parameters for the various game overlays\. Several things you may wish to change in this file depending on taste\. Font, Text Color, colors of various overlays, and width of lines\. Most of the overlays can be adjusted in the game options, but some lesser used overlays are only accessible in this INI file\.
- unit\_counters\.ini – This INI file sets the colors for the default black or white unit silhouettes\. All color artwork is done automatically\. There is really nothing here to edit unless you plan to change the black and white defaults to some other colors\.
- PathFlavors\.ini – This INI file holds various path finding parameters used by the game to move units on the map\. While this particular INI file is well documented with comments, it is most likely to break the game if you give it a value the game does not like\. Make a backup in case things break or you may find yourself reinstalling the game\.
!!! warning

    __Just to say it again, be very careful making changes to this file\. Start small\. Test a lot\. Have a backup\.


## INI File Layout

The following sections cover the basic layout found in the INI files and any Notes or Warnings resulting from editing these files\.

### Section Headers

A Header is a word found in “\[\]” in the INI files and is used to note the function or use of the following entries\. These are keywords used in the code to pull data from the named items that follow\. 
!!! warning

    __You should not alter, edit, or delete these entries as the game can and will crash\. You may not add new Headers either, as there is no supporting code\. Basically, leave them alone\.


### Data Keys

After the Section Header there can be lines with Data Keys\. These Data Keys are of the formation of “Key Name” = “Value”\. The Key Name is a value set by the programmers and should not be altered as the game will be looking for the Key Name to function\. The “=” sign is also mandatory and should not be changed or altered\. What you can change is the Value parameter as long as you keep to the same type of class of value\. These values can be one of the following:

- String – This is some alphanumeric entry like “Roboto”, “ProjectileSpeedM”, or “Every Cat is Black at Night”\.
- Integer – This is a \+/\- value 0 to 65000 like “268” or “1000”\.
- Boolean – This is true or false entry with entries like “True” or “F”\. In some cases, this can also be a “0” for false and “1” for true\.
- Hexadecimal Color Code – This is in the format of “0x12345678” where 12 is the alpha channel value \(Transparency – ff = solid and 00 is clear\), 34 is the two digits for Red, 56 is the two digits for Green, and 78 is the two digits for Blue in the Line of Fire Animation and “\#123456” in Overlays with 12 for Red, 34 for Green, and 56 for Blue\. NOTE: Valid Hexadecimal digits are 0\-9 and A through F\.

### Comments

These are notes that help explain the values for uses for the various entries\. These must start with a “;” and space and then any info you want to add\. This is a great way to record changes you make and note the original value\. For example: *; Changed VaporLineWidth from 10 to 13 – 4Jan25\. *
!!! warning

    __Do not add comments after Values or Headers as these will cause the items to not be read and result in crashes\. Place Comments above or below the line you wish to comment on\.


