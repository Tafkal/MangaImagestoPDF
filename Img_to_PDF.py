from PIL import Image
import os

mypath0 = os.getcwd()
f = []
for (dirpath, dirnames0, filenames0) in os.walk(mypath0):
    f.extend(filenames0)
    break
#print(dirnames0)
imagelist = []
for m in dirnames0:
    mypath1 = mypath0 + '\\' + m
    for (dirpath1, dirnames1, filenames1) in os.walk(mypath1):
        f.extend(filenames1)
        break
    for x in dirnames1:
        mypath2 = mypath1 + '\\' + x
        #print(mypath2)
        for (dirpath2, dirnames2, filenames2) in os.walk(mypath2):
            f.extend(filenames2)
            break
        i = 0
        for y in filenames2:
            mypath3 = mypath2 + '\\' + y
            #print(mypath3)
            if mypath3.endswith(('.jpg', '.png', '.jpeg', '.JPG', '.PNG', '.JPEG')):
                imagelist.append((Image.open(mypath3)).convert('RGB'))
            else:
                print(mypath3)
savepath = mypath0 + '.pdf'
print(savepath)
imagelist[0].save(savepath,save_all=True, append_images=imagelist)
