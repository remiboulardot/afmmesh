import numpy as np
import matplotlib.pyplot as plt

H=50
W=60
x=200
y=30

im=np.zeros((500,500))
tri=np.zeros((W,W))

if W%2==0:
    O=np.zeros(W/2)
    H1=np.zeros(W/2)
    O[0]=W/2.-1./2.
    H1[0]=2.*O[0]*H/W
    for i in range (1,(np.size(O))):
        O[i]=O[0]-i
        H1[i]=2*O[i]*H/W

else:
    O=np.zeros((W+1)/2)
    H1=np.zeros((W+1)/2)
    O[0]=W/2.-1./4.
    H1[0]=2.*O[0]*H/W
    for i in range (1,(np.size(O))):
        O[i]=W/2.-i
        H1[i]=2*O[i]*H/W

    
for k in range (0,np.size(O)):
    for i in range (0,W):
        for j in range (0+k,W-k):
            tri[0+k,j]=H1[(np.size(H1)-1-k)]
            tri[i,0]=H1[(np.size(H1)-1)]
            tri[i,W-1]=H1[(np.size(H1)-1)]
            tri[W-1-k,j]=H1[(np.size(H1)-1)-k]
            
for k in range (0,np.size(O)):
    for j in range (0,W):
        for i in range (0+k,W-k):
            tri[0,j]=H1[(np.size(H1)-1)]
            tri[i,0+k]=H1[(np.size(H1)-1)-k]
            tri[i,W-1-k]=H1[(np.size(H1)-1)-k]
            tri[W-1,j]=H1[(np.size(H1)-1)]

for i in range (x,x+W-1):
    for j in range (y,y+W-1):
        im[i,j]=tri[i-x,j-y]

print(tri)

image = plt.imshow(tri)
plt.show(image)

image2 = plt.imshow(im)
plt.show(image2)