# Using the Data Validation Tool

> **Note**: Images omitted — refer to original DOCX for figures.


Included in the Data Folder is an Excel Macro enabled file \(\*\.xlsm\) called Data Validation Tool\. This spreadsheet has a VBA code form that can be used to review each tab of a National Data Spreadsheet and tell you about any detected errors\. While it is not 100% foolproof, the tool does find 95% of the typical errors that can take time to find without the tool\. 

We are still in the process of improving the tool as well and any feedback or suggestions for other typical editing faults to cover is appreciated\.

The spreadsheet itself also contains instructions like the ones shown here for easy reference when using the tool\. The spreadsheet code and supporting internal tables are hidden and locked at this time to avoid any possible support issues\. 
!!! warning

    __The current Data Validation Tool is not updated to handle the new Tactical Transport data files and if run on a TT based files it will damage the Units tab of the spreadsheet and other areas\.__ We are working on a revised tool and hope to have that ready later this year\. Sorry for any editing issues this may cause in the interim\. Please follow the steps below to build a Data Check File for your data\.


## Make a Data Check File

As noted in the Warning above, the current version of the Data Validation program will damage a standard data file if processed and lead to game crashes\. Fortunately, we have a work\-around that we use to validate all the game’s data files\. That process is as shown below\.

### Steps to Follow

1. Select the data file from the Nation that you want to verify any changes or additions \(or if it is a new file\)\. In this example from the Belgian Nation Data Folder\.
> **Note**: Image omitted — refer to original DOCX for figures.



1. Make a copy of the file and name the file as \[Filename\]\-Check\.xls\. this will be an exact copy of the existing data file\.
> **Note**: Image omitted — refer to original DOCX for figures.



1. Open the Check file and click on the Units Tab\.
> **Note**: Image omitted — refer to original DOCX for figures.



1. Scroll the data until you can see columns P \(Mass\) through T \(ExtWt\) on the screen\.
> **Note**: Image omitted — refer to original DOCX for figures.



1. Select columns P though T\.
> **Note**: Image omitted — refer to original DOCX for figures.



1. Use the spreadsheet program’s tools to delete the selected columns\.
2. After deleting the unneeded columns, your sheet should like the image below with column O \(Size\) now next to column P \(FC/RF\)
> **Note**: Image omitted — refer to original DOCX for figures.



1. Click on the National tab and save\.
2. You are now ready to Validate the new Check File\!
## How to use this Tool

1. If the Data Validation Tool dialog is not showing, click the Run Tool button\.
> **Note**: Image omitted — refer to original DOCX for figures.



1. Once the dialog is shown \(image below\), click the Select Data File button and navigate to the data folder with your data file to validate\. The top text box will show the drive location of the games data folder based on its installed location on your system\. 
> **Note**: Image omitted — refer to original DOCX for figures.



1. Select the \[Filename\]\-Check data file you want to validate and click Okay\. 
!!! warning

    DO NOT __use the regular game data file or you can crash your game when the validation breaks the file__\.


> **Note**: Image omitted — refer to original DOCX for figures.



1. Move the opened data file spreadsheet to another screen or minimize it so you can see the dialog\.
2. Click on any button to have the validator check over the stated tabs on the data sheet and report any errors\. 
	3. You may need to maximize the spreadsheet if you do not have it open on another screen\. 
	4. Some sheets may take several seconds to process, and the tool will not "Processing\.\.\." at the bottom left if the sheet is being worked on\. In particular, the Formations and Units tab can take time to process if there are many entries or you have an older processor\.
> **Note**: Image omitted — refer to original DOCX for figures.



1. You can edit any mistakes in the spreadsheet and save them and then rerun the check without reloading the file\.
	2. Any field with an error in it will turn pink and there will be a red colored Errors column off to the right of the information in the spreadsheet tab\.
	3. The specific type of error, what information is bad, and the cell ID are shown if known\. There are some cases where the error will be detected, but the cause may not be relayed in the error message\. In those cases, there is usually a missing comma, wrong symbol in a formation or weapon system entry, or a typo in a name or ID tag value\.
	4. If there are no errors on the sheet the background for the Error cell will be green\. The only exception to this is the current Munitions tab\. There are several entries that are not fully active in the game, and they will show as an error, but will not affect the game\. The are munition entries starting with the “\!” symbol\.
> **Note**: Image omitted — refer to original DOCX for figures.



1. When your checks are complete, and all pages show green for errors you can click the Clear Errors button to remove the validation information\.
> **Note**: Image omitted — refer to original DOCX for figures.



1. Click Close File and then save your Check spreadsheet when the dialog pops up\.
2. From here you can either close the program or open a new Check file to validate and repeat the process\.
## Updating the Main Data File

Now that you have a validated Check file and the original National data file in the folder, we need to update the Check file into a new National file and archive the older National file in case we need it in the future\. Here are the steps to perform this action\.

1. Rename the existing National file to old\-\[Filename\]\.xls in file explorer\. For example, old\-CW 80s Belgium\.xls\.
2. Open both old\-\[Filename\]\.xls and the \[Filename\]\-Check\.xls files\.
3. In your Check data file, go to the Units tab, select column P and add in five new columns as shown below\.
> **Note**: Image omitted — refer to original DOCX for figures.



1. Go to the old\-\[Filename\]\.xls file and go to the Units tab\. Select cell range P2 through T? \(the last table entry in column T\) as seen below and then select copy\.
> **Note**: Image omitted — refer to original DOCX for figures.



1. Return to \[Filename\]\-Check\.xls and select cell P2 as seen below and then select paste\.
> **Note**: Image omitted — refer to original DOCX for figures.



1. Review the Units data sheet to make sure that all the data has pasted to the correct cells and fills all the entries to the bottom of the table as seen in the image below\.
> **Note**: Image omitted — refer to original DOCX for figures.



1. Save the file\.
2. Go into file explorer and change the \[Filename\]\-Check\.xls file to read \[Filename\]\.xls\.
3. The folder should now have the game required \[Filename\]\.xls and a backup called old\-\[Filename\]\.xls\.
If you need to process new edits to the National data file, you can make a new Check file as outlined above and delete or archive the old\-\[Filenam\]\.xls file as you repeat the process\.

## Additional Tool Features

This section will cover features of the Data Validation Tool and any new features or capabilities\.

### Worksheet Header Check

The Validation Program checks all the names used as headers for each of the main datasheet tabs in the workbook\. If any are incorrect, they are automatically replaced, and the repair is noted in the lower right of the Tools dialog box\. If all is correct the lower right notification notes the sheet’s headers have been checked\.

### Data Elements Check

The Data Validation Tool is updated to include checks for the newly added/removed characteristics and any other new data types referenced in the data sheets\.

### Formation Tab Checks

The tool checks for the valid range of Indented Nodes via the “ **Note**: Image omitted — refer to original DOCX for figures.

> **Note**: Image omitted — refer to original DOCX for figures.

> **Note**: Image omitted — refer to original DOCX for figures.



### Unused Units Check

The Data Validation Tool also performs a check to see if there are any Units not called out in the Formations tab\. This is based on scanning the COMPIDs used and those in the Units tab\. A red error field will pop up on the right side of the table and note any missing units\.

