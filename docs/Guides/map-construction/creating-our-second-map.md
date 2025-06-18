# Creating Our Second Map

> **Note**: Images omitted — refer to original DOCX for figures.


With all layers already set\-up, and elevation data imported, creating a second map inside this project is a lot easier and less effort than starting a project from scratch\. 

I will try to reuse a project for several maps, if possible\. The trick is to not wipe or remove, but to add:

- Add a new area box \(edit the area\_boxes layer\)
- Add a new elevation layer, with a style / elevation coloring specific to the new area, by duplicating the srtm\_38\_02 layer, rename it to srtm\_38\_02\_, and setting the style to match the minmum elevation for the area\. Disable the elevation layer for areas you aren’t working on\.
- Add a new hex grid layer covering the new area box
- Create a new Print Composer and set it cover the area box and line up with the hex grid
- Add new polylines and polygons to the “manual” layers
!!! note

    __ If your next area is adjacent or partially overlapping with an existing area, make sure to line up the new hex grid perfectly with the existing hex grid\. This enables you to reuse any work you’ve done beyond the area boxes edge, and create larger combinations of your maps\.


> **Note**: Image omitted — refer to original DOCX for figures.



Figure 85	A second area box, with a hex grid aligned with the first

