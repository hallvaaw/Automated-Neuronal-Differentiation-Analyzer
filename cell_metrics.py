# @String input_wells
# @String input_analysis
# @String image_dir
# @String file_prefix
# @String input_tiles
# @String cell_parameters
# @String outlines
# @String registration_input

from ij import IJ, ImagePlus
from ij.plugin import ImageCalculator


wells_list = input_wells.split(" ")
wells_list = wells_list[0:-1]
print("ANALYZING IMAGES FROM WELLS ", wells_list)
analysis_params = input_analysis.split(" ")
analysis_params = analysis_params[0:-1]
tiles = int(input_tiles) + 1


file_names = open('file_names.txt', 'r')
file_list = file_names.readlines()
file_names.close()
suffix_list = [str(i.rstrip()) for i in file_list]

cell = open("{}_parameters.txt".format(cell_parameters), 'r')
cell_read = cell.readlines()
cell.close()
cell_line_parameters = [str(i.rstrip()) for i in cell_read]

min_cell_size = int(cell_line_parameters[1])
max_cell_size = int(cell_line_parameters[2])
min_cell_circularity = float(cell_line_parameters[3])
max_cell_circularity = float(cell_line_parameters[4])
min_neurite_size = int(cell_line_parameters[5])
max_neurite_size = int(cell_line_parameters[6])
min_neurite_circularity = float(cell_line_parameters[7])
max_neurite_circularity = float(cell_line_parameters[8])
cell_threshold = str(cell_line_parameters[9])
neurite_threshold = str(cell_line_parameters[10])
scale = str(cell_line_parameters[11])

if cell_threshold == "NO THRESHOLD":
    cell_threshold = "Default"
if neurite_threshold == "NO THRESHOLD":
    neurite_threshold = "Default"

IJ.run("Set Measurements...", "area mean standard modal min centroid center perimeter bounding fit shape feret's integrated median skewness kurtosis area_fraction stack display add redirect=None decimal=3")

def particle_analysis(analysis):

    if registration_input == "yes":
        if analysis == "cells":
            for well in wells_list:
                for tile in range(1, tiles):
                    for ext in suffix_list:
                        print("ANALYZING CELL NUMBERS IN WELL {}".format(well))
                        IJ.open("{}/{}_{}_{}_output/{}_{}_{}_{}".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
                        imp = IJ.getImage()
                        IJ.run("Set Scale...", "distance={} known=1 pixel=1 unit=micrometer global".format(scale))
                        IJ.run("8-bit")
                        IJ.run("Auto Threshold", "method={}".format(cell_threshold))
                        IJ.run("Watershed")
                        IJ.run("Analyze Particles...", "size={}-{} micrometer circularity={}-{} show=Nothing display summarize".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity))
                        IJ.saveAs("Results", "{}/{}_{}_{}_cells_results/cells_{}_{}_{}_{}.csv".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
                        IJ.run("Clear Results")
                        if outlines == "yes":
                            IJ.run("Analyze Particles...", "size={}-{} micrometer circularity={}-{} show=Overlay".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity))
                            overlay_ = ImagePlus.getOverlay(imp)
                            IJ.newImage("blank_c", "RGB white", 1392, 1040, 1)
                            imp2 = IJ.getImage().setOverlay(overlay_)
                            imp2 = IJ.getImage()
                            imp3 = imp2.flatten()
                            IJ.run(imp3, "8-bit", "")
                            IJ.saveAs(imp3, "Tiff", "{}/{}_{}_{}_cells/outline_cells_{}_{}_{}_{}".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))

        elif analysis == "neurites":
            for well in wells_list:
                for tile in range(1, tiles):
                    for ext in suffix_list:
                        print("ANALYZING NEURITE LENGTHS IN WELL {}".format(well))
                        IJ.open("{}/{}_{}_{}_output/{}_{}_{}_{}".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
                        imp = IJ.getImage()
                        IJ.run("Set Scale...", "distance={} known=1 pixel=1 unit=micrometer global".format(scale))
                        IJ.run("8-bit")
                        IJ.run("Auto Threshold", "method={}".format(neurite_threshold))
                        IJ.run("Watershed")
                        IJ.run("Analyze Particles...", "size={}-{} micrometer circularity={}-{} show=Nothing display summarize".format(min_neurite_size, max_neurite_size, min_neurite_circularity, max_neurite_circularity))
                        IJ.saveAs("Results", "{}/{}_{}_{}_neurites_results/neurite_{}_{}_{}_{}.csv".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
                        IJ.run("Clear Results")
                        if outlines == "yes":
                            IJ.run("Analyze Particles...", "size={}-{} micrometer circularity={}-{} show=Overlay".format(min_neurite_size, max_neurite_size, min_neurite_circularity, max_neurite_circularity))
                            overlay_ = ImagePlus.getOverlay(imp)
                            IJ.newImage("blank_c", "RGB white", 1392, 1040, 1)
                            imp2 = IJ.getImage().setOverlay(overlay_)
                            imp2 = IJ.getImage()
                            imp3 = imp2.flatten()
                            IJ.run(imp3, "8-bit", "")
                            IJ.saveAs(imp3, "Tiff", "{}/{}_{}_{}_neurites/outline_neurites_{}_{}_{}_{}".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))


        elif analysis == "branching":
            ic = ImageCalculator()
            for well in wells_list:
                for tile in range(1, tiles):
                    for ext in suffix_list:
                        print("ANALYZING NEURITE BRANCHING IN WELL {}".format(well))
                        img = IJ.open("{}/{}_{}_{}_output/{}_{}_{}_{}".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
                        imp_c = IJ.getImage()
                        imp_n = IJ.getImage()
                        IJ.run("Set Scale...", "distance={} known=1 pixel=1 unit=micrometer global".format(scale))
                        IJ.run(imp_c, "8-bit", "")
                        IJ.run(imp_n, "8-bit", "")
                        IJ.run(imp_c, "Auto Threshold", "method={}".format(neurite_threshold))
                        IJ.run(imp_n, "Auto Threshold", "method={}".format(neurite_threshold))
                        IJ.run(imp_c, "Watershed", "")
                        IJ.run(imp_n, "Watershed", "")

                        IJ.run(imp_c, "Analyze Particles...", "size={}-{} micrometer circularity={}-{} show=Overlay".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity))
                        overlay_c = ImagePlus.getOverlay(imp_c)
                        IJ.run(imp_n, "Analyze Particles...", "size={}-{} micrometer circularity={}-{} show=Overlay".format(min_neurite_size, max_neurite_size, min_neurite_circularity, max_neurite_circularity))
                        overlay_n = ImagePlus.getOverlay(imp_n)
                        IJ.newImage("blank_c", "RGB white", 1392, 1040, 1)
                        imp_c2 = IJ.getImage().setOverlay(overlay_c)
                        imp_c2 = IJ.getImage()
                        imp_c3 = imp_c2.flatten()
                        IJ.run(imp_c3, "8-bit", "")
                        IJ.run(imp_c3, "Make Binary", "")

                        IJ.newImage("blank_n", "RGB white", 1392, 1040, 1)
                        imp_n2 = IJ.getImage().setOverlay(overlay_n)
                        imp_n2 = IJ.getImage()
                        imp_n3 = imp_n2.flatten()
                        IJ.run(imp_n3, "8-bit", "")
                        IJ.run(imp_n3, "Make Binary", "")
                        IJ.run(imp_n3, "Find Edges", "")

                        imp_res = ic.run("Multiply create", imp_n3, imp_c3)
                        IJ.run("Clear Results")

                        if outlines == "yes":
                            IJ.saveAs(imp_res, "Tiff", "{}/{}_{}_{}_branching/branching_{}_{}_{}_{}".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
                        IJ.run(imp_res, "Analyze Particles...", "size=0-infinity micrometer circularity=0.00-1.00 show=Nothing display summarize")
                        IJ.saveAs("Results", "{}/{}_{}_{}_branching_results/branching_{}_{}_{}_{}.csv".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
                        IJ.run("Clear Results")
    else:
        if analysis == "cells":
            for well in wells_list:
                for tile in range(1, tiles):
                    for ext in suffix_list:
                        print("ANALYZING CELL NUMBERS IN WELL {}".format(well))
                        IJ.open("{}/{}_{}_{}/{}_{}_{}_{}".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
                        imp = IJ.getImage()
                        IJ.run("Set Scale...", "distance={} known=1 pixel=1 unit=micrometer global".format(scale))
                        IJ.run("8-bit")
                        IJ.run("Auto Threshold", "method={}".format(cell_threshold))
                        IJ.run("Watershed")
                        IJ.run("Analyze Particles...", "size={}-{} micrometer circularity={}-{} show=Nothing display summarize".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity))
                        IJ.saveAs("Results", "{}/{}_{}_{}_cells_results/cells_{}_{}_{}_{}.csv".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
                        IJ.run("Clear Results")
                        if outlines == "yes":
                            IJ.run("Analyze Particles...", "size={}-{} micrometer circularity={}-{} show=Overlay".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity))
                            overlay_ = ImagePlus.getOverlay(imp)
                            IJ.newImage("blank_c", "RGB white", 1392, 1040, 1)
                            imp2 = IJ.getImage().setOverlay(overlay_)
                            imp2 = IJ.getImage()
                            imp3 = imp2.flatten()
                            IJ.run(imp3, "8-bit", "")
                            IJ.saveAs(imp3, "Tiff", "{}/{}_{}_{}_cells/outline_cells_{}_{}_{}_{}".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))

        elif analysis == "neurites":
            for well in wells_list:
                for tile in range(1, tiles):
                    for ext in suffix_list:
                        print("ANALYZING NEURITE LENGTHS IN WELL {}".format(well))
                        IJ.open("{}/{}_{}_{}/{}_{}_{}_{}".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
                        imp = IJ.getImage()
                        IJ.run("Set Scale...", "distance={} known=1 pixel=1 unit=micrometer global".format(scale))
                        IJ.run("8-bit")
                        IJ.run("Auto Threshold", "method={}".format(neurite_threshold))
                        IJ.run("Watershed")
                        IJ.run("Analyze Particles...", "size={}-{} micrometer circularity={}-{} show=Nothing display summarize".format(min_neurite_size, max_neurite_size, min_neurite_circularity, max_neurite_circularity))
                        IJ.saveAs("Results", "{}/{}_{}_{}_neurites_results/neurite_{}_{}_{}_{}.csv".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
                        IJ.run("Clear Results")
                        if outlines == "yes":
                            IJ.run("Analyze Particles...", "size={}-{} micrometer circularity={}-{} show=Overlay".format(min_neurite_size, max_neurite_size, min_neurite_circularity, max_neurite_circularity))
                            overlay_ = ImagePlus.getOverlay(imp)
                            IJ.newImage("blank_c", "RGB white", 1392, 1040, 1)
                            imp2 = IJ.getImage().setOverlay(overlay_)
                            imp2 = IJ.getImage()
                            imp3 = imp2.flatten()
                            IJ.run(imp3, "8-bit", "")
                            IJ.saveAs(imp3, "Tiff", "{}/{}_{}_{}_neurites/outline_neurites_{}_{}_{}_{}".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))


        elif analysis == "branching":
            ic = ImageCalculator()
            for well in wells_list:
                for tile in range(1, tiles):
                    for ext in suffix_list:
                        print("ANALYZING NEURITE BRANCHING IN WELL {}".format(well))
                        img = IJ.open("{}/{}_{}_{}/{}_{}_{}_{}".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
                        imp_c = IJ.getImage()
                        imp_n = IJ.getImage()
                        IJ.run("Set Scale...", "distance={} known=1 pixel=1 unit=micrometer global".format(scale))
                        IJ.run(imp_c, "8-bit", "")
                        IJ.run(imp_n, "8-bit", "")
                        IJ.run(imp_c, "Auto Threshold", "method={}".format(neurite_threshold))
                        IJ.run(imp_n, "Auto Threshold", "method={}".format(neurite_threshold))
                        IJ.run(imp_c, "Watershed", "")
                        IJ.run(imp_n, "Watershed", "")

                        IJ.run(imp_c, "Analyze Particles...", "size={}-{} micrometer circularity={}-{} show=Overlay".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity))
                        overlay_c = ImagePlus.getOverlay(imp_c)
                        IJ.run(imp_n, "Analyze Particles...", "size={}-{} micrometer circularity={}-{} show=Overlay".format(min_neurite_size, max_neurite_size, min_neurite_circularity, max_neurite_circularity))
                        overlay_n = ImagePlus.getOverlay(imp_n)
                        IJ.newImage("blank_c", "RGB white", 1392, 1040, 1)
                        imp_c2 = IJ.getImage().setOverlay(overlay_c)
                        imp_c2 = IJ.getImage()
                        imp_c3 = imp_c2.flatten()
                        IJ.run(imp_c3, "8-bit", "")
                        IJ.run(imp_c3, "Make Binary", "")

                        IJ.newImage("blank_n", "RGB white", 1392, 1040, 1)
                        imp_n2 = IJ.getImage().setOverlay(overlay_n)
                        imp_n2 = IJ.getImage()
                        imp_n3 = imp_n2.flatten()
                        IJ.run(imp_n3, "8-bit", "")
                        IJ.run(imp_n3, "Make Binary", "")
                        IJ.run(imp_n3, "Find Edges", "")

                        imp_res = ic.run("Multiply create", imp_n3, imp_c3)
                        IJ.run("Clear Results")

                        if outlines == "yes":
                            IJ.saveAs(imp_res, "Tiff", "{}/{}_{}_{}_branching/branching_{}_{}_{}_{}".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
                        IJ.run(imp_res, "Analyze Particles...", "size=0-infinity micrometer circularity=0.00-1.00 show=Nothing display summarize")
                        IJ.saveAs("Results", "{}/{}_{}_{}_branching_results/branching_{}_{}_{}_{}.csv".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
                        IJ.run("Clear Results")

for i in analysis_params:
    particle_analysis(i)
