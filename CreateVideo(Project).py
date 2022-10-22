import os
import cv2


path = 'C:/Users/sapsl/Downloads/Whitehat jr Python/C105/Images(project)'

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
h,w,c = frame.shape
size = (w,h)
out = cv2.VideoWriter('Project.mp4',cv2.VideoWriter_fourcc(*'XVID'),5,size)

for i in range(0,count-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print('Well done you passed !')