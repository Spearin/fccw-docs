# Weather in the Game

> **Note**: Images omitted — refer to original DOCX for figures.


Weather is presented explicitly in the game, to the player, and to the scenario designer\. Having full and consistent weather data is essential to clearly present \(and process\) the weather in the game\.

The Flashpoint Campaigns engine steps through the weather data in 5\-minute increments and interpolates between hourly observations\.

## User\-Interface

The current weather is presented in the ‘current situation’ panel, and implicitly through a map hue\. 

The bottom part of the turn/clock panel lists:

- Part of day \(night, dawn, day, night\)
- Cloud conditions and ground conditions
- Precipitation, if any
- Visual range
- Weather icon represents cloud and ground conditions
- Wind direction and speed
- Weather icon represents wind direction
- Illumination level \(as percentage\)
- Weather icon presenting lunar state \(night\)
- Next dawn/or dusk times \(start\- and end\-time\)
- Cloud base height, and whether the clouds are rising or falling

> **Note**: Image omitted — refer to original DOCX for figures.



The part of the day, and specifically the transitions from night through dawn to day, and from day through dusk to night, are also indicated by a hue change of the terrain\. 

> **Note**: Image omitted — refer to original DOCX for figures.



## Weather Forecast

The upcoming weather for the scenario is presented via the TOC Intel panel, in the Weather Forecast tab\. Here, a forecast is given for the next 24 hours, along with information on dawn and dusk timings and the lunar phase\.

The weather forecast provides information by the hour for the ‘modern era’, and by day part \(6 hour, fuzzified\) for the ‘Cold War era’\.

Additionally, the weather forecast provides a list of systems that might be impacted by those weather conditions \(roughly based on US FM 34\-81\-1\)\.

> **Note**: Image omitted — refer to original DOCX for figures.



> **Note**: Image omitted — refer to original DOCX for figures.



## Scenario Editor

The scenario creator defines the weather for the scenario he creates\. The scenario creator either selects a single ‘weather day’, resulting in ‘fixed’ weather for the scenario, or multiple ‘weather days’, resulting in pseudo\-random weather for the scenario\. 

In case of multiple ‘weather days’, one of these ‘weather days’ is picked at random at scenario start time, and used for the duration of the scenario, across saves and reloads of that scenario\. Whenever the scenario starts anew, the random selection is performed anew, most likely yielding different weather\. 

The Scenario Editor’s dialog to select weather \(‘weather days’\) for is shown below\. 

> **Note**: Image omitted — refer to original DOCX for figures.



In the Scenario Editor’s ‘Select Weather’ dialog, first the weather station is selected, in ‘1\. Select Weather Area’\. \(If the map used for the scenario shipped with the game, the Scenario Editor will automatically select the matching weather station, based on a configuration file\)\.

By pressing the ‘Load Station Weather’, the game loads the ‘years’ for which the selected station has weather data and shows this in the selection list under ‘2\. Select Year\(s\) of Data’\. Select at least one year to continue\.

Generally, the year will be after 2000, since weather stations didn’t start collecting and sharing extensive and complete per hour data until digital computers and the Internet became common\. For, for example, the Cold War era, we need to use later but regionally representative weather\.

Next, pick a date and date range\. To pick the weather representative of the scenario’s date, it’s recommended to pick \(a range around\) that date\. For example, for August 13, 1989, scenario, pick the August 13 date\. Weather from around August 13 will be representative of the seasonal weather and also have representative dawn and dusk times\.

Alternatively, for example, when foggy days are scarce in mid\-August, one might try picking weather from April, since this will have similar dawn and dusk times\. Whatever, weather is chosen, it is presented to be on the scenario’s date\.

As a next step, set weather criteria under ‘4\. SetWeather Filter Criteria’\. Selecting ‘Any’ for each criterion results in no filtering\.

Finally, press the ‘5\. Select the Weather Data’ button\. After a while, the data is loaded and filtered, the selected weather days \(if any\), are displayed in the table underneath\.

The table shows up to 30 days of selected weather, from 00:00hrs on the selected day until 23:00hrs on the following day\. All columns for the following day have their timestamp tagged with ‘\*’\.

Press ‘Proceed’ to select these ‘weather days’ for your scenario, or press ‘Cancel’ to discard any changes made\.

The selected weather data will be included in the scenario and the scenario can be distributed to others without these players being required to have the same weather data files installed on their computer\.

### How to Select Random Weather

To select random weather for the scenario, ensure the weather data selection contains more than one ‘weather day’\. This can be done in multiple ways:

- Include multiple years in the selection
- Expand the range around the selected weather data \(and press the ‘Select Weather Data’ button\)
- Relax the filter criteria

Make sure to press the ‘Select Weather Data’ button after making any of the changes\.

### How to Select Foggy Weather

To select foggy weather for the scenario, first select ‘Fog’ under ‘4\. Set Weather Filter Criteria’, ‘Conditions’\. And press the ‘Select Weather Data’ button\. 

If the result is zero ‘weather days’, then foggy days are scarce for the selected date\. To work around this and increase the number of foggy days returned, do:

- Include multiple years in the selection
- Expand the range around the selected weather data \(and press the ‘Select Weather Data’ button\)

Make sure to press the ‘Select Weather Data’ button after making any of the changes\.

If the result still is zero ‘weather days’, consider switching to another area/weather station’s weather\.

