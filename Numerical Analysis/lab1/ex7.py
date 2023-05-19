def addition(bin1, bin2):
	max_len = max(len(bin1), len(bin2))
	bin1 = bin1.zfill(max_len)
	bin2 = bin2.zfill(max_len)
	result = ''

	carry = 0

	for i in range(max_len - 1, -1, -1):
		r = carry
		r += 1 if bin1[i] == '1' else 0
		r += 1 if bin2[i] == '1' else 0
		result = ('1' if r % 2 == 1 else '0') + result
		carry = 0 if r < 2 else 1

	if carry != 0:
		result = '1' + result

	return result.zfill(max_len)


def binary_convert(my_number, places):
	whole, decimal = str(my_number).split(".")
	whole = int(whole)
	decimal = float('.'+decimal)
	res = bin(whole).lstrip("0b") + "."
	for x in range(places):
		decimal *= 2
		if decimal == 1:
			res += '1'
			break
		elif decimal > 1:
			decimal -= 1
			res += '1'
		else:
			res += '0'
	return res


def substract(bin1, bin2):
	max_len = max(len(bin1), len(bin2))
	bin1 = bin1.zfill(max_len)
	bin2 = bin2.zfill(max_len)

	carry = [0] * len(bin1)
	result = ''

	for i in range(max_len - 1, -1, -1):
		x = int(bin1[i])
		y = int(bin2[i])
		sub = (carry[i] + x) - y

		if sub == -1:
			result += '1'
			for j in range(i - 1, -1, -1):
				carry[j] = -1
				if bin1[j] == '1':
					break
		elif sub == 1:
			result += '1'
		else:
			result += '0'

	result = result[::-1]
	i = 0
	while i < len(result):
		if result[0] == '0':
			result = result[1:]
			i -= i
		i += 1

	return result


def multiplicate(bin1, bin2):
	bin1 = int(bin1)
	bin2 = int(bin2)

	def binProd(binone, bintwo):
		i = 0
		rem = 0
		summ = []
		bProd = 0
		while binone != 0 or bintwo != 0:
			summ.insert(i, (((binone % 10) + (bintwo % 10) + rem) % 2))
			rem = int(((binone % 10) + (bintwo % 10) + rem) / 2)
			binone = int(binone / 10)
			bintwo = int(bintwo / 10)
			i = i + 1
		if rem != 0:
			summ.insert(i, rem)
			i = i + 1
		i = i - 1
		while i >= 0:
			bProd = (bProd * 10) + summ[i]
			i = i - 1
		return bProd

	binMul = 0
	factr = 1
	while bin2 != 0:
		digit = bin2 % 10
		if digit == 1:
			bin1 = bin1 * factr
			binMul = binProd(bin1, binMul)
		else:
			bin1 = bin1 * factr
		bin2 = int(bin2 / 10)
		factr = 10
	return str(binMul)


def divide(bin1, bin2, precision):
	result = ''
	i = 1
	while len(result) < precision:
		divisor = bin1[:i]
		max_len = max(len(divisor), len(bin2))
		divisor = divisor.zfill(max_len)
		bin2 = bin2.zfill(max_len)

		if divisor >= bin2:
			minusop = substract(divisor, bin2)
			bin1 = minusop + bin1[i:]
			result += '1'
			i = len(minusop)
		elif i >= len(bin1):
			if '.' not in result:
				result += '.'
			bin1 += '1'
			result += '0'
		else:
			result += '0'
			if result[0] == '0':
				result = result[1:]
		i += 1
	return result


# summ = divide('10110110101', '100101', 30)
# summ = divide('111111100001', '100001111', 30)
summ = divide('1', '101', 30)
print(summ)
