# Formation Roles

The codes are found in the Formation Table and related to the overarching AI behavior, the units in that formation will act in the simulation. There is a Role call “CIV” that we may use in the future is civilians become more than “markers” in the game engine. There is also a value called “Supply” that is used internally as an error trap for the code and should not be utilized in the formation tables by users.

| **Role**   | **Description of Primary Formation Function** |
|------------|-----------------------------------------------|
| **Air**    | Any air unit type, functionality dictated by mission types (CAS, SEAD, Standoff, etc.) |
| **AntiTank** | Towed systems or man portable weapons, utilize good terrain/cover to snipe armored units, standoff, must account for limber/unlimber times to move (forward or back) |
| **Arty**   | Towed Arty units, standoff range, stay within range of forward elements for support, must account for limber/unlimber times to move (forward or back) |
| **Engineer** | Units with engineering capabilities only |
| **Flak**   | Overwatch units that provide anti-air fire versus helos and strike aircraft, NOT first line fighters and should retreat if lead elements are gone; if engaged some SPAAGs can engage ground forces |
| **Helo**   | Depending on class (Attack, Scout, Utility) they will Hunt, Recce, or avoid contact to do their missions. This is for Helos only. |
| **HQ**     | Generates orders for attached ground units, communicates up the command chain, maintains contact with sub-units, fights as necessary |
| **HQArty** | Generates orders for attached Arty/Air units, communicates up the command chain, maintains contact with sub-units, fights as a last resort |
| **Inf**    | Pure ground troops, maybe APCs but not IFVs (MechInf), engage enemies, take objectives, and utilize covered movements |
| **Logistical** | For sites like FARPs, Supply depots, POL, Maintenance, Coms/HQ, etc. |
| **MechInf** | A combination of IFVs and Infantry units used to fight and seize objectives |
| **Obsrv**  | Units with observation ability, standoff, not engaging, move only to track a target, usually looking at an AOI |
| **Recce**  | Scout out and find the enemy, standoff-based, fight if pressed |
| **SPArty** | Mobile Arty units, standoff range, stay within range of forward elements for support |
| **SPAT**   | Self-propelled weapons, utilize good terrain/cover to snipe armored units, standoff, should be overwatch types and not front-line units |
| ***Supply*** | *Dummy Role for Error Trapping – **Do not use** in Formation Roles* |
| **Tank**   | Armor forces used to kill other units and help with securing objectives, lead elements of an assault |
| **Truck**  | Formations providing utility transport, standoff, support type units |
| **WMD**    | Units with NBC weapons, must have a scripted release state for players and AI use |