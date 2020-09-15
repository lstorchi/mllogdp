import subprocess
import argparse
import time
import os

import numpy as np
import pandas as pd 
from rdkit import Chem
from rdkit.Chem import AllChem

import mllogdpcommon

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file", help="input xlsx file ", \
            required=True, type=str)

    args = parser.parse_args()
            
    filename = args.file
                    
    data = pd.read_excel(filename)

    molatomtypes = {}
    atomtypesset = set()
    mollogd = {}

    errorscounter = 0
    errorssmiles = []
    dim = len(data["SMILES"])
    for idx, ss in enumerate(data["SMILES"]):
        start = time.time()
        name = data["NO"][idx]

        mol = Chem.MolFromSmiles(str(ss))

        AllChem.Compute2DCoords(mol)
        AllChem.EmbedMolecule(mol, randomSeed=0xf00d) 
        Chem.Kekulize(mol)
        mol_3D = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol_3D, randomSeed=0xf00d)

        fout = Chem.SDWriter(name+".mol")
        fout.write(mol_3D)
        fout.close()

        end = time.time()

