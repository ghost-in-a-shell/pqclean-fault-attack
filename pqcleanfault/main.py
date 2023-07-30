import a_extract
import pkpv_extract
import skpv_extract
import variables
import chk_correctness
import solver_harness
import sys

a_str=variables.A_STR
a=a_extract.a_extract(a_str)
pk_str=variables.PUBLIC_KEY_STR
pkpv=pkpv_extract.pkpv_extract(pk_str)
sk_str=variables.PRIVATE_KEY_STR
skpv=skpv_extract.skpv_extract(sk_str)
ret=chk_correctness.chk_as_plus_s(pkpv,a,skpv)
if(ret==True):
    sys.exit(0)
skpv_computed=solver_harness.solve_as_plus_s(pkpv,a)
solver_harness.compare_res(skpv,skpv_computed)
#modeqs.mytest()