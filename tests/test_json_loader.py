import tempfile
import os

from json_loader import install_json_loader


data_content = """
{
  "s": "v",
  "o": {
    "s": "v",
    "a": [1, 2, 3],
    "b": true,
    "o": {
      "s": "v",
      "o": {
        "s": "v"
      }
    }
  }
}
"""


def test_json_load():
    tmp_dir = tempfile.mkdtemp()
    data_path = os.path.join(tmp_dir, 'data.json')
    with open(data_path, 'w+') as f:
        f.write(data_content)

    install_json_loader(tmp_dir)

    import data

    assert data.o.b is True
    assert data.o.o.s == 'v'
    assert data.o.o.o.s == 'v'

    os.unlink(data_path)
