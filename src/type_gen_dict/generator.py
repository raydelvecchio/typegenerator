class TypeGenerator:
    def __init__(self):
        self.accepted = ['ts']
        self.ts_map = {"int": "number", "float": "number", "bool": "boolean", "str": "string",
                       "list": "any[]", "NoneType": "null"}

    def generate_ts_type(self, data: dict, name: str, cutoff: int = 20, indent: int = 1) -> str:
        """
        Given a dictionary, display the structure of the given dictionary. Used to explore how data is returned.
        Data and name are used as input parameters; indent used as recursive param.
        """
        construct = ""
        if indent == 1:
            construct += f"type {name[0:cutoff]} = {{\n"

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

    def convert(self, data: dict, language: str, name: str = "ABC", verbose: bool = False) -> str:
        """
        Given a type to convert to, convert that dictionary and return it.
        Current types: 'ts' -> typescript.
        """
        if language not in self.accepted:
            raise Exception(f"Please input accepted languages, currently: {self.accepted}")

        convert_fn = getattr(self, f'generate_{language}_type')
        generated_type = convert_fn(data, name)
        if verbose:
            print(generated_type)
        return generated_type
