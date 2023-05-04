from Z2_CSV_Function import *
from Z1_ListFunction import *
from F14_Save import *

array_of_candi = [['123', '234', 'waduh', 'azazel',  Mark, None], Mark, None]

index_jinCandi = get_element_matriks(array_of_candi, 'azazel')
array_of_candi = Remove(array_of_candi, index_jinCandi)
print(array_of_candi)