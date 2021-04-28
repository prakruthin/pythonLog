import re
import time
from time import strftime
import yaml
import os
import datetime
x=[]
y=[]
mydir=os.path.join("C:\\project\\report", datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
os.makedirs(mydir)
mydir_out=mydir + "\\" + "output.txt"

def addToFile(line):
    with open(mydir_out, "a+") as file:
        file.write(line.split(' ')[9] + "\t" +line.split('   ')[-1])
    file.close()
    

class logParse:
    def parseData(log_file_path,yaml_file_path):
        regex1='.* ATTACH_REQUEST\(0x41\) for \(ue_id = (\d+)\)'
        regex2='.* CREATE SESSION REQ message to SPGW for ue_id 0x0000000(\w+)'
        regex3='.* MODIFY BEARER REQ to SPGW for ue_id = \((\d+)\).*'
        regex4='.* Received Attach Complete message for ue_id = \((\d+)\)'
        regex5='.* Authentication complete \(ue_id=0x0000000(\w+)'

        with open(yaml_file_path, "r") as f:
            data= yaml.load(f, Loader= yaml.FullLoader)
            keys= data["attach"]
            ueid=data["ue_id"]
            
        match=[]
        count={}
        
        for index in range(0,len(ueid)):
            with open(log_file_path,"r")as file:
                for line in file:
                    a = re.search(regex1,line)
                    b = re.search(regex2,line)
                    c = re.search(regex3,line)
                    d = re.search(regex4,line)
                    e = re.search(regex5,line)
                    if a:
                        aa=a.group(1)
                        if int(aa) == ueid[index]:
                            addToFile(line)
                            count[ueid[index]] = count.get(ueid[index],0) +1
                    if b:
                        bb=b.group(1)
                        if int(bb,16) == ueid[index]:
                            addToFile(line)
                            count[ueid[index]] = count.get(ueid[index],0) +1
                    if c:
                        cc=c.group(1)
                        if int(cc) == ueid[index]:
                            addToFile(line)
                            count[ueid[index]] = count.get(ueid[index],0) +1
                    if d:
                        dd=d.group(1)
                        if int(dd) == ueid[index]:
                            addToFile(line)
                            count[ueid[index]] = count.get(ueid[index],0) +1
                    if e:
                        ee=e.group(1)
                        if int(ee,16) == ueid[index]:
                            addToFile(line)
                            count[ueid[index]] = count.get(ueid[index],0) +1
                with open(mydir_out, "a+") as file:
                    file.write("\n")
            file.close()
        with open(mydir_out, "a+") as file:
            file.write("\n")
            for key,value in count.items():
                if(value>=6):
                    file.write("ue_id " + str(key) + " successfully attached \n" )
        file.close()    


def main():
    log_file_path = r"C:\project\input\attach1.log"
    export_file_path = r"C:\project\report"
    yaml_file_path = r"C:\project\input\config.yaml"
     
    time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
     
    file = "\\" + "Parser Output " + time_now + ".txt"
    export_file = export_file_path + file
    logparse = logParse
    logparse.parseData(log_file_path,yaml_file_path)

