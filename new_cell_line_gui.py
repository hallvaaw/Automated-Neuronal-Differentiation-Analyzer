#!/usr/bin/python3

import tkinter as tk

class NewCellParameters:

    thresholds = {"MaxEntropy", "IsoData", "Yen", "Otsu", "Li", "MinError(I)", "Huang", "Huang2", "Intermodes", "Mean", "Minimum", "Moments", "Percentile", "RenylEntropy", "Shanbhag", "NO THRESHOLD"}

    def __init__(self, wndw):
        self.wndw = tk.Frame(wndw)
        wndw.title("Choose analysis parameters")
        self.wndw.grid(column=0,row=0)
        self.wndw.columnconfigure(0, weight = 1)
        self.wndw.rowconfigure(0, weight = 1)
        self.wndw.pack()

        self.no_command = tk.Button(self.wndw, text = "If no, press this button to continue", command = lambda : (self.btn_no()))
        self.no_command.grid(row = 0, column = 1)
        tk.Label(self.wndw, text = "Adding new cell line?").grid(row = 0, column = 0)

        self.entry_cell_line_text = tk.StringVar(self.wndw)
        self.entry_cell = tk.Entry(self.wndw)
        self.entry_cell.grid(row = 1, column = 1, columnspan = 1)
        tk.Label(self.wndw, text = "Name of new cell line                      ").grid(row = 1, column = 0)

        self.entry_min_cell_s_text = tk.StringVar(self.wndw)
        self.entry_min_cell_s = tk.Entry(self.wndw)
        self.entry_min_cell_s.grid(row = 2, column = 1, columnspan = 1)
        tk.Label(self.wndw, text = "Set minimum size of cell in                ").grid(row = 2, column = 0)

        self.entry_max_cell_s_text = tk.StringVar(self.wndw)
        self.entry_max_cell_s = tk.Entry(self.wndw)
        self.entry_max_cell_s.grid(row = 3, column = 1, columnspan = 1)
        tk.Label(self.wndw, text = "Set maximum size of cell in                ").grid(row = 3, column = 0)

        self.entry_min_cell_c_text = tk.StringVar(self.wndw)
        self.entry_min_cell_c = tk.Entry(self.wndw)
        self.entry_min_cell_c.grid(row = 4, column = 1, columnspan = 1)
        tk.Label(self.wndw, text = "Set minimum cell circularity (min. 0.00)   ").grid(row = 4, column = 0)

        self.entry_max_cell_c_text = tk.StringVar(self.wndw)
        self.entry_max_cell_c = tk.Entry(self.wndw)
        self.entry_max_cell_c.grid(row = 5, column = 1, columnspan = 1)
        tk.Label(self.wndw, text = "Set maximum cell circularity (max. 1.00)   ").grid(row = 5, column = 0)

        self.entry_min_neurite_s_text = tk.StringVar(self.wndw)
        self.entry_min_neurite_s = tk.Entry(self.wndw)
        self.entry_min_neurite_s.grid(row = 6, column = 1, columnspan = 1)
        tk.Label(self.wndw, text = "Set minimum length of neurite              ").grid(row = 6, column = 0)

        self.entry_max_neurite_s_text = tk.StringVar(self.wndw)
        self.entry_max_neurite_s = tk.Entry(self.wndw)
        self.entry_max_neurite_s.grid(row = 7, column = 1, columnspan = 1)
        tk.Label(self.wndw, text = "Set maximum length of neurite              ").grid(row = 7, column = 0)

        self.entry_min_neurite_c_text = tk.StringVar(self.wndw)
        self.entry_min_neurite_c = tk.Entry(self.wndw)
        self.entry_min_neurite_c.grid(row = 8, column = 1, columnspan = 1)
        tk.Label(self.wndw, text = "Set minimum neurite circularity (min. 0.00)").grid(row = 8, column = 0)

        self.entry_max_neurite_c_text = tk.StringVar(self.wndw)
        self.entry_max_neurite_c = tk.Entry(self.wndw)
        self.entry_max_neurite_c.grid(row = 9, column = 1, columnspan = 1)
        tk.Label(self.wndw, text = "Set maximum neurite circularity (max. 1.00)").grid(row = 9, column = 0)

        self.entry_cell_threshold_text = tk.StringVar(wndw)
        self.entry_cell_threshold_text.set('Choose threshold')
        self.entry_cell_threshold = tk.OptionMenu(self.wndw, self.entry_cell_threshold_text, *self.thresholds)
        self.entry_cell_threshold.grid(row = 10, column = 1, columnspan = 1)
        tk.Label(self.wndw, text = "Set cell thresholding method         ").grid(row = 10, column = 0)

        self.entry_neurite_threshold_text = tk.StringVar(wndw)
        self.entry_neurite_threshold_text.set('Choose threshold')
        self.entry_neurite_threshold = tk.OptionMenu(self.wndw, self.entry_neurite_threshold_text, *self.thresholds)
        self.entry_neurite_threshold.grid(row = 11, column = 1, columnspan = 1)
        tk.Label(self.wndw, text = "Set neurite thresholding method      ").grid(row = 11, column = 0)

        self.submit = tk.Button(self.wndw, text = "Submit and continue", command = lambda : (self.btn_submit()))
        self.submit.grid(row = 15, column = 0)


        self.scale_text = tk.StringVar(self.wndw)
        self.scale = tk.Entry(self.wndw)
        self.scale.grid(row = 14, column = 1, columnspan = 1)
        tk.Label(self.wndw, text = "Set metric scale in pixels/µm        ").grid(row = 13, column = 0)
        tk.Label(self.wndw, text = "If measuring in pixels, type 0       ").grid(row = 14, column = 0)


    def btn_no(self):
        self.wndw.quit()

    def getCellLine(self):
        return self.entry_cell.get()

    def btn_submit(self):
        self.wndw.quit()
        return (self.entry_cell.get(), self.entry_min_cell_s.get(), self.entry_max_cell_s.get(), self.entry_min_cell_c.get(), self.entry_max_cell_c.get(), self.entry_min_neurite_s.get(), self.entry_max_neurite_s.get(), self.entry_min_neurite_c.get(), self.entry_max_neurite_c.get(), self.entry_cell_threshold_text.get(), self.entry_neurite_threshold_text.get(), self.scale.get())

root = tk.Tk()
newcell = NewCellParameters(root)
root.mainloop()

if "Choose threshold" not in newcell.btn_submit():
    f = open('new_cell_parameters.txt', 'w')
    for i in newcell.btn_submit():
        f.write(i+'\n')
    f.close()
