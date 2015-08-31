def number_to_token(number):
	return token_object(number).as_token()

def number_to_prev_token(number):
	t = token_object(number)
	t.is_prev_token(True)
	return t.as_token()

def token_to_number(token):
	return token_object(token, True).as_number()


class token_object:

	b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'

	char_1 = '' 
	char_16 = ''
	char_128 = ''
	char_16384 = '' 
	char_65536 = ''

	weight_1 = 0
	weight_16 = 0
	weight_128 = 0
	weight_8192 = 0
	weight_16384 = 0
	weight_65536 = 0

	isPrevToken = False
	prefix = 'C'
	nextToken = "AA"
	prevToken = "A_"

	def __init__(self, number_or_token, is_token = False):
		if(is_token):
			self._init_token(number_or_token)
		else:
			self._init_number(number_or_token)

	''' ''' 
	def _init_token(self, token):
		if(len(token) < 6):
			raise ValueError("Not A Valid Page Token")
	
		if(token[-1] != 'A'):
			self.isPrevToken = True

		# Remove prefix and previous/next tags
		t = token[1:-2]
		
		# Get Suffix Char and Remove it
		self.char_16384 = t[-1]
		t = t[0:-1]

		self.char_1 = t[1]
		self.char_16 = t[0]

		if(len(t)>2):
			self.char_128 = t[2]

		if(len(t)>3):
			self.char_65536 = t[3]

		pos = self.b64.index(self.char_1)
		self.weight_1 = (pos - (pos % 4)) / 4 # Converts these sequences to range(0, 15). 'AEIMQUYcgkosw048', 'BFJNRVZdhlptx159', 'CGKOSWaeimquy26-', 'DHLPTXbfjnrvz37_'

		if(pos % 4 == 3 or pos % 4 == 1): # every odd 8192
			self.weight_8192 = 1

		pos = self.b64.index(self.char_16)
		self.weight_16  = pos % 8 # Converts 'ABCDEFGH' and 'IJKLMNOP' into range(0, 7)

		if(len(t) > 2):
			pos = self.b64.index(self.char_128)
			self.weight_128 = pos

		if(len(t) > 3):
			pos =  self.b64.index(self.char_16384)
			self.weight_16384 = (pos - 1) /16 # Converts 'BRhx' into range(0, 3)
			self.weight_65536 = self.b64.index(self.char_65536)
	
	''' ''' 
	def _init_number(self, number):

		def get_weights(weights, number):
			res = []
			n = number
			for i in weights:
				q,r = divmod(n,i)
				res.append( q )
				n = r
			return res

		x = get_weights([65536, 16384, 8192, 128, 16, 1], number)
		self.weight_1 = x[5]
		self.weight_16 = x[4]
		self.weight_128 = x[3]
		self.weight_8192 = x[2]
		self.weight_16384 = x[1]
		self.weight_65536 = x[0]

		w16_offset = 0 if number < 128 else 8
		w1_offset = (self.weight_8192 % 2) + 2

		# converts range(0, 3) into 'BRhx'
		suffix_pos = (self.weight_16384 * 16 + 1) % 64
		self.char_16384 = self.b64[suffix_pos]

		if (number < 16384):
			self.char_16384 = 'E'
			w1_offset = 1
		if (number < 8192):
			w1_offset = 0
		if (number < 128):
			self.char_16384 = 'Q'

		self.char_1 = self.b64[ self.weight_1 * 4 + w1_offset] 		# converts range(0, 15) into  'AEIMQUYcgkosw048', 'BFJNRVZdhlptx159', 'CGKOSWaeimquy26-', 'DHLPTXbfjnrvz37_'
		self.char_16 = self.b64[ self.weight_16 + w16_offset] 		# converts range(0 ,7) into 'ABCDEFGH' and 'IJKLMNOP'
		self.char_128 = self.b64[self.weight_128] if number >= 128 else ""
		self.char_65536 = self.b64[self.weight_65536] if number >= 16384 else "" 

	def is_prev_token(self, b):
		self.isPrevToken = b

	def as_number(self):
		retval = 1 * self.weight_1 + \
			16 * self.weight_16 + \
			128 * self.weight_128 + \
			8192 * self.weight_8192 + \
			16384 * self.weight_16384 + \
			65536 * self.weight_65536
		return int(retval)

	def as_token(self):
		token = "{p}{n1}{n2}{n3}{n4}{n5}{s}".format(
			p = self.prefix,
			n1 = self.char_16, 
			n2 = self.char_1, 
			n3 = self.char_128, 
			n4 = self.char_65536, 
			n5 = self.char_16384, 
			s = self.prevToken if self.isPrevToken else self.nextToken )
		return token

	def _isValidToken(self, token):
		for t in token:
			if t not in self.b64:
				return False
		return True

# Convert number to Token
print(number_to_token(50))

# Convert token to number
print(token_to_number('CDIQAA'))

# Convert prevToken to number
print(token_to_number('CDIQAQ'))

# Gets the first ten pageTokens for 50 items each.
for i in range(0, 10):
    print(number_to_token(i * 50))