json-loader
===========

##### data.json

```json
{
  "obj": {
    "val": "hello"
  }
}
```

##### python code

```python
import json_loader
# add directory with .json files (working directory in this case)
json_loader.install_json_loader('.')
# import .json file (data.json)
import data
# access to json values
val = data.obj.val
assert val == 'hello'
```
