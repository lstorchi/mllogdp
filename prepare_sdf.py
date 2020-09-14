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

        mol = Chem.MolFromSmiles(str(ss))

        AllChem.Compute2DCoords(mol)
        AllChem.EmbedMolecule(mol, randomSeed=0xf00d) 
        Chem.Kekulize(mol)
        mol_3D = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol_3D, randomSeed=0xf00d)

        basename = "molecule_"+str(idx+1)

        fout = Chem.SDWriter(basename+".mol")
        fout.write(mol_3D)
        fout.close()

        os.remove(basename+".mol")

        end = time.time()

        print("Mol %10d of %10d has %5d "%(idx+1, dim, mol.GetNumAtoms()), 
                " atoms and LogD %10.5f (%12.7s s) in set %s"%(logd, (end - start), 
                    setid))

    print(errorscounter, " errors out of ", dim, " molecules ")
    for i, s in enumerate(errorssmiles):
        print("  %5d "%(i+1), s)

    fp.close()
