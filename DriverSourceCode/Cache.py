from KeyboardFunctions import KeyboardFunctions


class Cache:
    def __init__(self):
        self.keys_map = {}  # {'B2': 'foo(12)', ...}

        self.load_keys_layout()

    def press_key(self, key):
        if key not in self.keys_map:
            raise Exception(f'Key "{key}" not configured!')

        key_function: str = self.keys_map[key]

        if self.is_path_to_script(key_function):
            # Runs custom script from path
            KeyboardFunctions.run_custom_script(key_function)
            return

        if self.is_pre_made_function(key_function):
            # Calls pre-made function
            function_name = key_function.split('(')[0]
            attribute = getattr(KeyboardFunctions, function_name)

            if not callable(attribute):
                raise Exception(f'Illegal function name "{attribute}"')

            args = self.get_function_args(key_function)

            attribute(*args)
            return

        KeyboardFunctions.key_stroke(key_function)

    @classmethod
    def is_path_to_script(cls, key_function: str) -> bool:
        """
        Checks if key function is a path to script
        Path to script format example -> 'C:/.../script.py'
        Path needs to be surrounded with '' to be considered valid

        :param key_function: Function defined in KeysLayout.config file
        :return: True if syntaxe matches
        """
        if not key_function.startswith("'"):
            return False

        if not key_function.endswith("'"):
            return False

        return True

    @classmethod
    def is_pre_made_function(cls, key_function: str) -> bool:
        """
        Checks if key function is a valid pre-made function

        :param key_function: Function defined in KeysLayout.config file
        :return: True if name matches a pre-made function and has '()'
        """
        if '(' not in key_function:
            return False

        if ')' not in key_function:
            return False

        function_name = key_function.split('(')[0]

        if not hasattr(KeyboardFunctions, function_name):
            return False

        return True

    @classmethod
    def get_function_args(cls, key_function) -> list:
        # Gets what is inside ()
        raw_args = key_function.split('(')[1]
        raw_args = raw_args.split(')')[0]

        if not raw_args:
            return []

        if ',' in raw_args:
            return raw_args.split(',')

        return [raw_args]

    def load_keys_layout(self):
        with open('./KeysLayout.config', 'r') as file:
            file_content = file.readlines()
            file_content = self.clean_file_content(file_content)

        self.map_keys(file_content)

    def map_keys(self, file_content):
        self.check_config_file(file_content)

        self.keys_map = {}

        for line in file_content:
            # If line is blank, skip iteration
            if not line:
                continue

            key, function = line.split(':', 1)
            self.keys_map[key] = function

    def check_config_file(self, file_content):
        """
        Checks if the KeysLayout.config syntaxe is correct
        """
        # ToDo
        pass

    @classmethod
    def clean_file_content(cls, file_content):
        cleaned_content = []
        for line in file_content:
            line = line.replace('\n', '')
            line = line.replace(' ', '')

            # Skips line if it is blanck
            if not line:
                continue

            # Skips comments
            if line.startswith('#'):
                continue

            if '|' in line:
                line = line.split('|')  # separate multiple keys into a list
            else:
                line = [line]  # Puts single key inside a 1 index list

            cleaned_content += line

        return cleaned_content
