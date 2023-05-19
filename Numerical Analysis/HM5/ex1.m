clc clear
close all

C=[2 1 0 0 0;
-1 2 1 0 0;
0 -1 2 1 0;
0 0 -1 2 1;
0 0 0 -1 2]
b=[3 2 2 2 1];
b=b'
n=5
iC=inv(C)
X=iC*b
  


