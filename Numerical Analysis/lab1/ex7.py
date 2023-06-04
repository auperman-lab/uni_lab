def compare(bin1, bin2):
	if len(bin1) > len(bin2):
		return '>'
	elif len(bin1) < len(bin2):
		return '<'
	else:
		for i in range(len(bin1)):
			if ord(bin2[i]) > ord(bin1[i]):
				return '<'
			elif ord(bin2[i]) < ord(bin1[i]):
				return '>'

		return '='


def addition(bin1, bin2):
	num1, fl1 = str(bin1).split(".")
	num2, fl2 = str(bin2).split(".")
	numsumm = add(num1, num2)[0]
	flsum, carry = add(fl1, fl2)

	if carry == 0:
		numsumm = numsumm + '.' + flsum
	else:
		flsum = flsum[0:1] + '.' + flsum[1:]
		numsumm += flsum
	return numsumm


def add(bin1, bin2):
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

	return result, carry


def binary_convert(my_number, places):
	whole, decimal = str(my_number).split(".")
	whole = int(whole)
	decimal = float('.'+decimal)
	res = bin(whole).lstrip("0b") + "."
	for x in range(places):
		decimal *= 2
		if decimal == 1:
			res += '1'
			decimal = 0
		elif decimal > 1:
			decimal -= 1
			res += '1'
		else:
			res += '0'
	return res


def decimal_convert(bin):
	num, fl = str(bin).split(".")
	result = 0
	num = num[::-1]
	for i in range(len(num)):
		if num[i] == '1':
			result += 2**i
	for i in range(len(fl)):
		if fl[i] == '1':
			result += 2**(-i-1)
	return result


def substract(bin1, bin2):
	num1, fl1 = str(bin1).split(".")
	num2, fl2 = str(bin2).split(".")
	sign = ''
	if compare(num1, num2) == '=':
		if compare(fl1, fl2) == '<':
			fl1, fl2 = fl2, fl1
			sign = '-'
	elif compare(num1, num2) == '<':
		num1, num2 = num2, num1
		fl1, fl2 = fl2, fl1
		sign = '-'

	x = subs(num1, num2)
	if compare(fl1, fl2) == '<':
		for i in range(1, len(x)):
			if x[-i] == '1':
				x = x.replace(x[-i], '0', 1)
				for j in range(1, i - 1):
					x = x.replace(x[-j], '1', 1)
				break

		fl1 = '1' + fl1
		y = subs(fl1, fl2)
		y = y[1:]
	else:
		y = subs(fl1, fl2)


	result = sign + x + '.' + y
	i = 0
	while True:
		if result[i] == '0':
			result = result[1:]
		else:
			break

	return result


def subs(bin1, bin2):
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

	return result.zfill(max_len)


def multiplication(bin1, bin2):
	fl = bin1[::-1].index('.') + bin2[::-1].index('.')
	num1 = bin1.replace('.', '')
	num2 = bin2.replace('.', '')
	x = mult(num1, num2)
	fl = len(x) - fl
	return x[:fl] + '.' + x[fl:]


def mult(bin1, bin2):
	level = 0
	result = '0'
	for i in bin2[::-1]:
		if i == '1':
			inter = str(bin1)
			for i in range(level):
				inter += '0'
			result = add(result, inter)[0]
		level += 1
	return result


def divide(bin1, bin2, precision):
	result = ''
	i = 1
	while len(result) < precision:
		divisor = bin1[:i]
		max_len = max(len(divisor), len(bin2))
		divisor = divisor.zfill(max_len)
		bin2 = bin2.zfill(max_len)

		if divisor >= bin2:
			minusop = subs(divisor, bin2)
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


bin1 = float(input('first number: '))
bin2 = float(input('second number: '))
operation = input('what operation do u want: ')
plmea = int(input('what precision: '))
bin1 = binary_convert(bin1, plmea)
bin2 = binary_convert(bin2, plmea)
if operation == '+':
	x = addition(bin1, bin2)
	print('the number in binary form: ', x)
	print('the result in float form: ', decimal_convert(x))
elif operation == '-':
	x = substract(bin1, bin2)
	print('the number in binary form: ', x)
	print('the result in float form: ', decimal_convert(x))
elif operation == '*':
	x = multiplication(bin1, bin2)
	print('the number in binary form: ', x)
	print('the result in float form: ', decimal_convert(x))



