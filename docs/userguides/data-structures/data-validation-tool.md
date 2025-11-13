# Data Validation Tool

Included in the Data Folder is an Excel Macro enabled file (\*.xlsm) called Data Validation Tool. This spreadsheet has a VBA code form that can be used to review each tab of a National Data Spreadsheet and tell you about any detected errors. While it is not 100% foolproof, the tool does find 95% of the typical errors that can take time to find without the tool.

We are still in the process of improving the tool as well and any feedback or suggestions for other typical editing faults to cover is appreciated.

The spreadsheet itself also contains instructions like the ones shown here for easy reference when using the tool. The spreadsheet code and supporting internal tables are hidden and locked at this time to avoid any possible support issues.

**WARNING:**While the Validation tool will catch a good number of the errors that can crash the game, it is not perfect, and some errors may still make it into he files and break the game**. Make sure you review your data edits.**

## How to use this Tool

1. If the Data Validation Tool dialog is not showing (seen in the previous image) after starting the excel file, click the Run Tool button.

2. Once the dialog is shown (image below), click the Select Data File button and navigate to the data folder with your data file to validate. The top text box will show the drive location of the games data folder based on its installed location on your system.

3. Select the [Filename] data file you want to validate and click Okay.

4. Move the opened data file spreadsheet to another screen or minimize it so you can see the dialog.

5. Click on any button to have the validator check over the stated tabs on the data sheet and report any errors.

    a. You may need to maximize the spreadsheet if you do not have it open on another screen.

    b. Some sheets may take several seconds to process, and the tool will not "Processing..." at the bottom left if the sheet is being worked on. In particular, the Formations and Units tab can take time to process if there are many entries or you have an older processor.

    c. If the Check button turns **GREEN**then no errors were detected on the sheet.

    d. If the Check button turns **RED** then errors where found and the sheet needs to be reviewed and corrected.

6. You can edit any mistakes in the data spreadsheet and save it and then rerun the check without reloading the file.

    a. Any field with an error in it will turn pink and there will be a red colored Errors column off to the right of the information in the spreadsheet tab.

    b. The specific type of error, what information is bad, and the cell ID are shown if known. There are some cases where the error will be detected, but the cause may not be relayed in the error message. In those cases, there is usually a missing comma, wrong symbol in a formation or weapon system entry, or a typo in a name or ID tag value.

    c. If there are no errors on the sheet the background for the Error cell will be green.

7. When your checks are complete, and all Check buttons show green for no errors you can click the Clear Errors button to remove the validation information.

8. Click Close File and then save your data spreadsheet when the Save dialog pops up.

9. From here you can either close the program or open a new Check file to validate and repeat the process.

## Additional Tool Features

This section will cover features of the Data Validation Tool and any new features or capabilities.

### Worksheet Header Check

The Validation Program checks all the names used as headers for each of the main datasheet tabs in the workbook. If any are incorrect, they are automatically replaced, and the repair is noted in the lower right of the Tools dialog box. If all is correct the lower right notification notes the sheet’s headers have been checked.

### Data Elements Check

The Data Validation Tool is updated to include checks for the newly added/removed characteristics and any other new data types referenced in the data sheets.

### Formation Tab Checks

The tool checks for the valid range of Indented Nodes via the “<1” through “<8” codes in the Formation Code Data Field.

There are also checks that help with Composition errors with extra spaces, periods in place of commas, and commos as the last character. These are the most common errors in this field.

### Units Tab Checks

The Data Validation Tool checks both the Sils and NATO folders in the FCCW Module folder structure for matching image callouts from the Units tab for the counter silhouette filenames used in the data files. This is the PICID and NATOPIC entries in the Units data tab.

- NATO: Flashpoint Campaigns Cold War\Modules\Common\Data\NATO

- SILS: Flashpoint Campaigns Cold War\Modules\FCCW\Sils

### Unused Units Check

The Data Validation Tool also performs a check to see if there are any Units not called out in the Formations tab. This is based on scanning the COMPIDs used and those in the Units tab. A red error field will pop up on the right side of the table and note any unused units.

It is up to the user if they wish to add additional formations that use these units. In many cases the official data files have a section at the bottom of the Formations sheet for these unused units.

## Setting Up Microsoft Excel

As with all things Microsoft, in some cases the settings to run the Data Validation Program are such that it will not run due to access restrictions. The following steps should make it work. If not, you may need to look at other Windows settings that stop or block office macros and programs from running.

Perform the following steps:

1. Open Excel and select File/Options

2. Select Trust Center (red) and select Trust Center Settings (red arrow)

3. Select Trusted Locations (blue) and then select Add New Location...(green)

4. Click Browse and navigate to the Data Structure top folder and select it.

5. Check the box for Subfolders...

6. Click Okay

With luck the validator should run. If not, you may need to check the following settings.

In the Trust Center check these settings for ActiveX:

Also check the Macro Settings: