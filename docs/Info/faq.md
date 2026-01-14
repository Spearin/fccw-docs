# :fontawesome-regular-question-circle: Frequently Asked Questions

To answer questions in advance on various topics that we either don't control or can't support, we have created this FAQ document with the answers already prepared.

Please review this FAQ and its topics. We will often delete threads on the various forums covered in this document to keep the forum content focused on the game and any questions or problems players are having.

## Screen Resolution
While it is noted in the Minimum Game Specifications on the Product Page, the game requires a minimum vertical screen
resolution of 1080 pixels. Some older computers, laptops and handhelds like Steam Deck fail to meet this requirement and
will not display properly (cut off menus, main screen, and dialogs).

## Native MAC OS and Linux Support

- As much as it would be great to support native code for these two OS platforms, our small team does not have the time or expertise to make these builds and, more importantly, provide technical support for these two lesser-used game platforms.

- There are ways/emulators to make the game work on these two platforms, and tech support on that will be by the community more than by us for the same reasons above.

- If our capabilities change in the future, we will be more than happy to produce a native version and support it.

## Linux Set Ups that Run the Game

- From “the_korben” on Steam - Runs on Linux but needs Proton 10. Hi, I just thought I would report that I took a leap of faith
and bought FC:Cold War to test it on my Linux machine. Just like Southern Storm and Red Storm, it works (with a couple of
UI quirks) but requires (!) Proton 10. Any earlier version of Proton will not work. Also note that Gamescope might have some
issues with it because it technically may use multiple windows, but running it on a desktop with a regular compositor should
be fine. I am adding a couple of helpful tips here that came up during the discussions in this thread. In case you encounter
problems:

    - Do not use a Wayland backend for your Proton runner. If you use standard Proton 10 from Valve, you are good, because
it uses XWayland to manage everything. But newer alternative Proton versions often come with the option to use Wayland
backends. This will cause problems. Make sure these alternative Proton versions use XWayland and/or put
"PROTON_ENABLE_WAYLAND=0" into your command line parameters for the game.

    - Gamescope and window managers such as Sway or Hyprland might also run into window managing problems. Regular
desktop environments like KDE or GNOME should be fine. If you run the game via Steam Deck, you should switch to the
"Desktop Mode". If you cannot get around using Gamescope or a window manager, try running the game inside a Virtual
Desktop via the winecfg options.

    - In case you encounter the problem that context menus do not appear unless you drag the mouse over the entries, you
can try to run winecfg on the proton prefix for the game and set the Windows version to "Windows 7" instead of "Windows
10". Thanks to user "Desert Eagle" for this solution!

## Discord Overlay UI Interference

Players discovered a UI interference issue with both FCSS and FCCW after a Discord update (PC Application, not web
based) making the game UI unresponsive in many menus and dialogs. The fix for now is to Disable the Overlay function as
noted below.

To disable: Go to your Discord desktop application -> User Settings -> scroll down to Activity Settings -> Game overlay. Turn
off the enable overlay and enable legacy overlay options (at least while you are playing FCSS/FCCW). We recommend you
restart FCCW if it was running while you were turning these options off. Worst case, reboot your PC so everything starts up
fresh and correct.

If you are only running Discord on your browser then you should be ok as it does not have the same permissions or
interactions with other applications like the actual desktop app has.

## Working with Monitors with Different Windows Font Scaling

If you are running the game on multiple monitors and those monitors have different scaling setting in Windows, when
dragging dialogs from one screen to the other the dialog could become blurry. To correct that you can do the following steps.

- Browse to the game folder by right clicking the game in Steam and selecting `Manage > Browse local files`

- Locate the "FlashpointCampaigns.exe" file (not the Launcher) and right-click it to open Properties

- In the properties window, switch to the Compatibility tab

- (Optional) Click the "Change settings for all users" button

- Click the "Change high DPI settings" button

- At the bottom, enable "Override high DPI scaling behavior", and leave the dropdown selection as "Application"

- Click OK as needed to save all changes and run the game!

This should result in the panels rendering pixel perfect, albeit a little larger than before, but not looking fuzzy.

# Printed Game Manual(s)

Recently, Matrix Games stopped offering printed hardcover manuals with new game releases and that includes Cold War. If
you want a printed manual, you will have to use the PDFs and get them printed and bound by an outside service.

## 32-bit OS Support

- To better support larger scenarios and other needs in the game engine, we have moved to a Windows 64-bit build of the game engine.  32-bit (effectively Windows 7 and earlier) are no longer supported.

## Windows 10 64-bit Support

- The game ran fine on this platform as recently as August 2024; however, Microsoft no longer officially supports any version of Windows 10 and so we cannot either.

## Localizations

- Since we don't have the time to do the ports to Mac and Linux, Localization and the changes to the UI and code to support that endeavor are out of the question as well for our small team and limited time.

- We want to be able to focus on adding more content and features and doing bug fixes to the base game engine with the time and team we currently have.

## Steam Deck Support

- Due to the limited vertical resolution on the Steam Deck (800 pixels), our game will not display in a usable fashion. We require a 1080 minimum vertical resolution.

## Steam Features

- In general, Steam is one avenue of sales for the game, and we need to have a way for all players to utilize any created content or official DLCs. We can revisit the following Steam-specific items if we find ourselves with additional time and resources.

### Workshop

- There will be no initial support for the Steam Workshop at release. We are looking at what it will take to add the supporting code and interfaces to make this happen sometime after release.

### Achievements and Trading Cards

- We are not looking to do these for the series, and there are other features and content that we see as needing our time and effort. Sorry.

## Custom Hotkeys

- Due to many hotkey assignments in the game and referenced throughout our extensive documentation, we do not allow the remapping of hotkeys in-game.

- There are means of doing this externally if you need it. There is also a risk of crashing the game with an external key mapper. FYI.

## Backward Compatibility

- As much as we would have liked to stay backward compatible with older Flashpoint Campaigns games, the sheer number and scope of changes and new features made that impossible.

- That's both good and bad news.

- On the bad side, none of the scenarios, maps, campaigns, or even data from older games are forward compatible.

- The good news is we have expanded the functionality of the game engine and worked to include some player-suggested features to the long list of things we wanted to do with the new game engine.

## Incompatible 3rd Party Software

- Software to shut down if crashing occurs loading the game.

- While we try to be as careful as possible with our coding and tools used in the game engine, some 3rd party software that hooks into other software to do several audio and visual post-processing routines can crash the game.

- These also include programs that add overlays to your games, like the Steam Overlay.

- Currently, the list is as follows:

- Raptr

- Riva Tuner

- MSI
Afterburner

- Nahimic

- If you see odd CTDs (crashes to desktop), try disabling these packages if you have them.

## Other Game Crash Sources

- Other items to check if you are experiencing game crashes or load failures.

- **Unused game controllers** - It is a good idea to unplug these if you are not using them. In some cases, an uncentered stick/pad can send the game/OS live input signals that can cause weird map movement to system crashes.

- If you see a
strange map or cursor movement, you may need to disable unused controller drivers (like 3Dconnexion).

- **Verify your game files** - Make sure you have all the files, and none are missing or corrupted. This also includes making sure you have all the redistributable libraries. Steam has a handy feature for this. If you are not on Steam, try uninstalling and reinstalling the game.

- **Latest drivers loaded** – Make sure you have the latest and greatest drivers for your audio, video, and controllers.

## Controller Support

- None. Flashpoint Campaigns is a mouse and keyboard-based game given all the information and needs to perform point-and-click operations.

## Discord Channels

- Matrix has a Discord channel. They have also made a dedicated Flashpoint Campaigns Discord channel.  If you have an issue or game-related question needing an answer, please use the game's forums on Matrix and Steam. Thanks.

- While Discord offers a means to chat, you need a full-time Dev on the channel to catch any questions/suggestions/bugs, and the format is too freeform to allow decent capture of issues or bugs.