# Haas

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sit amet risus ex. Sed tempor vitae lacus nec pretium. Integer at auctor justo. Suspendisse posuere nibh velit, vitae euismod lectus euismod vitae. Mauris orci tortor, tempor ac dui vel, malesuada mollis eros. Quisque tempus malesuada aliquet.

1. Integer scelerisque libero eu nibh tincidunt pellentesque.
2. Sed faucibus, mi vitae venenatis aliquam, nunc ex vulputate odio, maximus bibendum lorem justo ut odio.
3. Sed vitae justo malesuada, vehicula tortor non, ullamcorper nibh.

# Table of Contents

1. [Usage](#usage-example)
2. [API Documentation](#api-documentation)

# Usage Example

```python
def todo():
    return "Implement me"
```

# API Documentation

**URL** : `/sample`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Rate limit** : 1 request per day

**Description** : Returns the string "Hello World!".

## Success Response

**Code** : `200 OK`

**Content examples**

```json
Hello World!
```

**Code** : `429 Too Many Requests`

**Content examples**

For a request made less than 24 hours before the previous request

```json
Too Many Requests
1 per 1 day
```