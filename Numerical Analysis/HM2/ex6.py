from numpy import log
arrrrrr = [0.124834, 0.089944, 0.065698, 0.048386, 0.035827, 0.026624, 0.019835, 0.014803, 0.011062, 0.0082745]
sum = 0
# for i in range(1,len(arrrrrr)-1):
#     sum += log(abs(arrrrrr[i+1]/arrrrrr[i]))/log(abs(arrrrrr[i]/arrrrrr[i-1]))
#
# print(sum/(len(arrrrrr)-2))


print(log(abs(arrrrrr[9]/arrrrrr[8]))/log(abs(arrrrrr[8]/arrrrrr[7])))