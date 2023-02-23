import csv

size= 50
private= "no"
twopole= "yes"

print("The following lakes meet your criteria:")

with open("lakedata.csv") as lakedata:
    for lake in csv.DictReader(lakedata):
        if float(lake["LakeSize"]) > size:
            if lake["PrivateResort"].lower() == private:
                if lake["2Pole"].lower() == twopole:
                    print(lake["LakeName"])
