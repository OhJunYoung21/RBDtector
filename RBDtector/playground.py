import pyedflib
from pyedflib import highlevel

signals, signal_headers, header = highlevel.read_edf(
    "/Users/oj/Desktop/Yoo_Lab/Yoo_data/RBD_EDF/PE210170_edf_for_RBDtector/Traces.edf")

print(signals, signal_headers, header)
