# Energy usage rates:
usage = [563.85, 553.46, 499.39, 384.71, 307.97, 208.79, 790.22, 444.06, 330.4, 330]

# Green Mountain Conserve 12 
# (500*0.0264 + 5.25 + 500*0.034821)*1.01
gmc12 = { 'nrgcharge' : 0.0264, 'deliverycharge' : 0.034821 }

# Green Mountain Conserve 12 Choice
# (10 + 500*0.006632 + 5.25 + 500*0.031617)*1.01
gmc12choice = { 'nrgcharge' : 0.006632, 'deliverycharge' : 0.031617 }

# Gexa Choice Conserve 9
gcc9 = { 'nrgcharge' : 0.0652, 'deliverycharge' : 0.0316, 'nrgcredit' : 25 }

# Figure out what the monthly and overall costs would be if I chose either of these plans:

total = 0
gmc12overall = 0
gmc12choiceoverall = 0
gcc9overall = 0
for i in usage:
	gmc12mo =  (i*gmc12["nrgcharge"] + 5.25 + i*gmc12["deliverycharge"])*1.01
	gmc12overall = gmc12overall + gmc12mo
	print "gmc12 for this month is ", gmc12mo

	gmc12choicemo = (10 + i*gmc12choice["nrgcharge"] + 5.25 + i*gmc12choice["deliverycharge"])*1.01
	gmc12choiceoverall = gmc12choiceoverall + gmc12choicemo
	print "gmc12choice for this month is ", gmc12choicemo

	gcc9mo =  (i*gcc9["nrgcharge"] + 5.25 + i*gcc9["deliverycharge"])*1.01 - gcc9["nrgcredit"]
	gcc9overall = gcc9overall + gcc9mo
	print "gcc9 for this month is ", gcc9mo, "\n"

	total = total + i

print "I used %0.3fkWh over the last year." % total 
print "For the gmc12 plan, overall cost would be: ", gmc12overall
print "For the gmc12choice plan, overall cost would be: ", gmc12choiceoverall
print "For the gcc9 plan, overall cost would be: ", gcc9overall



