# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:04:04 2022

@author: doeringe
"""
from tkinter import *
import tkinter.font as font


class SearchMask(Tk):
    def makeSelection(self):
        """
        Open pages to indicate search criteria.

        Returns
        -------
        None.

        """
        try:
            nGroups = int(self.numberOfGroups.get())
            pages = 0
            while pages < nGroups:
                select = self.followingPages()
                self.final_groups.append(select[0])
                self.final_sex.append(select[1])
                self.final_data.append(select[2])
                self.stores.append(select[3])
                pages += 1
            # return final_groups, final_sex, final_data, storage

        except ValueError:
            print("error")

    def label_window(self, window):
        """
        Configure and label each search window.

        Parameters
        ----------
        window : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        window.title("T-POT Search")
        window.geometry("700x900")
        # self.backgroundImage = PhotoImage(
        #    file="Documents\\T-POT\\Scripts\\bg_uk_res.png")
        #backgroundImage_Label = Label(window, image=self.backgroundImage)
        #backgroundImage_Label.place(x=0, y=50)
        heading = Label(window, text="T-POT Image Search", font=("Helvetica",
                                                                 20, "bold"),
                        pady=20, fg="black")
        heading.pack

    def make_checkboxes(self, var_, var_name, selection, window):
        """
        Create selection.

        Parameters
        ----------
        var_ : list
            list of variable values for selection
        var_name : str
            Name of variable for selection
        selection : dict
            Definition of default values for each entry in var_
        window : Tk root or Toplevel instance
            Window to show checkboxes in

        Returns
        -------
        selection : Tkinter IntVar
            Variable containing binary user selection

        """
        group_label = Label(window, text=var_name, font=("bold", 14),
                            pady=20)
        group_label.pack()

        for v in var_:
            selection[v] = IntVar()
            select = Checkbutton(window, text=v, variable=selection[v],
                                 onvalue=1, offvalue=0)
            select.pack()

        return selection

    def followingPages(self):
        """
        Create and fill pages after landing page.

        Returns
        -------
        selected_group : IntVar
            Binary selection for group
        selected_sex : IntVar
            Binary selection for sex
        selected_data : IntVar
            Binary selection for data
        storage_text : str
            Where to store the data. Path can be relative (from working
            directory) or absolute.

        """

        newWindow = Toplevel(self)
        self.label_window(newWindow)
        # newWindow.show()
        # close old one
        # window.withdraw()
        group_label = Label(newWindow,
                            text="Select one or more options. If more than" +
                                 " one imaging modality is selected, data will" +
                                 " be stored per subject.",
                            pady=10)
        group_label.pack()
        group = ["CN", "SCD", "MCI", "AD"]
        sex = ["Female", "Male"]
        data = ["PET - PIB Static", "PET - AV1451 Static",
                "PET - PIB Dynamic", "PET - AV1451 Dynamic",
                "MRI - MPRAGE (T1)", "MRI - T2", "MRI - diffusion",
                "fMRI - encoding", "fMRI - retrieval", "fMRI - resting"]
        selection_group = {i: 0 for i in group}
        selection_sex = {j: 0 for j in sex}
        selection_data = {h: 0 for h in data}

        # TODO if nothing is selected
        selected_group = self.make_checkboxes(group, "Group",
                                              selection_group, newWindow)
        selected_sex = self.make_checkboxes(sex, "Sex",
                                            selection_sex, newWindow)
        selected_data = self.make_checkboxes(data, "Data",
                                             selection_data, newWindow)
        storage_label = Label(newWindow,
                              text="Where should data be stored",
                              font=("bold", 14), pady=20)

        storage_label.pack()
        storage_text = StringVar()
        storage = Entry(newWindow, textvariable=storage_text)
        storage.pack()

        ok = Button(newWindow, text="Next", command=newWindow.destroy)
        ok.pack()
        return selected_group, selected_sex, selected_data, storage_text

    def __init__(self):
        Tk.__init__(self)

        self.final_groups = []
        self.final_sex = []
        self.final_data = []
        self.stores = []
        # self.label_window(self)
        self.title("T-POT Search")
        self.geometry("1400x900")
        self.backgroundImage = PhotoImage(
            file="Documents\\T-POT\\Scripts\\bg_uk_res.png")
        backgroundImage_Label = Label(self, image=self.backgroundImage)
        backgroundImage_Label.place(x=0, y=50)
        heading = Label(self, text="T-POT Image Search", font=("Helvetica",
                                                               20, "bold"),
                        pady=20, bg="white", fg="black")
        heading.place(x=700, y=140, anchor=CENTER)
        numberOfGroups_label = Label(self,
                                     text="How many groups do you want to create?",
                                     font=("bold", 14), fg="white", pady=10,
                                     bg='steelblue')
        numberOfGroups_label.place(relx=0.5, rely=0.4, anchor=CENTER)
        # self.wm_attributes("-transparentcolor", 'grey')
        numberOfGroups_text = StringVar()
        numberOfGroups = Entry(self, textvariable=numberOfGroups_text)
        numberOfGroups.place(relx=0.5, rely=0.45, anchor=CENTER,
                             width=300, height=30)
        self.numberOfGroups = numberOfGroups

        ok = Button(self, text="Next", command=self.makeSelection)
        ok['font'] = font.Font(size=12)
        ok.place(relx=0.5, rely=0.55, anchor=CENTER)

        ok2 = Button(self, text="I'm done", command=self.destroy)
        ok2.place(relx=0.5, rely=0.6, anchor=CENTER)
        ok2['font'] = font.Font(size=12)


def getSelection(final_selection, selection_name):
    """


    Parameters
    ----------
    final_selection : TYPE
        DESCRIPTION.
    selection_name : str
        Name of variable of interest

    Returns
    -------
    None.

    """
    for i in range(len(final_selection)):
        for j in final_selection[i].keys():
            final_selection[i][j] = final_selection[i][j].get()
        if all(value == 0 for value in final_selection[i].values()):
            raise ValueError("No selection made for \"" + selection_name +
                             "\" in group " + str(i+1) + ". Please restart program.")
