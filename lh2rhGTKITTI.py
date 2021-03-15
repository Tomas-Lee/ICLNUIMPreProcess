#-*-coding:utf-8-*-
#!/usr/bin/env python3
import sys
import numpy as np
from scipy.spatial.transform import Rotation as R
# 返回嵌套列表，每个元素都是一个字符串

def parseFile(filepath):
    with open(filepath) as f:
        lines=f.read().split('\n')
        list=[  [v.strip() for v in line.split() if v.strip()!=""]  for line in lines if len(line)>0]
    return list

if __name__ == "__main__":
    poses1=parseFile("/media/atom/DISK1160/datasets/ICLNUIM/lr3nkitti.txt")
    f=open("/media/atom/DISK1160/datasets/ICLNUIM/lr3nkitti_rh.txt","wt")
    for i in range(0,len(poses1)//3):  #对每个位姿来说
        #总共3*4维度的矩阵
        line0=poses1[3*i]
        line1=poses1[3*i+1]
        line2=poses1[3*i+2]
        tmp=[]
        # translation part 理解为z轴反向
        tmp.append(str(i)) #timestamp
        tmp.append(line0[3]) #tx
        tmp.append(line1[3]) #ty
        tmp.append(str(-float(line2[3]))) #tz
        # rotation part
        r00 = float(line0[0])
        r01 = float(line0[1])
        r02 = - float(line0[2])
        r10 = float(line1[0])
        r11 = float(line1[1])
        r12 = - float(line1[2])
        r20 = - float(line2[0])
        r21 = - float(line2[1])
        r22 = float(line2[2])
        rotrh=np.array([
            [r00,r01,r02],
            [r10,r11,r12],
            [r20,r21,r22]
        ])
        quat_rh = R.from_dcm(rotrh).as_quat()

        tmp.append(str(quat_rh[0])) #sx
        tmp.append(str(quat_rh[1])) #sy
        tmp.append(str(quat_rh[2]))  # sz
        tmp.append(str(quat_rh[3]))  # sw
        print(tmp)
        f.writelines(" ".join(x for x in tmp) + "\r\n")
    f.close()
















