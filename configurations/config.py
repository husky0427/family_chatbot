from typing import Dict
import yaml
from collections import Mapping


class YamlConfig(Mapping):

    def __init__(self, path: str):
        self._path = path
        self._data = self._get_yml_data()

    def _get_yml_data(self):
        with open(self._path, 'r') as f:
            data = yaml.safe_load(f)
        return data
    
    def __getitem__(self, __k):
        return self._data[__k]

    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)
    
    def __str__(self):
        return str(self._data)
    

if __name__ == "__main__":
    cwb_config = YamlConfig("configurations/cwb.yml")
    print(cwb_config)