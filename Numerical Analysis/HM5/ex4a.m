clc clear
close all

A=[0 1 5 -7 23 -1 7 8 1 -5;17 0 -24 -75 100 -18 10 -8 9 -50;
3 -2 15 0 -78 -90 -70 18 -75 1;5 5 -10 0 -72 -1 80 -3 10 -18;
100 -4 -75 -8 0 83 -10 -75 3 -8;70 85 -4 -9 2 0 3 -17 -1 -21;
1 15 100 -4 -23 13 0 7 -3 17;16 2 -7 89 -17 11 -73 0 -8 -23;
51 47 -3 5 -10 18 -99 -18 0 12;1 1 1 1 1 1 1 1 1 0];
b=[10 -40 -17 43 -53 12 -60 100 0 100];
b=b';
n=10;
C=[A b]

t=C(1,:);
C(1,:) = C(5,:);   %swap first and fifth  row
C(5,:) = t;

t=C(2,:);
C(2,:) = C(6,:);   %swap second and sixth  row
C(6,:) = t;

t=C(3,:);
C(3,:) = C(7,:);   %swap third and seven  row
C(7,:) = t;

t=C(4,:);
C(4,:) = C(6,:);   %swap fourth and sixth row
C(6,:) = t;

t=C(6,:);
C(6,:) = C(9,:);   %swap six and ninght  row
C(9,:) = t;

t=C(7,:);
C(7,:) = C(8,:);   %swap seven and eight  row
C(8,:) = t;

t=C(8,:);
C(8,:) = C(9,:);   %swap eight and ninght  row
C(9,:) = t;


C(10,:) = C(10,:)-1 ;

C(9,:) = C(9,:)+C(1,:)+C(3,:)
[L,U]=lu(C);

x = zeros(n,1);                                             
x(n) = U(n,n+1)/U(n,n);

for i=n-1:-1:1
    summ = 0;
    for j=i+1:n
        summ = summ + U(i,j)*x(j,:);
        x(i,:) = (U(i,n+1) - summ)/U(i,i);
    end
end
x

