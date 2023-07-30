import modeqs
import params

def compare_res(s1,s2):
    for i in range(params.KYBER_K):
        for j in range(params.KYBER_N):
            if s1[i][j]!=s2[i][j]:
                print("Oops! wrong answer!\n")
                return False
    print("Attack perfectly done!")
    return True

def solve_as_plus_s(pkpv,a):
    skpv_computed=[[0 for _ in range(params.KYBER_N)] for _ in range(params.KYBER_K)]
    for i in range(int(params.KYBER_N/4)):
        base=4*i
        zeta=params.ZETA[64+i]*params.KYBER_RINV
        #group 1
        matrix=[[0 for _ in range(params.KYBER_K*2+1)] for _ in range(params.KYBER_K*2)]
        for j in range(params.KYBER_K):
            for k in range(params.KYBER_K):
                matrix[2*j][2*k]=a[j][k][base]
                matrix[2*j][2*k+1]=(a[j][k][base+1]*zeta)%params.KYBER_Q
                matrix[2*j+1][2*k]=a[j][k][base+1]
                matrix[2*j+1][2*k+1]=a[j][k][base]
            matrix[2*j][-1]=pkpv[j][base]
            matrix[2*j+1][-1]=pkpv[j][base+1]
        for j in range(2*params.KYBER_K):
            matrix[j][j]+=1
        ret=modeqs.run_test(params.KYBER_Q,matrix)
        if (len(ret)!=1):
            print("multi solution error!\n")
        for j in range(params.KYBER_K):
            skpv_computed[j][base]=ret[0][j*2]
            skpv_computed[j][base+1]=ret[0][j*2+1]
        

        #group 2  
        matrix=[[0 for _ in range(params.KYBER_K*2+1)] for _ in range(params.KYBER_K*2)]
        for j in range(params.KYBER_K):
            for k in range(params.KYBER_K):
                matrix[2*j][2*k]=a[j][k][base+2]
                matrix[2*j][2*k+1]=(a[j][k][base+3]*(-zeta))%params.KYBER_Q
                matrix[2*j+1][2*k]=a[j][k][base+3]
                matrix[2*j+1][2*k+1]=a[j][k][base+2]
            matrix[2*j][-1]=pkpv[j][base+2]
            matrix[2*j+1][-1]=pkpv[j][base+3]
        for j in range(2*params.KYBER_K):
            matrix[j][j]+=1
        ret=modeqs.run_test(params.KYBER_Q,matrix)
        if (len(ret)!=1):
            print("multi solution error!\n")
        for j in range(params.KYBER_K):
            skpv_computed[j][base+2]=ret[0][j*2]
            skpv_computed[j][base+3]=ret[0][j*2+1]
    print(skpv_computed)
    print("\nprivate key get!\n")
    return skpv_computed
        