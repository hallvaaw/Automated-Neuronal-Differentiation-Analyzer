# Automated Neuronal Differentiation Analyzer

Automated Neuronal Differentiation Analyzer (ANDA) is an image analysis tool used for analysis of microscopy images from 2d neuronal cell cultures. The pipeline is a series of Python and Jython scripts executed in succession by a Bash script. Important metrics in neurodevelopment such as cell body count, neurite lengths and neurite branching points are retrieved from images and analysed using [Fiji](https://imagej.net/Fiji/Downloads).

![image](https://github.com/hallvaaw/NeuroX/blob/master//front_page_pics/header_png.png "ANDA")

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

Before using ANDA, be sure to have back up of all images. Also ensure that you have enough space to run the analysis as the analysis creates output files that require some space. At least twice the space used by the images should be available.

Make a new directory "work_dir" and place all the code files here.


### Image directory structure

Sort all images in one head directory (i.e "experiment_1_images") with subdirectories for every well and image tile. The naming convention is {prefix}\_{well}_\{image tile} (see figure 1).



![image](https://github.com/hallvaaw/NeuroX/blob/master//front_page_pics/dir_structure.jpg "directory structure")

*Figure 1: Directory structure of the image files.*



See figure 2 for the standard naming convention of IncuCyte image files. Use this to set the correct prefix, well etc.

![image](https://github.com/hallvaaw/NeuroX/blob/master//front_page_pics/file_name_parts.jpg "file name")
*Figure 2: Standard naming convention for naming IncuCyte files.*

## Starting the tool

From the terminal and while in "work_dir", start the Bash script by typing "bash ANDA.sh" or "./ ANDA.sh" and hit Enter.

### Adding new cell line

Upon starting ANDA, you are presented a window were you can add parameters for a new cell line. Add the new parameters and hit "Submit and Continue".
If you are not going to add a new cell line, hit "If no, press this button to continue".
If you want to add a new cell line, but do not have the parameters, close the window and see section "Finding new cell parameters".

### Setting the analysis parameters

In the next window set the analysis parameters by filling out the required information (figure 3).
* Choose the main directory containing all the subdirectories as image directory.
* Choose the first image in the first subdirectory as reference image.
* Select the full path to the ImageJ program. Usually this is /home/.../Fiji.app/
* Set neurite aspect ratio threshold for exclusion of false positive neurites. Set this value to zero if you want to include every identified object.
* Select analysis metrics, operative system, wells to be analysed and cell line.
* Select if you want to save object outlines or not. Note that if you choose to do so, object outlines will be saved in directories with the suffix "_{cells/neurites/branching}".
* Select if you want to register images or not.
* Start the analysis by pressing "Submit and continue".

#### To register images or not
Image registration uses the Fiji plugin "Register Virtual Stack Slices" to geometrically align and stack the images. However, how well the registration goes depends a lot on the quality of the data, with low quality data running the risk of throwing errors or yield badly registered images. A successful registration gives a stack of stabilized images which are easier to process or crop. However it makes no difference for the image analysis itself whether the images are registered or not. If you want stabilized time series of your data, choose registration but beware that this will take considerably longer time to run. The registered images are saved in folders with suffix "output".

![image](https://github.com/hallvaaw/NeuroX/blob/master//front_page_pics/main_gui.jpg "Graphical user interface")
*Figure 3: TkInter graphical user interface for selecting parameters for image analysis.*
## Running the analysis

The tool will now run through all selected wells and apply the analysis metric(s) you chose. Depending on the system you are running on, and the number of images you are analysing this will take a while. To abort press "Ctrl+C".

When the analysis has finished, the results are stored in csv files named "results_{metric}.csv" in the same directory as the image subfolders.
Note that there are also csv files stored in the directories with names ending with "results". These csv files contain unsummarized data on every identified particle in every image.
If you chose to register the images, the transform files are saved in the directories with names ending with "transform".

### Removing empty folders

If you want to remove all the empty folders that are left after analysis, run this command from the command line in the image folder:  "find -type d -empty -delete".
#### Caution:
This command will remove all empty directiories. Make sure that you are running it at the right place.


## Finding new cell parameters

If you want to add a new cell line, but do not have the parameters required for the particle analysis, you can use the appendix script to find them.

### How to use

1. In Fiji, open the appendix script by File -> Open... or press "Ctrl+O"
2. Press "Run" and select an image with the cell line.
3. Select the thresholding algorithm you want to test, or choose "NO THRESHOLD" if the image is already segmented i.e with [Trainable Weka segmentation.](https://imagej.net/Trainable_Weka_Segmentation)
4. Select the minimum and maximum particle size in number of pixels. Use a narrow range as possible. Set constant minimum and maximum values by changing line 23 and 24 in the script (see figure 5).
5. Select the minimum and maximum circularity of the particles. A perfect circle has circularity equal to 1.00, whereas the least circular shape has circularity equal to 0.00. Try for instance a range from 0.40-1.00 for cell bodies and 0.00-0.40 for neurites to begin with.
PS: type in integers from 0-100 (see figure 4), not decimal numbers!
6. Choose the folder where you want the outlines to be saved and press "OK".
7. The script will now run particle analysis with the ranges set and save the outlines in a folder. The names of the files shows the parameters as such: {treshold}\_{minimum particle size + step *n*}\_{maximum particle size}\_{minimum circularity + step *m*}_{maximum circularity}.tif
8. Use the outlines to compare to the original image. Set a new and more precise range until you have found the parameters that makes the best outline.

![image](https://github.com/hallvaaw/NeuroX/blob/master/front_page_pics/find_params_gui.jpg "Find parameters")
*Figure 4:Graphical user interface for testing and determining cell line parameters.*
![image](https://github.com/hallvaaw/NeuroX/blob/master/front_page_pics/find_params_script.jpg "Change to set constant minimum particle size and circularity")
*Figure 5: Script for finding cell line parameters. Change line 23 and 24 to integer values for constant lower particle size and circularity, respectively. Use if you for instance have found cell size, but want to determine cell circularity.*



