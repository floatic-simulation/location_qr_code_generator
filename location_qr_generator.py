import qrcode
import os

zone_list = ["A","B","C"]  # list of Zone
aisle_num = 2  # number of aisles in zone
rack_num = 4  # number of racks in aisle
A_level_num = 3  # number of levels in zone A
BC_level_num = 4  # number of levels in zone B, C

cell_num = 4  # number of cells in level

image_path = "./qr_img" # path to save image
abs_path = os.path.abspath(image_path)

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
        level_num = BC_level_num
    
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