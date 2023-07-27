import params
import variables

#pkpv extract function: generate 3*256 pkpv in decimal form
def pkpv_extract(pk_str):
    res=[]
    print("extracting pkpv from public key.../n")
    print("public key:\n"+pk_str+"\n\n")
    #extract pkpv encoded
    if len(pk_str)!=2368:
        print("error: public key length error")
        return res
    pkpv_encoded=pk_str[:-64]
    res=[[] for _ in range(params.KYBER_K)]
    for i in range(params.KYBER_K):
        for j in range(int(params.KYBER_N/2)):
            base=i*3*params.KYBER_N+j*6
            str1=pkpv_encoded[base+3]+pkpv_encoded[base+0]+pkpv_encoded[base+1]
            str2=pkpv_encoded[base+4]+pkpv_encoded[base+5]+pkpv_encoded[base+2]
            num1=int(str1,16)
            num2=int(str2,16)
            res[i].append(num1)
            res[i].append(num2)
    return res

if __name__ == "__main__":
    pk_str=variables.PUBLIC_KEY_STR
    pkpv=pkpv_extract(pk_str)
    print(pkpv)
