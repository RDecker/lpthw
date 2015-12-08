mbps = 1024
psize = 1024

print "I'm going to assume the rate of transfer is %d Mbps." % mbps
print "I'm going to assume the package size is %d GB." % psize
print mbps/8.0, " MBps.  This is how fast it would be in megabytes."

print (psize*1024), " MB.  This is how many megabytes there are to be transferred."

print (psize*1024)*(mbps/8.0), " seconds.  This is how many seconds it will take to transfer."

print ((psize*1024)/(mbps/8.0))/60.0, " minutes.  This is how many minutes it will take to transfer."

print (((psize*1024)/(mbps/8.0))/60.0)/60.0, " hours.  This is how many hours it will take to transfer."
