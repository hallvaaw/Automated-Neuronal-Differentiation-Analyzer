# NeuroX

NeuroX is an image analysis tool used for analysis of microscopy images from 2d neuronal cell cultures. The pipeline is a series of Python and Jython scripts executed in succession by a Bash script. Important metrics in neurodevelopment such as cell body count, neurite lengths and neurite branching points are retrieved from images and analysed using [Fiji](https://imagej.net/Fiji/Downloads).

## Installing

### Dependencies
* [Fiji](https://imagej.net/Fiji/Downloads)
* Python 3
  - Packages:
    - numpy
    - pandas
    - tkinter

All necessary Python packages can be installed when installing [Anaconda](https://www.anaconda.com/products/individual).

### Windows
* [Git Bash](https://gitforwindows.org)



## How to use

Before using NeuroX, be sure to have back up of all images.

Make a new directory "work_dir" and place all the code files here.


### Image directory structure

Sort all images in one directory with subdirectories for every image location. The naming convention is {prefix}\_{well}_\{image tile} (see fig. 1).

![image](https://github.com/hallvaaw/NeuroX/blob/master/dir_structure.jpg "directory structure")
*Figure 1: Directory structure of the image files.*

See figure 2 for the standard naming convention of IncuCyte image files. Use this to set the correct prefix, well etc.

*Figure 2: Standard naming convention for naming IncuCyte files.*

## Starting the tool

In "work_dir" start the Bash script by typing "bash NeuroX.sh" or "./ NeuroX.sh" and hit Enter.

#### Adding new cell line

Upon starting the tool, you are presented a window were you can add parameters for a new cell line. Add the new parameters and hit "Submit and Continue".
If you are not going to add a new cell line, hit "If no, press this button to continue".
If you want to add a new cell line, but do not have the parameters, close the window and see section XXXXX.

#### Setting the analysis parameters

In the next window set the analysis parameters by filling out the required information.
* Choose the main directory containing all the subdirectories as image directory.
* Choose the first image in the first subdirectory as reference image
* Select the full path to the ImageJ program. Usually this is /home/.../Fiji.app/
* Select analysis metrics, operative system, wells to be analysed and cell line.
* Select if you want to register images or not.

## Running the analysis

The tool will now run through all selected well and apply the analysis metric you chose. Depending on the system you are running on, and the number of images you are analysing this will take a while. To abort press "Ctrl+C".

When the analysis has finished, the results are stored in csv files named "results_{metric}.csv" in the same directory as the image subfolders.

### Removing empty folders

If you want to remove all the empty folders that are left after analysis, run this command from the command line in the image folder:  "find -type d -empty -delete".
#### Caution:
This command will remove all empty directiories. Make sure that you are running it at the right place.


## Finding new cell parameters

If you want to add a new cell line, but do not have the parameters required for the particle analysis, use can use the appendix script to find them.

### How to use

1. In Fiji, open the appendix script by File -> Open... or press "Ctrl+o"
2. Press "Run" and select an image with the cell line.
3. Select the thresholding algorithm you want to test, or choose "NO THRESHOLD" if the image is already segmented i.e with Trainable Weka segmentaion.
4. Select the minimum and maximum particle size in number of pixels. Use a narrow range as possible. Set constant minimum and maximum values by changing line 23 and 24 in the script (see fig).
5. Select the minimum and maximum circularity of the particles. A perfect circle has circularity equal to 1.00, whereas the least circular shape has circularity equal to 0.00. Try for instance a range from 0.40-1.00 for cell bodies and 0.00-0.40 for neurites to begin with.
PS: type in integers from 0-100 (see fig ), not decimal numbers!
6. Choose the folder where you want the outlines to be saved and press "OK".
7. The script will now run particle analysis with the ranges set and save the outlines in a folder. The names of the files shows the parameters as such: {treshold}\_{minimum particle size + step *n*}\_{maximum particle size}\_{minimum circularity + step *m*}_{maximum circularity}.tif
8. Use the outlines to compare to the original image. Set a new and more precise range until you have found the parameters that makes the best outline.

![image](https://github.com/hallvaaw/NeuroX/blob/master/find_params_gui.jpg "Find parameters")
*Figure :Graphical user interface for testing and determining cell line parameters.*
![image](https://github.com/hallvaaw/NeuroX/blob/master/find_params_gui.jpg "Change for constant minimum particle size and circularity")
*Figure : Script for finding cell line parameters. Change line 23 and 24 to integer values for constant lower particle size and circularity, respectively. Use if you for instance have found cell size, but want to determine cell circularity.*
