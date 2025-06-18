# Standard Operating Procedures \(SOP\)

> **Note**: Images omitted — refer to original DOCX for figures.


One of the more requested features from earlier games was the ability to set Standard Operation Procedures in more detail for your units\. We have that now and it is a very powerful tool for you as the commander to wield\. This tool gives you the flexibility to adjust many different operational parameters of your units, per unit, per waypoint, and for new orders\. Grayed\-out parameters are not available for the selected unit\.

These SOPs can be applied to the selected unit or easily copied to other units in the formation or of a similar platform type\.

To open the SOP Manager, you can right\-click on a unit or select Menu hyperlink from a report and select it from the Unit Popup Menu, select a unit and hit Ctrl\+k on the keyboard, click on the Edit Order SOP button on the Orders tab of the Dashboard for the selected unit or open the dialog from the SOP Main Menu option\.

> **Note**: Image omitted — refer to original DOCX for figures.



## Scope

The Scope sets which order \(new, current singular order like Screen or Hold, or per waypoint of a move\) the settings are applied to\. Once all the settings are adjusted to the parameters you want for the unit\(s\) there are options on how to Apply them as noted in Section 23\.7 below\.

Selecting the “? Scope” button will pop up the following message providing information on how the Scope is used\.

> **Note**: Image omitted — refer to original DOCX for figures.



## Stance

- __Tactical Initiative__ – This is the likelihood of a unit deviating from its orders or pathing based on the current situation it is in \(under fire, outnumbered, etc\.\)\. These settings are None, Slight, Moderate, or Generous\.
- __Acceptable Losses__ – This is the unit\(s\) willingness to take losses before seeking a change in orders\. This works with the Tactical Initiative above to set how a unit reacts\. The settings for this item are Do or Die, Substantial, Moderate, or Minimal\.
- __Preferred Standoff Range__ – The number of 500m hexes you wish the unit\(s\) to be distant from any detected enemy units\.

## Combat

- __Direct Fire Discipline – __This sets the range or ability to shoot at enemy units in direct fire\. The available settings are Refuse fire, Hold until fired on, Point blank \(0 to 1 hex\), Short Range \(1/3 Max Range\), Medium Range \(2/3 Max Range\), and Maximum Range\.
- __Relocate When __– This determines under what condition a unit will seek to scoot to a new location for better protection or to avoid enemy fire\. The possible selections are After each fire mission, After all fire missions, While the enemy spotted, After receiving any fire, After receiving direct fire, After taking any losses, After taking direct fire losses, or Never\. Some of these settings work better for certain types of units\. The after\-fire mission settings work better for artillery for instance\.
- __Provide Direct Support to __– This setting is for Indirect Fire Units only and allows you to set specific direct support operations for your artillery assets\. The default setting is support for All Requesting Units\. This is equal to General support as noted in Section 25\.4 below\. Other options that support specific units are Units in the same formation or lower, Specified HQ or lower, or Refuse all requests \(which stops the FSCC from using this unit in any supporting call for fires\)\. In the selection box below is a listing of units to attach support to\.

## Movement

- __Preferences__ – When a unit moves from waypoint to waypoint there are a few options for how that travel can be done\. The hasty move will prefer roads, and Deliberate or Assaulting move orders will mix roads with cross\-country movement\. You can set stricter movement preferences by checking the boxes for Concealment \(more off\-road and seeking better\-covered terrain to move through, Roads \(favor taking roads instead of cross country\) and Avoid NBC \(which will path units around NBC\-contaminated locations on the map\)\.
- __Minefield Contact__ – This is the unit\(s\) response to entering a minefield\. The options here are Ignore and Run \(do not delay and accept the potential for more subunit losses crossing the field\)\.

In Stride Breach \(units slow down to follow a leader through the field hoping to avoid mines by traveling in the same tracks\), or Stop and Reduce \(units halt and either wait for engineers to remove enough mines to open a path through or do the work themselves at a slower rate\)\.

## Transports

- __Passengers Disembark at Range__ – There are two options for disembarking transported troops and teams from their carriers\. The first option is setting a few hexes \(500m\) from the final waypoint\. This is useful for assaults or recon efforts in hostile territory\. The other option is setting a few hexes from a spotted enemy\. This is useful if on the move and your troops encounter unexpected enemy contact\.
- __Carriers when Empty__ – Once transporting APCs \(Armored Personnel Carriers\) or IFVs \(Infantry Fighting Vehicles\) disembark their troops or teams, this setting tells the transporting units what they should do\. For APCs, the better choice is to Hide Nearby \(seek cover and do not engage the enemy\) as these vehicles are usually poorly armed and armored\. The other option is Support Passengers \(seek good cover but engage enemy units with on\-board weapon systems\) to improve firepower against the enemy, but risks losing transports to enemy fire\.

## Recovery

- __Resupply__ – This option lets you set a limit for the unit’s Ammo level and when it hits the trigger level or below, the unit will go into resupply until it either Recovers to the set percentage over time or recovers for a set amount of time which restores an amount of ammo based on the amount of time set\.
- __Readiness__ – This option lets you set a limit for the unit’s Readiness level and when it hits the trigger level or below, the units will go into resupply until it either Recovers to the set percentage over time or recovers for a set amount of time which restores an amount of readiness based on the amount of time set\.

## Inspect and Apply

There are six buttons on the left of the dialog that are used to do the following:

- __Inspect Selected Unit__ – If you want to select and see the SOPs for another unit on the map, select a new unit on the map and then click the Inspect Selected Unit button to have the SOP Manager display its SOP values\.
- __Apply to This Unit Only__ – Applies all the changes made only to the selected unit\. 
- __Cancel__ – Restores the original SOP values before any changes are made\. Once You do an Apply, there is no way to revert changes via this option\.
- __Apply to Self and All Subordinates__ – This setting is helpful if you want to set all the units in a formation \(HQ and subordinates\)\. The higher the HQ, the more units will be changed down the order of battle chain\. When applied a dialog will pop up showing all the affected units\.

> **Note**: Image omitted — refer to original DOCX for figures.



- __Apply to All Units of the Same Type__ – This setting is useful if you want to set all the units of a selected type \(like Tanks, APCs, HQs, etc\.\)\.

When applied a dialog will pop up showing all the affected units\.

> **Note**: Image omitted — refer to original DOCX for figures.



- __Apply to This and Later Unit Orders__ – This option allows you to take the current SOP setting and apply them to all the orders in the Scope list\.

At the bottom of the dialog is a check box to Automatically Apply Current Settings on the Scope Change\. If this is active, any changes that are applied to the indicated scope will apply if you select a new unit and click the Inspect Selected Unit button\. With it active if you switch to a new order in the scope selection, any changes will be applied to the previous order scope\. 

## Copy SOPs via the Spotlight Panel

There are a few more tricks with SOPs\. Once you have an SOP loaded \(and edited\) in the SOP Manager, you can apply it to parts of the OOB Tree in the Spotlight Panel \(toggle the view with F10 to see the OOB Tree as the Unit Details are showing\)\. Select a unit to paste the current SOP setting in the SOP Manager and right\-click\. From the popup menu select the option you wish to “paste” to the selected unit\.

The trick with the SOP Manager is to keep it open, go out, and paste the SOP where you need it\. Think of it as a clipboard more than an editor for a single unit's SOP\. You can apply the setting to any number of units in the Spotlight\.

