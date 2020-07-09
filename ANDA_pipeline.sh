#!/bin/bash

scripts_dir=$(pwd) # Directory with scripts
python3 ${scripts_dir}/new_cell_line_gui.py &&
new_cell_line=$(awk 'FNR == 1 {print}' ${scripts_dir}/new_cell_parameters.txt)
if [[ ${new_cell_line} != "" ]]; then
 sed -e "8s/;/&${new_cell_line};/" 96_well.py > 96_well_v2.py
 mv 96_well_v2.py 96_well.py
 mv new_cell_parameters.txt ${new_cell_line}_parameters.txt
fi
python3 ${scripts_dir}/96_well.py
dir_name=$(awk 'FNR == 1 {print}' ${scripts_dir}/pipeline_parameters.txt)
reference_image=$(awk 'FNR == 2 {print}' ${scripts_dir}/pipeline_parameters.txt)
imagej_path=$(awk 'FNR == 3 {print}' ${scripts_dir}/pipeline_parameters.txt)
prefix=$(awk 'FNR == 4 {print}' ${scripts_dir}/pipeline_parameters.txt)
image_tiles=$(awk 'FNR == 5 {print}' ${scripts_dir}/pipeline_parameters.txt)
params=$(awk 'FNR == 6 {print}' ${scripts_dir}/pipeline_parameters.txt)
os=$(awk 'FNR == 7 {print}' ${scripts_dir}/pipeline_parameters.txt)
well_names=$(awk 'FNR == 8 {print}' ${scripts_dir}/pipeline_parameters.txt)
well=$(awk 'FNR == 8 {print $1}' ${scripts_dir}/pipeline_parameters.txt)
cell_line=$(awk 'FNR == 9 {print}' ${scripts_dir}/pipeline_parameters.txt)
outlines_=$(awk 'FNR == 10 {print}' ${scripts_dir}/pipeline_parameters.txt)
registration=$(awk 'FNR == 11 {print}' ${scripts_dir}/pipeline_parameters.txt)
wells_compact=$(awk 'FNR == 12 {print}' ${scripts_dir}/pipeline_parameters.txt)
params_compact=$(awk 'FNR == 13 {print}' ${scripts_dir}/pipeline_parameters.txt)
ar_threshold=$(awk 'FNR == 14 {print}' ${scripts_dir}/pipeline_parameters.txt)
cp -v ${cell_line}_parameters.txt ${dir_name}/${cell_line}_parameters.txt


cd $dir_name # Folder with images to be analyzed
ls ${dir_name}/${prefix}_${well}_1/ | grep tif > file_names.txt
folder_extensions=(transform output branching cells neurites segmented)
for well in $well_names
do
  for((i=1;i<=$image_tiles; i++));
  do
    for ext in {0..5};
    do
      mkdir ${prefix}_${well}_${i}_${folder_extensions[$ext]}
    done
  done
done
# Image registration with ImageJ
if [[ $registration == "yes" ]]; then
  if [[ $os == "linux" ]]; then
    ${imagej_path}/ImageJ-linux64 --ij2 --headless --run ${scripts_dir}/stack_register.py "input_wells='${well_names}', image_dir='$dir_name', ref_name='$reference_image', file_prefix='$prefix', input_tiles='$image_tiles'"
  elif [[ $os == "windows" ]]; then
    ${imagej_path}\ImageJ-win64.exe --ij2 --headless --run ${scripts_dir}/stack_register.py "input_wells='${well_names}', image_dir='$dir_name', ref_name='$reference_image', file_prefix='$prefix', input_tiles='$image_tiles'"
  elif [[ $os == "mac" ]]; then
    ${imagej_path}\ImageJ-macosx --ij2 --headless --run ${scripts_dir}/stack_register.py "input_wells='${well_names}', image_dir='$dir_name', ref_name='$reference_image', file_prefix='$prefix', input_tiles='$image_tiles'"
  fi
fi
for well in $well_names
do
  for((i=1;i<=$image_tiles; i++));
  do
    for ext in {2..4};
    do
      mkdir ${prefix}_${well}_${i}_${folder_extensions[$ext]}_results
    done
  done
done
# Image analysis
if [[ $os == "linux" ]]; then
  ${imagej_path}/ImageJ-linux64 --ij2 --headless --run ${scripts_dir}/cell_metrics.py "input_wells='${well_names}', input_analysis='${params}', image_dir='${dir_name}', file_prefix='${prefix}', input_tiles='${image_tiles}', cell_parameters='${cell_line}', outlines='${outlines_}', registration_input='${registration}'"

elif [[ $os == "windows" ]]; then
  ${imagej_path}\ImageJ-win64.exe --ij2 --headless --run ${scripts_dir}/cell_metrics.py "input_wells='${well_names}', input_analysis='${params}', image_dir='${dir_name}', file_prefix='${prefix}', input_tiles='${image_tiles}', cell_parameters='${cell_line}', outlines='${outlines_}', registration_input='${registration}'"

elif [[ $os == "mac" ]]; then
  ${imagej_path}\ImageJ-macosx --ij2 --headless --run ${scripts_dir}/cell_metrics.py "input_wells='${well_names}', input_analysis='${params}', image_dir='${dir_name}', file_prefix='${prefix}', input_tiles='${image_tiles}', cell_parameters='${cell_line}', outlines='${outlines_}', registration_input='${registration}'"

fi
python3 ${scripts_dir}/data_sorting.py $params_compact $wells_compact $prefix $dir_name $image_tiles $ar_threshold # Sorting data and returning human readable data
# find ${scripts_dir} -type d -empty -delete # Remove empty directories
