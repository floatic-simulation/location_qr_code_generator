import qrcode
import os
import pandas as pd

location_code = "A2-01-01-04"

zone_list = ["A","B","C"]
aisle_num = 2
rack_num = 4
A_level_num = 3
B_level_num = 4

cell_num = 4

image_path = "./qr_img"
abs_path = os.path.abspath(image_path)

location_code_list = []
qr_path_list = []

qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
for zone in zone_list:
    if zone == "A":
        level_num = A_level_num
    elif zone == "B" or zone == "C":
        level_num = B_level_num
    
    for aisle in range(aisle_num):
        for rack in range(rack_num):
            for level in range(level_num):
                for cell in range(cell_num):
                    location_code = f"{zone}{aisle+1}-{rack+1}{cell+1}-{level+1:0>2}"
                    qr.add_data(location_code)
                    qr.make(fit=True)
                    img = qr.make_image(fill_color="black", back_color="white")
                    img.save(f"{abs_path}/{location_code}.png")
                    print(location_code, ".png saved")
                    location_code_list.append(location_code)
                    qr_path_list.append(abs_path)

df = pd.DataFrame({'image_path':qr_path_list, 'location_code':location_code_list})
with pd.ExcelWriter("testbed_location_codes.xlsx") as writer:
     df.to_excel(writer, sheet_name = 'location_codes')

