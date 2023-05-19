clc clear
close all

C=[3 -1 3;1 2 -1;1 2 0]
b=[11 2 0];
b=b'
n=3

A=[C b];

[L,U]=lu(A);

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


% strait forward method
A=[C b];

A(2,:) = A(2,:) - (A(2,1)/A(1,1))*A(1,:);
A(3,:) = A(3,:) - (A(3,1)/A(1,1))*A(1,:);

A(3,:) = A(3,:) - (A(3,2)/A(2,2))*A(2,:);
A
x3=A(3,4)/A(3,3)
x2=(A(2,4)-x3*A(2,3))/A(2,2)
x1=(A(1,4)-x2*A(1,2)-x3*A(1,3))/A(1,1)


                                     
