import pyedflib

edf_path = '/Users/oj/Desktop/Yoo_Lab/Yoo_data/RBD_EDF/PE210170_edf/Traces.edf'

try:
    f = pyedflib.EdfReader(edf_path)
    print(f"파일이 정상적으로 열렸습니다. 데이터의 개수: {f.signals_in_file}")
    f.close()
except Exception as e:
    print(f"파일을 열 수 없습니다: {e}")
