# Circle of Willis Type/Configuration selector - MeVisLab GUI:

Intended to be used on:
- TOF MRA images to determine the type of Circle of Willis.
- Larger sets of images from 100 up to at least 2000 images.

## OS it worked/has been tested on:
- macOS Sierra

## Software and version used:
- Python Version 2.7.13 - Anaconda2 build
- MeVisLab Version 3.0.1 (2017-08-20 Release)
- R Version 3.4.2

## Hardware limitations:
- Depending on the size of your images, mostly RAM.

## Remember to:
- Set the correct paths; see File Structure.
- Nothing else should not need to be tampered with to work.

## "Recommended" File Structure:
Overall project folder with:
- Code folder
- Images folder sorted by ID folders
- Folder with progress cache and collected/translated csv files.

## How to setup:
1. Start MeVisLab
2. Open MeVisLab script ("gui_naming_types.mlab") and you will most likely see errors due to missing or non-existing file paths. These errors occur since MeVisLab calls "initial" and "wake-up" Python code. So if you don't trust this git and its code, you should just quit now or run it in a safe environment.
3. Re-open MeVisLab edited script ("gui_naming_types.mlab") and start to classify images. To continue to the next image press "Execute" in the RunPythonCode module in the "MAIN" code segment; not "initial" or "wake-up".
4. Collect all intermediate csv files to a larger one by running "pandas_collecter.py".
5. Translate the results to something more easily manageable (also csv format) by using one of the parsers.

### Remarks:
The GUI might be a little buggy regarding its buttons in the View3D module in MeVisLab. Suspect that the issue arose from zooming, but no workaround has been tempted. The buttons in the View2D should work. When every image has been typeset, then an error will show that there is no more images. Lastly, the GUI should remember old types (if you haven't deleted the individual csv files) and remember which image you were trying to typeset through the cache. The cache can be manually changed as well as the other csv files.
