
# @String input_wells
# @String image_dir
# @String target_dir
# @String transf_dir
# @String ref_name
# @String file_prefix
# @String input_tiles
# @int featuresModelIndex
# @int registrationModelIndex
# @boolean use_shrinking_constraint






##### Register Virtual Stack Slices headless mode
##### Run the code in a terminal without user input to register the images

wells_list = input_wells.split(" ") # Changes the input array to a list
wells_list = wells_list[0:-1]

print("ANALYZING IMAGES FROM WELLS ", wells_list)
tiles = int(input_tiles) + 1


file_names = open('file_names.txt', 'r')
file_list = file_names.readlines()
file_names.close()
suffix_list = [str(i.rstrip()) for i in file_list]


print("REGISTERING IMAGES FROM WELLS {}".format(wells_list))
from ij import IJ
from register_virtual_stack import Register_Virtual_Stack_MT

for well in wells_list:
    for tile in range(1, tiles):
        for ext in suffix_list:
            IJ.open("{}/{}_{}_{}/{}_{}_{}_{}".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))
            IJ.run("8-bit")
            IJ.run("Auto Threshold", "method=IsoData")
            IJ.run("Watershed")
            IJ.saveAs("Tiff", "{}/{}_{}_{}_segmented/{}_{}_{}_{}".format(image_dir, file_prefix, well, tile, file_prefix, well, tile, ext[-22:]))



p = Register_Virtual_Stack_MT.Param()


# Standard parameters

p.sift.initialSigma = 1.60
p.sift.steps = 3
p.sift.minOctaveSize = 64
p.sift.maxOctaveSize = 10240 # Default is 1024

p.sift.fdSize = 8
p.sift.fdBins = 8
p.rod = 0.95 # Default is 0.92

p.maxEpsilon = 25.00
p.minInlierRatio = 0.05

p.featuresModelIndex = 0 # 0 = Translation
p.registrationModelIndex = 0 # 0 = Translation


for well in wells_list:
    for tile in range(1, tiles):
        source_dir = "{}/{}_{}_{}/".format(image_dir, file_prefix, well, tile)
        target_dir = "{}/{}_{}_{}_output/".format(image_dir, file_prefix, well, tile) # Target directory is where the stacked images end up
        transf_dir = "{}/{}_{}_{}_transform/".format(image_dir, file_prefix, well, tile) # Image transforms are XML files
        reference_name = "{}_{}_{}_{}".format(file_prefix, well, tile, ref_name[-22:]) # The first image in a time series
        print("REGISTERING: {}_{}_{}".format(file_prefix, well, tile))
        Register_Virtual_Stack_MT.exec(source_dir, target_dir, transf_dir, reference_name, p, use_shrinking_constraint)

