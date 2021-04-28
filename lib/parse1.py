import re
import time
from time import strftime
import yaml
x=[]
y=[]
def main():
    log_file_path = r"C:\project\input\attach1.log"
    export_file_path = r"C:\project\report"
    yaml_file_path = r"C:\project\input\config.yaml"
     
    time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
     
    file = "\\" + "Parser Output " + time_now + ".txt"
    export_file = export_file_path + file
    print(export_file)
    print(export_file_path)
    
    parseData(log_file_path, export_file,yaml_file_path)

def parseData(log_file_path, export_file,yaml_file_path):
    with open(yaml_file_path, "r") as f:
        data= yaml.load(f, Loader= yaml.FullLoader)
        keys= data["attach"]
        id=data["ue_id"]
        for key in keys:
            temp=key.split('   ')[1]
            x.append(temp)
            temp1=key.split('   ')[2]
            y.append(temp1)
            
    print(y)        
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

    
    with open("temporary.txt","r")as file:
        match_list_update=[]
        for line in file:
            for index in range(0,len(y)): 
                #print(x[index], y[index])
                if (y[index] ) in line:
                    #print(line)
                    match_list_update.append(line)
    file.close()

    with open(export_file, "w+") as file:
        match_list_clean_update = list(set(match_list_update))
        for item in match_list_clean_update:
            file.write(item)
    file.close()


if __name__ == '__main__':
    main()