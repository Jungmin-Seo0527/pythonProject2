import tensorflow as tf
import numpy as np

x_data = [[3.0367,3.0425,3.3397,-0.99045,3.423,0.2693,-1.1766,-4.7361,5.3896,3.0758,-1.1489,9.9533],
[2.7176,1.0652,-0.99097,19.1761,-5.5935,6.2652,-1.2459,-4.2913,5.0646,-5.7023,-1.1575,9.2537],
[4.9138,11.7769,-5.8121,-4.0509,-3.2838,10.1371,-0.59905,9.1879,-4.2661,0.24085,7.0565,5.3849],
[0.83343,-5.153,-3.725,8.1058,4.8634,-5.8331,-2.2264,-3.1765,2.9388,18.1387,13.7407,-0.48222],
[-6.4287,-3.4657,-5.6525,7.3222,6.9143,27.0728,-3.5611,-4.8113,-4.348,0.78448,-0.0030512,7.5281],
[13.8886,8.012,11.1369,-4.4268,-5.0791,-3.2375,4.1561,4.3187,-4.7691,-2.5098,4.624,2.0536],
[7.1847,10.3765,1.6401,14.6955,3.2212,-0.22966,-6.3964,9.3798,2.2691,3.1776,-0.32438,8.2528],
[9.7358,5.589,5.1949,-5.2593,7.9016,10.418,2.5522,-6.3092,6.5341,-3.9553,-4.7576,1.7508],
[6.9143,-3.6478,-0.09931,10.3621,6.9537,8.062,0.067512,4.3036,-0.09676,4.4682,2.4592,-1.6708],
[1.8957,6.9168,2.7181,1.8146,0.77212,5.0723,4.2155,7.3778,-2.2394,4.4687,2.5044,-1.1798],
[0.38715,-2.402,1.5092,4.7396,1.72,14.3328,-3.0694,-0.81462,1.5214,4.7808,2.5404,4.8027],
[-0.38407,3.9969,4.0232,0.32064,7.1644,-2.3705,-0.58516,21.9621,6.8355,-2.5812,2.1873,0.86815],
[-0.12033,4.9082,10.0198,3.5026,-4.0332,0.86541,-2.5458,4.4667,0.59111,5.6413,1.3074,-1.1901],
[-1.2799,7.64,6.684,17.836,9.0961,21.7038,13.6462,-0.61059,-1.522,0.35935,0.28155,0.33684],
[-1.3556,2.3997,2.8633,2.4016,7.6155,16.2121,9.3199,3.9137,3.9031,2.5472,-3.3478,5.356],
[3.5287,3.0737,3.4421,12.0861,4.7381,0.6285,5.1205,-1.8116,11.5171,2.225,-0.13706,-3.2485],
[7.6051,-0.88018,-1.8493,-1.0615,0.62603,0.98835,6.1407,1.9872,5.0221,5.8979,-3.0724,15.8918],
[-3.2737,6.7668,5.371,2.1178,-1.7296,4.9087,6.2268,-2.6894,-2.063,5.972,13.8893,0.44607],
[2.538,0.42231,5.7989,2.4851,-2.7478,2.2306,2.6574,0.2634,-1.781,3.3702,0.24794,3.0935],
[6.994,0.18032,3.9655,0.31784,5.5598,5.5493,-0.18505,-2.8686,12.8853,0.78956,2.7917,5.3351],
[3.03,1.9476,9.0884,6.7412,-3.1598,-0.83728,2.0206,6.4183,-1.4002,8.292,1.6292,0.12347],
[-3.4428,-0.48016,7.8566,4.0738,2.2861,24.8564,8.9939,5.3655,1.6589,5.3785,3.3482,5.1957],
[3.7206,4.8677,-3.059,-3.0399,3.4051,6.6543,-0.52846,-0.11423,2.2169,3.949,15.8789,-1.3854],
[0.9894,3.2415,0.75393,0.67471,1.1817,0.071388,5.6709,3.7361,0.19823,-2.6092,1.2673,3.092],
[3.9905,-2.3985,-3.0521,0.84963,2.4394,2.4627,1.4738,-3.8507,-3.4119,6.346,7.9273,-2.5802],
[0.68037,0.79672,-5.7579,10.8021,-5.9477,3.2416,3.5368,6.0629,-4.7425,0.59731,4.4462,-5.9201],
[-4.7808,2.1087,9.7594,-3.7361,11.7889,-3.0925,4.1154,5.4737,-5.6236,10.538,0.60679,-3.399],
[-4.7515,-1.7421,4.0543,6.2684,6.0023,-3.4862,1.5341,-3.3574,15.1437,2.3212,-3.6082,-5.7447],
[5.0354,3.6137,4.5796,-0.6299,-0.99998,9.9146,13.4442,10.6482,-5.8012,-4.5994,-2.5311,3.7207],
[1.1345,17.9121,8.0562,-3.3906,-6.4625,-4.3648,8.7059,12.5361,5.1371,6.2488,2.3997,-0.56447],
[-2.7502,-0.60342,-1.7342,15.6136,14.9576,7.6989,-5.8101,-5.8045,10.5786,3.8036,-3.6834,-2.9722],
[-1.9891,-1.4018,4.7165,-4.9763,-2.2459,0.62165,7.3463,-3.1096,-1.9136,-2.9885,2.8868,-1.3945],
[-3.4617,-5.5307,-2.2833,11.4253,-0.99871,-5.6975,-5.6634,7.2028,-1.7988,4.4583,4.2763,-6.3253],
[-6.4365,6.3598,2.0367,-5.8402,4.6789,5.6548,6.6635,-1.4083,6.3451,0.98689,-0.58971,-4.3267],
[10.9964,4.778,-0.73166,7.571,6.7645,2.1903,-1.7141,12.5902,-5.2453,13.4218,-0.77401,-3.7408],
[8.6192,-5.5129,0.12131,31.9228,10.2918,7.2259,-5.4469,-3.5394,-1.3182,32.6301,0.54229,30.9541],
[-3.7572,1.2489,16.3421,7.958,-0.47686,-4.573,-2.9807,5.1713,8.4391,-5.6329,-2.8319,-0.94483],
[6.2146,7.6489,11.6014,0.10441,-5.8534,-3.1193,-3.5833,17.0007,4.1134,9.8963,-1.843,-4.25],
[-3.7727,0.020527,2.1257,4.3105,12.8783,5.0592,8.8969,-3.94,-4.6955,-2.7594,7.1158,7.2056],
[-2.6549,-0.26004,10.2555,5.761,13.9678,7.5244,0.50197,6.9404,7.3291,1.2771,-5.9211,27.2784],
[5.5195,7.7761,0.47714,3.9052,35.4852,8.994,11.0953,-5.1867,10.6583,5.798,5.97,-5.7642],
[12.6401,-3.235,-4.168,4.3641,4.01,-1.7028,2.2527,7.8847,14.8453,17.6986,1.174,3.149],
[0.78204,7.6639,4.6016,-1.4011,3.4639,14.9064,4.5344,1.6616,2.9906,9.8005,2.3532,6.7219],
[-2.0277,8.1101,4.3989,-0.61637,2.3185,-2.476,4.5107,7.9178,3.4303,8.4625,-2.9387,-0.2983],
[3.737,7.4865,5.7865,8.0628,0.13527,7.7094,6.5283,1.939,3.4566,-1.8388,0.39755,8.5774],
[14.7043,-2.6301,0.82521,2.9108,1.0686,3.3226,9.481,5.9597,-3.6075,1.0032,-0.91889,7.205],
[-0.041086,4.4843,2.8592,-0.56336,-0.67778,5.0131,10.6882,7.2693,9.2343,8.4412,10.7164,-0.13888],
[-1.2541,0.89787,1.0454,1.0454,0.37058,5.5466,5.9859,5.8715,13.7113,10.1236,5.229,2.5572],
[8.377,6.3075,-2.8922,8.8444,8.0994,6.5659,6.404,5.459,7.6354,2.462,9.5073,-2.1173],
[16.9889,1.3172,1.2943,-2.6669,14.8529,0.02552,-1.2645,-0.0095414,-0.059363,3.0951,11.0695,1.8402],
[8.668,10.8616,-2.7717,9.0759,-3.0839,15.0278,11.7375,3.4642,-1.3439,8.4602,13.332,-2.461],
[-1.1857,11.8064,6.6318,0.65487,2.3052,1.2988,12.4337,4.5825,-1.3202,1.3764,6.6253,1.922],
[-1.3126,2.7313,1.0475,5.2481,14.3249,1.6992,8.9189,1.9954,6.1279,11.851,0.35319,-1.5829],
[5.5791,2.4373,5.8665,3.8697,4.7422,1.1744,5.1095,9.9944,-2.8003,-1.0716,2.3167,14.4973],
[-0.26534,7.2429,2.931,0.68542,-3.4813,-0.50061,11.7005,4.9651,4.4146,8.846,16.1458,3.4386],
[2.0832,3.8488,3.3328,5.6005,3.5624,7.6956,-2.9478,-2.9588,5.0367,18.9567,0.46326,1.4384],
[4.3772,3.5248,7.3014,-1.5919,2.6442,7.3464,1.1529,2.3725,3.28,1.3621,12.5696,1.9763],
[1.7754,-1.2336,2.3919,1.6555,5.6213,-2.4985,-2.5511,1.5386,4.802,5.2613,3.3652,-3.5027],
[-3.477,12.4105,15.9297,-2.3454,1.4526,3.3066,-5.7917,7.0732,-6.0428,5.6982,7.3475,11.8635],
[-4.7683,1.3595,8.5958,-5.567,-4.5077,4.0047,5.1069,-3.3632,8.5255,-2.9592,8.2515,11.9283],
[-3.8813,5.9749,3.2003,-1.5935,-4.73,-1.6705,7.0581,13.9128,12.0206,-1.7436,4.1973,-1.5443],
[16.2287,4.703,-3.6096,-4.0817,2.4206,7.8797,10.1809,-0.78423,-0.65366,5.789,5.7207,20.6175],
[-5.7968,-4.4614,-2.1124,6.9017,3.6551,11.8799,9.8806,-3.3925,-6.2721,-4.1113,14.3347,16.3985],
[11.2165,4.1989,4.2944,-0.90813,-2.2811,-0.78012,-1.4207,15.2585,10.7757,17.9342,-5.9566,-5.969],
[15.3873,8.1656,-3.4378,-2.3996,-0.032134,-1.2264,2.835,-4.8374,-1.7312,2.8489,7.4493,-1.296],
[-1.1775,-2.5872,5.7555,-1.8112,-1.6925,-3.8196,-2.0539,5.4791,0.71531,-5.5227,-5.5756,8.4799],
[0.22624,9.9942,9.2969,-6.3067,-6.2615,13.8361,4.1797,-5.4827,4.0595,3.8187,8.964,-1.9653],
[7.5739,0.5064,-0.8099,-5.305,13.8663,4.19,-1.1425,3.8558,15.857,1.835,-2.4353,5.7093],
[-5.236,15.0625,-1.1055,-4.6189,7.0158,-5.6168,0.84028,10.7234,15.1803,3.184,-6.3804,-4.4849],
[-2.6304,9.7348,0.85775,10.7986,-3.7419,1.0932,15.1195,5.6596,-1.7036,-5.3311,-3.7169,2.1753],
[7.8283,-5.7199,-3.3445,-3.3192,9.0939,3.2413,5.4124,-0.29078,-6.5121,-3.3154,-5.8478,14.1853],
[1.4893,4.4249,-3.3152,-4.1362,-4.618,-0.99245,0.12541,1.5172,5.8933,2.0961,4.399,-3.9252],
[-4.7001,-3.8382,7.4697,7.2603,-4.953,-1.4763,23.8932,11.8545,8.6527,3.6107,-0.80485,2.8935],
[11.568,2.0045,-5.75,10.4185,8.6242,16.3724,0.27206,1.0019,10.1626,6.8039,13.1875,-5.406],
[5.5152,2.3888,10.2367,-5.5387,8.49,-3.9677,-4.9543,6.8427,1.3885,-2.9718,0.42351,4.0118],
[13.348,10.7654,1.3831,1.341,0.75095,7.2454,4.9835,-1.3584,3.4549,13.6587,4.3072,0.48311],
[4.8479,10.1021,0.45195,3.6066,-2.4043,8.2075,4.413,-0.36222,1.0337,-3.0057,7.9821,5.2649],
[3.7098,3.9289,-2.8195,-0.18262,2.3993,4.6452,8.388,5.3909,-0.36097,8.7621,5.9372,0.41473],
[0.78335,-1.3732,0.99386,3.744,13.8003,-3.1251,-0.55913,0.55172,1.4597,1.1079,5.2027,5.8305],
[-3.0187,0.040852,-2.8956,6.3594,-1.1666,2.076,1.2124,-0.83232,-0.35626,2.1433,5.9427,2.9999],
[5.3046,3.6668,5.2748,-0.61752,-1.6972,0.71706,0.76586,0.68916,-1.7083,4.3527,7.7306,10.8064],
[9.056,4.7593,1.9897,0.61157,13.9585,11.0181,-2.9643,5.7871,18.0758,9.9535,7.0337,1.9518],
[4.8849,1.0256,10.4214,-2.841,7.5366,-0.1797,2.0712,-2.6539,9.9228,0.61259,-0.83709,0.47819],
[-1.21,1.9062,6.7174,0.62409,7.8748,7.5468,-2.9652,4.2014,-3.3742,14.9388,19.3905,3.0816],
[-1.6682,7.7575,15.134,-2.7705,-0.8257,12.4892,2.719,-0.18209,0.92839,0.93133,16.2854,4.8797],
[-2.9457,-0.10741,14.9571,-0.05641,-1.5353,1.0415,0.81805,5.1292,9.3131,-0.36719,20.3384,0.01826],
[3.8101,16.5118,-0.17167,-3.3237,1.9899,3.1437,7.6055,1.5449,4.1945,-0.23185,1.9951,5.7359],
[-2.9126,-1.8885,1.2567,17.1922,0.44896,3.7616,0.8538,0.096393,-3.8827,-1.2701,6.8394,3.3792],
[4.9133,3.8731,8.2275,1.0869,1.1738,1.5088,1.7914,3.4416,1.8737,6.4722,-3.3505,-3.3952],
[2.5214,12.5357,0.55296,2.4174,2.6331,1.7155,3.0866,-2.3185,3.2559,13.646,0.45209,0.31666],
[4.5632,1.8324,20.1472,0.014071,-0.25074,-2.9254,2.1634,-0.12727,2.8592,-3.0436,-2.5062,0.97164],
[3.1006,6.8111,4.0717,-3.5349,-3.8978,8.777,9.0308,-2.6639,0.88848,1.8004,-6.1228,3.2095],
[-6.425,4.7442,7.9479,12.144,-5.1796,0.81431,8.2419,-5.5298,-4.5799,3.18,1.8195,-3.5091],
[4.2286,-3.4039,8.4526,18.6688,-5.9513,2.5168,4.3826,-3.8129,-5.0906,-2.1983,7.6085,16.8863],
[7.6594,-4.0092,4.8435,-3.762,7.0295,4.3282,-4.1208,-6.2188,0.25356,13.5215,24.8373,-1.5944],
[-1.1692,2.4487,1.9442,8.6872,-6.0829,-4.6879,-2.3124,6.3141,6.4912,5.4856,5.5882,-3.9317],
[-6.3263,-4.2778,6.6373,7.5313,19.8085,1.7495,2.3944,-1.8158,-2.4162,-1.6051,-1.8033,6.751],
[5.1751,13.1099,-6.4023,-6.4334,7.4631,6.4708,-3.6782,-2.2757,-1.3167,-1.743,0.81408,-5.032],
[-1.8096,3.2806,4.5056,-3.5436,-1.0458,-2.6753,5.5953,-2.6397,-3.9371,-5.9264,-2.4466,2.0232],
[-0.93568,-5.6378,-5.7793,5.5023,-1.0314,34.9214,16.9559,-6.5376,-6.3289,8.5091,2.5664,-5.4477]]
y_data = [[9.0158,6.3743],
[9.1873,5.5377],
[0.82465,8.022],
[13.4302,2.0033],
[0.29173,7.6317],
[11.3502,6.5421],
[12.6948,7.3433],
[17.7465,6.6591],
[2.4135,7.1374],
[8.9445,6.4098],
[12.9779,6.7838],
[1.1766,2.2395],
[3.3596,9.2853],
[10.3046,6.7336],
[13.356,0.81461],
[4.5015,2.8419],
[18.2753,2.291],
[4.9724,6.7629],
[12.9698,7.0368],
[16.7421,7.273],
[0.38869,5.8375],
[18.4175,0.91678],
[11.0912,9.308],
[3.9891,5.2532],
[2.5348,7.4873],
[6.2934,1.8717],
[19.6079,7.1283],
[16.513,6.8322],
[13.788,5.3088],
[3.7771,4.9302],
[11.1908,8.2828],
[4.0574,5.2775],
[16.1562,3.551],
[10.9551,7.1744],
[4.0502,6.4376],
[0.0017803,5.1318],
[11.3966,0.070367],
[17.8494,8.3319],
[15.5033,7.8814],
[7.4726,1.5231],
[7.0452,6.451],
[18.6387,0.93321],
[14.7756,0.55267],
[15.1432,4.6349],
[0.90009,8.4203],
[3.2942,1.1507],
[5.4312,3.1439],
[12.1218,6.7747],
[19.7528,9.9326],
[15.1507,2.7506],
[19.0803,4.1108],
[4.3325,6.2913],
[0.29738,0.433],
[3.6052,2.0047],
[14.3872,4.4287],
[16.9099,3.8979],
[16.751,7.4842],
[11.6772,1.6057],
[10.5768,4.6267],
[7.5909,0.9323],
[5.1829,3.3584],
[7.5022,1.4626],
[6.3354,2.8123],
[16.4025,3.4209],
[17.44,2.6803],
[15.5086,6.0921],
[0.35938,7.0151],
[0.31505,6.8389],
[17.558,4.3181],
[12.6269,5.8604],
[4.5482,7.8465],
[5.7527,9.2438],
[5.9695,5.363],
[6.6729,2.3729],
[10.9048,1.0769],
[2.7431,0.94427],
[6.2177,8.1264],
[10.2712,8.6648],
[19.6097,3.2665],
[4.3923,5.1822],
[7.0601,8.5948],
[5.2004,8.4372],
[11.656,7.1941],
[6.8705,0.092739],
[3.8489,5.0739],
[0.48484,5.5004],
[5.5237,6.9624],
[17.6271,0.24681],
[6.8241,4.2141],
[1.6002,0.79354],
[1.4475,9.0034],
[19.3862,3.9131],
[6.2717,5.5331],
[15.841,7.9831],
[17.2652,7.9796],
[0.12753,9.199],
[0.35924,0.29416],
[14.229,5.3841],
[10.4918,5.0224],
[1.3134,2.3004]]
# Evaluation our model using this test dataset
x_test = [[3.0367,3.0425,3.3397,-0.99045,3.423,0.2693,-1.1766,-4.7361,5.3896,3.0758,-1.1489,9.9533]]
y_test = [[9.0158,6.3743]]
          
X = tf.placeholder("float", [None, 12])
Y = tf.placeholder("float", [None, 2])
W = tf.Variable(tf.random_normal([12, 2]))
b = tf.Variable(tf.random_normal([2]))

hypothesis = tf.nn.softmax(tf.matmul(X, W)+b)
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(cost)

# Correct prediction Test model
#prediction = tf.arg_max(hypothesis, 1)
#is_correct = tf.equal(prediction, tf.arg_max(Y, 1))
#accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

# Launch graph
with tf.Session() as sess:
   # Initialize TensorFlow variables
   sess.run(tf.global_variables_initializer())
   for step in range(2001):
       cost_val, W_val, _ = sess.run([cost, W, optimizer], 
                       feed_dict={X: x_data, Y: y_data})
       if step%200==0:
          print(step, cost_val)

   # predict
 #  print("Prediction:", sess.run(prediction, feed_dict={X: x_test}))
   # Calculate the accuracy

  # print("Accuracy: ", sess.run(accuracy, feed_dict={X: x_test, Y: y_test}))
