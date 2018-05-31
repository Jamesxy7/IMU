#coding：UTF-8

import numpy

def LoadData(filename):
    f = open(filename, 'r')
    dt_record = []
    IMU_id = []
    ax, ay, az =[],[],[]
    gx,gy,gz = [],[],[]
    INS_vx, INS_vy, INS_vz = [],[],[]
    INS_E,INS_N, INS_U = [],[],[]
    roll,pitch, yaw = [],[],[]

    next(f)
    for line in f.readlines():
        lineArr = line.strip().split()
        dt_record.append(lineArr[0])
        IMU_id.append(lineArr[1])
        ax.append(lineArr[2])
        ay.append(lineArr[3])
        az.append(lineArr[4])
        gx.append(lineArr[5])
        gy.append(lineArr[6])
        gz.append(lineArr[7])
        INS_vx.append(lineArr[8])
        INS_vy.append(lineArr[9])
        INS_vz.append(lineArr[10])
        INS_E.append(lineArr[11])
        INS_N.append(lineArr[12])
        INS_U.append(lineArr[13])
        roll.append(lineArr[14])
        pitch.append(lineArr[15])
        yaw.append(lineArr[16])
    f.close()
    print(yaw)
    return dt_record,IMU_id,ax,ay,az,gx,gy,gz,INS_E,INS_N,INS_U,roll,pitch,yaw

IMU = LoadData('imu.txt')

