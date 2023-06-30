def isDivisible(self, s):
	    s=str(s)
		n=0
		sm=0
		for i in range(len(s)-1,-1,-1):
		    sm+=int(s[i])*(2**n)
		    n+=1
	    if sm%3==0:
	        return 1
	    else:
	        return 0
