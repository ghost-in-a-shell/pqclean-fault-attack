import params
import variables

#skpv extract function: generate 3*256 skpv in decimal form
def skpv_extract(sk_str):
    res=[]
    print("extracting skpv from private key...\n")
    print("private key:\n"+sk_str+"\n\n")
    #extract skpv encoded
    if len(sk_str)!=2304:
        print("error: private key length error")
        return res
    skpv_encoded=sk_str
    res=[[] for _ in range(params.KYBER_K)]
    for i in range(params.KYBER_K):
        for j in range(int(params.KYBER_N/2)):
            base=i*3*params.KYBER_N+j*6
            str1=skpv_encoded[base+3]+skpv_encoded[base+0]+skpv_encoded[base+1]
            str2=skpv_encoded[base+4]+skpv_encoded[base+5]+skpv_encoded[base+2]
            num1=int(str1,16)
            num2=int(str2,16)
            res[i].append(num1)
            res[i].append(num2)
    return res

if __name__ == "__main__":
    sk_str=variables.PRIVATE_KEY_STR
    skpv=skpv_extract(sk_str)
    print(skpv)
