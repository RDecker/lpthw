print "I'm going to assume the rate of transfer is 500 Mbps."
print "I'm going to assume the package size is 300 GB."
print 500/8.0, " MBps.  This is how fast it would be in megabytes."

print (300*1024), " MB.  This is how many megabytes there are to be transferred."

print (300*1024)*(500/8.0), " seconds.  This is how many seconds it will take to transfer."

print ((300*1024)/(500/8.0))/60.0, " minutes.  This is how many minutes it will take to transfer."

print (((300*1024)/(500/8.0))/60.0)/60.0, " hours.  This is how many hours it will take to transfer."
