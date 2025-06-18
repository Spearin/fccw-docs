# Replacing Sound Assets

> **Note**: Images omitted — refer to original DOCX for figures.


Flashpoint Campaigns has several music and sound effects built into the game engine to add to the atmosphere of the battle raging on the screen\. You can replace these sounds if you follow the format options below and, in many cases, add more sounds to increase the variety of effects heard in\-game\. If you decide to replace our sounds, I suggest saving them in another folder so they can be recovered if something fails to work with your sound effects\.

Apart from the two themes, all other sounds are played only during turn resolution when the action is being played out on the screen\.

## Vehicle Sounds

Every vehicle type used in the game and found in the data files has a sound effect for it that is heard when the unit is moved in game\. These sound effects add to the overall atmosphere of the game\.

### Use

The following list is all the current movement sound types used in the game based on the mobility type of the unit\.

- armcar\.wav, helo\.wav, leg\.wav, jet1\.wav thru jet5\.wav, track1\.wav and track2\.wav, truck\.wav, ssm\.wav, screw1\.wav, screw2\.wav, and prop1\.wav and prop2\.wav

These sounds are hard coded based on the mobility type of the unit\. To replace them, you must use the same file name and replace the existing sound file\. We would recommend backing up the default Vehicle sound files to another folder so they can be recovered in case the new sound file does not work\.

Each movement sound should be about 1 second long and not longer than 3 seconds\. Any longer and you may get delays in gameplay or unexpected sound play in\-game\. Test the sounds to make sure you are now getting overlapping plays in the action is fast on the screen\.

The volume levels are controlled in the game options\. 

### Location of Assets

All vehicle sounds are located in the /Modules/Common/Audio folder\.

### Format Requirements

It must be a WAV\-type file to work with the game engine\. No MP3s or OOGs\.

The Bit Rate must be 512kbps\. Other bit rates may work\. If you choose a setting and hear no audio, try another bit rate\.

WAV files are also recorded for Stereo output\. 

The file name must match the name in the list above\. There is no file name link in the data file for movement sounds since they are based on the mobility class of the unit and hard coded to the given sound\.

## Combat Sounds

Every weapon type used in the game and found in the data files has a sound effect that is heard when the weapon is fired in the game\. These sound effects add to the overall atmosphere of the game\.

### Use

The following list is all of the current combat sound types used in the game\.

- Weapon Sounds: agl\.wav, atgm\.wav, auto cannon\.wav, blast\.wav, bomb\.wav, flak gun\.wav, flame\.wav, gat\.wav, HSA\.wav, hvy arty\.wav, LSA\.wav, med arty\.wav, missiles\.wav, mortar\.wav, MSA\.wav, rpg\.wav, sam\.wav, tank gun\.wav, HvyArtyStrike1\.wav, and LtArtyStrike1\.wav\.
- General Combat Sounds: airstrike\.wav, hit\.wav, miss\.wav, nuke\.wav, and AC\_Crash\.wav sounds\.

For each sound type, there may be more than one sound file\. This is the case for most of the weapons and a few of the general combat sounds\. If there are multiple sounds, each name will have a numeric value added to the filename\. For example, HSA1\.wav and HSA2\.wav are two of the Heavy Small Arms files used\. We have added many different sounds for the same type of weapon to have a variety of sounds during a battle\. You can replace any or all of our sounds in the Audio folder\. Just place your modified sound files in the Custom folder using the same names as the files in the Audio folder, and those sounds will be used instead\. Just remember to back up the originals in case any problems arise\.

Each combat sound should last no more than 1 second\. It is a good idea not to make them longer than they are now\. Overextending the sounds could lead to dropped sound effects or other unwanted behaviors from the audio\.

The volume levels are controlled in the game options\. Care should be taken to try to match the existing volumes and not have sounds of the same type with widely varying volume levels\.

### Location of Assets

All combat sounds are located in the /Modules/Common/Audio folder\.

### Format Requirements

It must be a WAV\-type file to work with the game engine\. No MP3s or OOGs\.

The Bit Rate must be 512kbps\. Other bit rates may work\. If you choose a setting and hear no audio, try another bit rate\.

WAV files are also recorded for Stereo output\. 

There are two ways to create/replace the existing combat sounds\.

- You can replace the existing file with a new sound with the same exact name\. These sounds will play for any scenario that uses the standard sounds\.
- The path of more work would be to change the sound filename of a specific weapon in the data files and then add the new sound file to the Audio folder\. These sounds will only work when new scenarios are made using the modified data files\.

## Theme Music 

The game has two pieces of theme music\. One gets the blood flowing before the fighting begins and the other sets a calmer and serene atmosphere to review the day's destruction\.

### Use

The Main Theme starts when the game is loaded and loops through until a scenario is started\. 

The End Theme is played during the post\-mortem of a scenario\. 

The volume level is controlled in the game options\. 

Both pieces of music last around 3 minutes\. You can replace it with any length music file you like, but wav files get large quickly \(about 10mb\-20mb per minute based on the sample rate used\)\.

### Location of Assets

Both themes are located in /Modules/Common/Audio folder\.

### Format Requirements

It must be a WAV\-type file to work with the game engine\. No MP3s or OOGs\.

The Bit Rate must be 1411kbps and use a 16\-bit format\. Other bit rates and bit formats may work, but as we found out after launch, specific OS versions and codices may not work together with non\-standard bitrates\. If you choose a setting, hear no audio, or generate a crash in the game engine, try another bit rate or bit format\.

WAV files are also recorded for Stereo output\. 

The file name must match the one in the folder strictly to be used by the game engine or risk them not playing or generating an error\.

## Background Battle Sounds

The game has three sound files that create the sounds of distant combat as an ambient effect\. They are a mix of various weapons and movement sounds\.

### Use

Each battle background lasts around 1 minute\. You can replace it with any length file you like, but WAV files get large quickly \(about 3 MB per minute at 512kbps sample rate\)\. To replace them, you must use the same file name and replace the existing sound file or place your sound file in the Custom folder with the same name as the original\. We would recommend backing up the original Background Battle Sounds to another folder so they can be recovered in case the new sound file does not work\.

The volume level for the background sounds is controlled in the game options\. 

### Location of Assets

Background Battle sounds are located in /Modules/Common/Audio folder\.

### Format Requirements

It must be a WAV\-type file to work with the game engine\. No MP3s or OOGs\.

The Bit Rate must be 512kbps, but other bit rates may work\. If you choose a setting and hear no audio, try another bit rate\.

WAV files are also recorded for Stereo output\. 

The file name must be “Battle\_backgroundX\.wav” to be used by the game engine \(we use Battle\_background1\.wav through Battle\_background3\.wav in\-game\)\. The game will randomly play one of them at random times during the scenario\. The name of the new file must match one of the existing ones to work\. As noted above you can also place your modified file in the Custom folder to play instead of the defaults\.

