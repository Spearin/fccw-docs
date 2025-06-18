# Weather System

> **Note**: Images omitted — refer to original DOCX for figures.


> **Note**: Image omitted — refer to original DOCX for figures.

  
Figure 1: Weather data \(filtered for 'precipitation', as shown in Flashpoint Campaigns’ Scenario Editor\)

For the Flashpoint Campaigns game engine, we have introduced a data driven weather system, which presents the commander/player with higher fidelity weather influencing the battle, and with weather forecasts to feed into tactical considerations\.

The scenarios included in the game each come with historic weather data, and present \(subtle\) climate differences between the regions\.

The scenario designer can select specific weather types for his scenario, and pick fixed or pseudo\-random weather\.

Being data driven, the Flashpoint Campaigns weather system enables the user to add new weather, to represent locations and climates different from the West/Central/East\-European weather included in the base game\. 

## Weather Elements Supported

The following weather elements are supported:

> **Note**: Image omitted — refer to original DOCX for figures.



Most of these elements are input to the game’s mechanics\. 

Many of these weather elements have analogue values \(temperature, wind speed, cloud ceiling, visibility, illumination, precipitation amount\)\. The elements with discrete values are listed below:

> **Note**: Image omitted — refer to original DOCX for figures.



For more details on the exact data input format, see Section __Error\! Reference source not found\.__\.

## Weather Elements Not Supported

As of this version, the following weather elements are not supported:

- Dust storms \(reducing visibility\)
- Icy surfaces, frozen rivers and snow heights   
\(these can be accounted for in the map’s, by setting mobility values for hex locations, and between hex locations, and by removing water obstacles\)
- Hail, sleet \(can be approximated by liquid precipitation\)
- Lightning \(too much detail for a 500m platoon\-and\-up level game/simulation\)
- Wave, surf, and tidal conditions

## Limitations

All the game’s map areas are assumed to have the exact same weather\. Generally, with most map sizes 20x15km and 40x30km, this is a fair approximation\. However, it falls short in representing valley floor ground fog in mountainous regions\.

The game does not support time zones\. Make sure the weather data is defined in time matching \(or close to\) the local time zone, so dawn and dusk times feel natural in the scenario\.

Dawn should occur no earlier than 00:00hrs \(not in the preceding evening\) and dusk no later than 23:00hrs \(not in the next morning\)\.

The minimum amount of weather required for a scenario is 24 \+ 23 hours, from 00:00hrs on the day of the scenario start to 23:00hrs on the day after the scenario start\. This is because the Scenario Editor allows scenarios to last for maximum 24 hours and start at 23:00hrs latest\.

