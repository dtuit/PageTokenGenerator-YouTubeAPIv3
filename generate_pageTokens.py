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
16384 -> ... = 'CGKOSWaeimquy26-'
'''


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

def getPageToken(page, maxResults=50):
    return numberToToken(page*maxResults)

# Example Usage: Will first ten pages of 50 items.
for i in range(0, 10):
    print(getPageToken(i))