# Issuing Orders

> **Note**: Images omitted — refer to original DOCX for figures.


You control your forces by giving orders to your units\. Be aware that a certain period is needed by the staff to formulate and transmit your orders\. The unit will need time to prepare for the new order which is a function of the type of order, the training, readiness, and the tactical situation of the unit to which it is issued\. 

Orders take as long as they take to run to completion, and this may not coincide neatly with the Orders Phase intervals\. Orders persist to the next turn if you do not issue new ones\. If you keep interrupting orders with new orders, the delay time will increase as orders have to be rescinded and then new orders will be generated for the units\.

## Open the Unit Menu

Orders can be given to a unit by right\-clicking on the unit icon on the map and selecting an order from the displayed Unit Popup Menu\. Some orders require selecting to set them \(Screen, On Call, Hold, Resupply, etc\.\)\. Others require the player to designate waypoints or target points \(Moves, Assault, Barrage, Hunting, etc\.\)\. With these last orders, you must finish the order by selecting one of the options in the Orders on Arrival dialog that pops up when you are done selecting waypoints for the move\. 

If you decide during the issuing of a move or bombardment order that you want to do something else, you can click the Esc key to stop the order\. Accepting an order and then issuing a new order can also be done\. This case does not add additional time to the command delay as the order is not yet in process\.

In the image below, you can see the Orders Block of the Unit Popup Menu\. The listed orders may be in two sections of the dialog and show up based on the type of unit with Orders that are proper to use for the particular unit type\.

For more detailed information about plotting movement, see Section 22 below\.

> **Note**: Image omitted — refer to original DOCX for figures.



> **Note**: Image omitted — refer to original DOCX for figures.

You can also open the Unit Popup Menu by clicking on the hyperlinked Menu option beneath the unit counter in some reports and displays\. This is useful for Off\-Map Assets like artillery and air units\.

> **Note**: Image omitted — refer to original DOCX for figures.

> **Note**: Image omitted — refer to original DOCX for figures.

## Primary Unit Orders

- __Assault__ – Move in a spread\-out formation using both road and off\-road movement to be ready to attack an enemy\.
- __Move Deliberate__ – A more defensive move than Assault, but still can travel on or off\-road\.
- __Move Hasty__ – Faster than Assault and Deliberate moves, but trades speed for defensive coverage uses\. It sticks mainly to roads\.
- __Screen__ – A non\-moving state of seeking moderate cover and ready to attack or move if required\.
- __Hold__ – A non\-moving state of seeking the best cover in the hex and some cases, digging in for improved defensive protection if the unit is in the hex for 30 minutes\. This is the best choice for defending locations\.
- __Rest and Resupply__ – The unit is in a state of rearming, refueling, and resting to recover readiness and morale\. This only works if the unit is not in combat\. Aircraft and Helicopters will return to base to rearm and refuel\.

## Indirect Fire\-Specific Orders

- __Is Under FSCC \(Staff\) Control__ – This toggle allows you to have the Staff AI provide fire missions for the unit or place it under your direct control\. Not really an order but affects how orders are done for this unit\.
- __On Call__ – The unit is ready for new orders, either movement or barrage\.
- __Barrage__ – These are orders to fire certain types of munitions at a set of targets on the map\.
- Suppression Fire – Low rate of fire of high explosive \(HE\) rounds that has limited kill power but does inflict readiness loss to targeted units\.
- Neutralizing Fire \- High rate of fire of high explosive \(HE\) rounds maximizing kill power and inflicting readiness loss to targeted units\.
- Saturation Area Fire \- This option is found only on multiple rocket launchers\. It allows all the unit’s rockets to be fired off in rapid succession and strike a much larger target zone\. If this mission is chosen, you can only select one target point and the rounds will land in the target hex and the surrounding six hexes\. This is a devastating attack that can cause severe losses to man and machine\. Units firing a saturation attack automatically go to zero ammo and must resupply before shooting again\.
- Smoke – Fires rounds that deploy a smoke screen of various types that obscure vision and sensors\.
- Scatterable Mines \(FASCAM\) – This ammunition deploys a hex\-wide minefield in the targeted hexes\.
- Improved Conventional Munitions \(ICM\) – These rounds deploy several submunitions capable of destroying both armored and soft targets\.
- Nuclear Munition – These are single rounds with a tactical nuclear warhead that can cause massive area\-wide damage and nuclear contamination\.
- Chemical Munition – These rounds can drop persistent or non\-persistent chemical attacks into hexes\. Non\-persistent strikes will dissipate over time\.
- __Counter Battery__ – Your units are set to fire on located enemy artillery units\. While on Counter\-battery they will not shoot other missions\.

## Engineering Specific Orders

- __Remove \(Blow\) Bridge__ – Allows an engineer to blow a fixed bridge if they are in an adjacent hex\.
- __Lift Mines__ – Allows an engineer to clear lanes in a minefield for units to pass safely through\.
- __Remove Engineered Obstacle__ – This allows an engineer to remove obstacles to create lanes for units to pass through\.
- __Demolish Positions – __Allows the engineer to destroy improved position in a hex\.
- __Lay/Recover Bridge – __Allows a Short\-Span Bridging vehicle to place or retrieve a temporary bridge over a hex\-side water obstacle\.

## Helicopter Specific Orders

- __Hunt__ – This makes the helicopter move from point to point looking for enemy units to engage while doing its best to use terrain to mask its movement\.

## Aircraft Specific Orders

- __Is Under FSCC \(Staff\) Control__ – This toggle allows you to have the Staff AI provide fire missions for the unit or place it under your direct control\. Not really an order, but affects how orders are done for this unit\.
- __On Call__ – The unit is on station and waiting to be called back in for a strike\.
- __Air Strike__ – Order an aircraft to attack a given hex with its carried ordinance\. Depending on the type of aircraft and weapons, targets may be restricted to specific types\.

## Unit Orders Delay Factors 

Orders take time to transmit, absorb, and implement\. Some are fast and some will take time\. For many orders, there is a preparation time before the order can commence and then a period during which the order is executed\. If the unit is On Call or is already performing the same kind of order requested \(i\.e\., Move to Move, Screen to Screen, just with different parameters\) then the Orders Delay equals 2 minutes\. Otherwise, the Orders Delay equals the standard Orders Delay \(2 to 60 minutes, average 5 to 10 minutes\)\. 

Other delay factors include: 

- If the unit is being rested, then the order delay is increased by 10 minutes\. 
- If the unit needs to relinquish a dug posture, then the Orders Delay is increased by 5 minutes\. 
- If the unit is not currently moving and the new order requires movement, then the order delay is increased by 5 minutes\. 
- If the unit is under fire, then the order delay is increased by 50%\. 
- If the scenario electronic warfare intensity is Medium then the Orders Delay is increased by 20%, if EW intensity is High then it is increased by 33%\. 
- If the unit is ordered to Assault, then the order delay cannot be less than 30 minutes\. 

These are base delays and will vary based on the training level of the forces, the readiness of the forces, and command and control losses\.

## Involuntary Orders Changes

Not all units always follow orders under all circumstances\. Self\-preservation will take over long before the very last bullet is fired, or life is lost\. There may be an involuntary change of orders if the unit reaches a stress threshold limit\. This limit is calculated using the current morale, training, and readiness levels, losses, HQ proximity, and national factors for following orders and command flexibility\. If the limit is exceeded, attacks will stall, and defenses will turn into retreats\. Specifically: 

- Assaults, Moves, and Resupply orders become Screens 
- Screens, and Holds become Scoots for relative safety 
- Specialist units \(e\.g\., artillery, supply, etc\.\) revert to On Call or Scoot to safety
- Overwatch and Support units will stop advancing if their associated Main Effort and Line units are lost in battle\.
- Units in a group move will halt movement to keep spacing and formation by role \(recon front, main effort, and line, then overwatch, and support in the rear\)\.
!!! note

    __ Units doing an automatic Scoot will show an “F” for the order type when moving\. Units that trigger a Withdrawal via SOP settings, will show a “W” for their orders\. As a player, you cannot set these order types, they are reactions to whatever is going on in the game with the unit in question\.


## Issuing Group Orders

It is possible to give orders to more than one unit at a time by the following means:

- Shift \+ Left mouse clicking on each unit you wish to issue a standard order to\. These can be units from different groups and headquarters\.
- Select All Subordinate units in a formation by selecting their HQ with Alt \+ Left mouse click\.

This will highlight all subordinate units in that group\.

> **Note**: Image omitted — refer to original DOCX for figures.



To issue any orders to the selected group, right\-click on any of the highlighted units to see the Unit Popup Menu and select an order\. If you select a movement order, the AI will provide intelligent pathing to keep the units in a cohesive formation and then spread them out at the final waypoint in defensive locations \(if possible\) to avoid stacking\. You can select each unit and alter the placement of the waypoints as you see fit\.
!!! note

    __ Select the most used order for all waypoints that you want and then use each unit’s Dashboard to change the type of movement order at various waypoints\. See Section 22\.1\.1 below


See more information in Section 22 below\.

