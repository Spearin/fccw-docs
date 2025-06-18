# Plotting Movement and Fires

> **Note**: Images omitted — refer to original DOCX for figures.


One of the primary functions of a Commander is to direct your forces across the map to take or hold objectives\. You will need to know how to order your forces and how to utilize artillery assets and airpower to achieve your mission goals and preserve your forces the best you can\. The following information will show you how to move your units, issue orders, adjust and change movement types along the path, and issue artillery and air strikes on target locations\.

## Movement

To order a unit or group of units \(See Section 21\.9 above\) Right click on them to bring up the Unit Popup Menu\. From there select a movement order\. In this case, a Deliberate Move\. Next, select up to six waypoints to path the unit to the location you want it to end up in\.

The AI is smart and will intelligently path the units based on the terrain and your SOP selections \(See Section 23 below\)\. Once you have selected the path you can click on the Commit button in the Plotting Mode dialog that popped up when you started placing waypoints\. If you wish to stop and cancel the order, you can click the Cancel button\. 

> **Note**: Image omitted — refer to original DOCX for figures.



> **Note**: Image omitted — refer to original DOCX for figures.



After pushing the Commit button, an Orders on Arrival dialog will pop up and you can set the final order state of the unit\. The options for this box vary to match the type of unit and any special orders it has access to\.

> **Note**: Image omitted — refer to original DOCX for figures.



In this case, we will select a Screen order\. Now the final path is shown for the unit\.

> **Note**: Image omitted — refer to original DOCX for figures.



At this point, if you need to adjust the path, you can click and drag the Waypoint Marker to a new hex location\. In this example, we will move Waypoint \#2 to the south to the road junction\. To make this a better move we also need to move Waypoint \#1 one hex to the south to make the path choose the road heading south\-east\.

> **Note**: Image omitted — refer to original DOCX for figures.



At this point, you also have the option to Right\-click on any waypoint and pop up a Waypoint Editor menu\.

> **Note**: Image omitted — refer to original DOCX for figures.



Selecting the Edit Waypoint menu option will open the Unit’s Dashboard on the Orders tab to allow you to make several changes to the order as detailed in the following sections\. You can remove the waypoint by selecting the Delete Waypoint menu option\. This will also delete any SOP setting for that waypoint\. At the bottom is an estimated arrival time of the unit to that waypoint and the type of move to that waypoint\.

Hovering over a Waypoint with the mouse will bring up a hint showing the Unit Name, Waypoint Number and Movement Order, and the start and arrival time of the unit to that waypoint\.

> **Note**: Image omitted — refer to original DOCX for figures.



### Chaining Different Movement Orders

After plotting a set of waypoint movements, you have the option to go into the Dashboard for any unit \(must be done per unit even if a formation or group move is issued\) and change the standing order\. Below is the initial plotted set of move orders for our unit\.

> **Note**: Image omitted — refer to original DOCX for figures.



To view and change an order, select the waypoint order you want to change and right\-click on it to bring up a menu of optional orders\. In this case, let’s select a Move Hasty order so the unit moves the first part of this move quickly\. 

> **Note**: Image omitted — refer to original DOCX for figures.



After changing the order, the waypoint order shown changes, the arrival times change for all waypoints as the first time is shorter, and the counter changes from a Deliberate Move marker \(blue triangle\) to a Hasty Move marker \(Black Triangle\)\.

> **Note**: Image omitted — refer to original DOCX for figures.



For some attacks, you may want to have the opening waypoints that are in friendly territory to be hasty and then move to Deliberate Moves when enemy contact is possible and then shift to Assault if you are taking a contested objective\. You can also change the terminal \(final\) order at this point as well\. 

### Altering Waypoint Timing

In some cases, you as the commander may want several units to arrive in an area at the same time or close to it as events can alter that timing\. To change the final time of arrival in the last waypoint, you have the option to set a delay time for each selected order in the Dashboard\.  As you alter the times with a delay you can set your point of timing\. From there you can alter other units to have the exact arrival time by adjusting arrival at your scheduled time\.

> **Note**: Image omitted — refer to original DOCX for figures.



In the case above adding 7 minutes of delay to the start of the first order shifts the time to start the Screen in the destination from 06:33 to 06:40\.

### Lost Transport Indicator

Another quality\-of\-life addition to the unit counter is the Lost Transport Indicator\. When a unit \(mechanized or motorized – vehicles and squads/teams\) can no longer move its troops due to losses of the transport subunits, the Leg movement indicator \(L\) turns orange to note this condition\. This helps to show the difference between a dismounted unit that shows the “L” indicator when troops are out of the transports in a non\-movement order\. 

> **Note**: Image omitted — refer to original DOCX for figures.



## Fires

The other aspect of plotting orders is setting up fire missions\. This covers both on and off\-map indirect fire units like mortars, guns, and rockets if any of these assets are available in the scenario\.

To issue a bombardment order, open the Unit Popup Menu by either right\-clicking on an on\-map artillery unit or opening the Fire Support report and clicking on the Menu hyperlink\. Once open, click on the Bombardment option in the menu to open the mission menu with the attack options\. 

> **Note**: Image omitted — refer to original DOCX for figures.



__NOTE__: The choices of mission types are based on the ammunition allocated to the firing unit by the scenario designer\.

Once you have selected the type of fire mission, the Plotting Mode dialog will pop up and tell you that you can place up to six Target Reference Points \(TRPs\) on the map and within range of the unit \(inside its indicated Maximum Range \(shown on the map\) and beyond any Minimum Range indicated for the unit\. These locations are where the munitions will drop\. 

The only other possible coverage of a strike is with rockets that can do a Saturation Strike that is centered on the selected hex but also hits the ring of hexes around the TRP\.

> **Note**: Image omitted — refer to original DOCX for figures.



After hitting the Commit button, the hexes being attacked will be highlighted and fire lines from the firing battery will be shown on the map\. The Dashboard will also pop up automatically \(you can turn this off in the game options\) so you can set various parameters of the fire missions and even change the type of fire mission\.

> **Note**: Image omitted — refer to original DOCX for figures.



On the Orders Panel for a Fire Mission, you have the following options to adjust or change for the selected TRP:

- __Mission Preset__ – This dropdown allows you to change the type of bombardment mission from the type set initially with the setting of the TRPs\. If the mission is changed from the original via the Ammunition dropdown, then the Preset will be called Custom\.
- __Ammunition__ – There is the option here to select different types of ammunition\. This is helpful in cases like HE rounds where a few different types may be available\. 
- __Rounds__ – You can set the number of rounds to shoot on the mission\. The total number of available is noted after the slash \(/\)\. You cannot shoot more rounds than you have\.
- __Start Time__ – You can set the time to ASAP which will fire as soon as the delay of the order is done \(for opening salvos during the first turn set up, planned missions will start to fall immediately\)\. There is the option to delay the mission several minutes if timing is vital to your plan\.
- __Duration__ – This sets how long the mission will last and sets the number of rounds per minute that get fired\. In the example below that would be 2 rounds per gun in the unit per minute over 10 minutes\. With eight tubes in this unit that is 16 rounds impacting every minute\.
- __Area Fire__ – If the artillery unit is a rocket launcher, The Area Fire option will be active and if checked, will fire a saturation strike \(target hex and the surrounding ring of six hexes\)\. This strike fires all rockets on the launching platforms\.

> **Note**: Image omitted — refer to original DOCX for figures.



## Calling in Airstrikes

To call in an Airstrike, you need to have available aircraft in the scenario\. There are two ways to check and then call in an airstrike\. The first option is to open the Fire Support Report and look at the Fire Support Assets tab\. In this case, Section B shows available Close Air Support \(CAS\) that you can call in\. The second way is to open the Off Map Asset \(OMA\) dialog and look for what aircraft you have\. 

Aircraft may not be available until they arrive as a reinforcement to provide support and that will be noted in the dialogs\. Most aircraft will also have a hard withdrawal time when they return to base and can no longer be used\. Weather and time of day can also impact air operations\. Some aircraft are not capable of night or all\-weather operations over the battlefield\. Aircraft have one other threat that you as the commander need to consider and that is the current Air Superiority level over the battlefield\. If control of the air is owned by your side, your air strike has a much better chance of getting to the target and delivering ordnance on targets\. If the airspace is contested or owned by the enemy, your air strikes run the risk of being run off or worse, shot down\.

> **Note**: Image omitted — refer to original DOCX for figures.



> **Note**: Image omitted — refer to original DOCX for figures.



Selecting the hyperlinked Menu option will bring up the Unit Popup Menu and you need to go down to the Strike section that looks as seen below and select the Airstrike option\. 

If you want to order in\-air units instead of the FSCC doing it when targets of value show up, you should click the Is Under FSCC \(Staff\) Control and turn the checkmark off\. Selecting On Call will cancel any strikes and return the aircraft to its on\-station location where it awaits a call to strike\.

There is also the option on the menu \(not shown\) to Rest and Resupply, this will return the aircraft to the base to rearm and refuel and then return on\-station for future use\.

> **Note**: Image omitted — refer to original DOCX for figures.



After selecting an Airstrike, the Plotting Mode dialog pops up and you can select a single hex to be the target of the airstrike\.

> **Note**: Image omitted — refer to original DOCX for figures.



Select a target hex and click the Commit button to issue the order\. Pressing Cancel will stop the order and return you to the game with the aircraft On Call\.

Once the aircraft is ready to attack it will appear on the map near the target location and will attack the best target it sees in the area\. The discretionary radius of target selection is set in the Nation Data and cannot be altered\.

