#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
#from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
import math
# from geometry_msgs.msg import 
from std_msgs.msg import Float64
from Real_Assembly.msg import ekfImage

bridge = CvBridge()






def lines_merge(rectified_lines):
        best_lines = []
        for i in range(0,len(rectified_lines)):
                for j in range(i+1,len(rectified_lines)):
                        if abs(rectified_lines[i][4] - rectified_lines[j][4]) < 0.25 and abs(rectified_lines[i][5] - rectified_lines[j][5])<10:
                                if rectified_lines[i][0] < rectified_lines[j][0] and rectified_lines[i][2] < rectified_lines[j][2]:
                                        slope = float((rectified_lines[j][3] - rectified_lines[i][1])/(rectified_lines[i][0] - rectified_lines[j][2]))
                                        bias = rectified_lines[i][1] - slope*rectified_lines[i][0]
                                        best_lines.append([rectified_lines[i][0],rectified_lines[i][1],rectified_lines[j][2],rectified_lines[j][3],slope,bias])
                                elif rectified_lines[i][0] < rectified_lines[j][0] and rectified_lines[i][2] > rectified_lines[j][2]:
                                        best_lines.append([rectified_lines[i][0],rectified_lines[i][1],rectified_lines[i][2],rectified_lines[i][3],rectified_lines[i][4],rectified_lines[i][5]])
                                elif rectified_lines[i][0] > rectified_lines[j][0] and rectified_lines[i][2] > rectified_lines[j][2]:
                                        slope = float((rectified_lines[i][3] - rectified_lines[j][1])/(rectified_lines[j][0] - rectified_lines[i][2]))
                                        bias = rectified_lines[j][1] - slope*rectified_lines[j][0]
                                        best_lines.append([rectified_lines[j][0],rectified_lines[j][1],rectified_lines[i][2],rectified_lines[i][3],slope,bias])
                                elif rectified_lines[i][0] > rectified_lines[j][0] and rectified_lines[i][2] < rectified_lines[j][2]:
                                        best_lines.append([rectified_lines[j][0],rectified_lines[j][1],rectified_lines[j][2],rectified_lines[j][3],rectified_lines[j][4],rectified_lines[j][5]])
        return best_lines



def stair(img):
    # img = np.uint8(img)
    print(img.shape)
    img = (img*256).astype(np.uint8)
    # cv2.imshow("Image-stair",img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    edges = cv2.Canny(img, 30, 40, 3)
    edges_rectified = edges.copy()
    (h, w) = edges.shape
    for i in range(h):
        for j in range(6,w-6):
            if edges[i][j] == 255 and (img[i][j-5] == 0 or img[i][j+5] == 0):
                edges_rectified[i][j] = 0


    minLineLength = 20
    maxLineGap = 5
    accumulator_threshold = 20
    lines = cv2.HoughLinesP(edges_rectified, 1, np.pi/180,accumulator_threshold,minLineLength,maxLineGap)
    rect_lines = []
    img_copy = img.copy()
# print(len(lines))
    for line in lines:
    # print(line.shape)
        for x1, y1, x2, y2 in line:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
            if x2!=x1:
                slope = float((y2-y1)/(x1-x2))
		# slope = float((y2 - y1)/(x1 - x2))
                #slope = float((y2 - y1)/(x2 - x1))
                bias = y1 - slope*x1
                rect_lines.append([x1,y1,x2,y2,slope,bias])

    lines_final = []
    final_lines = set()
    count = 0
    while count<1:
            print(count)
            if count == 0:
                    temp_list = []
                    temp_list = lines_merge(rect_lines)
                    lines_final = temp_list
            else:
                    temp_list = []
                    temp_list = lines_merge(lines_final)
                    lines_final = temp_list
            count = count + 1
#rejecting all the lines lyinh below the sensor
    final = []
    final_lines = set(tuple(i) for i in lines_final)
    slope_list = []
    (H,W) = img.shape
    for line in final_lines:
            if line[1]>(H/2) or line[3]>(H/2):
                    continue
            else:
                    final.append(line)

    highest_length = 0
    x2_ans = 0
    x1_ans = 0
    y1_ans = 0
    y2_ans = 0
    list_covariances = []
    list_lines = []
    for line in final:
            x1 = line[0]
            y1 = line[1]
            x2 = line[2]
            y2 = line[3]
            slope_list.append(line[4])

            pol = img_copy.copy()

            if line[4]==0.0 or line[4]==-1.0:
                if line[4]>=0:
                        angle = math.atan(line[4])
                        angle = math.atan(line[4]) + (3*(np.pi/2))
                        rho = x1*math.cos(angle) + y1*math.sin(angle)
                        kZero = x1*math.sin(angle) - x2*math.cos(angle)
                        kOne = x2*math.sin(angle) - x2*math.cos(angle)
                        cov = np.zeros((2,2))
                        diff = (kZero - kOne)
                        add = (kZero + kOne)
                        cov[0][0] = (2/diff*diff)
                        cov[0][1] = (add/(diff*diff))
                        cov[1][0] = cov[0][1]
                        cov[1][1] = 0.5 + ((add*add)/(2*diff*diff))
                        delta_parameters = np.zeros((3,2))
                        list_parameters = []
                        delta_parameters[0][0] = -math.sin(angle)
                        delta_parameters[0][1] = 0
                        delta_parameters[1][0] = math.cos(angle)
                        delta_parameters[1][1] = 0
                        delta_parameters[2][0] = 0
                        delta_parameters[2][1] = -1
                        # list_parameters.append(-math.sin(angle))
                        # list_parameters.append(0)
                        # list_parameters.append(math.cos(angle))
                        # list_parameters.append(0)
                        # list_parameters.append(0)
                        # list_parameters.append(-1)
                        Rj = np.zeros((3,3))
                        Rj = np.dot(np.dot(delta_parameters,cov),delta_parameters.T)
                        lmj = np.ones((3,1))
                        lmj[0][0] = math.cos(angle)
                        lmj[1][0] = math.sin(angle)
                        lmj[2][0] = -rho
                        list_parameters.append(Rj[0][0])
                        list_parameters.append(Rj[0][1])
                        list_parameters.append(Rj[0][2])
                        list_parameters.append(Rj[1][0])
                        list_parameters.append(Rj[1][1])
                        list_parameters.append(Rj[1][2])
                        list_parameters.append(Rj[2][0])
                        list_parameters.append(Rj[2][1])
                        list_parameters.append(Rj[2][2])
                        list_parameters.append(Rj[2][0])
                        list_parameters.append(Rj[2][1])
                        list_parameters.append(Rj[2][2])
                        list_parameters.append(lmj[0][0])
                        list_parameters.append(lmj[1][0])
                        list_parameters.append(lmj[2][0])
                        # list_parameters.append(-1)
                        # lmj = np.ones((3,1))
                        # lmj[0][0] = math.cos(angle)
                        # lmj[1][0] = math.sin(angle)
                        # lmj[2][0] = -rho
                        # list_covariances.append(Rj)
                        # list_lines.append(lmj)
                        list_covariances.append(list_parameters)
                        # list_covariances.append(cov)
                else:
                        angle = np.pi + math.atan(line[4])
                        angle = (np.pi)/2 + angle
                        rho = x1*math.cos(angle) + y1*math.sin(angle)
                        kZero = x1*math.sin(angle) - x2*math.cos(angle)
                        kOne = x2*math.sin(angle) - x2*math.cos(angle)
                        cov = np.zeros((2,2))
                        diff = (kZero - kOne)
                        add = (kZero + kOne)
                        cov[0][0] = (2/diff*diff)
                        cov[0][1] = (add/(diff*diff))
                        cov[1][0] = cov[0][1]
                        cov[1][1] = 0.5 + ((add*add)/(2*diff*diff))
                        delta_parameters = np.zeros((3,2))
                        delta_parameters[0][0] = -math.sin(angle)
                        delta_parameters[0][1] = 0
                        delta_parameters[1][0] = math.cos(angle)
                        delta_parameters[1][1] = 0
                        delta_parameters[2][0] = 0
                        delta_parameters[2][1] = -1
                        Rj = np.zeros((3,3))
                        Rj = np.dot(np.dot(delta_parameters,cov),delta_parameters.T)
                        lmj = np.ones((3,1))
                        lmj[0][0] = math.cos(angle)
                        lmj[1][0] = math.sin(angle)
                        lmj[2][0] = -rho
                        list_parameters.append(Rj[0][0])
                        list_parameters.append(Rj[0][1])
                        list_parameters.append(Rj[0][2])
                        list_parameters.append(Rj[1][0])
                        list_parameters.append(Rj[1][1])
                        list_parameters.append(Rj[1][2])
                        list_parameters.append(Rj[2][0])
                        list_parameters.append(Rj[2][1])
                        list_parameters.append(Rj[2][2])
                        list_parameters.append(Rj[2][0])
                        list_parameters.append(Rj[2][1])
                        list_parameters.append(Rj[2][2])
                        list_parameters.append(lmj[0][0])
                        list_parameters.append(lmj[1][0])
                        list_parameters.append(lmj[2][0])
                        # list_covariances.append(Rj)
                        list_covariances.append(list_parameters)
                        # list_covariances.append(Rj.flatten())
                        # list_lines.append(lmj)
    # cv2.line(img_copy,(x1_ans,y1_ans),(x2_ans,y2_ans),(0,255,0),2)
    # return img_copy
    # return (list_covariances, list_lines)
#     return list_covariances
#     covariances = np.array(list_covariances)
    return (list_covariances)
    # return img_copy






#Publisher
def talker(CovarianceDepth):
#     pub = rospy.Publisher('/husky_velocity_controller/cmd_vel', Twist, queue_size=10)
    pub = rospy.Publisher('heading_angle', ekfImage, queue_size=10)


    rospy.init_node('hello_world_subscriber_depth', anonymous=True)
    r = rospy.Rate(1)
    msg = ekfImage()
    msg.RGB.data = CovarianceDepth
    msg.Depth.data = CovarianceDepth
    pub.publish(msg)
#     msg = Twist()
#     Kp = 5
#     msg.linear.x = 0
#     msg.linear.y = 0
#     msg.linear.z = 0
#     msg.angular.x = 0
#     msg.angular.y = 0
#     msg.angular.z = (Kp)*(depth_diff*0.01)
    # while not rospy.is_shutdown():
        # str = "hello world %s"%rospy.get_time()
        # rospy.loginfo(str)
    # pub.publish(angle)
    r.sleep()














CovarianceDepth = []

# The following call back func is executed when the message reaches the topic
def call_back(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s",data.data)
    format_s ="32FC1"
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding=format_s)
    cv_image_array = np.array(cv_image,dtype=('f8'))
    cv_image_norm = cv2.normalize(cv_image_array, cv_image_array, 0, 1, cv2.NORM_MINMAX)
    # print(np.shape(cv_image_norm))
    (CovarianceDepth) = stair(cv_image_norm)
    # d_r = cv_image_norm[y2_ans+10][x2_ans]
    # d_l = cv_image_norm[y1_ans+10][x1_ans]
    print("Pratyush")
#     print(((d_r - d_l)/(abs(x2_ans - x1_ans))))
    # print(np.arccos((d_r - d_l)/(abs(x2_ans - x1_ans)))*(360/6.2831853072) - 90)
    # angle = (np.arccos((d_r - d_l)/(abs(x2_ans - x1_ans)))*(360/6.2831853072) - 90)
#     print((d_r-d_l)*256)

    # depth_diff = (d_r-d_l)*256
    # print(CovarianceDepth)
    talker(CovarianceDepth)
#     if abs(depth_diff)>2:
        # print("Not Aligned :(")
        # talker(depth_diff)
#     else:
        # print("Aligned :)")
#     print(y1_ans)
#     print(y2_ans)
    # print()
#     cv2.line(cv_image_norm,(x1_ans,y1_ans),(x2_ans,y2_ans),(0,255,0),4)
#     cv2.imshow("Image",cv_image_norm)
#     cv2.waitKey()
#     cv2.destroyAllWindows()
    #cv_image = bridge.compressed_imgmsg_to_cv2(data, desired_encoding="rgb8")
    #cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s",np.shape(cv_image))
    #gray = cv2.convertScaleAbs(cv_image, alpha=255/cv_image.max())
    #cv2.imwrite("depth_norm_new.jpg",cv_image)

def listener():
    rospy.init_node('hello_world_subscriber_depth',anonymous=True)
    #rospy.Subscriber('hello_pub',String,call_back)
    rospy.Subscriber('/camera/depth/image_raw',Image,call_back)
    print(CovarianceDepth)
    #rospy.Subscriber('/camera/color/image_raw',Image,call_back)
    #rospy.Subscriber('/camera/color/image_raw/compressedDepth',CompressedImage,call_back)
    rospy.spin()


if __name__ == '__main__':
    listener()
