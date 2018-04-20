# One-way ANOVA. 'filename' is the name of a csv file where the 
# first field in each line is the name of a group and the second line 
# is a numerical value. Mimics Excel output. 

from sys import argv

import scipy.stats

script, filename = argv

x_dict = {}

data = []

source = open(filename,'r')
for line in source:
	temp = line.strip()
	temp = temp.split(',')
	
	if temp[0] in x_dict:
		x_dict[temp[0]].append(float(temp[1]))
	else:
		x_dict[temp[0]] = [float(temp[1])]

	data.append((temp[0],float(temp[1])))

x_summary = {}

for x in x_dict:
	count_x = len(x_dict[x])
	sum_x = sum(x_dict[x])
	avg_x = sum_x/float(count_x)
	var_x = sum([(n-avg_x)**2 for n in x_dict[x]])/float(count_x - 1)
	x_summary[x] = (count_x, sum_x, avg_x, var_x)

print '\nSUMMARY'
print ''.join(['=' for i in range(0,80)])
print '%16s%16s%16s%16s%16s' % ('Group','Count','Sum','Average','Variance')
print ''.join(['-' for i in range(0,80)])
for x in sorted(x_summary):
	output = (x,)
	for i in range(0,4):
		output += (x_summary[x][i],)
	print '%16s%16d%16.4f%16.4f%16.4f' %  output
print ''.join(['=' for i in range(0,80)])
	
mean = sum([d[1] for d in data])/len([d[1] for d in data])

ss_all = sum([(d[1] - mean)**2 for d in data])
ss_x = sum([(sum(x_dict[d[0]])/len(x_dict[d[0]]) - mean)**2 for d in data])


means = {x:sum(x_dict[x])/len(x_dict[x]) for x in x_dict}
ss_wi = sum([(means[d[0]] - d[1])**2 for d in data])

df_all = len(data) - 1
df_x = len(x_dict) - 1

df_wi = df_all - df_x

ms_all = ss_all/float(df_all)
ms_x = ss_x/float(df_x)
ms_wi = ss_wi/float(df_wi)
p_value = 1 - scipy.stats.f.cdf(ms_x/ms_wi,df_x,df_wi)

print '\nANOVA'
print ''.join(['=' for i in range(0,100)])
print '%16s%16s%16s%16s%16s%16s' % ('Source','SS','df','MS','F','p-value')
print ''.join(['-' for i in range(0,100)])
print '%16s%16.4f%16d%16.4f%16.4f%16.4f' % ('Between Groups', ss_x, df_x, ms_x, ms_x/ms_wi, p_value)
print '%16s%16.4f%16d%16.4f' % ('Within Groups', ss_wi, df_wi, ms_wi)
print ''
print '%16s%16.4f%16d' % ('Total', ss_all, df_all)
print ''.join(['=' for i in range(0,100)]), '\n'
