# import numpy as np
# record_id = 1
# name = 'asf'
# price = 12.34
# num_in_shops = 3
# if isinstance(record_id, np.uint16):
#     print('success in id')
# if isinstance(name, str):
#     print('success in name')
# if isinstance(price, float) or isinstance(price, np.uint8):
#     print('success in price')
# if isinstance(num_in_shops, np.uint32):
#     print('success in num_shops')


# str = "1,GTA5,1999.99,121424"
# ind = str.strip().split(',')[0]
# print(ind)

field = 'id'
field_idx = {"id": 0, "name": 1, "price": 2, "num_in_shops": 3}[field]
print(field_idx)