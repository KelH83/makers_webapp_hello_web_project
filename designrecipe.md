
## 1. Design the Route Signature

```
Path: http://localhost:5001/sort-names
Parameters: names

# Receives list of names route
POST /sort-names


Path: http://localhost:5001/names
Parameters: add

# Return a list of pre-defined names, plus the name given.
GET /names?add=Eddie

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie

```

## 2. Create Examples as Tests

```python
# POST /sort-names
#  Expected response (200 OK):
"""
List of names inputted returned in Alphabetical order
"""

# POST /sort-names
#  Parameters:
#    names: names=Joe,Alice,Zoe,Julia,Kieran
#  Expected response (200 OK):
# Alice,Joe,Julia,Kieran,Zoe

# GET /names?add=Eddie
#  Expected response (200 OK):
# Julia, Alice, Karim, Eddie
"""
List of names inputted returned in Alphabetical order
"""

# GET /names?add=Eddie
#  Parameters:
#    add: add=Eddie
#  Expected response (200 OK):
# Julia, Alice, Karim, Eddie

```

## 3. Test-drive the Route

Here's an example for you to start with:

```python
"""
POST /sort-names
  Expected response (200 OK):
  "Alice,Joe,Julia,Kieran,Zoe"
"""
def test_sort_names(web_client):
    response = web_client.get('/sort_names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

"""
GET /names?add=Eddie
  Expected response (200 OK):
  "Julia, Alice, Karim, Eddie"
"""
def test_get_names(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'
```

