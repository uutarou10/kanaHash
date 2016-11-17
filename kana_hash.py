import get_boin
# nで渡ってきた文字列をhash化して返す
def hash(n):
	code = ''
	charCode = {
		'あ':'1',
		'い':'2',
		'う':'3',
		'え':'4',
		'お':'5'
	}
	
	for char in n:
		tmp = charCode.get(get_boin.getBoin(char))
		if tmp == None:
			pass
		else:
			code += tmp
	
	left = int(code[:int(len(code) / 2)])
	right = int(code[int(len(code) / 2):])

	return left + right

if __name__ == '__main__':
	print(hash("のなかこうた"))
