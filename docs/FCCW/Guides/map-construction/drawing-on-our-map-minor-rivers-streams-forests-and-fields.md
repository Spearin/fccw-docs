# Drawing on Our Map: Minor Rivers, Streams, Forests and Fields

> **Note**: Images omitted — refer to original DOCX for figures.


## Identifying Minor Rivers and Streams

The hardest part of drawing minor rivers and streams is identifying the ones that represent real water obstacles, and ignoring the ones which are too small to represent much of an obstacle\. Sadly, map data such as OpenStreetMap often is not reliable in displaying minor rivers and streams: sometimes the blue lines on the map represent 10m wide streams \(true obstacles\), other times the blue lines represent narrow ditches \(no obstacle\), and worst of all, sometimes true streams are not drawn on the map\.

> **Note**: Image omitted — refer to original DOCX for figures.



Figure 72	OpenStreetMap view and a zoomed\-in satellite view of the \(bridge across\) water obstacle

What works best for me is to use OpenStreetMap to identify potential water obstacles\. For each potential obstacle, I try to find a bridge across the obstacle, and use the satellite view to assess the size of the obstacle / bridge\. \(Narrow streams typically run amidst trees, so their size is hard to judge unless they cross a road\)\. Another way is to study the elevation; valleys typically feature a stream\.

For me, looking for streams and switching back and forth between OpenStreetMap and satellite view often is done quicker outside QGis, using my web browser and ArcGIS’s web site http://www\.arcgis\.com/home/webmap/viewer\.html

The illustration above shows a nameless stream that is wide enough to be an obstacle and runs from the Weser River north towards the highway, then tunnels below the highway and appears as a tiny ditch north of the highway\. In other words, it only presents an obstacle between the highway and the Weser\.

## Enabling Snap to Grid for Drawing Tight Polylines and Polygons

For the minor rivers and streams, and for the forest and field polygons, we can draw more quickly and more precise by having our lines / point snap to the hex grid\.

To snap to the hex grid when drawing, use “Settings” menu, Snapping Options\. Change Snapping mode to “Advanced”\. Then scroll down to our grid\_500\_minden\. Tick the checkbox, and change the tolerance to 25, units to “pixels”\. Next, press “Apply” and “OK”\.

> **Note**: Image omitted — refer to original DOCX for figures.



Figure 73	Enabling/disabling snapping to our hex grid

> **Note**: Image omitted — refer to original DOCX for figures.



Figure 74	Streams \(light blue hex side lines\) and minor rivers \(medium blue hex side lines\) added to the map

In contrast to the earlier game \(Flashpoint Campaigns: Red Storm\), there is no longer a need to manually tag the hex sides of an obstacle with obstacle ids\. The Flashpoint Map Values Scanner automatically detects and tags obstacles\.

The next render from OTS HQ shows the minor rivers and streams on the map\.

> **Note**: Image omitted — refer to original DOCX for figures.



Figure 75	OTS render of our works\-in\-progress with minor rivers / streams added

## Drawing Forests and Vineyards/Orchards

Whereas we drew the towns and rivers using hex shapes, we’ll be drawing the forests as polygons\. That way, we will need less effort to cover larger areas, and can better approximate the actual shapes of the forests\.

Personally, I approximate the forest shape using one or more \(out of six\) pizza slices in the hex\.

Before drawing the forests, make sure snapping to the hex grid is enabled\. Choose a satellite map to draw on top of\. Since the default style \(dark green triangles\) is hard so see on top of the satellite map, change the style of the manual\_forest layer to editing\_style\_forests\. This will display the forest polygons in easy to see, semi\-transparent solid red\.

> **Note**: Image omitted — refer to original DOCX for figures.
!!! note

    __ the process of going over all the satellite map, spotting and drawing the forests is also a great opportunity to spot other missed features\. In my case, I spotted and added a minor river, several “full hex” lakes, some “hex side” minor lakes, a missed secondary road, etc\.


Figure 76	Drawing forest polygon \(using a temporary high\-contrast "editing" style\)

## Drawing Fields

Drawing fields is next\. Draw any flat area, without too many buildings or trees, as a field\. Fill a complete hex or fill up a partial forest hex with field\. Leave any hex with many buildings or trees blank; Flashpoint Campaigns will see this as “Mixed”, with slightly higher visibility hindrance and mobility hindrance than a clear field\.

Drawing fields into partial forests goes easier when we are also snapping to the forest layer\. So, use “Settings” menu, “Snapping Options”, and enable snapping to manual\_forests, with tolerance set to 25 pixels \(as units\), and Mode set ‘to vertex’\.

> **Note**: Image omitted — refer to original DOCX for figures.



Figure 77	Snapping to the hex grid and the manual\_forests layer

> **Note**: Image omitted — refer to original DOCX for figures.



Figure 78	Fields drawn on the map, using the editing\_style\_fields for better visibility

## Drawing Banks

For Flashpoint Campaigns, riverbanks and major lake banks need to be drawn explicitly, as lines on the inside \(water side\) of the land\-water hexside boundary\. If we were to use snapping to the hex grid, the bank lines would up on the hexside and into both hexes, which is not what we want\.

Instead, we’ll just use the manual\_lake\_major and manual\_river\_major polygons to snap to and deselect snapping to any other layers\.

> **Note**: Image omitted — refer to original DOCX for figures.



Figure 79	Snapping only to layers manual\_lake\_major and manual\_river\_major

With snapping set\-up correctly, enable layer manual\_bank for editing, and draw lines along the river and lake shapes near hex sides with land hexes, as illustrated below:

> **Note**: Image omitted — refer to original DOCX for figures.



Figure 80	Banks drawn along the sides of major rivers and major lakes

## Inspection Time: Fixing Road Flow and Elevation

We are done doing the bulk drawing\. This is a good time to take a critical look at our results and correct those spots that don’t seem quite right\.

The things to look for are:

- Hill shapes which aren’t correctly represented in the hex elevation values, for example because a narrow hill shape is split across two hexes, and doesn’t have a back impact on elevation of these hexes
- Awkward or unrealistic roads running uphill or downhill for no good reason

> **Note**: Image omitted — refer to original DOCX for figures.



Figure 81	Two ridges \(red markings\) not interpreted as higher elevations along their full lengths

Our map has a few locations where the elevation values do not correctly reflect the ridge’s elevation\. We are going to correct this in QGis, by placing hex shaped polygons in those locations where we want to correct elevation and set the correct elevation value for them\. The layer’s style is set\-up such that it will display a polygon with the right color for the elevation set\.

Enable manual\_elevation\_corrections layer for editing\. Select a hex shape on the manual\_urban layer, copy it, switch to the manual\_elevation\_corrections layer, and paste it at the location where you want to correct the elevation\. Next, with the shape still selected, use the Layer menu, Open Attribute Table\. For the newly created shape, enter in the “elevation” column the intended elevation, then press the Save Edits button\.

> **Note**: Image omitted — refer to original DOCX for figures.



Figure 82	Setting the elevation for a shape in the elevation\_corrections\_layer

> **Note**: Image omitted — refer to original DOCX for figures.



Figure 83	Three corrections, shown in the table and on the map

