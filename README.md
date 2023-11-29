# Dict -> Type Generator
Repository to convert Python dictionaries to Typescript Types. Input any full python dictionary, and receive as
output a fully formatted and TypeScript type for that dictionary!

# Installation
You can find the project on PyPi [here](https://pypi.org/project/type_gen_dict/0.0.1/). To install, execute the below.
```bash
pip install type-gen-dict
```

# Example
```python
    import type_gen_dict as tg
    generator = tg.TypeGenerator()
    sample = {"1": "hello!", "2": 10, "3": "10/29/22", "4": True, "5": [1, "hi", False], "6": None,
              "7": {"8": 1, "9": 2, "10": {"11": True, "12": {"13": None, "14": (1, "hi", True, set())}}}}
    generator.convert(sample, 'ts', verbose=True)
```
**Output:**
```typescript
type ABC = {
  1: string;
  2: number;
  3: string;
  4: boolean;
  5: any[];
  6: null;
  7: {
    8: number;
    9: number;
    10: {
      11: boolean;
      12: {
        13: null;
        14: [number,string,boolean,object,];
      }
    }
  }
}
```

# Pip Deploy
1. `python3 setup.py sdist bdist_wheel`
2. `pip install twine`
3. `twine upload dist/*`
