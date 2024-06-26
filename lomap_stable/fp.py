# ******************
# MODULE DOCSTRING
# ******************

"""

LOMAP: fingerprint calculations
=====

Alchemical free energy calculations hold increasing promise as an aid to drug
discovery efforts. However, applications of these techniques in discovery
projects have been relatively few, partly because of the difficulty of planning
and setting up calculations. The Lead Optimization Mapper (LOMAP) is an
automated algorithm to plan efficient relative free energy calculations between
potential ligands within a substantial of compounds.

"""

# *****************************************************************************
# Lomap2: A toolkit to plan alchemical relative binding affinity calculations
# Copyright 2015 - 2016  UC Irvine and the Authors
#
# Authors: Dr Gaetano Calabro' and Dr David Mobley
#
# *****************************************************************************


# ****************
# MODULE IMPORTS
# ****************


from rdkit import Chem
from rdkit.Chem import rdFMCS
from rdkit.Chem import AllChem
from rdkit.Chem.Draw.MolDrawing import DrawingOptions
from rdkit.Chem import Draw
from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols
import sys
import math
from rdkit import RDLogger
import logging
import argparse

# *******************************
# Figureprint Class
# *******************************


__all__ = ['FIGUREPRINT']


class Figureprint(object):
    """

    This class is used to compute the Maximum Common Subgraph (MCS) between two
    RDkit molecule objects and to score their similarity by using defined rules

    """

    def __init__(self, moli, molj):
        """
        Inizialization function

        Parameters
        ----------

        moli : RDKit molecule object
            the first molecule used to perform the Figureprint calculation
        molj : RDKit molecule object
            the second molecule used to perform the Figureprint calculation
        options : argparse python object
            the list of user options

        """
        # Local pointers to the passed molecules
        self.moli = moli
        self.molj = molj

        self.fps_moli = FingerprintMols.FingerprintMol(self.moli)
        self.fps_molj = FingerprintMols.FingerprintMol(self.molj)
        self.fps_tan = DataStructs.FingerprintSimilarity(self.fps_moli, self.fps_molj)

    def get_fps_tan(self):
        return self.fps_tan
