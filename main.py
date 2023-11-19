class TypeGenerator:
    def __init__(self):
        self.ts_map = {"int": "number", "float": "number", "bool": "boolean", "str": "string",
                       "list": "any[]", "NoneType": "null"}

    def generate_ts_type(self, data: dict, name: str, indent=1) -> str:
        """
        Given a dictionary, display the structure of the given dictionary. Used to explore how data is returned.
        Data and name are used as input parameters; indent used as recursive param.
        """
        construct = ""
        if indent == 1:
            construct += f"type {name} = {{\n"

        for key, value in data.items():
            t = type(value).__name__
            if t in self.ts_map:
                fill = self.ts_map[t]
            else:
                fill = 'object'

            is_dict = t == "dict"

            if is_dict:
                construct += f"{'  ' * indent}{key}: {{\n"
                construct += self.generate_ts_type(value, name, indent+1)
                construct += f"{'  ' * indent}}}\n"
            else:
                construct += f"{'  ' * indent}{key}: {fill};\n"

        if indent == 1:
            construct += "}"

        return construct

    def convert(self, data: dict, language: str, name="ABC", verbose=False) -> str:
        """
        Given a type to convert to, convert that dictionary and return it.
        Current types: 'ts' -> typescript.
        """
        convert_fn = getattr(self, f'generate_{language}_type')
        generated_type = convert_fn(data, name)
        if verbose:
            print(generated_type)
        return generated_type


if __name__ == "__main__":
    tg = TypeGenerator()
    sample = {"1": "hello!", "2": 10, "3": "10/29/22", "4": True, "5": [1, 2, 3], "6": None,
              "7": {"8": 1, "9": 2, "10": {"11": True, "12": {"13": None}}}}
    tg.convert(sample, 'ts', verbose=True)
