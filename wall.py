import numpy as np
import cv2
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 3

img1 = cv2.imread('wall1s.jpg',0)          # queryImage
img2 = cv2.imread('wall2s.jpg',0) # trainImage

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1,des2,k=2)

# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
    if m.distance < 0.85*n.distance:
        good.append(m)

if len(good)>MIN_MATCH_COUNT:
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()

    h,w = img1.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)

    img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

else:
    print "Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT)
    matchesMask = None

draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)

plt.imshow(img3, 'gray')
plt.show()

M = cv2.getPerspectiveTransform(np.delete(dst_pts,3,0),np.delete(src_pts,3,0))

dst = cv2.warpPerspective(img2,M,(240,90))

cv2.imwrite("wall2.png",dst)


M = np.float32([[1,0,0],[0,1,0]])
tmp = cv2.warpAffine(img1,M,(240,90))
cv2.imwrite("wall1.png",tmp)

for j in range(tmp.shape[0]):
    for i in range(tmp.shape[1]):
        if dst[j,i] == 0:
            dst[j,i] = tmp[j,i]

plt.imshow(dst)
cv2.imwrite("wall12.png",dst)
