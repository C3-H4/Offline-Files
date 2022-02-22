import subprocess, filecmp , os
from shutil import copyfile
from os import path


#       Does not require a order for path1/2
def mostrecent(path1,path2,filename):
    if os.path.getctime(path1) > os.path.getctime(path2):
        copyfile((path1+"\\"+filename),(path2+"\\"+filename))
    else:
        copyfile((sort[i][2]+"\\"+sort[i][0]),(sort[i][1]+"\\"+sort[i][0]))


current_network = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')
ssid_line = [x for x in current_network if 'SSID' in x and 'BSSID' not in x]
if ssid_line:
    ssid_list = ssid_line[0].split(':')
    connected_ssid = ssid_list[1].strip()
confirmation = False   


if connected_ssid == ("VM012354"):
  confirmation = True
  print (connected_ssid)

try:
    l =[]
    s =[]
    server_path = (r"Z:\Software Engineering")
    laptop_path = (r"C:\Users\USER\Desktop\Software Engineering") # Changed For safety
    path = [[laptop_path,l],[server_path,s]]
      
    #def Validation(path):


    for x in path:
      for root, dirs, files in os.walk(x[0]):
          for filename in files:
              (x[1]).append([filename,root])

    sort = []

    ii = []
    jj = []


    for i in range (0,len(s)):
        for j in range (0,len(l)):
            beginl =(l[j][1].find("Software Engineering"))
            begins =(s[i][1].find("Software Engineering"))
            if (l[j][0]) == (s[i][0]) and ((l[j][1])[beginl:]) == ((s[i][1])[begins:]):
                sort.append([l[j][0],l[j][1],s[i][1]])
                
                ii.append(i)
                jj.append(j)


    for x in reversed(ii):
        del s[x]

    for x in reversed(jj):
        del l[x]


    ## --------------------------Same Files --------------------------------
    for i in range (0,len(sort)):
        
        check = filecmp.cmp((sort[i][1]+"\\"+sort[i][0]),(sort[i][2]+"\\"+sort[i][0]))
        if check == False:
            print ("Needs to be updated")
            mostrecent((sort[i][1]),(sort[i][2]),(sort[i][0]))
            
            
        else:
            check = True

    ## ----------------------------New File/Folder from computer --------------------------
    lsts = [l,s]

    for u in range (0,len(lsts)):
        x = lsts[u]
        if (x) ==[]:
            vData = ("empty")
        else:
            for i in range (0,len(x)):
                tempin = x[i][1].find("Software Engineering")
                num = (tempin)+20
                folder =  ((((x[i][1])[num:]).split(os.sep))[1:])
                empty = []
                for w in range (0,len(folder)):
                    together = ("\\"+folder[w])
                    empty.append(together)

                if "Z" in x[i][1] :
                    p = (laptop_path+("".join(empty)))
                else:
                    p = (server_path+("".join(empty)))
                if (os.path.exists(p)) == False:
                    for t in range (0,len(empty)):
                        folder2beremoved = "".join(empty[(t+1):])
                        updated = p[:((len(p))-(len(folder2beremoved)))]
                        if (os.path.exists(updated)) == False:
                            os.mkdir(updated)

                        
                    copyfile((x[i][1]+"\\"+x[i][0]),(p+"\\"+x[i][0]))
                    print ("             Dir & File doesnt exist\nDirectory created: {}\nFile copied: {}\n".format(p,(x[i][0])))
                else:
                    copyfile((x[i][1]+"\\"+x[i][0]),(p+"\\"+x[i][0]))
                    print ("             Dir exists\nFile copied: {}\n".format((x[i][0])))

except:
    print ("Double check if the server is connected")






