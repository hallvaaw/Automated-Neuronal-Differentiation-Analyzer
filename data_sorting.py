#!/usr/bin/python3

import numpy as np
import pandas as pd
import sys
from datetime import datetime

params_compact = sys.argv[1]
analysis_params = params_compact.split(";")
analysis_params = analysis_params[0:-1]
wells_compact = sys.argv[2]
wells_list = wells_compact.split(";")
wells_list = wells_list[0:-1]
file_prefix = sys.argv[3]
file_prefix = str(file_prefix)
image_dir = sys.argv[4]
image_dir = str(image_dir)
fields = int(sys.argv[5]) + 1
ar_thresh = float(sys.argv[6])

file_names = open('file_names.txt', 'r')
file_list = file_names.readlines()
file_names.close()
extension_list = [i.rstrip() for i in file_list]

def dataframe_particle_analysis(analysis):
    num_count = []
    well_ = []
    slice_ = []
    tile = []
    length = []
    ar_removals = []

    if analysis == "neurites":
        for well in wells_list:
            for field in range(1, fields):
                for ext in extension_list:
                    try:
                        data = pd.read_csv(f"{image_dir}/{file_prefix}_{well}_{field}_neurites_results/neurite_{file_prefix}_{well}_{field}_{ext[-22:]}.csv")
                        if ar_thresh > 0:
                            data_2 = data[data["AR"] > ar_thresh]
                            mean_major = np.mean(data_2["Major"])
                            ar_removals.append(len(data) - len(data_2))
                        else:
                            mean_major = np.mean(data["Major"])
                            ar_removals.append(0)
                        count = len(data["Area"])
                        num_count.append(count)
                        length.append(mean_major)
                        tile.append(field)
                        well_.append(f"{well}")

                    except FileNotFoundError:
                        print(f"File {image_dir}/{file_prefix}_{well}_{field}_neurites_results/neurite_{file_prefix}_{well}_{field}_{ext[-22:]}.csv not found")
                        ar_removals.append(0)
                        count = 0
                        num_count.append(count)
                        length.append(0)
                        tile.append(field)
                        well_.append(f"{well}")


                d = {'Count': num_count,
                    'Mean_length': length,
                    'Well': well_,
                    'Tile': tile,
                    'False positives': ar_removals
                    }
                df = pd.DataFrame(data = d)
                df.to_csv(f"{image_dir}/{datetime.today().strftime('%Y-%m-%d')}results_neurites.csv")

    elif analysis == "cells":
        for well in wells_list:
            for field in range(1, fields):
                for ext in extension_list:
                    try:
                        data = pd.read_csv(f"{image_dir}/{file_prefix}_{well}_{field}_cells_results/cells_{file_prefix}_{well}_{field}_{ext[-22:]}.csv")
                        count = len(data["Area"])
                        num_count.append(count)
                        well_.append(f"{well}")
                        tile.append(field)

                    except FileNotFoundError:
                        print(f"File {image_dir}/{file_prefix}_{well}_{field}_cells_results/cells_{file_prefix}_{well}_{field}_{ext[-22:]}.csv not found")
                        count = 0
                        num_count.append(count)
                        tile.append(field)
                        well_.append(f"{well}")

                d = {'Count': num_count,
                    'Well': well_,
                    'Tile': tile}
                df = pd.DataFrame(data = d)
                df.to_csv(f"{image_dir}/{datetime.today().strftime('%Y-%m-%d')}results_cells.csv")

    elif analysis == "branching":
        for well in wells_list:
            for field in range(1, fields):
                for ext in extension_list:
                    try:
                        data = pd.read_csv(f"{image_dir}/{file_prefix}_{well}_{field}_branching_results/branching_{file_prefix}_{well}_{field}_{ext[-22:]}.csv")
                        count = len(data["Area"])
                        num_count.append(count)
                        well_.append(f"{well}")
                        tile.append(field)

                    except FileNotFoundError:
                        print(f"File {image_dir}/{file_prefix}_{well}_{field}_branching_results/branching_{file_prefix}_{well}_{field}_{ext[-22:]}.csv not found")
                        count = 0
                        num_count.append(count)
                        tile.append(field)
                        well_.append(f"{well}")

                d = {'Count': num_count,
                    'Well': well_,
                    'Tile': tile}
                df = pd.DataFrame(data = d)
                df.to_csv(f"{image_dir}/{datetime.today().strftime('%Y-%m-%d')}results_branching.csv")

for i in analysis_params:
    dataframe_particle_analysis(i)
