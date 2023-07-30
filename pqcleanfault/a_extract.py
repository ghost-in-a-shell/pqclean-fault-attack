import params
import variables

#a extract function: generate 3*3*256 a in decimal form
def a_extract(a_str):
    res=[]
    print("extracting a from a_str...\n")
    print("a_str:\n"+a_str+"\n\n")
    #extract pkpv encoded
    if len(a_str)!=6912:
        print("error: matric a length error")
    res=[[[] for _ in range(params.KYBER_K)] for _ in range(params.KYBER_K)]

    for i in range(params.KYBER_K):
        for j in range(params.KYBER_K):
            for k in range(int(params.KYBER_N/2)):
                base=(i*3+j)*3*params.KYBER_N+k*6
                str1=a_str[base+3]+a_str[base+0]+a_str[base+1]
                str2=a_str[base+4]+a_str[base+5]+a_str[base+2]
                num1=int(str1,16)
                num2=int(str2,16)
                res[i][j].append(num1)
                res[i][j].append(num2)
    return res

if __name__ == "__main__":
    a_str=variables.A_STR
    a=a_extract(a_str)
    print(a)