#!/usr/bin/env python3
"""
@uthor: Himaghna 4th February 2019
Description: Read energy form outcar/contcar file
       Usage read_energy_from_outcar.py 'outcar file'
       If no argument supploed, searches current working directory for
        filename 'OUTCAR'.
       If filesearch is unsuccessful raises FileNotFound Error
"""
from argparse import ArgumentParser
import os
import ase.io

def __main__():
    """
    Reads potential energy in eV from OUTCAR file
    :return: energy: float
    """
    parser = ArgumentParser()
    parser.add_argument('-fn', '--filename',
                        help='OUTCAR/ CONTCAR file to read energy',
                        default=None)
    args = parser.parse_args()
    filename = args.filename
    if not filename:
        # filename not passed
        filename = os.path.join(os.getcwd(), 'OUTCAR')
    if not os.path.isfile(filename):
        raise FileNotFoundError('OUTCAR not found')
    atom_obj = ase.io.read(filename)
    energy = atom_obj.get_potential_energy()
    print('Potential Energy is {}'.format(energy))
    return energy


if __name__ == __main__():
    __main__()