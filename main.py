import hashlib
import pandas as pd

def hashUsingTuplesFirst() -> []:
    hashes = []
    file = open("title.basics.mod.tsv")

    for row in file:
        columns = row.split()
        hash_string = str(tuple(columns))
        hashes.append(hashlib.md5(hash_string.encode("utf-8")).hexdigest())

    file.close()
    return hashes

def hashWithoutTuple() -> []:
    hashes = []
    file = open("title.basics.mod.tsv")

    for row in file:
        columns = row.split()
        hash_string = "(" + ", ".join(f"'{str(column)}'" for column in columns) + ")"
        hashes.append(hashlib.md5(hash_string.encode("utf-8")).hexdigest())

    file.close()
    return hashes

def hashUsingPandas() -> []:
    hashes = []
    file = open("title.basics.mod.tsv")
    df = pd.read_csv(file, sep='\t')

    for row in df:
        hash_string = str(row)
        hashes.append(hashlib.md5(hash_string.encode("utf-8")).hexdigest())

    file.close()
    return hashes


hashUsingTuplesFirst()
hashWithoutTuple()
hashUsingPandas()




