# Appendix B\. Default FCSS Map Data Types

> **Note**: Images omitted — refer to original DOCX for figures.


> **Note**: Image omitted — refer to original DOCX for figures.



Figure 89	Default Map Data Types for FCSS \(MapDataTypes\_FCSS\.xls\)

The map data types file defines how the Flashpoint Map Values Scanner interprets the terrain bitmap and sets values for the game terrain hexes and hex sides\.

The map data types file is an ordinary spreadsheet that can be edited with Microsoft Office or the free LibreOffice software\.

The map data types file consists of five sections:

- Elevations \(column ‘B’ has type ‘elevation’\)
- Hex visibility / cover / mobility \(column ‘B’ has type ‘hex’\)
- Road connections \(column ‘B’ has type ‘road’\)
- Steep slope height \(column ‘B’ has type ‘slope’, typically 1 entry only\)
- Hex edges \(column ‘B’ has type ‘edge’\)

## Elevation

The elevation section defines the colors for each of the elevations\. Although it does not impose a hard limit on the number of elevation steps, 15 steps are a good practical limit since it \(a\) is hard to discern more than 15 background colors on the map, and \(b\) 15 steps of 50m covering 750m of elevation difference suffices for the terrain surrounding Europe’s major road systems\.

The fifteen elevation colors list corresponds to the ‘fcss\_elevation\_data\_style\_XXX\_step50\_levels15\.qml’ styles files for QGis, in the example project, subfolder ‘\_qgis\_elevation\_styles’\.

For a more mountainous region \(think Golan Heights, from the Jordan river valley up to the Mt\. Hermon foothills\), we would need 20\+ steps of 50m\. We can define these colors as gray values, in the 83 \- 180 range as follows:

> **Note**: Image omitted — refer to original DOCX for figures.



Figure 90	Elevation color definitions for up to 50 elevation steps

Use the Qgis style file fcaiw\_elevation\_data\_style\_0000\-1950\_step50\.gray\.qml to format the elevation data in the right colors for the above elevation definitions\.
!!! note

    __ When scanning the hex and spotting different elevation colors, the most frequently occurring elevation color \(the statistical ‘modus’ or ‘mode’\) will be chosen as the hex’s elevation color\.


## Hex Visibility / Cover / Mobility

This section defines several types of built\-up areas, forests/agriculture, roads \(and their influence on mobility, visibility\), and several entries to ignore hex effects for hex side obstacles\.

## Road Connections

This section defines mobility properties for road types in hexes and across hex sides\.

## Slope Hex Sides

A single row defines the minimum elevation step \(in meters\) for which the hex side will be automatically labeled 'impassable' for vehicles\.

## Edges \(Hex Sides\)

This section defines edge properties for hex sides\. Mobility '0' edges cannot be traversed unless a bridge is placed\. Mobility > 0 edges can be passed, albeit leading to a delay\. Column 'G' indicates whether the obstacle is a wet or dry one\. Amphibious vehicles may cross a wet obstacle without requiring a bridge, but do not have an advantage in dealing with dry obstacles \(think ‘anti\-tank’ ditches\)\.

## How to Define an Additional Type of Terrain?

For example, to represent green house filled areas, we can define a new ‘hex’ entry that reflects moderate to poor visibility \(hard to see through greenhouses\), moderate mobility \(entry can be forced\), and poor cover:

> **Note**: Image omitted — refer to original DOCX for figures.



Figure 91	Defining an additional type of terrain: green house covered hexes

The color RGB = 190,193,160 is chose to detect green house pixels in the map bitmap\.

To pick a color, pick a unique triplet of RGB values \(each in range 0, 255\)\. For each of those color channels, take a low value up to 2 lower \(but not lower than 0\), and a high value up to 2 higher \(but not higher than 255\)\.

