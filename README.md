# Page Token Generator YouTubeAPIv3
Converts integers into their equivelent pageToken and back
Generates and parses page tokens for use with the YouTube Data API v3.

Verified to generate tokens for items 0 to over 1,000,000 using the following request
theoretically should work upto 4,194,304

- GET https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=1&playlistId=UUsvaJro-UrvEQS9_TYsdAzQ&fields=nextPageToken%2CprevPageToken%2CpageInfo%2Citems%2Fsnippet(title%2Cposition)&key={YOUR_API_KEY}

### Usage
```python
# Convert number to Token
print(PageTokenGenerator.number_to_token(50))

# Convert token to number
print(PageTokenGenerator.token_to_number('CDIQAA'))

# Convert prevToken to number
print(PageTokenGenerator.token_to_number('CDIQAQ'))

# Gets the first ten pageTokens for 50 items each.
for i in range(0, 10):
    print(PageTokenGenerator.number_to_token(i * 50))
```

### Note
- Search endpoint only allows a maximum 500 results 
- cant use with comments, commentThreads endpoints as a different pageToken system is used
