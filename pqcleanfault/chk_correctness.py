
import params

def chk_as_plus_s(pkpv,a,skpv):
    pkpv_computed=[[0 for _ in range(params.KYBER_N)] for _ in range(params.KYBER_K)]
    for i in range(int(params.KYBER_N/4)):
        base=4*i
        zeta=params.ZETA[64+i]*params.KYBER_RINV
        for j in range(params.KYBER_K):
            #case 0
            cur=0
            for k in range(params.KYBER_K):
                cur+=a[j][k][base+1]*skpv[k][base+1]*zeta
                cur+=a[j][k][base]*skpv[k][base]
                cur=cur%params.KYBER_Q
            cur+=skpv[j][base]
            cur=cur%params.KYBER_Q
            pkpv_computed[j][base]=cur
            #case 1
            cur=0
            for k in range(params.KYBER_K):
                cur+=a[j][k][base+0]*skpv[k][base+1]
                cur+=a[j][k][base+1]*skpv[k][base]
                cur=cur%params.KYBER_Q
            cur+=skpv[j][base+1]
            cur=cur%params.KYBER_Q
            pkpv_computed[j][base+1]=cur
            #case 2
            cur=0
            for k in range(params.KYBER_K):
                cur+=a[j][k][base+3]*skpv[k][base+3]*(-zeta)
                cur+=a[j][k][base+2]*skpv[k][base+2]
                cur=cur%params.KYBER_Q
            cur+=skpv[j][base+2]
            cur=cur%params.KYBER_Q
            pkpv_computed[j][base+2]=cur
            #case 3
            cur=0
            for k in range(params.KYBER_K):
                cur+=a[j][k][base+2]*skpv[k][base+3]
                cur+=a[j][k][base+3]*skpv[k][base+2]
                cur=cur%params.KYBER_Q
            cur+=skpv[j][base+3]
            cur=cur%params.KYBER_Q
            pkpv_computed[j][base+3]=cur

    for i in range(params.KYBER_K):
        for j in range(params.KYBER_N):
            if pkpv_computed[i][j]!=pkpv[i][j]:
                print("chk_as_plus_s error: Input variables wrong! Please check!\n")
                return True
    print("chk_as_plus_s check passed!\n")
    return False