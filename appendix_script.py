#@File (label="Select image", style="file") image_open
#@String (label="Select threshold", choices={"MaxEntropy", "IsoData", "Yen", "Otsu", "Li", "MinError(I)", "Huang", "Huang2", "Intermodes", "Mean", "Minimum", "Moments", "Percentile", "RenylEntropy", "Shanbhag", "NO THRESHOLD"}, style="listBox") threshold
#@String (label="Minimum particle size (0-9999)") size_min
#@String (label="Maximum particle size(0-9999)") size_max
#@String (label="Minimum circularity (0-100)") circ_min
#@String (label="Maximum circularity (0-100)") circ_max
#@File (label="Select folder for saving the images", style="directory") image_save

from ij import IJ

if threshold == "NO THRESHOLD":
    threshold = "Default"


for n in range(int(size_min), int(size_max)):
    for m in range(int(circ_min), int(circ_max)):

        IJ.open("{}".format(image_open))
        IJ.run("8-bit")
        IJ.run("Auto Threshold", "method={}".format(threshold))
        IJ.run("Watershed")
        
        n = n # Change to set constant minimum particle size
        m = m # Change to set constant minimum particle circularity

        IJ.run("Analyze Particles...", "size={}-{} circularity={}-{} show=[Bare Outlines] display summarize".format(n, size_max, (float(m)/100), (float(circ_max)/100)))
        IJ.saveAs("Tiff", "{}/{}_{}_{}_{}_{}.tif".format(image_save, threshold, n, size_max, m, circ_max))
        IJ.run("Close", "{}/{}_{}_{}_{}_{}.tif".format(image_save, threshold, n, size_max, m, circ_max))
        IJ.run("Close", "{}".format(image_open))
