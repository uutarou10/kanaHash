import kana_hash
if __name__ == '__main__':
	count = {}
	for line in open('dummy_name.csv','r') :
		h = kana_hash.hash(line.split(',')[1].strip('\n'))
		if h in count:
			count.update({h:count[h]+1})
		else:
			count.update({h:1})
	
#	print(len(count))
	f = open('output.txt','w')
	for k,v in sorted(count.items(), key=lambda x: x[0]):
#		print('{0} : {1}'.format(str(k),str(v)))
		f.write('{0},{1}\n'.format(str(k),str(v)))
	else:
		f.close()
