# Combat Operations

> **Note**: Images omitted — refer to original DOCX for figures.


Combat is the very focus of this game\. Because of that, it is very detailed and may be confusing at first\. In this section, everything that has to do with combat is explained\. The different unit and ammunition types that are included in the game will make sure that a lot of different types of combat will occur during a scenario or a campaign\. Even chemical \(persistent and non\-persistent\) and nuclear weapons might be used\.

## Unit Postures

During a battle, units will go through various changes in Posture\. This is a measure of how visible and how protected a unit is based on its movement state and the local terrain\. Posture states are listed below:

- __Very Exposed:__ Unit moving/sitting in terrain with no real cover or concealment regardless of order\. Very easy to spot\. No additional protection from the terrain against any form of enemy fire\.
- __Exposed: __Unit moving/sitting in terrain with minimal cover or concealment based on order\. Moving units are easier to spot\. No additional protection from the terrain against any form of enemy fire\.
- __Covered: __Unit moving/sitting in terrain with useful cover or concealment\. Spotting dependent on movement and terrain levels and thermal/radar signature is mildly degraded\.

Depending on the terrain, protection from direct fire is a function of the cover afforded by the terrain\. 

- __Dug In __Unit sitting in terrain with a Hold order will spend 20\-30 minutes digging into the covered terrain or units in an Improved Position location\. Unit is difficult to spot and thermal/radar signature is reduced a moderate amount based on the cover of the terrain\. Extra protection from the terrain against any direct enemy fire\. Not effective at artillery or air strike damage\.
- __Fortified: __Unit sitting in a fortification with extreme cover and concealment\. Very difficult to spot and radar and thermal signatures are greatly reduced\. Extra protection from the fortification provides more reduction against any form of enemy fire\.

## Unit Facing

There is no control over the unit facing in the game\. It is assumed that the units are smart enough to show a frontal aspect if the enemy is detected\. If caught by surprise, a target unit at range may have some subunits get hit in the flank as they are not in a defensible position\. At a range of one hex, there is an increased chance of getting a flank attack on a target unit as some of the subunits are assumed to be close enough and, in a position, where flank shots are possible\. If both the attacker and defender are in hex, attacks have a better chance to be flank or rear aspect shots as cover and spacing allow for more advantageous engagements\. Infantry attacking armored fighting vehicles \(AFVs\) in built\-up terrain \(cities and forests\) have a bonus to these better aspect shots\.

## Direct Fires

All combat occurs during the turn resolution phase\. Spotting is checked for all units and then each unit with Assault, Hold, Screen, Move\-Deliberate, Move\-Hasty, or Direct Support orders looks for suitable targets among the enemy units that it can sight directly or indirectly in some cases\. A combat event for each pairing of attacker and defender is created and entered in the main game event queue\. 

The combat event is resolved between the two units at the subunit level\. The attacking unit calculates the quality and quantity of fire that it can effectively protect against the defender given the number of subunits that it has, the armaments that they mount and their effectiveness versus the target subunit, the range to the target, armaments base accuracy, attacker orders, crew quality, suppression from incoming fire, multiple targets, and special bonuses such as advanced gun sights\. 

This effective projection of fire is applied to the defending unit which will take losses about the quantity and intrinsic protection rating of its runners, defender orders, posture, usable terrain bonus, movement, stealth, range, and special bonuses such as armor \(Chobham, advanced composite, laminated, or reactive\)\. The defender is also penalized if he has not sighted the attacker \- surprise is assumed for the first few shots \- and if the range is one or less then there is a further penalty due to the assumption that more flanking shots are available when at such close range\. 

The attacker uses up munitions by the round or burst used to engage the enemy and is marked as “firing”\. This “firing” status makes it easier for other units to spot it during the turn\. Attacking also reduces a unit’s readiness by a small amount as the crew deals with the rigors of loading and firing weapons or scanning for targets\. Units occasionally gain a boost to morale if they achieve kills without taking losses\. 

Defending units can take losses because of combat\. These losses are tracked to individual subunits\. Readiness and morale will both be degraded in these cases\. Morale can take a bigger hit if the HQ is out of range or if a friendly unit within 1000 meters is wiped out\.

Units are not mindless zombies that die to the last subunit\. If losses in the unit are too great and readiness and morale are low, a unit will spontaneously give up its mission orders and try to retreat to a safer location by scooting\.

## Indirect Fires \(IDF\)

Where direct fires have the shooter seeing the target, indirect fires rely on another unit to spot a target and provide targeting information for the indirect fire units to use to shoot with\. The advantage of indirect fire is its much longer ranges and less exposure to direct combat\.

Indirect fires are guns, rockets, and mortars that fire munitions \(or are munitions in the case of rockets\) over the battlefield\.

These systems show up on the map as various explosion animations in the target hex based on the type of munitions used\. In our earlier games, artillery fired in a piecemeal fashion with several rounds being resolved each turn they attacked\. Now, each gun fires rounds, and the attack lasts over a duration as shells are fired until the mission is over\. This means enemy units can move into and out of the hex\(es\) being attacked\. In some cases, the fire will be adjusted to follow targets if they are under direct observation and there are timely communications with the observer and shooter\.

Artillery fire missions can be of a few types as noted below:

__Direct Fire__ – Some field gun\-equipped artillery platforms can point themselves at an enemy and fire directly\. The wisdom of this is highly debatable but it can be done\. Interestingly, Soviet tactics put great store in this technique and 122mm and 152mm SP howitzer assets can be attached to their assault formations to use direct fire against targets\. While it is certainly much quicker than trying to organize on\-call fire the cost to the lightly protected artillery would be horrendous\. They used this technique extensively in the second half of WW2 with the SU\-76 \(76mm guns mounted in light tank chassis\) and the 2S1 and 2S3 vehicles are the Cold War inheritors of that tradition\. All other force structures might want to consider this a measure of last resort\.

__Pre\-Plotted Fires__ – These fire missions represent pre\-registered targets for the artillery units to shoot at the start of a battle\. For the AI player, the artillery barrages need to be set up in the Scenario Editor to start right at the start of the battle\. For the player, this kind of strike needs to be plotted in the Setup Phase before the start of the battle and will start falling right when the first turn is executed\. 

__Direct Support__ – These are artillery assets that are dedicated to supporting a selected unit or set of units\. These assets will not take on fire support requests from other units or provide counter\-battery fires and are ready to perform fire missions only for the enemy units spotted by the units placed in direct support\. These missions usually have slightly shorter command delays than the General Support operations\.

__General Support__ – These are artillery assets that will take requests for fire from any friendly unit on the map and process them based on target type, urgency, and availability via the FSCC\. Standard command delays exist for this type of support\.

__Counter Battery__ – These assets are set to fire on located enemy artillery units that are in the range of the counter\-battery unit\. This includes both on and off\-map assets and targets\.

### Fire Support Control Center \(FSCC\)

Fire support mission requests are made either through player intervention during the orders phase or automatically through their staff FSCC \(AI\) during the turn resolution phase\. Line units will automatically generate fire support requests during the turn resolution based on their sighting activities as the turn unfolds\. Fire support requests are also generated by the staff when ordered to prepare a fire support plan as part of the AI planning cycle\. 

Fire support requests are rated for target type, priority, and weight of fire, type of munition needed, and are queued in descending order of importance \(priority multiplied by weight of fire requested\)\. Fire support requests are discarded if the target is lost or too much time passes between the initial call and the unit being able to shoot\. This is done so as not to waste ammunition shelling the empty ground\. 

During turn resolution, the FSCC is called to match fire support requests to available air and artillery assets\. To be “available” an artillery unit must have an On Call, Direct Support, or Counter Battery order and otherwise be ready to fire \(i\.e\., not wiped out, not moving, not already assigned an FSCC mission, etc\.\) or be an On\-Call aircraft\. 

Other missions are served first by eligible artillery units with Direct Support orders, then by General Support units, and finally by units with counter\-battery orders if they are available\.

Available air and artillery units are assigned to the mission until the requested weight of fire has been accumulated\. The necessary combat events are created in the game event queue and the selected units will fire\. The fire support request is marked as done and the rest of the list is processed until the supply of available artillery units is exhausted\. 

Artillery units that have manually been assigned a Barrage mission will fire as ordered and revert to On Call when done shooting all missions\. At that time, they will be available to service FSCC or player requests\. If an artillery unit runs low or out of ammunition, it will go on a resupply order to replenish its stocks\. Depending on SOP settings, artillery units will scoot after shooting to avoid potential enemy counterbattery fire\.

### Observed Versus Blind Fire

When shooting with indirect fire assets, they can fire on known observed targets or on locations where targets were detected by electronic means or lost visual contacts where there is no observer to the fire\. Observed fires will have a better chance to hit and the ability to shift hexes if the target moves into a new hex\. Blind fires will be much less effective for the same volume of fire when there is no one to adjust the fire to the targets\.

## Air Defense \(AD\)

There are both dedicated anti\-air units and some units with weapons capable of engaging air targets in the game\. These platforms are defined as follows:

__Surface\-to\-Air Missile Units \(SAMs\) __– These units use surface\-to\-air missiles with radar, IR, or optical guidance to track and engage enemy aircraft and helicopters\. These units have a limited number of missiles and usually have air search radar or advanced optical systems to find targets\.

__Flak Units \(AAA\)__ – These units rely on cannons or machine guns to engage air targets with a wall of lead or proximity fuse explosives\. Ammunition for these units is tracked in bursts of fire\. These units can have air search radars and other optical means to find and track targets\.

__Air Defense Limited \(ADL\) Units__ – Some units have machine guns, auto\-cannons, or in some cases Anti\-Tank Guided Missiles \(ATGMs\) that can be used to engage air targets in a limited capacity\. For these units to shoot at an air target they must be the target of an air strike engage a hover helicopter or engage a helicopter approaching them in a roughly 30\-degree cone \(these weapons cannot effectively track a moving crossing target\)\.

Some platforms may have a mix of these systems to use\.

## Air Strikes

When an airstrike is called in the air strike controller will automatically select the best value target location for the air strike within the discretionary radius allowed \(they will default to the stated target if other targets only tie it for value\)\. The target value is based on the number of visible targets and less apparent air defense strength\. If the target location is empty of targets when the air strike arrives, the attack is aborted, and the aircraft returns to its on\-call station\. 

An airstrike attack starts with the sound effect of the approaching jet\(s\) and the following sequence of events happens: 

- The target location will flash, and the attacking aircraft will appear over the target unit\. 
- All eligible defending units \(Air Defense \(AD\) units and units with air defense capable weapons\) located within range of the target location will attempt to detect the attacking aircraft\. 
	- Air defense units are much better than standard units with anti\-air weapons\. Units with Air Defense Capable weapons must have the aircraft approaching it directly to engage\.
		- Those AD units that happen to spot the fast\-moving attackers will fire during the approach\. 
	- If the aircraft is a Level Bomber flying at higher altitudes above the battlefield will only be engaged by weapons that reach the target altitude\. 
	- Both aircraft and air defense units have a few electronic and other systems used to degrade the performance of the enemy\. 
		- Combat hints will alert the player to radar detections, AD attack evasions, and finally loss of aircraft if one or more is shot down\. If an aircraft is shot down, then an appropriate sound effect is played\. 
	- Pilot readiness plays heavily into their ability to detect AD fire and avoid it\. If you push your pilots on repeated passes the fatigue may lead to a mistake and a loss of the aircraft and crew\. 
		- On the ordnance delivery pass the bomb special effects are rendered in the impact location and combat losses are immediately applied to all units located there\. Friendly and enemy units are both equally at risk if they occupy the impact location\. 

When the mission is over the aircraft will be given Resupply orders if it is out of ammo or it will return to its on\-call station awaiting another strike order\. Aircraft given a Resupply order will return to base to rearm and refuel and will be available again after 30\+ minutes\.

## Helicopter Hunting

One of the new orders in the game is the Hunting Order for helicopters\. This order allows you to set several waypoints \(up to six\) that the helicopter will fly between looking for enemy units to Spot \(Recon Helicopters\) or engage \(Attack Helicopters\)\. The helicopters will continue to move from hex\-to\-hex masking with cover where possible\. Helicopters under fire will attempt to scoot away from the attacking units\. When an armed helicopter runs out of munitions it will fly back to the nearest FARP \(Forward Arming and Refueling Point\)\.

## NBC Warfare

These weapons are extremely powerful and not to be taken lightly\. Weapons of mass destruction come in three types: Nuclear weapons, Persistent Chemical weapons, and Non\-persistent Chemical weapons\. 
!!! note

    __ The game does not include biological weapons on the battlefield\.


__Nuclear weapons__ \- A nuclear strike \(which has a very awesome animation\) is resolved as a series of separate attacks against all units caught within the blast range\. For game purposes, we assume a tactical nuclear capability of approximately a 10kt yield with a 2 km blast radius\. Subunits will be eliminated based on distance from the blast center by their intrinsic protection rating, NBC rating, cover, and posture\. Units also suffer massive losses in both readiness and morale even if they survive the blast and are automatically contaminated with radiation\. Contamination can cause additional losses over time if not dealt with in a short time after the attack\. All bridges, smoke clouds, minefields, and chemical contamination within the blast zone will be eliminated\.

The ground will be contaminated with two hexes from the blast center for the rest of the game\. Units moving through the contaminated zones run the risk of additional losses and get contaminated\. All helicopters within a 5 km radius will be eliminated by the blast’s shock wave\. To decontaminate units, they must enter a Resupply order and spend time being cleared of the hazard\.

__Persistent Chemical Weapons__ \- A persistent chemical strike consists of various nerve or blood agents that can quickly incapacitate or kill exposed troops\. Units caught in a persistent chemical attack can suffer losses based on their NBC rating take a considerable loss of readiness while getting into protective gear \(MOPP suits\) and suffer additional morale loss from the attack\. Persistent chemical strikes leave markers on the map for the rest of the game\. Any units moving through are attacked and contaminated\. Like nuclear contamination, chemical contamination can be removed by a resupply order\. Contaminated units fight with reduced combat effectiveness caused by the protective gear\.

__Non\-Persistent Chemical Weapons__ \- A non\-persistent chemical strike consists of various nerve or blood agents that can quickly incapacitate or kill exposed troops\. Units caught in a non\-persistent chemical attack can suffer losses based on their NBC rating take a significant loss of readiness while getting into protective gear \(MOPP suits\) and suffer additional morale loss from the attack\. Non\-persistent chemical strikes leave a gas cloud on the map that will dissipate over a short period based on the weather conditions\. Any units moving through the gas cloud are attacked\.

## Electronic Warfare \(EW\)

Electronic Warfare is the art of spectrum warfare\. This is the use of electronic equipment to jam or spoof radio communications or jam search radars\. This work is done by assets above your command level but may benefit your forces if your side is working to disrupt the enemy\. On the other hand, if the enemy is disrupting your forces, command delays will increase as your communication efforts are hampered by enemy action\. 

In a scenario, these levels are set by the scenario designer, and you can review the levels in the Intelligence Report\. The enemy's EW interference is noted on the Command Panel as well\.

## Air Superiority

Air Superiority is a rating of whose force controls the airspace over the battlefield\. When your forces on the air, your air strike can get on the map with weak opposition from enemy fighters\. If the enemy owns the skies, there is a greater risk of losing air strikes on the way to their mission targets and even on\-map helicopters can fall victim to an air\-to\-air missile from a fighter\. All these actions are abstracted with messages popping up on the screen when interdictions occur in the game\.

In a scenario, these levels are set by the Scenario designer, and you can review the current level in the Operations Report or note the level under the weather panel display on the Game Panel\.

