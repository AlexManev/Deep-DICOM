import sys
import os
import numpy as np
import tensorflow as tf
import pydicom
from glob import glob


# Import data from folder
DICOM = "ExportedStudy/Dicom"
OUTPUT_PATH = working_path = "data/out"

g = glob(DICOM + "/*");

print("Total number of images: %d \nFirst 5 elements:" %len(g))
print("\n".join(g[:5]))

#Loading CT Scan Images and calculate HU units for each pixel
def load_scan(path):
    # print("\nfile: "+path+"/"+s) for s in os.listdir(path)
    slices = [pydicom.read_file(path + "/" + s) for s in os.listdir(path)]
    slices.sort(key = lambda x: int(x.InstanceNumber))
    try:
        slice_thickness = np.abs(
            slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2])
    except:
        slice_thickness = np.abs(
            slices[0].SliceLocation - slices[1].SliceLocation
        )
    for s in slices:
        s.SliceThickness = slice_thickness;

    return slices

patient = load_scan(DICOM);
print(patient[0])
