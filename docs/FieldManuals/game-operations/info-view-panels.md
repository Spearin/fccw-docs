# Info View Panels

> **Note**: Images omitted — refer to original DOCX for figures.


There are five additional information panels that you will use during the game for various functions\. There are the Unit Popup Menu, Unit Dashboard, Sub\-Unit Inspector, Command Log, and Off\-Map Assets\. The following sections will detail them all\.

## The Unit Popup Menu

The Unit Popup Menu is the primary means of interfacing with the selected unit or units\. Right\-clicking on a unit will bring up the menu\. You can also select multiple units and then right\-click one of the units to bring up the menu\. Any orders given to one selected unit will also apply to any other selected units\.

### General Menu Layout

> **Note**: Image omitted — refer to original DOCX for figures.



1. The first section provides a means to open the Unit Dashboard \(See Section 14\.2 below\) or open the Subunit Inspector \(See Section 14\.3 below\) for the unit right clicked on\.
2. The second section of the menu has SOP\-related commands\. Set and Adjust SOP are covered in Section 11\.5 above\. The SOP Manager is covered in Section 23 below\.
3. The third section of the menu shows all of the available orders for the selected unit\. The selections will change based on the unit’s capabilities\. See Section 21 below for details of the orders\.
4. The fourth section of the menu contains functions related to unit Commands, Roles, and Overlays\. 
    - __Flash HQ Location__ – Flash the hex location of the unit’s immediate HQ unit\.
    - __Select Unit and Subordinates as Current Group __– This is a shortcut to select a formation of units based on a single selected unit\.
    - __Detach and Make Unit Independent__ – Removes the selected unit from the formation and HQ it is under and places it as its force\. For most subunits, it is better and safer to use the Order of Battle Tree to do subordinations see Section 20 below\.
    - __Unit Role__: \- Displays the unit’s current role in the battle\. Can be changed via the arrow and sub\-menu that pops up\. See Section 18 below\.
    - __Show __– Clicking the arrow with bring up a sub\-menu with the Unit Overlay options\. See Section 11\.6 above for details on the various overlays\.
## Unit Dashboard

The Unit Dashboard is the central interface for dealing with many important factors of the selected unit\. Double\-clicking a unit on the map will bring up the Dashboard\. Having a unit selected and hitting F6 will also bring up the Dashboard\. From the Unit Popup Menu, you can open the Dashboard via the menu item selection there\.

### General Layout

> **Note**: Image omitted — refer to original DOCX for figures.



1. The top bar shows the name of the selected unit\.
2. You can click the Lock to freeze the panel on the selected unit\. The Expand/Collapse icon will collapse the tabbed section of the dialog to save space\.
3. This area shows the counter of the currently selected unit\. Below the counter is an indication of the current tactical posture of the unit\. 
4. This area of text relays the current SitRep \(Situation Report\) of the unit\. This is the composition of the unit, the hex the unit is in \(hyperlinked can click to go there on the map\), the unit’s commander rank and name, the experience level of the unit, and the unit’s role\. Finally, an indication of the unit is under fire and the number of spotted enemy units\. In cases of critical alerts, like low ammo, a line will show up in this area noting the problem\.
5. The information in this area covers the unit’s Critical Ammo level \(primary weapons\), Readiness, Morale, Range to HQ \(local HQ for the unit\), and any Orders Delay\. The percentages from 100% high to 0% low and have status icons to the right\. These icons are a green circle for good condition, a yellow upward triangle for marginal condition, a red downward triangle for critical condition, and finally, a black square for a combat ineffective condition\.
6. The tabbed area covers the unit’s Orders, Subunits, Staff, and Unit Log information, as detailed in the following sections\. 
> **Note**: Image omitted — refer to original DOCX for figures.



### Orders Tab

> **Note**: Image omitted — refer to original DOCX for figures.



1. This window lists the unit’s orders noting the type of order, the hex location of the order, and the estimated start time of the order execution\. As seen below, you can click to select any of the orders and then right\-click to bring up a popup menu to change the selected order\. The selection is context\-sensitive based on the initial order\.
> **Note**: Image omitted — refer to original DOCX for figures.

> **Note**: Image omitted — refer to original DOCX for figures.

1. If you change an order\(s\), you can then hit Apply to make the changes or cancel to ignore changes\.
2. This is a text summary of the currently selected order with time and distance information\.
3. This option, when shown, allows you to add additional delay time BEFORE an order starts\. This is useful if you are trying to synchronize units to get to locations at the same time\.
4. This window provided a summary of the unit’s current SOP \(Standard Operating Procedures\) for the highlighted order\.
5. Click this button to edit the current unit’s SOP\. See Section 23 below for details on how to set the SOP items\.
### Subunits Tab

> **Note**: Image omitted — refer to original DOCX for figures.



1. In this window, you will see all the subunits within the selected unit on the map\. If there are more units than can be seen in the dialog, a scroll bar will be shown to allow you to see all the items\. You can click on any of the subunits in the first window to display information about that subunit in the second window\. If units have fallen out or have been destroyed or died, icons will appear over the subunit art, and the information in the second window will note that state\.
2. This window shows a breakdown of the subunit's Weapons and current Ammunition levels, Emitters \(radars\) if they have them, or EW detectors \(ESM or Radar detectors\)\. The hyperlink at the top will open the Subunit Inspector \(SUI\) to see more details about the subunit\.
3. You can move the splitter bar left or right to resize the windows\.
4. You can resize the dialog by dragging the corner point\. The dialog has a minimum size set by the game\.
### Staff Tab

> **Note**: Image omitted — refer to original DOCX for figures.



The Staff tab of the Dashboard provides many valuable bits of information about the selected unit\. 

1. Under Staff Alerts and Reminders, you will get information on weapons that are out of ammo, what artillery units can support this unit \(if available\), unique unit capabilities and any claims of enemy units destroyed\.
2. Under Ammo Summary, shows the total ammo inventory for the unit in the Staff page of the Unit Dashboard to save clicking around to look it up manually\.
3. Under Active Contacts, a list of detected enemy units is shown\. Contact number, type of detection \(visual, thermal, radar, etc\.\), number and type of units \(if known\), range of the contact, and a hyperlinked Hex location\.
### Log Tab

> **Note**: Image omitted — refer to original DOCX for figures.



The Log tab lists messages that are recorded to the various unit logs, related to the actions of the selected unit\. Both the game Time and Tag \(type of message\) are listed with the Message\. On the face of it, Radio Logs/Unit Logs don’t look like much has changed\. On closer inspection, you will see that all messages are not Tagged \(instead of just some of them as before, unit names are highlights, and locations are given subtle highlights \(just bold, no color\)\.

Unit names you can now click on to take you to that unit if it’s not in the frame\. You can also click on a location to go to that location on the map\.

In the top right corner, there is a search field that filters the display down to just messages involving the desired text \(searching for a particular unit or vehicle type\)\. Search is case\-sensitive\.

The message Tag can be of the following types:

- __sitrep__ – This is a breakdown of the current active subunits in the unit, hex location, unit readiness, unit morale, and average ammo level, and the number of spotted enemy units\.
- __orders __– If the unit gets a new order or a change in orders, the new order is listed here with start and end times and hexes if available\.
- __loss __– If the unit loses any subunits, they are listed here and the hex they were lost in\.
- __spot __– This message notes that your unit has spotted an enemy unit, a temporary enemy bridge, a VP location, and other spottable items\.
- __claim __– If your unit kills or believes it has killed enemy subunits, they will be listed in this entry with the number, type, and hex of the kills\.
- __\(empty\) __– These entries are mainly updates on a unit moving to a new hex and the detail of the cover, concealment, and mobility of the hex moved into\.

Another obvious change is the little filter icon next to Tags\. Also, you can right click on it, or anywhere on the log, will cause a pop\-up filtering menu as shown below\.

> **Note**: Image omitted — refer to original DOCX for figures.



For convenience, the Tags column can be set to show only the dominant primary tag for a log entry, or to show all the tags that are in the entry\.

We can now easily filter the logs by Tag type\. If you want to see just the message that involves just bullets firing, Select “Shots Only”\. 

To see different set of things you want to be visible, then select Custom Filter Settings, a popup menu will have very large list of Tags\. Uncheck the Tag types that you don’t want to see, and then once done set your filter to “Custom Filter”\.

To set up different colors to make your tags stand out using different colors\. Select the “Highlight Settings” and a popup menu with a very large list of Tags\. For example, let’s say I want to see messages with the Tag “Mines”, select “Mines” from the list and you then can set the color for that Tag\.
!!! note

    __ Be Caution for you to not overdo it, it may be too hard to read the text\.


## Sub\-Unit Inspector \(SUI\)

The Sub\-Unit Inspector is the primary tool for deep diving into all the information on a given sub\-unit in the game\. The following sections will detail all the various tabs and the information displayed\. You can open this dialog with the F6 key for any selected unit\.

### General Layout

1. You can click the lock to freeze this dialog or click the “X” to close\.
2. Sub\-unit name and then the type of sub\-unit in parenthesis\.
3. Unit Code of the sub\-unit from the data file\.
4. Sub\-unit silhouette or image if available via mod\.
5. National Flag or Emblem\.
6. This listing notes the number of the selected sub\-units that are Active, Fallen Out, or Destroyed in the current scenario\.
7. The date unit is active in the game\.
8. This is a five\-tabbed panel that covers the Platform, Weapons, Sensors, Systems, and Transport that the selected sub\-unit has\. These tabs are detailed in the following sections\.
9. If there is more than one type of sub\-unit available based on the Scope chosen, you can use the controls here to page through them\.
10. You can use the drop\-down selections here to look at other national data files \(Source\) in the scenario and change the Scope from Selected Unit, Units in the Scenario, or all units in the data file\.
11. You can use this icon to drag the SUI larger or smaller\.
> **Note**: Image omitted — refer to original DOCX for figures.



### Platform Tab

The Platform tab provides information related to the general capabilities of a given sub\-unit\. Here you will find the values for Victory Point cost, Crew size, Use date, and Size rating\. 

Then the Mobility Type and Maximum Speed\.

Protection Ratings \(Armor\) for the Front, Flank \(side\), and Top/Rear of the sub\-unit or a static Protection Factor for aircraft and helicopters are shown in this section\.

Next, under Particulars is a listing of platform\-specific characteristics/traits that it has that can impact gameplay, if available\.

> **Note**: Image omitted — refer to original DOCX for figures.



### Weapons Tab

Every weapon system on a platform/sub\-unit is listed on this tab with its various performance parameters and any unique characteristics that the systems possess\.

Shown are the Weapon Name and Type\. Then the number of rounds or bursts of ammo carried typically \(those values can be different in scenarios based on supply and munitions loadouts\)\. The damage rating for the weapon or munition is shown with its type\. Lastly, the maximum range in meters is listed\. If the weapon system has any unique characteristics used in the game, those are listed after the munition specifications\.

> **Note**: Image omitted — refer to original DOCX for figures.



Basic Ammo comes in various types as noted below:

- __Armor Piercing \(AP\)__ – These are solid, long\-rod projectiles used to defeat armor\.
- __High Explosive Anti\-Tank \(HEAT\) __– This round uses an explosive charge to create a plasma jet that cuts through armor\.
- __High Explosive \(HE\) – __These rounds use a blast fragmentation warhead and affect an area\. 
- __Area \-__ This type of damage reflects weapons that impact an area and are used against soft targets that cover an amount of ground\.

### Sensors Tab

The Sensors tab shows all the equipment on a platform that is used to detect, spot, or range enemy units on the map\.  If a system has detection capability, it will list the ranges \(under optimal conditions\) that it can Detect an enemy unit, Classify the type of enemy unit, and identify the sub\-units of an enemy unit\. Other Sensor systems have an impact on combat calculations\.

> **Note**: Image omitted — refer to original DOCX for figures.



### Systems Tab

Any other systems that provide a unique capability not already covered in the other tabs will be noted here\.

> **Note**: Image omitted — refer to original DOCX for figures.



### Transport Tab

> **Note**: Image omitted — refer to original DOCX for figures.



The Transport tab shows all the transport capability on a platform that is used to provide a unique capability not already covered in the other tabs will be noted here\.

### Further Information on Capabilities

To get more details on these various Capabilities, you can check out the information in FM02: Battlefield Primer and in deeper detail in FM09: Data Structures and Editing\.

 

## Command/Unit Log

The Command/Unit Log is a dialog that shows all the latest Log messages for all units in your force\. It will list the last 50 entries\. You can dig deeper by looking at the Unit Log in the Dashboard for each unit\. This dialog can be opened and closed on the screen with the F7 key\. The dialog does allow for expanding and collapsing via the arrow’s icon in the upper right of the dialog\.

A complete listing of log entries can be found in the Operations Report on the Log tab\.

> **Note**: Image omitted — refer to original DOCX for figures.



As the game unfolds, a series of messages are recorded to the unit logs with a time stamp, a “tag” or type of log entry, and then the text of the entry\. 

### Log Capabilities

- All messages are now Tagged \(instead of just some of them as before\) 
- Tags are now filterable \(see below\)
- Unit names are highlighted to make them easier to find and hotlink to the Dashboard
- Locations are given a subtle highlight \(just bold, no color\) and are hot linked to flash on the map
- The log is searchable – see the top right corner
- Highlight colors may be specified by tag type so that specific tags can be emphasized or de\-emphasized \(see below\)

> **Note**: Image omitted — refer to original DOCX for figures.

> **Note**: Image omitted — refer to original DOCX for figures.

There is a new filter icon \(a yellow funnel icon\) next to the “Tags” column header\. Right\-click on it, or anywhere else on the log, to pop up the filtering menu\.

For convenience, the Tags column can be set to show only the dominant primary tag for a log entry, or to show all tags\.

__Filtering__\. The log can be filtered by Tag types\. To see just the messages that involve bullets flying, use the “Shots Only” combat filter\. For further customization, use the “Custom Filter Settings” popout to uncheck the Tag types you don't want to see, and then set the filter to “Custom Filter\.” You will not see messages you don't care about\.

__Highlight Settings__\. The highlight settings are a way to make the tags you want to stand out using different colors\. Use with care\! It's all too easy to set everything to have a highlight color and become dazzled by the beautiful but unreadable Christmas tree\-like effect that results\. 

This new system is used everywhere we show the unit logs – this log, the unit dashboard, the counter\-battery screen, and the TOC Ops Unit Logs report\. 

If this dialog has the Windows focus, then it can be closed by tapping the Escape key\.  


## Off\-Map Assets

The Off\-Map Assets dialog provides you with a listing of any of your forces that exist off\-map for the scenario\. This is currently an aircraft or artillery asset in a scenario that you can order to support your on\-map forces\. As you can see in the dialog below, this shows the headquarters and an artillery battery located 2km off the West edge of the game map\. 

1. Name of the overall force being supported by the off\-map assets\.
2. Name the smaller off\-map asset formations available to use\.
3. The counter of each supporting off\-map unit, name, type, size, training level, and off\-map location of the unit
4. Menu hyperlink that will open the Unit Popup Menu so you can issue orders to these off\-map assets\.
5. This text block tells for each unit what its Current Orders are, Readiness, Morale, Ammo levels, and current Delay for orders to process\.
6. This second text block shows the unit’s composition by platform and type and then a breakdown of the ammo carried by the unit\.
> **Note**: Image omitted — refer to original DOCX for figures.



