#!/usr/bin/python3

import tkinter as tk
from tkinter import filedialog

class PipelineStart:

    cell_lines = 'CGN;NT2N;SH-SY5Y;'
    cell_lines_set = set(cell_lines.split(";"))
    plate_sizes = ('6', '12', '24', '48', '96')
    chars = ("A", "B", "C", "D", "E", "F", "G", "H", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    rows = chars[0:8]
    well_rows = (('A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10', 'A11', 'A12'),('B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09', 'B10', 'B11', 'B12'),('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08', 'C09', 'C10', 'C11', 'C12'),('D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09', 'D10', 'D11', 'D12'),('E01', 'E02', 'E03', 'E04', 'E05', 'E06', 'E07', 'E08', 'E09', 'E10', 'E11', 'E12'),('F01', 'F02', 'F03', 'F04', 'F05', 'F06','F07','F08',   'F09', 'F10', 'F11', 'F12'),('G01', 'G02', 'G03', 'G04', 'G05', 'G06', 'G07', 'G08', 'G09', 'G10', 'G11', 'G12'),('H01', 'H02', 'H03', 'H04', 'H05', 'H06', 'H07', 'H08', 'H09', 'H10', 'H11', 'H12'))
    well_columns = (('A01', 'B01', 'C01', 'D01', 'E01', 'F01', 'G01', 'H01'),('A02', 'B02', 'C02', 'D02', 'E02', 'F02', 'G02', 'H02'),('A03', 'B03', 'C03', 'D03', 'E03', 'F03', 'G03', 'H03'),('A04', 'B04', 'C04', 'D04', 'E04', 'F04', 'G04', 'H04'),('A05', 'B05', 'C05', 'D05', 'E05', 'F05', 'G05', 'H05'),('A06', 'B06', 'C06', 'D06', 'E06', 'F06', 'G06', 'H06'),('A07', 'B07', 'C07', 'D07', 'E07', 'F07', 'G07', 'H07'),('A08', 'B08', 'C08', 'D08', 'E08', 'F08', 'G08', 'H08'),('A09','B09','C09', 'D09', 'E09', 'F09', 'G09', 'H09'),('A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10'),('A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11'),('A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12'))
    wells_ = ("A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08", "A09", "A10", "A11", "A12", "B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B09", "B10", "B11", "B12", "C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12", "D01", "D02", "D03", "D04", "D05", "D06", "D07", "D08", "D09", "D10", "D11", "D12", "E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "F01", "F02", "F03", "F04", "F05", "F06", "F07", "F08", "F09", "F10", "F11", "F12", "G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08", "G09", "G10", "G11", "G12", "H01", "H02", "H03", "H04", "H05", "H06", "H07", "H08", "H09", "H10", "H11", "H12")
    wells_short = ("A1 ", "A2 ", "A3 ", "A4 ", "A5 ", "A6 ", "A7 ", "A8 ", "A9 ", "A10", "A11", "A12", "B1 ", "B2 ", "B3 ", "B4 ", "B5 ", "B6 ", "B7 ", "B8 ", "B9 ", "B10", "B11", "B12", "C1 ", "C2 ", "C3 ", "C4 ", "C5 ", "C6 ", "C7 ", "C8 ", "C9 ", "C10", "C11", "C12", "D1 ", "D2 ", "D3 ", "D4 ", "D5 ", "D6 ", "D7 ", "D8 ", "D9 ", "D10", "D11", "D12", "E1 ", "E2 ", "E3 ", "E4 ", "E5 ", "E6 ", "E7 ", "E8 ", "E9 ", "E10", "E11", "E12", "F1 ", "F2 ", "F3 ", "F4 ", "F5 ", "F6 ", "F7 ", "F8 ", "F9 ", "F10", "F11", "F12", "G1 ", "G2 ", "G3 ", "G4 ", "G5 ", "G6 ", "G7 ", "G8 ", "G9 ", "G10", "G11", "G12", "H1 ", "H2 ", "H3 ", "H4 ", "H5 ", "H6 ", "H7 ", "H8 ", "H9 ", "H10", "H11", "H12")
    labels = []
    row_btn = []
    col_btn = []
    all_btn = []

    def __init__(self, wndw):

        self.wndw = tk.Frame(wndw)
        wndw.title("Set parameters")
        self.wndw.grid(column=0,row=0)
        self.wndw.columnconfigure(0, weight = 1)
        self.wndw.rowconfigure(0, weight = 1)
        self.wndw.pack()
        self.y = ""

        self.files_dir_button = tk.Button(self.wndw, text = "Select a image directory          ", borderwidth = 2, command = lambda : (self.get_files_dir()))
        self.files_dir_button.grid(row = 0, column = 0)

        self.reference_button = tk.Button(self.wndw, text = "Select registration reference file", borderwidth = 2, command = lambda : (self.get_registration_reference()))
        self.reference_button.grid(row = 1, column = 0)

        self.imagej_button = tk.Button(self.wndw, text = "Full path to ImageJ directory     ", borderwidth = 2, command = lambda : (self.get_imagej_path()))
        self.imagej_button.grid(row = 2, column = 0)


        self.entry_prefix_text = tk.StringVar(self.wndw)
        self.entry_prefix = tk.Entry(self.wndw) # Common file prefix
        self.entry_prefix.grid(row = 3, column = 1, columnspan = 1)
        tk.Label(self.wndw, text="Common file name prefix           ").grid(row = 3, column = 0)

        self.image_locations_text = tk.StringVar(self.wndw)
        self.image_locations = tk.Entry(self.wndw) # NO. image tiles per well
        self.image_locations.grid(row = 4, column = 1, columnspan = 1)
        tk.Label(self.wndw, text="Number of image tiles per well    ").grid(row = 4, column = 0)

        self.ar_threshold_text = tk.StringVar(self.wndw)
        self.ar_threshold = tk.Entry(self.wndw)
        self.ar_threshold.grid(row = 5, column = 1, columnspan = 1)
        tk.Label(self.wndw, text = "Set neurite aspect ratio threshold").grid(row = 5, column = 0)

        self.cell_line = tk.StringVar(wndw)
        self.cell_line.set('CGN')

        self.choice_cell_line = tk.OptionMenu(self.wndw, self.cell_line, *self.cell_lines_set)

        self.choice_cell_line.grid(row = 5, column = 2)
        tk.Label(self.wndw, text = "Choose cell line").grid(row = 4, column = 2)


        self.submit_button = tk.Button(self.wndw, text = "Submit and continue", cursor = "hand1", borderwidth = 2, command = self.return_all)
        self.submit_button.grid(row = 10, column = 2)

        self.params_list = []
        self.params_str = ""
        tk.Label(self.wndw, text = "Select analysis metrics").grid(row = 7, column = 0)
        self.neurites = tk.Button(master = self.wndw, text = "Neurite lengths          ", borderwidth = 2, command = lambda : (self.btn_neurites()))
        self.neurites.grid(row = 8, column = 0)

        self.cells = tk.Button(master = self.wndw, text = "Cell body count          ", borderwidth = 2, command = lambda : (self.btn_cells()))
        self.cells.grid(row = 9, column = 0)

        self.branching = tk.Button(master = self.wndw, text = "Neurite branching points ", borderwidth = 2, command = lambda : (self.btn_branching()))
        self.branching.grid(row = 10, column = 0)

        self.clear = tk.Button(master = self.wndw, text = "Clear metrics selection  ", borderwidth = 2, command = lambda : (self.btn_clear()))
        self.clear.grid(row = 11, column = 0)

        self.os_choice = ""
        tk.Label(self.wndw, text = "Select OS").grid(row = 8, column = 1)
        self.windows_button = tk.Button(master = self.wndw, text = "Windows", borderwidth = 2, command = lambda : (self.btn_windows()))
        self.windows_button.grid(row = 9, column = 1)
        self.linux_button = tk.Button(master = self.wndw, text = " Linux ", borderwidth = 2, command = lambda : (self.btn_linux()))
        self.linux_button.grid(row = 10, column = 1)
        self.mac_button = tk.Button(master = self.wndw, text = "  Mac  ", borderwidth = 2, command = lambda : (self.btn_mac()))
        self.mac_button.grid(row = 11, column = 1)

        self.show_outlines = "no"
        self.show_outlines_button = tk.Button(master = self.wndw, text = "Save motif outlines", borderwidth = 2, command = lambda : (self.btn_save_outlines()))
        self.show_outlines_button.grid(row = 9, column = 2)

        self.register_choice = "no"
        self.register_button = tk.Button(master = self.wndw, text = "Register images", borderwidth = 2, command = lambda : (self.btn_register()))
        self.register_button.grid(row = 8, column = 2)

        self.wells_list = []
        self.wells_str = ""
        self.wells_list_sorted = []
        self.wells_str_sorted = ""
        self.wells_array = ""

        self.input_frame = tk.Frame(master = self.wndw, width = 0, height = 0, bd = 80)
        self.frame = tk.Frame(master = self.input_frame, relief = tk.RAISED, borderwidth = 2)
        self.frame.grid(row = 2, column = 2)

        for row in range(1, 9):
            for column in range(1, 13):
                if column <= 9:
                    well_name = self.rows[row-2]+"0"+str(column)
                else:
                    well_name = self.rows[row-2]+str(column)
                tk.Label(self.wndw, text = column).grid(row = 2, column = column+3)
                well = len(self.labels)
                self.labels.append(tk.Button(
                    master = self.wndw,
                    text = self.wells_short[well],
                    state = tk.NORMAL,
                    command = lambda well = well: (self.btn_click(self.wells_[well]), self.disable(well))))
                self.labels[well].grid(row = row+2, column = column+3)


            self.wndw.grid(row = row+2, column = column+3)

        self.clear_wells = tk.Button(master = self.wndw, text = "Clear well selection", borderwidth = 2, command = lambda well = well: self.btn_clear_wells(well))
        self.clear_wells.grid(row = 2, column = 2)

        self.all = tk.Button(master = self.wndw, text = "  Select all wells  ", borderwidth = 2, command = lambda well = well: (self.btn_all(well)))
        self.all.grid(row = 1, column = 2)

    def btn_save_outlines(self):
        self.show_outlines = "yes"
        self.show_outlines_button.configure(state=tk.DISABLED)
        return self.show_outlines

    def btn_register(self):
        self.register_choice = "yes"
        self.register_button.configure(state=tk.DISABLED)
        return self.register_choice

    def btn_windows(self):
        self.os_choice = "windows"
        self.windows_button.configure(state=tk.DISABLED)
        self.mac_button.configure(state=tk.DISABLED)
        self.linux_button.configure(state=tk.DISABLED)
        return self.os_choice

    def btn_linux(self):
        self.os_choice = "linux"
        self.linux_button.configure(state=tk.DISABLED)
        self.mac_button.configure(state=tk.DISABLED)
        self.windows_button.configure(state=tk.DISABLED)
        return self.os_choice

    def btn_mac(self):
        self.os_choice = "mac"
        self.mac_button.configure(state=tk.DISABLED)
        self.linux_button.configure(state=tk.DISABLED)
        self.windows_button.configure(state=tk.DISABLED)
        return self.os_choice

    def get_files_dir(self):
        self.files_dir = tk.filedialog.askdirectory()
        self.files_dir_button.configure(state=tk.DISABLED)
        return self.files_dir

    def get_registration_reference(self):
        self.registration_reference = tk.filedialog.askopenfilename()
        self.reference_button.configure(state=tk.DISABLED)
        return self.registration_reference

    def get_imagej_path(self):
        self.imagej_path = tk.filedialog.askdirectory()
        self.imagej_button.configure(state=tk.DISABLED)
        return self.imagej_path

    def btn_click(self, item):
        self.wells_list.append(str(item))
        return self.wells_list

    def btn_clear_wells(self, x):
        self.wells_array = ""
        self.wells_list.clear()
        self.wells_str = ""
        self.wells_list_sorted.clear()
        self.wells_str_sorted = ""
        for i in range(len(self.labels)):
            self.labels[i].configure(state=tk.NORMAL)
        return self.wells_list

    def disable(self, x):
        self.labels[x].configure(state=tk.DISABLED)

    def btn_all(self, x):
        for i in range(len(self.labels)):
            self.labels[i].configure(state=tk.DISABLED)
            self.btn_click(self.wells_[i])

    def return_cell_line(self):
        return str(self.cell_line.get())

    def return_sorted_wells_list(self):

        for i in str(self.wells_list):
            if i in self.chars:
                self.wells_str += i
        for i in range(0, len(self.wells_str), 3):
            self.wells_list_sorted.append(self.wells_str[i:i+3])
        self.wells_list_sorted = str(sorted(set(self.wells_list_sorted)))
        for i in self.wells_list_sorted:
            if i in self.chars:
                self.wells_str_sorted += i
        for i in range(0, len(self.wells_str_sorted), 3):
            pre = self.wells_str_sorted[i:i+3]
            if pre[1] == "0":
                self.wells_array += pre[0]+pre[2]+" "
            else:
                self.wells_array += pre + " "
        return self.wells_array

    def return_wells_compact(self):
        self.wells_compact = self.wells_array.replace(" ", ";")
        return self.wells_compact

    def btn_neurites(self):
        self.params_list.append("neurites")
        self.neurites.configure(state=tk.DISABLED)
        return self.params_list

    def btn_cells(self):
        self.params_list.append("cells")
        self.cells.configure(state=tk.DISABLED)
        return self.params_list

    def btn_branching(self):
        self.params_list.append("branching")
        self.branching.configure(state=tk.DISABLED)
        return self.params_list

    def disable(self, x):
        self.labels[x].configure(state=tk.DISABLED)

    def btn_clear(self):
        self.functions_list = [self.neurites, self.cells, self.branching]
        self.params_list.clear()
        for i in range(len(self.functions_list)):
            self.functions_list[i].configure(state=tk.NORMAL)
        return self.params_list

    def return_params_list(self):
        return self.params_list

    def return_params_str(self):
        for i in self.params_list:
            self.params_str += i+" "
        return self.params_str

    def return_params_compact(self):
        self.params_compact = self.params_str.replace(" ", ";")
        return self.params_compact

    def return_all(self):
        (self.prefix, self.image_loc, self.ar_threshold) = (self.entry_prefix.get(), self.image_locations.get(), self.ar_threshold.get())
        self.return_params_str()
        self.return_sorted_wells_list()
        self.return_wells_compact()
        self.return_params_compact()
        self.wndw.quit()
        return (self.files_dir, self.registration_reference, self.imagej_path, self.prefix, self.image_loc, self.ar_threshold, self.params_str, self.os_choice, self.wells_array, str(self.cell_line.get()), self.wells_compact, self.params_compact)

    def return_output_list(self):
        self.output_list = [i for i in (self.files_dir, self.registration_reference, self.imagej_path, self.prefix, self.image_loc, self.params_str, self.os_choice, self.wells_array, str(self.cell_line.get()), self.show_outlines, self.register_choice, self.wells_compact, self.params_compact, self.ar_threshold)]
        return self.output_list


root = tk.Tk()
pipe_start = PipelineStart(root)
root.mainloop()
f = open('pipeline_parameters.txt', 'w')
for i in pipe_start.return_output_list():
    f.write(i+'\n')
f.close()
