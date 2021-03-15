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
    poses1=parseFile("/media/atom/DISK1160/datasets/ICLNUIM/lr3gt.txt")
    f=open("/media/atom/DISK1160/datasets/ICLNUIM/lr3gtrh.txt","wt")
    for pose in poses1:
        tmp=[]
        # translation part 理解为z轴反向
        tmp.append(pose[0]) #timestamp
        tmp.append(pose[1]) #tx
        tmp.append(pose[2]) #ty
        tmp.append(str(-float(pose[3]))) #tz
        # rotation part 
        sx=float(pose[4])   #qx
        sy=float(pose[5])
        sz=float(pose[6])
        sw=float(pose[7])   #qw
        # 得到Head Pitch Bank
        matrix_lh=R.from_quat([sx,sy,sz,sw]).as_matrix()
        matrix_lh[0,2]=-matrix_lh[0,2]
        matrix_lh[1,2]=-matrix_lh[1,2]
        matrix_lh[2,0]=-matrix_lh[2,0]
        matrix_lh[2,1]=-matrix_lh[2,1]


        # Sz_array=np.diag(np.array([1,1,-1]))
        # scipy_lh=R.from_quat([sx,sy,sz,sw])
        # rot_rh=Sz_array*scipy_lh.as_dcm()*Sz_array
        # print(rot_rh)
        quat_rh=R.from_dcm(matrix_lh).as_quat()



        tmp.append(str(quat_rh[0])) #sx
        tmp.append(str(quat_rh[1])) #sy
        tmp.append(str(quat_rh[2]))  # sz
        tmp.append(str(quat_rh[3]))  # sw
        print(tmp)
        f.writelines(" ".join(x for x in tmp) + "\r\n")
    f.close()
















