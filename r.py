
data = []

with open('reviews.txt.crdownload', 'r') as f :
	for line in f :
		data.append(line)
	
		
print('總共有', len(data), '比留言')

sum_len = 0
for d in data :
	sum_len += len(d)
print('平均留言長度為:', sum_len/len(data), '個字')


