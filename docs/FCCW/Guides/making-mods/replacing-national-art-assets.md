# Replacing National Art Assets

> **Note**: Images omitted — refer to original DOCX for figures.


One of the easier to implement but harder to actually produce \(in most cases\) is artwork for the game\. Each piece of art is in a given location with a set of parameters for format and size and a specific set of options for looks\. The trick is making something that either fits with the current game or with the new material you are making within the given envelope of constraints\. Each of the following sections will detail those characteristics and provide some ideas of what you can do\. 

National Art assets are those items related to the nation\-specific art elements found in the /Modules/Common/Data folders\.

## > **Note**: Image omitted — refer to original DOCX for figures.

> **Note**: Image omitted — refer to original DOCX for figures.

Unit Silhouettes

The default OTS unit silhouettes are the black side view of vehicles and equipment \(tanks, APCs, Aircraft, and Field Guns\) on a white background and the black, light gray, and white NATO symbols for the various infantry squads seen in the game\.

### Use

Each image is called out by a specific platform \(AFV, Aircraft, or Infantry\) in the game on the Unit Tab of the National Data file using the PICID column and a NATO symbol from the NATOPIC column\. The game engine will look for the name first in the Common folder and NATO folder\. If you want to override the game defaults, you can place silhouette files in the Common/Custom folder and the NATO symbol art in the /NATO/Custom folder\.

The background of the PNG formatted image needs to be transparent\. In the case of NATO image elements, the interior of those elements is white, but the surrounding exterior is transparent\.

> **Note**: Image omitted — refer to original DOCX for figures.

The unit images can be full color as well as the grayscale \(we use black with grays/transparency in the edge from the anti\-aliasing effect\), as this works well with the Halo and Colored Silhouettes option in the game\.

Platforms should face/head to the right \(appear to be driving or flying left to right\) in the image\. The game engine will automatically flip the image for player two\. This does not apply to infantry units using NATO images for their PICID that start with an underline\. Any file name starting with an underline \(for example: “\_Inf\.bmp”\) will not flip direction based on the side played\. All art in the NATO Folder does not flip by default for any side\.

### Location of Assets

All new vehicle and equipment Silhouettes should be located in the /Modules/Common/Data/Common folder\. If they are a Mod to replace existing images, they should be placed in the /Modules/Common/Data /Common/Custom folder\. 

All the NATO unit images are located in the /Modules/Common/Data /NATO folder\. If they are a Mod to replace existing images, they should be placed in the /Modules/Common/Data /NATO/Custom folder

### Size and Format Required

A silhouette must be at least 256 pixels wide by 128 pixels tall and have a 2 to 1 aspect ratio\. The game scales these images to be used in various UI dialogs and on the counters\. 
!!! note

    __ Any image with a 2 to 1 aspect ratio will work and get scaled in the game’s UI\. If the image is not in a 2 to 1 aspect ratio format, the image will appear distorted in the game\. If you have 4k or larger screens, you may wish to make your art larger to maintain better detail when zoomed in\.


The image must be saved as a “PNG” type file with a transparent background\. Leave at least 4 pixels on the bottom and 5\-10 on the sides and top as a buffer zone around the images\. Aircraft and helicopters should be centered in the middle of the image with a minimum of 5 to 10\-pixel buffer to the edge\. This will minimize the overlap of other counter graphics\.

The file name must match one or more file names in the Units Tab of the data file\(s\) to be used in the game\. For example, to replace the image for a T\-80U, you need to save your new image with the same name, “T80U\.png”\.

Each unit requires both a picture image and a NATO picture image in the data file\. For infantry\-type units, this is the same NATO artwork, but located in the two noted folders with different filenames\.

## SubUnit Inspector Images

Users can add Subunit Inspector \(SUI\) images for each platform to replace the standard silhouette image in the SUI\. 

> **Note**: Image omitted — refer to original DOCX for figures.



### Use

These images \(in the red rectangle\) will replace the standard silhouettes seen in the SUI display\. They are not rotated and get as shown as saved\.

If your image is smaller or larger than the image location size, the game engine will scale it to fit the image dimensions in the dialog\.

### Location of Assets

All the SUI images are located in \\Modules\\Common\\Data\\\\Unit Images folder\. This will allow for using different images for the same item based on the country of origin\.

### Size and Format Required

The SUI image is 256 pixels wide by 128 pixels tall at a minimum, and if larger, it should maintain the 2 to 1 size ratio to fit the image location\. 
!!! note

    __ Any image with a 2 to 1 aspect ratio will work and get scaled in the game’s UI\. If the image is not in a 2 to 1 aspect ratio format, the image will appear distorted in the game\. If you have 4k or larger screens, you may wish to make your art larger to maintain better detail when zoomed in\.

!!! note

    __ The larger the file size, the more memory the game will use or need\. Color images use more memory for images of the same size\.


It must be saved as a PNG\-type file\. Other file formats will not be displayed\.

The file name must match the current silhouette name by adding a “\-S” to the unit’s name\. For example, if you want to add an image for the Soviet T\-80U \(like above\), you need to save your new image as “T80U\-S\.png” in the Soviet Unit Images folder\.

## Unit Badges/Insignias/National Flags

Each force in a scenario can be represented with a Unit Badge\. In the game, we have supplied three types\. First, a stylized national flag, next, a stylized nation insignia, and finally, several unit badges or patches from actual units from each nation\. 

> **Note**: Image omitted — refer to original DOCX for figures.

> **Note**: Image omitted — refer to original DOCX for figures.

> **Note**: Image omitted — refer to original DOCX for figures.

### Use

The badges are an immersion factor for the player\. They are meant to provide a link to the country or force the player is fighting for\. These badges can really be anything you want\. Currently we went with unit patches or badges, national symbols, and flag icons\.

As you will see from many of the badges, the use of the PNG format allows for transparency in the image without the use of a target color that is removed later\. There does appear to be a case with the image container in the game engine that will take some colors and make them transparent based on the pixel in the lower left corner of the image\. If this causes a problem with your image, I suggest erasing the 4 corner pixels or making a one\-pixel transparent border around the image\. In our case most of the badges have some 3d effect and shadows to give then a “pop” on the screen\. You can make your any way you want\.

Each badge/flag/insignia is located in Badges folder\. If you want it to be available for selection in scenario construction or in\-game avatar selection \(same dialog is used for selection\) it must be in every country folder, you want it to appear for\.

If your image is smaller or larger than the 100 x 100\-pixel size, the game engine will scale it to fit the window\.

### Location of Assets

All the Badges are located in /Modules/Data//Badges folder\.

### Size and Format Required

A badge must be 100 pixels wide by 100 pixels tall minimum\. If made larger, the 1 to 1 aspect ratio must be followed of the in\-game image will be distorted\. 
!!! note

    __ Any image with a 1 to 1 aspect ratio will work and get scaled in the game’s UI\. If the image is not in a 1 to 1 aspect ratio format, the image will appear distorted in the game\. If you have 4k or larger screens, you may wish to make your art larger to maintain better detail when zoomed in\.

!!! note

    __ The larger the file size, the more memory the game will use or need\.


It must be saved as a “PNG” type file\.

The file name can be any name you wish to identify the badge\. The shorter the name, the better it will appear in the Avatar Selection dialog\.

## Counter Background Art

> **Note**: Image omitted — refer to original DOCX for figures.

Every Nation has art for the counter background that needs to convey the country of origin based on the color scheme used\.

### Use

This art is used for the counter background and is an image file allowing the users to modify or create their own for each nation\. We added in our versions with a more pronounced 3d edge and a bit of a gradient color change across the counter\. If you decide to make your own, you need to be aware of the following:

- The existing location of the text and symbols as well as the silhouette cannot be moved\.
- The existing black and white text is hard coded and cannot change\. The larger white text does have a black outline to help stand out, but the smaller black unit designation text is too tiny for a white outline\. If you choose colors that are too dark or use too many colors, you run the risk of washing the text out or making it too hard to read\.
- Less is more\. A simple single color or a simple stripe is better than a full color image of some kind\.
- You can add graphic elements to the background\. We did a subtle maple leaf imprint for the Canadian counter background and in another case small unit badges were added to the single\-color background for US units\. Again, less is more, and you must keep the counter information visible\.

### Location of Assets

Counter Backgrounds are located in /Modules/Data//Backgrounds folder\. The currently selected default background needs to be stated in the National tab of each data file\. If missing the game will generate an error\.

### Size and Format Required

Counter Background art must be 300 pixels wide by 300 pixels tall and color\. Larger images can be used, but a 1 to 1 aspect ratio needs to be maintained to avoid a distorted counter image in\-game\.
!!! note

    __ Any image with a 1 to 1 aspect ratio will work and get scaled in the game’s UI\. If the image is not in a 1 to 1 aspect ratio format, the image will appear distorted in the game\. If you have 4k or larger screens, you may wish to make your art larger to maintain better detail when zoomed in\.

!!! note

    __ The larger the file size, the more memory the game will use or need\.


It must be saved as a “PNG” type file\.

The file name can be anything you want\. We do recommend using something that uses the nation’s name or code to be easily recognized\. To use it in game, the name must be entered into the National tab of the data file you are using or to replace the ones used by OTS files, the graphic must use the same name as the existing default background\. I would strongly suggest backing the original art file up for a rainy day\.

## Flags

These are art files used that place a nation’s flag in a number of places in the UI for identification purposes\.

> **Note**: Image omitted — refer to original DOCX for figures.

> **Note**: Image omitted — refer to original DOCX for figures.

### Use

This art is used primarily in the Scenario/Campaign selection screen to filter items by nation, In the Subunit Inspector and on the Commander Panel on the main screen\.

### Location of Assets

Flags are located in /Modules/Data//Flags folder\. Each nation needs one flag for the game to show it\. If missing, the game may generate an error\.

### Size and Format Required

Flag art must be 256 pixels wide by 144 pixels tall and color\. 
!!! note

    __ Larger images may be used, but we have not tested if the game UI will scale them in all places\.


It must be saved as a “PNG” type file\.

The file name can be anything you want\. We do recommend using something that uses the nation’s name or code to be easily recognized\. The game will select the first flag it finds in the Flags folder\.
!!! note

    __ There is no need to have more than one flag file in the folder as only one is needed for the UI\.


