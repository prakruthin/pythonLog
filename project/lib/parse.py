import re
import time
from time import strftime
import yaml
import os
import datetime


class logParse:
    def parseData(log_file_path,yaml_file_path,mydir_out):
        regex=['.* ATTACH_REQUEST\(0x41\) for \(ue_id = (\d+)\)','.* CREATE SESSION REQ message to SPGW for ue_id 0x0000000(\w+)','.* MODIFY BEARER REQ to SPGW for ue_id = \((\d+)\).*','.* Received Attach Complete message for ue_id = \((\d+)\)','.* Authentication complete \(ue_id=0x0000000(\w+)']
        x=[]
        y=[]
        count={}
        ueid=logParse.getUeid(yaml_file_path)

        for index in range(0,len(ueid)):
            with open(log_file_path,"r")as file:
                match=[]
                inter=[]
                for line in file:
                    a = re.search(regex[0],line)
                    b = re.search(regex[1],line)
                    c = re.search(regex[2],line)
                    d = re.search(regex[3],line)
                    e = re.search(regex[4],line)
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
                count[ueid[index]] = len(match)
                logParse.addToFile(match,mydir_out)
            file.close()
        logParse.printResult(count,mydir_out)

    def getUeid(yaml_file_path):
        try:
            f=open('C:\project\input\config.yaml', "r")
            data= yaml.load(f, Loader= yaml.FullLoader)
            return data["ue_id"]
            f.close()

        except Exception as e:
            print(e)
            return []
        
    def printResult(count,mydir_out):
        try:
            file=open(mydir_out, "a+")
            file.write("\n")
            for key,value in count.items():
                if(value>=6):
                    file.write("ue_id " + str(key) + " successfully attached \n" )
            file.close() 
        except Exception as e:
            print(e)   

    def addToFile(match,mydir_out):
        try:
            file=open(mydir_out, "a+")
            for line in match:
                file.write(line.split(' ')[9] + "\t" +line.split('   ')[-1])
            file.write("\n")
            file.close()
        except Exception as e:
            print(e) 

def main():
    log_file_path = r"C:\project\input\attach1.log"
    yaml_file_path = r"C:\project\input\config.yaml"
    mydir=os.path.join("C:\\project\\report", datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    mydir_out=mydir + "\\" + "output.txt"
    
    logparse = logParse
    os.makedirs(mydir)
    logparse.parseData(log_file_path,yaml_file_path,mydir_out)

