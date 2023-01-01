class Cache:
    def __init__(self):
        self.keys_map = {}  # {'B2': 'foo(12)', ...}

        self.load_keys_layout()

    def load_keys_layout(self):
        with open('./KeysLayout.config', 'r') as file:
            file_content = file.readlines()
            file_content = self.clean_file_content(file_content)

        self.map_keys(file_content)

    def map_keys(self, file_content):
        self.check_config_file(file_content)

        self.keys_map = {}

        for line in file_content:
            key, function = line.split(':', 1)
            self.keys_map[key] = function

    def check_config_file(self, file_content):
        """
        Checks if the KeysLayout.config syntaxe is correct
        """
        # ToDo
        pass

    @staticmethod
    def clean_file_content(file_content):
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
