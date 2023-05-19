clc clear
close all


A=[8 3 2;16 6 4.001;4 1.501 1]
B=[20 ;40.02 ;10.01];
P=[1; 1; 1];
n=10;
%format long; A,B;
e=10^-5;
N=size(A,1)
X=zeros(N,1);
Y=zeros(N,1);
C = [A B];



C(2,:) = C(2,:) -2*C(1,:); %second row minus double first row
C(3,:) = C(3,:) -0.5*C(1,:); %third row minus half first row
t = C(2,:);  % swap third and secon row
C(2,:) = C(3,:);
C(3,:) = t;

A(:,1) = C(:,1);
A(:,2) = C(:,2);
A(:,3) = C(:,3);
B = C(:,4);

% Matrix is now diagonally dominant
A
B

for j = 1:n
    for i = 1:N
        X(i) = (B(i)/A(i,i)) - (A(i,[1:i-1,i+1:N])*P([1:i-1,i+1:N]))/A(i,i);
        P(i) = X(i);
    end
    if abs(Y-X)<e
      break
    endif
    Y=X;
end

X