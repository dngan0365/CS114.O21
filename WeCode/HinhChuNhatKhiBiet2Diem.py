import math
def Random(A,B,kc2):
    a=(A[1]-B[1])/(A[0]-B[0])
    b=A[1]-A[0]*(A[1]-B[1])/(A[0]-B[0])
    if b !=0:
        cv1=b
        cv2=-b/a
        sin=cv2/math.sqrt(cv1**2+cv2**2)
    else: sin=1/math.sqrt(1+(a+b)**2)
    if sin<0: sin=-sin
    if kc2<0:
        bsau=b+(-math.sqrt(-kc2)/sin)
    else:
        bsau=b+math.sqrt(kc2)/sin
    aquaA=-(A[0]-B[0])/(A[1]-B[1])
    bquaA=A[1]+A[0]*(-aquaA)
    xc=(bquaA-bsau)/(a-aquaA)
    yc=aquaA*xc+bquaA
    C=[xc,yc]
    aquaB=aquaA
    bquaB=B[1]+B[0]*(-aquaB)
    xd=(bquaB-bsau)/(a-aquaB)
    yd=aquaB*xd+bquaB
    #print(xd, yd)
    D=[xd,yd]
    return C,D
def Find2Point(A,B,kc2):
    if A[1]-B[1]==0:
        C=[A[0],A[1]+kc2]
        D=[B[0],B[1]+kc2]
    elif A[0]-B[0]==0:
        C=[A[0]+kc2,A[1]]
        D=[B[0]+kc2,B[1]]
    else:
        C,D=Random(A,B,kc2)
    return C,D

def Xuat(A,B,C,D,a):
    ds=[]
    if a==1:
        if B[0]>A[0]:
            ds=[A,C,D,B]
        else: ds=[A,B,D,C]
    else:
        if B[0]>A[0]:
            ds=[A,B,D,C]
        else: ds=[A,C,D,B]
    print(f'({(round(ds[0][0]))}, {(round(ds[0][1]))}) ({(round(ds[1][0]))}, {(round(ds[1][1]))}) ({(round(ds[2][0]))}, {(round(ds[2][1]))}) ({(round(ds[3][0]))}, {(round(ds[3][1]))})')

def main():
    A=[float(x) for x in input().split()]
    B=[float(x) for x in input().split()]
    kc2=(A[0]-B[0])**2+(A[1]-B[1])**2
    C1,D1=Find2Point(A,B,kc2)
    C2,D2=Find2Point(A,B,-kc2)
    Xuat(A,B,C1,D1,1)
    Xuat(A,B,C2,D2,2)


if __name__=='__main__':
    main()


