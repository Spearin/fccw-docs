# File XLS Import/Export Editing

> **Note**: Images omitted — refer to original DOCX for figures.


Being able to both export certain key scenario data, edit it via an Excel file and then import changes back into a scenario file is a powerful tool for advanced users\. Like anything data editing related, you can also break the scenario with a bad data element input\. 
!!! warning

    __ Right now, there is no tool like the Data File Validation Tool to sweep for bugs and typos\. We strongly advise that you make well understood small changes\. Also, it is a particularly good idea to have your scenario backed up in case something breaks\.


## Exporting Scenario Data

First, we must enter the Scenario Editor from the Main Menu screen\. Click on the “Scenario” button in the Edit section\.

> **Note**: Image omitted — refer to original DOCX for figures.



Next, we need to load a scenario that we want to make a change in\. Click on the “Load Standalone SCN File” button\.

> **Note**: Image omitted — refer to original DOCX for figures.



For this example, I am going to edit a scenario called “Brothers in Arms”\. As the information notes, it is a small scenario featuring Cold War American, West\-German and East\-German units\. Click “Load” to load the scenario\.

> **Note**: Image omitted — refer to original DOCX for figures.



Here is the scenario after loading\.

> **Note**: Image omitted — refer to original DOCX for figures.



Now, go to the Top Menu and click on “Scenario Editor” and then click on “Export Game Data to XLSX file”\.

> **Note**: Image omitted — refer to original DOCX for figures.



An Announcements dialog will pop up with some important information about using the XLS Export/Import tool\. Worth a quick review\.

> **Note**: Image omitted — refer to original DOCX for figures.



Hit “Proceed” and you are presented with the Save File screen for the exported XLSX file\. By default, the game uses the scenario name\. You can use that or change it to something else\. It may be a good idea to export the file twice and name one with “\_Original” or something similar in case you wish to revert changes back to the original scenario information\.

> **Note**: Image omitted — refer to original DOCX for figures.



Click “Proceed” to save your export file\. If all goes well with the export, you will see the following dial box\. Hit “OK”\. If you are exporting to the same file after the first time, you will get a confirmation dialog to overwrite the existing file\.

> **Note**: Image omitted — refer to original DOCX for figures.



The exported XLSX file is now located in the Scenarios sub\-folder of the FCCW module\. In this example, we are using a scenario for Cold War and the “Brothers in Arms\.xlsx” file is in the \[installed location\]/Modules/FCCW/Scenarios or if a Steam install it is located in \[Steam Drive\]\\ D:\\SteamLibrary\\steamapps\\common\\Flashpoint Campaigns Cold War\\Modules\\FCCW\\Scenarios as seen below\.

> **Note**: Image omitted — refer to original DOCX for figures.



Next is the discussion on editing the file in Excel \(or comparable program\)\.

## Editing Scenario Data

First, we need to open the exported scenario data as noted above with Excel or compatible program\. Once opened in Excel, there are four tabs of various data in the exported file\.
!!! note

    __ Currently, the only data that can be edited and imported back into a scenario is in the Units tab\. In the future we will be working to make all four tabs full import/export capable\.


You can browse the other tabs if you wish\. For now, let’s concentrate on the Units tab and click it to look at what parameters are available to edit\. 

> **Note**: Image omitted — refer to original DOCX for figures.



Click the Unit tab and you should see the following columns of data\. A bit of an eye chart but we will go over each one next as to what you can and can’t do\.

> **Note**: Image omitted — refer to original DOCX for figures.



1. Name: This is the name of the unit seen on the counter and in any of the dialogs where a unit name is shown\. This can be edited freely\.
2. Tag: This is the generated Tag ID from the Formation creation, and it is generally the same as the Name field\. Edit to match the Name field if changed\.
3. Parent Name: This field tells which unit a sub\-unit is subordinate too\. To match up to an HQ unit this field needs to be the same as the Tag field of the commanding HQ\. 
4. Nationality: This is the data folder name of the National Data Filename found in column “U”\. If you are adding new units from a new National folder the name in column “D” and the XLS Filename in “U” must be named exactly as they are in the folder and file or the game will crash when it can’t find the data\. You can mix units from any number of nations in this manner\. The subunits in column “M” must ALL come from the same national data file\.
5. % Ammo: You can set the percentage of ammo units in the scenario here\. 0 to 125% are valid integer values to use\.
6. HQ Size: This is the same HQ size value found in the data editing information of Data Files\. This represents the command level of the HQ, not the actual size of the HQ\. 
!!! note

    __ the “\.\.\.” symbol for a platoon is 3 periods and __NOT__ the ellipse symbol\. Excel will auto correct this if you do not change it in the Options/Proofing/Autocorrect Settings\. Find the Ellipse correction, highlight it and then delete it\.


1. Icon Type: This is an internal value, and it should not be changed\. If you are adding new units, you will want to add this in and try to match existing values seen in the scenario\. For example, if you add and new Tank Company, you will want to use the “itTank” reference\.
	2. Valid Icon Types are the following: itRecce, itHelo, itTank, itMechInf, itInf, itSPAT, itAntiTank, itHQ, itEngineer, itFlak, itSPArty, itArty, itTruck, itAir, itWMD, itDrone
3. Location: This is a 4\-digit map coordinate or a “0” if the unit is off\-map followed by /North\(\-\) or South\(\+\) distance in kilometers, /West\(\-\) or East \(\+\) distance in kilometers, and /0/0\. 
!!! note

    __ It is possible to place a unit out of effective range adjusting these numbers and that can lead to a crash\. Using the in\-game Off\-Map Asset Placement dialog is a safer way to make these adjustments in the Scenario Editor\.


1. Morale: You can change the Morale value of any unit in this field\. Valid integer values are 0 to 100\.
2. Readiness: You can change the Readiness value of any unit in this field\. Valid integer values are 0 to 100\.
3. Training: You can change the Training value of any unit in this field\. Valid integer values are 0 to 100\.
4. Unit Size: This is the actual size of the unit based on the number of subunits\.
	5. Valid Unit Sizes are the following: stArmy, stCorps, stDivision, stBrigade, stRegiment, stBattalion, stCompany, stBattery, stSquadron, stPlatoon, stSection, stSquad
6. Subunit ID List: This is the most edited column in many cases\. This lists all the subunits by Tag ID from the National Data File referenced in Column “U”\. You can add or remove any number of units in this field if they are from the noted data file\. The last unit MUST have a trailing comma\. 
7. Side: Units are either Side 0 \(Blue\) or Side 1 \(Red\)\. No other sides are currently supported\.
8. Force Index: Be careful editing this field\. It matches up to the Force package in the scenario editor at an N\+1 value\. For example, a force index of 0 will be the Force 1 listing in the scenario editor\. If you add units to an existing Force, they will inherit the Battleplanes of that force \(if they have any\)\. New Forces if created have no Battle Plans until they are created in the Scenario Editor\.
9. Arrival Offset in Mins \(Minutes\): A “\-1” indicates that the unit starts on the map or off\-map at the start of the scenario\. Any integer time in minutes within the play time of the scenario can be used to set the arrival time of a reinforcement\.
10. Withdrawal Offset in Mins \(Minutes\): A “\-1” indicates that the unit stays on the map or off\-map for the duration of the scenario\. Any integer time in minutes within the play time of the scenario can be used to set the withdrawal time “X” minutes into the scenario\.
11. Internal Values: __DO NOT__ edit or attempt to add for new units\. The game will import any new units and not look for this field\. We may try to move this to its own tab in the future\.
!!! warning

    __ changing ANY values in this field or adding or removing values will cause the game to crash if this file is imported with adjusted values\.


1. Unit Status: This is the game state of the unit\. “usActive” is the default state of any unit that is in the scenario\. You can also set to “usInactive”\. This unit will not act until fired on or until it spots an enemy unit\. Units set to come on as reinforcements will have a “usReinforcement” code in this field\.
2. Default BP Template: This is from the Formation’s tab of the National Data file\.
3. National Data Filename: As noted earlier, this is the XLS filename of the datafile related to the Subunit IDs seen in Column “M”\. The file must also reside in the Nationality Folder noted in Column “D”\. This relationship is critical for proper data values to be read in during the import of the modified XLSX file\.
## Best Use Cases for the Tool

The following list provides several uses for this Import/Export tool for the game\.

- You can easily rename units and display the Tags seen in the scenario\.
- You can resubordinate units to new HQs by changing the Parent Name to another different Parent Name\.
- You can quickly adjust the starting ammo levels for all the units in the scenario\.
- You can quickly adjust the Morale, Readiness, and Training levels of all the units in the scenario\.
- You can add or remove subunits from the units in the scenario\.
- You can swap subunits in a unit\. This is useful to change a unit’s subunits from one type of platform to another\. For example, change M1A1s to M\-60s\.
- You can remove unwanted units from the scenario by deleting the row\.
- If you are very careful, you can add new units to the scenario\. Great care must be used to properly add values for the Internal values\. It is a good idea to copy an existing similar cell and then change the second value to be one greater than the highest value for a side and match the location value with the fifth value in the string\.
- You can change or add units from another nation by changing the Nationality and National Data Filename and then adding the correct units in the subunit list and also making the Name, Tag, and Parent Tag correct\.

After you have done all the edits on the Exported Data File, save, and close it\. In the next section we will go over the Import Data File steps\.

## Importing Scenario Data

After saving the edited date file, the next step is to import the modified data back into the scenario\. 

Click on the “Scenario Editor” menu item and then select “Import Scenario from XLSX” item\.
!!! warning

    __ It is important to load up the correct scenario for the datafile that you are trying to import\. The import will replace the unit’s data with a different scenario/map combination\. The best way to avoid an issue is to leave the scenario up while the editing to the Excel file is being done\. That also helps see units, locations, and other items helpful to the editors\.


> **Note**: Image omitted — refer to original DOCX for figures.



The following dialog box will pop up warning about loading the wrong file into your scenario\. Click proceed to get to the Import Data from XLXS file dialog\.

> **Note**: Image omitted — refer to original DOCX for figures.



> **Note**: Image omitted — refer to original DOCX for figures.



Select the correct XLSX data file to import in the list, in this case “Brothers in Arms\.xlsx” and then hit “Load” to have the data imported into the scenario\. Currently there are no indicators that things are done\. Give the process a few seconds and then look for your modifications\.

Save your scenario by clicking the Save Scenario button in the Scenario Editor dialog if all the changes appear to be made and are as intended\.
!!! note

    __ If you made alterations to an existing scenario, we strongly suggest changing or altering the scenario name to note the new file so it can be understood when loading all scenarios for game selection\.


## Limitations/Uses of this Tool

As noted in the previous sections, there are several possible pitfalls doing this export/import shuffle, but this tool does give the user the ability to make several scenario changes on the fly without having to rebuild a scenario from scratch or even using saved packages\. If the simulation is being used as a training tool, the ability to make rapid changes to adjust force balance and soft factors is a time saver\.

