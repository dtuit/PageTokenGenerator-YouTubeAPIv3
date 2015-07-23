'''
Generates PageTokens for use with the Youtube Data API v3

A PageToken Consists of:

"C" + b8 + b16 [+ b64 + b64 ] + "{s}AA"
b8 is a base 8 alphabet etc.

b8 =
0 -> 127 = 'ABCDEFGH' 
128 -> ... = 'IJKLMNOP' 

b16 = 
0 -> 8191 = 'AEIMQUYcgkosw048',  
8192 -> 16383 = 'BFJNRVZdhlptx159',  
16384 -> 24575 = 'CGKOSWaeimquy26-'
24575 -> ... = 'DHLPTXbfjnrvz37_'

s = 
0 -> 127 = 'Q'
128 -> 16383 = 'E'
16383 -> 32767 = 'R'
32768 -> ?? = 'h'

'''

class PageTokenGenerator:
    def number_to_token(number):
        b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'

        def get_weights(weights, number):
            res = []
            n = number
            for i in weights:
                q,r = divmod(n,i)
                res.append( q )
                n = r
            return res

        x = get_weights([65536, 16384, 8192, 128, 16, 1], number)

        prefix = 'C'

        b8_offset = 0 if number < 128 else 8
        b16_offset = (x[2] % 2) + 2

        suffix_pos = (x[1] * 16 + 1) % 64
        suffix = b64[suffix_pos]

        if (num < 16384):
            suffix = 'E'
            b16_offset = 1
        if (num < 8192):
            b16_offset = 0
        if (num < 128):
            suffix = 'Q'

        token = "{p}{n1}{n2}{n3}{n4}{s}".format(
            p = prefix,
            n1 = b64[ x[4] + b8offset ],
            n2 = b64[ x[5]*4 + b16offset ],
            n3 = b64[ x[3] ] if number >= 128 else "",
            n4 = b64[ x[0] ] if number >= 16384 else "",
            s = suffix + "AA"
            )

        return token

    def page_to_token(page, max_results):
        return self.number_to_token(page*maxResults)


def numberToToken(number):
    b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'

    def getWeights(weights, number):
        res = []
        n = number
        for i in weights:
            q,r = divmod(n,i)
            res.append( q )
            n = r
        return res

    x = getWeights([16384,8192,128,16,1], number)

    prefix = "C"
    y = "Q"
    if ( number >= 128 ): y = "E"
    if ( number >= 16384): y = "R"
    suffix = "%sAA" % y

    b8offset = 0 if number < 128 else 8
    b16offset = x[0]*2 + x[1] 

    token = "{p}{n1}{n2}{n3}{n4}{s}".format(
        p = prefix,
        n1 = b64[ x[3] + b8offset ],
        n2 = b64[ x[4]*4 + b16offset ],
        n3 = b64[ x[2] ] if number >= 128 else "",
        n4 = b64[ x[1] ] if number >= 16384 else "",
        s = suffix)

    return token

def getPageToken(page, maxResults):
    return numberToToken(page*maxResults)

# Example Usage: Gets the first ten pageTokens for 50 items.
for i in range(0, 10):
    print(getPageToken(i, 50))