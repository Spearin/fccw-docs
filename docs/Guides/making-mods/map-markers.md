# Map Markers

> **Note**: Images omitted — refer to original DOCX for figures.


These are the various markers seen on the map other than counters\. They show everything from losses, craters, obstacles, smoke, NBC effects, victory locations, and more\. Each one of these items can be modified with a new image placed in the Custom Folder\.

> **Note**: Image omitted — refer to original DOCX for figures.

> **Note**: Image omitted — refer to original DOCX for figures.

> **Note**: Image omitted — refer to original DOCX for figures.

> **Note**: Image omitted — refer to original DOCX for figures.

> **Note**: Image omitted — refer to original DOCX for figures.

> **Note**: Image omitted — refer to original DOCX for figures.

## Use

Most of the map markers are placed when designing the scenario\. This includes the following: 

- Bridge Markers \(including side\-based engineering bridges\)
- Chemical and Radiation Markers
- Improved Positions \(IP\) Markers
- Minefield Markers \(full hex and edge\)
- Obstacle Markers \(full hex and edge\)
- Victory Point Location \(VP\) Markers

Some of the markers are placed by the game engine during orders resolution\. This includes the following:

- Kill Markers \(vehicles and squads\)
- Chemical and Radiation Markers
- Crater Markers
- Gas and Smoke Markers

The Gas and Smoke marker images have full image transparency so the map underneath will show through somewhat giving the effect of real smoke\. 

VP markers will have the cost\(s\) of the hex placed in the center of the box seen on the graphic\.

## Location of Assets

All of the defaults OTS Map Markers are located in /Modules/Common/Map Markers folder\. If you make a new custom marker\(s\) they should be placed in the /Assets/Map Markers/Custom folder with the same filename\. Any markers in the Custom folder will be Size and Format Required

The size of the image can vary based on its function in the game\. We recommend staying within the size of the marker you wish to replace\. If you go beyond or below the existing size the marker will bleed over into other hexes or be distorted or too small to see\. 

The images must be saved as a PNG type file\. This will preserve any transparency in the image\.

The file name must match the one in the folder exactly to be used by the game engine\. Craters have been given a unique ability to be randomly used when needed by the game engine\. If you name your images “CraterX\.png” where X is a sequence of numbers from 1 to some number \(in our case 5\), the game will select one at random when artillery or airstrikes it a hex\.

