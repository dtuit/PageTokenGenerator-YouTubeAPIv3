# Page Token Generator YouTubeAPIv3
Generates page tokens for use with the YouTube Data API v3. 
Generates tokens for items 0 to 99999 (every posible token)

### Usage
```python
# Example Usage: Gets the first ten pageTokens for 50 items each.
for i in range(0, 10):
    print(PageTokenGenerator.page_to_token(i, 50))
```
