import re
import time
from time import strftime
import yaml
import os
import datetime
x=[]
y=[]

class logParse:
    def parseData(log_file_path, export_file,yaml_file_path):
        regex1='.* ATTACH_REQUEST\(0x41\) for \(ue_id = (\d+)\)'
        regex2='.* CREATE SESSION REQ message to SPGW for ue_id 0x0000000(\w+)'
        regex3='.* MODIFY BEARER REQ to SPGW for ue_id = \((\d+)\).*'
        regex4='.* Received Attach Complete message for ue_id = \((\d+)\)'
        regex5='.* Authentication complete \(ue_id=0x0000000(\w+)'

        with open(yaml_file_path, "r") as f:
            data= yaml.load(f, Loader= yaml.FullLoader)
            keys= data["attach"]
            ueid=data["ue_id"]
            for key in keys:
                temp=key.split('   ')[1]
                x.append(temp)
                
        count=0
        with open(log_file_path, "r") as file:
            match_list = []
            for line in file:
                for index in range(0,len(x)): 
                    if (x[index] ) in line:
                        match_list.append(line)
                        
        file.close()
        final={}
        for i in range(1,15):
            final[str(i)]=0

        with open("temporary.txt","w+")as file: #writingi into file 
            match_list_clean = list(set(match_list))
            for item in match_list_clean:
                file.write(item.split(' ')[9] + "\t" +item.split('   ')[-1])   
        file.close()
        
        #with open("temporary.txt","r")as file:
        match=[]
        for index in range(0,len(ueid)):
            print("for ue_id = " + str(ueid[index]))
            with open("temporary.txt","r")as file:
                for line in file:
                    a = re.search(regex1,line)
                    b = re.search(regex2,line)
                    c = re.search(regex3,line)
                    d = re.search(regex4,line)
                    e = re.search(regex5,line)
                    if a:
                        aa=a.group(1)
                        if int(aa) == ueid[index]:
                            match.append(line)
                    if b:
                        bb=b.group(1)
                        if int(bb,16) == ueid[index]:
                            match.append(line)
                    if c:
                        cc=c.group(1)
                        if int(cc) == ueid[index]:
                            match.append(line)
                    if d:
                        dd=d.group(1)
                        if int(dd) == ueid[index]:
                            match.append(line)
                    if e:
                        ee=e.group(1)
                        if int(ee,16) == ueid[index]:
                            match.append(line)
            file.close()

        mydir=os.path.join("C:\\project\\report", datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        os.makedirs(mydir)
        mydir_out=mydir + "\\" + "output.txt"

        count=0
        with open(mydir_out, "w+") as file:
            match_update = list(set(match))
            for item in match_update:
                file.write(item)
                count += 1
            if(count==5):
                file.write("Attach success")
        file.close()


def main():
    log_file_path = r"C:\project\input\attach1.log"
    export_file_path = r"C:\project\report"
    yaml_file_path = r"C:\project\input\config.yaml"
     
    time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
     
    file = "\\" + "Parser Output " + time_now + ".txt"
    export_file = export_file_path + file
    print(export_file)
    print(export_file_path)
    logparse = logParse
    logparse.parseData(log_file_path, export_file,yaml_file_path)

