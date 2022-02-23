import time

import PySimpleGUI as sg
import os.path
import subprocess, filecmp , os
from shutil import copyfile










def ACTION(LAN,LOCAL):
    #       Does not require a order for path1/2
    def mostrecent(path1, path2, filename):
        if os.path.getctime(path1) > os.path.getctime(path2):
            copyfile((path1 + "\\" + filename), (path2 + "\\" + filename))
        else:
            copyfile((sort[i][2] + "\\" + sort[i][0]), (sort[i][1] + "\\" + sort[i][0]))




    try:
        l = []
        s = []
        server_path = (LAN)
        laptop_path = (LOCAL)  # Changed For safety
        path = [[laptop_path, l], [server_path, s]]


        # def Validation(path):

        for x in path:
            for root, dirs, files in os.walk(x[0]):
                for filename in files:
                    (x[1]).append([filename, root])
        sort = []

        ii = []
        jj = []

        for i in range(0, len(s)):
            for j in range(0, len(l)):
                beginl = (l[j][1].find(os.path.basename(os.path.normpath(LOCAL))))
                begins = (s[i][1].find(os.path.basename(os.path.normpath(LAN))))
                if (l[j][0]) == (s[i][0]) and ((l[j][1])[beginl:]) == ((s[i][1])[begins:]):
                    sort.append([l[j][0], l[j][1], s[i][1]])

                    ii.append(i)
                    jj.append(j)

        for x in reversed(ii):
            del s[x]

        for x in reversed(jj):
            del l[x]

        ## --------------------------Same Files --------------------------------
        for i in range(0, len(sort)):

            check = filecmp.cmp((sort[i][1] + "\\" + sort[i][0]), (sort[i][2] + "\\" + sort[i][0]))
            if check == False:
                print("Needs to be updated")
                mostrecent((sort[i][1]), (sort[i][2]), (sort[i][0]))


            else:
                check = True

        ## ----------------------------New File/Folder from computer --------------------------
        lsts = [l, s]
        print (lsts)

        for u in range(0, len(lsts)):
            x = lsts[u]
            if (x) == []:
                vData = ("empty")
            else:
                for i in range(0, len(x)):
                    tempin = x[i][1].find("Software Engineering")
                    num = (tempin) + 20
                    folder = ((((x[i][1])[num:]).split(os.sep))[1:])
                    empty = []
                    for w in range(0, len(folder)):
                        together = ("\\" + folder[w])
                        empty.append(together)

                    if "Z" in x[i][1]:
                        p = (laptop_path + ("".join(empty)))
                    else:
                        p = (server_path + ("".join(empty)))
                    if (os.path.exists(p)) == False:
                        for t in range(0, len(empty)):
                            folder2beremoved = "".join(empty[(t + 1):])
                            updated = p[:((len(p)) - (len(folder2beremoved)))]
                            if (os.path.exists(updated)) == False:
                                os.mkdir(updated)

                        copyfile((x[i][1] + "\\" + x[i][0]), (p + "\\" + x[i][0]))
                        print("             Dir & File doesnt exist\nDirectory created: {}\nFile copied: {}\n".format(p,(x[i][0])))
                    else:
                        copyfile((x[i][1] + "\\" + x[i][0]), (p + "\\" + x[i][0]))
                        print("             Dir exists\nFile copied: {}\n".format((x[i][0])))

    except:
        print("Double check if the server is connected")





local_file_list_column = [
    [
        sg.Text("Local - Folder"),
        sg.In(size=(40,2),enable_events=True,key="-FOLDER-local"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(60,20),
            key="-FILE LIST-local"
        )
    ],
]

lan_file_list_column = [
    [
        sg.Text("Server - Folder"),
        sg.In(size=(40,2),enable_events=True,key="-FOLDER-lan"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(60,20),
            key="-FILE LIST-lan"
        )
    ],
]


Bottom = [

        [
            sg.ProgressBar(max_value=100, key="Percentage",size=(20,20)),
            sg.Button(button_text="Start",key="Submit-button", enable_events=True)
        ]
    ]


layout = [
    [
        sg.Column(local_file_list_column),
        sg.VSeparator(),
        sg.Column(lan_file_list_column),
        sg.Column(Bottom),

    ]

]

window = sg.Window("Sync Folder", layout)


while True:
    event, values = window.read()
    if event =="Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-FOLDER-local":
        folder = values["-FOLDER-local"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        window["-FILE LIST-local"].update(file_list)


    if event == "-FOLDER-lan":
        folder = values["-FOLDER-lan"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        window["-FILE LIST-lan"].update(file_list)

    if event == "Submit-button":
        folder_lan = values["-FOLDER-lan"]
        folder_local = values["-FOLDER-local"]
        ACTION(folder_lan,folder_local)



window.close()










