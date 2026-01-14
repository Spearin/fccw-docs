# Combat Operations

Combat is the very focus of this game and is detailed in this section. The different unit and ammunition types that are included in the game ensure that many different types of combat occur during a scenario or campaign. Even chemical (persistent and non-persistent) and nuclear weapons might be used.

## Unit Postures

Units go through various changes in posture during a battle. This is a measure of how visible and protected a unit is based on its movement state and the local terrain features (see Section 16.5 above) that may provide Cover (see Section 11.8.3 above) and/or Concealment (see Section 11.8.4 above). Posture states are listed below:

- **Very Exposed** – Unit is moving/sitting in terrain with no real Cover or Concealment regardless of order. Very easy to Spot. No additional protection from the terrain against any form of enemy fire.

- **Exposed** –Unit is moving/sitting in terrain with minimal Cover or Concealment based on orders (e.g., a Hold order). Moving units are easier to Spot. No additional protection from the terrain against any form of enemy fire.

- **Covered** –Unit is moving/sitting in terrain with useful Cover and/or Concealment. Spotting that is dependent on movement, terrain, or thermal/radar signature is mildly degraded. Protection from direct fire is a function of the Cover afforded by the terrain.

- **Dug In** –Unit is sitting in terrain with a Hold order and will spend 20-30 minutes digging into the Covered terrain. It includes units in an Improved Position location (see Section 16.10 above). Unit is difficult to Spot and thermal/radar signature is reduced by a moderate amount based on the Cover of the terrain. There is extra protection from the terrain against any direct enemy fire. This unit will not be effective at artillery or air strike damage.

- **Fortified** –Unit is sitting in a fortification with extreme Cover and Concealment (see Section 16.10 above). Very difficult to Spot and thermal/radar signatures are greatly reduced. Extra protection from the Fortification in addition to the terrain provides more protection against any form of enemy fire.

## Unit Facing

There is no control over what direction units face in the game. It is assumed that the units are smart enough to show a frontal aspect if the enemy is Detected. If caught by surprise, a target unit at range may have some subunits get hit in the flank as they are not in a defensible position. At a range of one hex, there is an increased chance of getting a flank attack on a target unit as some of the subunits are assumed to be close enough and in a position where flank shots are possible. If both the attacker and defender are in the same hex, attacks have a better chance of being flank or rear aspect shots as Cover and spacing allow for more advantageous engagements. Infantry attacking armored fighting vehicles (AFVs) in built-up terrain (cities and forests) have a bonus to these better aspect shots.

## Direct Fires

All combat occurs during the turn resolution phase (see Section 13.1 above for how to start this). Spotting is checked for all units and then each unit with Assault, Hold, Screen, Move Deliberate, Move Hasty, or Direct Support orders looks for suitable targets among the enemy units that it can sight directly, or indirectly in some cases. A combat event for each pairing of attacker and defender is created and entered in the main game event queue.

The combat event is resolved between the two units at the subunit level. The attacking unit calculates the quality and quantity of fire that it can effectively use against the defender from several factors including the number of subunits it has, the armaments mounted and their effectiveness against the target subunit, the range to the target, the armaments’ base accuracy, attacker orders, crew quality, suppression from incoming fire, the presence of multiple targets, and any special bonuses such as advanced gun sights.

This effective projection of fire is applied to the defending unit which takes losses based on the quantity and intrinsic protection rating of its runners, defender orders, posture, usable terrain bonus, movement, stealth, range, and any special bonuses such as armor (e.g., Chobham, advanced composite, laminated, or reactive). The defender is also penalized if they have not sighted the attacker – surprise is assumed for the first few shots – and if the range is zero to one hex(es), there is a further penalty due to the assumption that more flanking shots are available when at such close range.

The attacker uses up munitions by the round or burst to engage the enemy and is marked as “Firing”. This “Firing” status makes it easier for other units to Spot it during the turn. Attacking also reduces a unit’s Readiness by a small amount as the crew deals with the rigors of loading and firing weapons or scanning for targets. Units occasionally gain a boost to Morale if they achieve kills without taking losses.

Defending units can take losses from combat which are tracked at the level of individual subunits. Readiness and Morale will both be degraded in these cases (see Section 26 below). Morale can take a bigger hit if the HQ is out of range or if a friendly unit within 1000 meters is wiped out.

Units are not mindless zombies that die to the last subunit. If losses in the unit are too great and Readiness and Morale are low, a unit will spontaneously give up its mission orders and try to retreat to a safer location by Scooting (see Section 21.8 above).

## Indirect Fires (IDF)

Where direct fires have the shooter seeing the target, indirect fires rely on another unit to Spot a target and provide targeting information for the indirect fire units to use to shoot with. The advantages of indirect fire are its much longer ranges and reduced exposure to direct combat.

Indirect fires are guns, rockets, and mortars that fire munitions (or are munitions in the case of rockets) over the battlefield.

These systems show up on the map as various explosion animations in the target hex based on the type of munitions used. In our earlier games, artillery fired in a piecemeal fashion with several rounds being resolved each turn they attacked. Now, each gun fires rounds over a specified duration and shells are fired until the mission is over (see also Section 22.2 above). This means enemy units can move into and out of the hex(es) being attacked. In some cases, fire will be adjusted to follow targets if they are under direct observation and there are timely communications with the observer and shooter.

Artillery fire missions can be of a few types as noted below:

- **Direct Fire** – Some field-gun-equipped artillery platforms can point themselves at an enemy and fire directly. The wisdom of this is highly debatable but it can be done. Interestingly, Soviet tactics put great store in this technique and 122 mm and 152 mm SP howitzer assets can be attached to their assault formations to use direct fire against targets. While it is certainly much quicker than trying to organize on-call fire, the cost to the lightly protected artillery would be horrendous. They used this technique extensively in the second half of World War II with the SU-76 (76 mm guns mounted in light tank chassis), and the 2S1 and 2S3 vehicles are the Cold War inheritors of that tradition. All other force structures might want to consider this a measure of last resort.

- **Pre-Plotted Fires** – These fire missions represent pre-registered targets for the artillery units to shoot at the start of a battle. For the AI player (i.e., the computer opponent), artillery barrages need to be set up in the scenario editor to start right at the beginning of battle. For the human player, this kind of strike needs to be plotted in the set-up phase prior to starting battle and will begin falling right when the first turn is executed.

Unlike on-call fire missions that react to enemy contact, pre-planned strikes shape the battlefield, disrupt enemy positions, and support friendly movements at critical times. They are carefully timed and targeted based on the operation plan, ensuring artillery fire is already in motion when the battle starts. This gives friendly forces a tactical advantage by suppressing enemies, covering maneuvers, or interdicting reinforcements.

- **Direct Support** – These artillery assets are dedicated to supporting a selected unit or set of units (see Section 23.3 above to set this combat SOP). These assets will not take on fire support requests from other units nor provide counter battery, but are ready to perform fire missions for the unit(s) it is placed in Direct Support of when they Spot enemy units. These missions usually have slightly shorter command delays for order processing than the General Support operations described next.

- **General Support** – These artillery assets take requests for fire from any friendly unit on the map and process them based on target type, urgency, and availability via the Fire Support Control Center (FSCC; see next subsection). Standard command delays exist for this type of support.

- **Counter Battery** – These assets are set to fire on located enemy artillery units if they are within range, including both on- and off-map units. While on Counter Battery they will not shoot other missions. Units with Counter Battery orders can be available to the FSCC (see next subsection) for fire support requests if they are not already engaged, and are under FSCC control.

### Fire Support Control Center (FSCC)

Fire support mission requests are made either through player intervention during the orders phase or automatically through their AI staff Fire Support Control Centre, or FSCC, during the turn resolution phase. To set a unit to be under FSCC control, toggle this setting via the Unit Popup Menu item or the check box in the Fire Support Assets tab (see Section 15.4.1 above for more on this Staff Report).

Line units automatically generate fire support requests during the turn resolution based on their sighting activities as the turn unfolds. Fire support requests are also generated by the staff when ordered to prepare a fire support plan as part of the AI planning cycle.

Fire support requests are listed in the Fire Missions tab of the Fire Support Staff Report (see Section 15.4.2 above) and are queued by their Start Time. Also listed are their End Time, Status (Active or Planned), Contact, Target hex number (marked by four-digit column/row grid coordinates), Type of ammunition, number of Rounds, Duration of fire, which Asset is firing, and the Asset Status (Ammo and Readiness). Fire support requests are discarded if the target is lost or too much time passes between the initial call and the unit being able to shoot. This is done so as not to waste ammunition shelling the empty ground.

During turn resolution, the FSCC is called to match fire support requests to available air and artillery assets. To be “available”, an artillery unit must have an On Call, Direct Support to All requesting units, or Counter Battery order and otherwise be ready to fire (i.e., not wiped out, not moving, not already assigned an FSCC mission, etc.) or be an on-call aircraft.

Missions are served first by eligible artillery units with eligible Direct Support orders, then by General Support units, and finally by units with Counter Battery orders if they are available (see previous subsection).

Available air and artillery units are assigned to the mission until the requested weight of fire has been accumulated. The necessary combat events are created in the game event queue and the selected units will fire. The fire support request will be marked as finished and then the rest of the list is processed until the supply of available artillery units is exhausted.

Artillery units that have manually been assigned a Barrage mission will fire as ordered and revert to On Call when done shooting all missions. At that time, they will be available to service FSCC or player requests. If an artillery unit runs low or out of ammunition, it goes on a Resupply order to replenish its stocks. Depending on SOP settings (see Section 23 above), artillery units will Scoot after shooting to avoid potential enemy counter battery fire.

### Observed Versus Blind Fire

When shooting with indirect fire assets, units can fire on known observed targets, on locations where targets were Detected by electronic means, or on lost visual contacts where there is no observer to the fire. Observed fires have a better chance to hit and have the ability to shift hexes if the target moves into a new hex. Blind fires will be much less effective for the same volume of fire when there is no one to adjust the fire to the targets, however this happens often anyway.

## Air Defense (AD)

There are both dedicated anti-air units and units with weapons capable of engaging air targets in the game. These platforms are defined as follows:

- **Surface-to-Air Missile Units (SAMs)** – These units use surface-to-air missiles with radar, infrared, or optical guidance to track and engage enemy aircraft and helicopters. These units have a limited number of missiles and usually have air search radar or advanced optical systems to find targets.

- **Flak Units (AAA)** – These units rely on cannons or machine guns to engage air targets with a wall of lead or proximity fuse explosives. Ammunition for these units is tracked in bursts of fire. These units can have air search radars and other optical means to find and track targets.

- **Air-Defense-Limited (ADL) Units** – Some units have machine guns, auto-cannons, or in some cases anti-tank guided missiles (ATGMs) that can be used to engage air targets in a limited capacity. For these units to shoot at an air target, they must either be the target of an air strike engaged by a hovering helicopter or engage a helicopter approaching them in a roughly 30-degree cone (these weapons cannot effectively track a moving crossing target).

Some platforms may have a mix of these systems to use.

## Air Strikes

Calling in an Air Strike sends a request to the Air Strike Controller to automatically select the best value target location for the strike to acquire the most possible Victory Points (see Section 15.1.2 above) within the discretionary radius allowed. The Air Strike Controller will default to the stated target if other targets only tie it for value. The value is based on the number of visible targets and the less-apparent air defense strength. The attack will be aborted if the target location is empty of targets when the air strike arrives and the aircraft will return to its On Call station.

An air strike attack starts with the sound effect of the approaching jet(s) and the following sequence of events happens:

- The target location flashes and the attacking aircraft appears over the target unit.

- All eligible defending units (air defense [AD] units and units with AD-capable weapons) located within range of the target location attempt to Detect the attacking aircraft.

- AD units are much better at defense than standard units with anti-air weapons. Units with AD-capable weapons must have the aircraft approaching it directly to engage.

- Air defense units that happen to Spot the fast-moving attackers will fire during the approach.

- If the aircraft is a level bomber flying at higher altitudes above the battlefield, it will only be engaged by weapons that reach the target altitude.

- Both aircraft and AD units have a few electronic and other systems used to degrade the performance of the enemy.

- Combat hints alert the player to any events of radar detection, AD attack evasion, or loss of aircraft if one or more is shot down. If an aircraft is shot down, then an appropriate sound effect is played.

- The pilots’ Readiness plays heavily into their ability to detect AD fire and avoid it. If you push your pilots on repeated passes, fatigue may lead to a mistake and a loss of the aircraft and crew. See Section 26 below for combat soft factors like Readiness.

- The bomb’s special effects are rendered in the impact location on the ordnance delivery pass and combat losses are immediately applied to all units located there. Friendly and enemy units are both equally at risk if they occupy the impact location.

After the mission is over, the aircraft will be given Resupply orders if it is out of Ammo or it will return to its On Call station to await another Strike order. Aircraft given a Resupply order will return to base to rearm and refuel and will be available again after 30+ minutes.

## Helicopter Hunting

One of the new orders in the game is the Hunt order for helicopters. This order involves setting multiple waypoints (up to six; see Section 22 above for information on plotting movement) that the helicopter will fly between to look for enemy units to Spot (recon helicopters) or engage (attack helicopters). Hunting helicopters move from hex to hex, masking with Cover where possible as they are flying low. Helicopters under fire will attempt to Scoot away from the attacking units (see Section 21.8 above for involuntary order changes). When an armed helicopter runs out of munitions it will fly back to the nearest FARP (Forward Arming and Refueling Point; see Section 19.3 above) to resupply.

## NBC Warfare

Nuclear, chemical, and biological (NBC) weapons are extremely powerful and not to be taken lightly. Using these weapons will also cost Victory Points which must be taken into consideration when choosing to deploy them (see Section 15.1.2 above for victory information). Weapons of mass destruction come in three types: nuclear weapons, persistent chemical weapons, and non-persistent chemical weapons.

!!! note

    The game does not include biological weapons on the battlefield.

- **Nuclear Weapons** – A nuclear strike (which has a very awesome animation) is resolved as a series of separate attacks against all units caught within the blast range. For game purposes, we assume a tactical nuclear capability of an approximately 10 kiloton yield with a 2 kilometer blast radius. Subunits will be eliminated based on distance from the blast center by their intrinsic protection rating, NBC rating, Cover level, and posture. Units also suffer massive losses in both Readiness and Morale even if they survive the blast and are automatically contaminated with radiation. Contamination can cause additional losses over time if not dealt with quickly after the attack by issuing a Rest and Resupply order. All bridges, smoke clouds, minefields, and chemical contamination within the blast zone will be eliminated.

The ground will be contaminated for two rings of hexes from the blast center for the rest of the game (i.e., a diameter of five hexes). Units moving through the contaminated zones run the risk of additional losses and becoming contaminated. All helicopters within a 5 km radius will be eliminated by the blast’s shock wave. Units must receive a Rest and Resupply order and spend time being cleared of the hazard to decontaminate.

- **Persistent Chemical Weapons** – A persistent chemical strike consists of various nerve or blood agents that can quickly incapacitate or kill exposed troops. Units caught in a persistent chemical attack can suffer losses based on their NBC rating, take a considerable loss of Readiness while getting into protective gear (e.g., MOPP, OZK suits, etc.), and suffer additional Morale loss from the attack. Persistent chemical strikes leave markers on the map for the rest of the game. Any units moving through are attacked and contaminated. Like nuclear contamination, chemical contamination can be removed by a Rest and Resupply order. Contaminated units fight with reduced combat effectiveness caused by the protective gear.

- **Non-Persistent Chemical Weapons** – A non-persistent chemical strike similarly consists of various nerve or blood agents that can quickly incapacitate or kill exposed troops. Units caught in a non-persistent chemical attack can suffer losses based on their NBC rating, take a significant loss of Readiness while getting into protective gear (e.g., MOPP, OZK suits, etc.), and suffer additional Morale loss. Non-persistent chemical strikes leave a gas cloud on the map that dissipates over a short period based on the Weather conditions. Any units moving through the gas cloud are attacked.

## Electronic Warfare (EW)

Electronic Warfare is the art of spectrum warfare. This is the use of electronic equipment to jam or spoof radio communications or jam search radars. This work is done by assets above your command level but may benefit your forces if your side is working to disrupt the enemy. On the other hand, if the enemy is disrupting your forces, command delays increase as your communication efforts are hampered by enemy action.

These levels are set by the scenario designer and the levels can be reviewed in the EW Report tab of the Intelligence Staff Report (see Section 15.3.5 above). The enemy's EW interference is noted on the Commander Panel (see Section 13.2 above) as well.

## Air Superiority

Air Superiority is a rating of whose force controls the airspace over the battlefield. When your forces own the air, your air strike can get on the map with weak opposition from enemy fighters. If the enemy owns the skies, there is a greater risk of losing air strikes on the way to their mission targets and even on-map helicopters can fall victim to an air-to-air missile from a fighter. All these actions are noted with messages popping up on the screen when interdictions occur in the game.

Air Superiority is set by the scenario designer and the current level can be reviewed in the Air Support tab of the Fire Support Staff Report (see Section 15.4.5 above) or noted under the Weather Panel display in the Core Game Panels (see Section 13.1 above).