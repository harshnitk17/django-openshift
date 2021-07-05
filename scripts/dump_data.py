import os
import json
from b2charm.models import Parameters
import pathlib


def run():
    present_path = pathlib.Path().resolve()
    present_path = str(present_path).rstrip("/hflav")
    dump_path = present_path + "/b2charm/dump"
    for filename in os.listdir(dump_path):
        if filename.endswith(".json") :
            file_path = os.path.join(dump_path, filename)
            f = open(file_path)
            data = json.load(f)
            id = data["id"]
            try:
                par = Parameters.objects.filter(data__id=id).first()
                par.data = data
                par.save()
                print (filename, " : Parameter already exists in database, Values updated")
            except:
                par = Parameters()
                par.data = data
                par.save()
                print (filename, " : New Parameter added to database")
            f.close()
            
            
