# Multi\-Unit Overrun \(11 Apr 2025\)

> **Note**: Images omitted — refer to original DOCX for figures.


This is a new feature we have just added in\.

__The Problem:__

Many attacking units can become stuck on one or a few resilient units, holding up their assault and preventing them from advancing\. This creates an unrealistic strategy of putting a small number of units with a resilient SOP setup \(ex: never relocate, do\-or\-die\) in “choke points” in the enemy’s path to significantly \(on the scale of hours\) slow down their assault and cause attacking units to clump up in a way that leaves them incredibly vulnerable to indirect fire\.

We recently added a system allowing isolated units to “surrender” when faced with overwhelming odds without an escape route, but the issue remains when it is multiple units bogging down the advance\.

Ex:

> **Note**: Image omitted — refer to original DOCX for figures.



__The Solution:__

We implement an ‘Overrun’ mechanic that can wipe out groups of units that find themselves significantly outnumbered, with no chance of inflicting damage, and that have no chance at escape\. This allows us to quickly resolve these undesirable scenarios and discourages the “gamey” strategy of clogging up chokes with a small number of resilient units\.

__The Implementation Details:__

Units will be overrun under the following conditions:

- There is an in\-hex attacker\-defender step ratio of __4__:1\. The defending units are expected to earn cumulatively less than __0\.1__ kills against the attackers\.__ __The attacking units are expected to earn cumulatively more than __0\.1__ kills against the defenders\.__ __All units \(both the attacker and defenders\) have been in the hex for __120 __seconds\. 
- And the defender is not actively trying to withdraw\.
- All of these variables can be edited using magic numbers\.

When a unit is overrun, the following occurs:

- 
	- The attacking units take a readiness penalty of __10%\. __This can be tweaked under “Umpire” > “View and Edit Readiness Factors” > “loss from overrunning”
- The overrun unit and all grounded friendly units in its hex are destroyed\.
- The kills are claimed by one random attacker unit\.
- These claims are shown in the attacker’s radio log\.
- The losses are shown in the defender’s radio log\.
- A hint is shown on the map for both players in the location where the overrun occurred\. 

