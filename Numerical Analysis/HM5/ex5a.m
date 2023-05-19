A=[8 3 2;16 6 4.001;4 1.501 1]
B=[20 ;40.02 ;10.01]
N=length(B)
X=zeros(N,1);
C=[A B];
C(2,:) = C(2,:) -2*C(1,:); %second row minus double first row
C(3,:) = C(3,:) -0.5*C(1,:); %third row minus half first row
t = C(2,:);  % swap third and secon row
C(2,:) = C(3,:);
C(3,:) = t;

Aug=C
for j =1:N
  Aug(j,:) = Aug(j,:)/Aug(j,j);
  for i =1:N
    if i~=j
      m = Aug(i,j);
      Aug(i,:) = Aug(i,:)-m*Aug(j,:);
    endif
  endfor
endfor
Aug