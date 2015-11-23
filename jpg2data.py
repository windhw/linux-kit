import Image
import struct
im=Image.open("D://src.jpg")
(w,h) = im.size
f=file("D://dest.data","wb")
for j in range(h):
    for i in range(w):
        (r,g,b) = im.getpixel((i,j))
        n = (r>>3) | ((g>>2)<<5) | ((b>>3) <<11 )
        d = struct.pack("<H",15)
        f.write(d)
f.close()
