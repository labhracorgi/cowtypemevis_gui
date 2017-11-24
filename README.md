# Circle of Willis Type/Configuration selector - MeVisLab GUI:

Intended to be used on:
- TOF MRA images to determine the type of Circle of Willis.
- Larger sets of images from for example 100 images up to at least 2000 images.
- When only configuration combinations of binary artery categories are necessary of the following arteries: ACA, ACoA, MCA, ICA, PCoA, PCA and VBA. A mirrrored configuration will be its own configuration.

### Motivation for this repository:
To make available "tools" and code used to manually classify Circle of Willis configurations for a large amount of images. Especially with regards to Horikoshi (2002) and Krabbe-Hartkamp (1998) notation, and another "new" notation of presenting slightly more complex configurations.

## OS it worked/has been tested on:
- macOS Sierra

### Software and version used:
- Python Version 2.7.13 - Anaconda2 build
- MeVisLab Version 3.0.1 (2017-08-20 Release)
- R Version 3.4.2

### Hardware limitations:
- RAM, depending on the size of your images.
- GPU, due to 3D rendering of images.

## Remember to:
- Set the correct paths; see File Structure.
- Nothing else than these paths should need to be tampered with for the code to work.

### "Recommended" File Structure:
Overall project folder with:
- Code/***GUIscripts***
- Images/***ID***/tof_mra.nii
- GUI_other/***csv|cache***/csv_file.csv

## How to setup:
1. Start MeVisLab
2. Open MeVisLab script ("gui_naming_types.mlab") and you will most likely see errors due to missing or non-existing file paths. ***These errors occur since MeVisLab calls "initial" and "wake-up" Python code. So if you don't trust this git and its code, you should just quit now or run it in a safe environment.***
3. Re-open MeVisLab edited script ("gui_naming_types.mlab") and start to classify images. 
4. To continue to the next image press "Execute" in the RunPythonCode module in the "MAIN" code segment; not "initial" or "wake-up". Continue like this until the program says it is done and an insignificant "error" stops the code.
5. Collect all intermediate csv files to a larger one by running "pandas_collecter.py".
6. Translate the results to something more easily manageable (also csv format) by using one of the parsers.

### Remarks:
The GUI might be a little buggy regarding its buttons in the View3D module in MeVisLab. Suspect that the issue arose from zooming, but no workaround has been tempted, yet. The buttons in the View2D should still work. When every image has been typeset, then an error will show that there is no more images. Lastly, the GUI should remember old types (if you haven't deleted the individual csv files) and remember which image you were trying to typeset through the cache. The cache can be manually changed as well as the other csv files. Every image could take between 1-5 minutes to typeset properly.
