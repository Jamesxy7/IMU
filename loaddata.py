# -*- coding: utf-8 -*-

import pandas as pd


def loadfile(filename):
    data = pd.read_csv(filename, sep=' ', header=1)

## 导入IMU数据
data1 = pd.read_csv('imu.txt', sep=' ', header=0)
dt_IMU = data1.dt_record.tolist()
IMU_id = data1.IMU_id.tolist()
ax = data1.ax.tolist()
ay = data1.ay.tolist()
az = data1.az.tolist()
gx = data1.gx.tolist()
gy = data1.gy.tolist()
gz = data1.gz.tolist()
INS_vx = data1.INS_vx.tolist()
INS_vy = data1.INS_vy.tolist()
INS_vz = data1.INS_vz.tolist()
INS_E = data1.INS_E.tolist()
INS_N = data1.INS_N.tolist()
INS_U = data1.INS_U.tolist()
roll = data1.roll.tolist()
pitch = data1.pitch.tolist()
yaw = data1.yaw.tolist()

print(dt_IMU, yaw)

## 导入RTK数据
data2 = pd.read_csv('RTK.txt',sep=' ', header=0)
dt_RTK = data2.dt_record.tolist()
RTK_E = data2.RTK_E.tolist()
RTK_N = data2.RTK_N.tolist()
RTK_U = data2.RTK_U.tolist()
Speed = data2.Speed.tolist()
Heading = data2.Heading.tolist()
print(dt_RTK,Heading)