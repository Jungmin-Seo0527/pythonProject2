import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pylab as plt

def look_structure_position(XXX,YYY,ZZZ):
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111, projection='3d') # Axe3D object

    x1 = [0,42]
    y1= [0,0]
    z1 = [0,0]
    ax.plot(x1, y1, z1,'k')

    x2 = [0,42]
    y2 = [24,24]
    z2 = [0,0]
    ax.plot(x2, y2, z2,'k')
    x3 = [42,42]
    y3 = [0,24]
    z3 = [0,0]
    ax.plot(x3, y3, z3,'k')
    x4 = [0,0]
    y4 = [0,24]
    z4 = [0,0]
    ax.plot(x4, y4, z4,'k')
    x5 = [0,0]
    y5 = [0,0]
    z5 = [0,6]
    ax.plot(x5, y5, z5,'k')
    x6 = [0,0]
    y6 = [24,24]
    z6 = [0,6]
    ax.plot(x6, y6, z6,'k')
    x7 = [42,42]
    y7 = [24,24]
    z7 = [0,6]
    ax.plot(x7, y7, z7,'k')
    x8 = [42,42]
    y8 = [0,0]
    z8 = [0,6]
    ax.plot(x8, y8, z8,'k')


    x9 = [0,42]
    y9 = [0,0]
    z9 = [3,3]
    ax.plot(x9, y9, z9,'k')

    x10 = [0,0]
    y10 = [0,24]
    z10 = [3,3]
    ax.plot(x10, y10, z10,'k')

    x11 = [42,42]
    y11 = [0,24]
    z11 = [3,3]
    ax.plot(x11, y11, z11,'k')

    x12 = [0,42]
    y12 = [24,24]
    z12 = [3,3]
    ax.plot(x12, y12, z12,'k')


    x13 = [0,42]
    y13 = [0,0]
    z13 = [6,6]
    ax.plot(x13, y13, z13,'k')
    x14 = [0,0]
    y14 = [0,24]
    z14 = [6,6]
    ax.plot(x14, y14, z14,'k')
    x15 = [0,42]
    y15 = [24,24]
    z15 = [6,6]
    ax.plot(x15, y15, z15,'k')
    x16 = [42,42]
    y16 = [0,24]
    z16 = [6,6]
    ax.plot(x16, y16, z16,'k')
    ##여기까지가 전체 틀
    ##아래서 부터는 방


    x17 = [9,9]
    y17 = [0,9]
    z17 = [0,0]
    ax.plot(x17, y17, z17,'k')
    x18 = [18,18]
    y18 = [0,9]
    z18 = [0,0]
    ax.plot(x18, y18, z18,'k')
    x19 = [0,18]
    y19 = [9,9]
    z19 = [0,0]
    ax.plot(x19, y19, z19,'k')

    x20 = [9,9]
    y20 = [0,9]
    z20 = [3,3]
    ax.plot(x20, y20, z20,'k')
    x21 = [18,18]
    y21 = [0,9]
    z21 = [3,3]
    ax.plot(x21, y21, z21,'k')
    x22 = [0,18]
    y22 = [9,9]
    z22 = [3,3]
    ax.plot(x22, y22, z22,'k')

    x23 = [9,9]
    y23 = [0,9]
    z23 = [6,6]
    ax.plot(x23, y23, z23,'k')
    x24 = [18,18]
    y24 = [0,9]
    z24 = [6,6]
    ax.plot(x24, y24, z24,'k')
    x25 = [0,18]
    y25 = [9,9]
    z25 = [6,6]
    ax.plot(x25, y25, z25,'k')

    x26 = [9,9]
    y26 = [9,9]
    z26 = [0,6]
    ax.plot(x26, y26, z26,'k--')
    x27 = [18,18]
    y27 = [9,9]
    z27 = [0,6]
    ax.plot(x27, y27, z27,'k--')
    x28 = [9,9]
    y28 = [0,0]
    z28 = [0,6]
    ax.plot(x28, y28, z28,'k--')
    x29 = [18,18]
    y29 = [0,0]
    z29 = [0,6]
    ax.plot(x29, y29, z29,'k--')
    x29_2 = [0,0]
    y29_2 = [9,9]
    z29_2 = [0,6]
    ax.plot(x29_2, y29_2, z29_2,'k--')

    x30 = [24,24]
    y30 = [0,9]
    z30 = [0,0]
    ax.plot(x30, y30, z30,'k')
    x31 = [33,33]
    y31 = [0,9]
    z31 = [0,0]
    ax.plot(x31, y31, z31,'k')
    x32 = [24,42]
    y32 = [9,9]
    z32 = [0,0]
    ax.plot(x32, y32, z32,'k')

    x33 = [24,24]
    y33 = [0,9]
    z33 = [3,3]
    ax.plot(x33, y33, z33,'k')
    x34 = [33,33]
    y34 = [0,9]
    z34 = [3,3]
    ax.plot(x34, y34, z34,'k')
    x35 = [24,42]
    y35 = [9,9]
    z35 = [3,3]
    ax.plot(x35, y35, z35,'k')


    x36 = [24,24]
    y36 = [0,9]
    z36 = [6,6]
    ax.plot(x36, y36, z36,'k')
    x37 = [33,33]
    y37 = [0,9]
    z37 = [6,6]
    ax.plot(x37, y37, z37,'k')
    x38 = [24,42]
    y38 = [9,9]
    z38 = [6,6]
    ax.plot(x38, y38, z38,'k')

    x39 = [24,24]
    y39 = [9,9]
    z39 = [0,6]
    ax.plot(x39, y39, z39,'k--')
    x40 = [33,33]
    y40 = [9,9]
    z40 = [0,6]
    ax.plot(x40, y40, z40,'k--')
    x41 = [24,24]
    y41 = [0,0]
    z41 = [0,6]
    ax.plot(x41, y41, z41,'k--')
    x42 = [33,33]
    y42 = [0,0]
    z42 = [0,6]
    ax.plot(x42, y42, z42,'k--')
    x43 = [42,42]
    y43 = [9,9]
    z43 = [0,6]
    ax.plot(x43, y43, z43,'k--')

    ##뒤에거 y=15쪽



    x17_3 = [9,9]
    y17_3 = [15,24]
    z17_3 = [0,0]
    ax.plot(x17_3, y17_3, z17_3,'k')
    x18_3 = [18,18]
    y18_3 = [15,24]
    z18_3 = [0,0]
    ax.plot(x18_3, y18_3, z18_3,'k')
    x19_3 = [0,18]
    y19_3 = [15,15]
    z19_3 = [0,0]
    ax.plot(x19_3, y19_3, z19_3,'k')

    x20_3 = [9,9]
    y20_3 = [15,24]
    z20_3 = [3,3]
    ax.plot(x20_3, y20_3, z20_3,'k')
    x21_3 = [18,18]
    y21_3 = [15,24]
    z21_3 = [3,3]
    ax.plot(x21_3, y21_3, z21_3,'k')
    x22_3 = [0,18]
    y22_3 = [15,15]
    z22_3 = [3,3]
    ax.plot(x22_3, y22_3, z22_3,'k')

    x23_3 = [9,9]
    y23_3 = [15,24]
    z23_3 = [6,6]
    ax.plot(x23_3, y23_3, z23_3,'k')
    x24_3 = [18,18]
    y24_3 = [15,24]
    z24_3 = [6,6]
    ax.plot(x24_3, y24_3, z24_3,'k')
    x25_3 = [0,18]
    y25_3 = [15,15]
    z25_3 = [6,6]
    ax.plot(x25_3, y25_3, z25_3,'k')

    x26_3 = [0,0]
    y26_3 = [15,15]
    z26_3 = [0,6]
    ax.plot(x26_3, y26_3, z26_3,'k--')
    x27_3 = [9,9]
    y27_3 = [15,15]
    z27_3 = [0,6]
    ax.plot(x27_3, y27_3, z27_3,'k--')
    x28_3 = [18,18]
    y28_3 = [15,15]
    z28_3 = [0,6]
    ax.plot(x28_3, y28_3, z28_3,'k--')
    x29_3 = [18,18]
    y29_3 = [24,24]
    z29_3 = [0,6]
    ax.plot(x29_3, y29_3, z29_3,'k--')
    x29_2_3 = [18,18]
    y29_2_3= [9,9]
    z29_2_3 = [0,6]
    ax.plot(x29_2_3, y29_2_3, z29_2_3,'k--')
    #여기까지가 좌측상단

    x30_3 = [24,24]
    y30_3 = [15,24]
    z30_3 = [0,0]
    ax.plot(x30_3, y30_3, z30_3,'k')
    x31_3 = [33,33]
    y31_3 = [15,24]
    z31_3 = [0,0]
    ax.plot(x31_3, y31_3, z31_3,'k')
    x32_3 = [24,42]
    y32_3 = [15,15]
    z32_3 = [0,0]
    ax.plot(x32_3, y32_3, z32_3,'k')

    x33_3 = [24,24]
    y33_3 = [15,24]
    z33_3 = [3,3]
    ax.plot(x33_3, y33_3, z33_3,'k')
    x34_3 = [33,33]
    y34_3 = [15,24]
    z34_3 = [3,3]
    ax.plot(x34_3, y34_3, z34_3,'k')
    x35_3 = [24,42]
    y35_3 = [15,15]
    z35_3 = [3,3]
    ax.plot(x35_3, y35_3, z35_3,'k')


    x36_3 = [24,24]
    y36_3 = [15,24]
    z36_3 = [6,6]
    ax.plot(x36_3, y36_3, z36_3,'k')
    x37_3 = [33,33]
    y37_3 = [15,24]
    z37_3 = [6,6]
    ax.plot(x37_3, y37_3, z37_3,'k')
    x38_3 = [24,42]
    y38_3 = [15,15]
    z38_3 = [6,6]
    ax.plot(x38_3, y38_3, z38_3,'k')

    x39_3 = [24,24]
    y39_3 = [15,15]
    z39_3 = [0,6]
    ax.plot(x39_3, y39_3, z39_3,'k--')
    x40_3 = [33,33]
    y40_3 = [15,15]
    z40_3 = [0,6]
    ax.plot(x40_3, y40_3, z40_3,'k--')
    x41_3 = [42,42]
    y41_3 = [15,15]
    z41_3 = [0,6]
    ax.plot(x41_3, y41_3, z41_3,'k--')
    x42_3 = [24,24]
    y42_3 = [24,24]
    z42_3 = [0,6]
    ax.plot(x42_3, y42_3, z42_3,'k--')

    x43_3 = [33,33]
    y43_3 = [24,24]
    z43_3 = [0,6]
    ax.plot(x43_3, y43_3, z43_3,'k--')

    ##이제 센서 위치 점찍기

    x=[4.5,13.5,28.5,37.5,4.5,13.5,28.5,37.5,21,4.5,13.5,28.5,37.5,4.5,13.5,28.5,37.5,21]
    y=[4.5,4.5,4.5,4.5,19.5,19.5,19.5,19.5,12,4.5,4.5,4.5,4.5,19.5,19.5,19.5,19.5,12]
    z=[2.9,2.9,2.9,2.9,2.9,2.9,2.9,2.9,2.9,5.9,5.9,5.9,5.9,5.9,5.9,5.9,5.9,5.9]
    ax.scatter(x,y,z,c='red',s=50)

    #졸라맨 그리기
    #머리
    xp = [XXX]
    yp = [YYY]
    zp = [ZZZ+0.5]
    ax.scatter(xp,yp,zp,c='blue',s=150)
    #몸
    xp_m=[XXX,XXX]
    yp_m=[YYY,YYY]
    zp_m=[ZZZ+0.5-0.5,ZZZ+0.5]
    ax.plot(xp_m, yp_m, zp_m,'b')
    #왼팔
    xp_LH=[XXX-0.9, XXX]
    yp_LH=[YYY,YYY]
    zp_LH=[ZZZ+0.5-0.5+0.2+0.2+0.06, ZZZ+0.5-0.5+0.2+0.06]
    ax.plot(xp_LH, yp_LH, zp_LH,'b')
    #오른팔
    xp_RH=[XXX+0.9, XXX]
    yp_RH=[YYY,YYY]
    zp_RH=[ZZZ+0.5-0.5+0.2+0.2+0.06, ZZZ+0.5-0.5+0.2+0.06]
    ax.plot(xp_RH, yp_RH, zp_RH,'b')
    #오른발
    xp_RL=[XXX+0.7, XXX]
    yp_RL=[YYY,YYY]
    zp_RL=[ZZZ+0.5-0.5-0.5, ZZZ+0.5-0.5]
    ax.plot(xp_RL, yp_RL, zp_RL,'b')
    #왼
    xp_LL=[XXX-0.7, XXX]
    yp_LL=[YYY,YYY]
    zp_LL=[ZZZ+0.5-0.5-0.5, ZZZ+0.5-0.5]
    ax.plot(xp_LL, yp_LL, zp_LL,'b')


    #면 그리기

    for i in np.arange(18,24,0.3):
        a=[i,i]
        b=[0,24]
        c=[3,3]
        ax.plot(a, b, c,'lightgray')
    for i in np.arange(9,15,0.3):
        a=[0,42]
        b=[i,i]
        c=[3,3]
        ax.plot(a, b, c,'lightgray')
    for i in np.arange(18,24,0.3):
        a=[i,i]
        b=[0,24]
        c=[0,0]
        ax.plot(a, b, c,'lightgray')
    for i in np.arange(9,15,0.3):
        a=[0,42]
        b=[i,i]
        c=[0,0]
        ax.plot(a, b, c,'lightgray')
    ##for i in range(0,42):
    ##    a=[i,i]
    ##    b=[0,24]
    ##    c=[6,6]
    ##    ax.plot(a, b, c,'k--')
    plt.xlim(0,42)
    plt.ylim(0,24)
    plt.title("ax.plot")
    plt.show()
    ##가운데 2층 흐릿하게 색칠할수있을까??
