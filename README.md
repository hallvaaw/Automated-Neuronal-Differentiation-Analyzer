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

See figure 2 for the standard naming convention of IncuCyte image files.

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
* Select the full path to the ImageJ program. Usually this is /home/<>/Fiji.app/
* Select analysis metrics, operative system, wells to be analysed and cell line.
* Select if you want to register images or not.

## Running the analysis

The tool will now run through all selected well and apply the analysis metric you chose. Depending on the system you are running on, and the number of images you are analysing this will take a while. To abort press "Ctrl+C".

When the analysis has finished, the results are stored in csv files named "results_{metric}.csv" in the same directory as the image subfolders.

### Removing empty folders

If you want to remove all the empty folders that are left after analysis, run this command from the command line in the image folder:  "find -type d -empty -delete".
#### Caution:
This command will remove all empty directiories. Make sure that you are running it at the right place.
