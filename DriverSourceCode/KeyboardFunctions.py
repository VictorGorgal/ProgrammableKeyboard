class KeyboardFunctions:
    @classmethod
    def key_stroke(cls, sequence: str):
        # Generate a list with all key seqeunces
        if '+' in sequence:
            sequence = sequence.split('+')
        else:
            sequence = [sequence]

        print(sequence)

    @classmethod
    def shutdown(cls):
        print('shutdown')

    @classmethod
    def restart(cls):
        print('restart')

    @classmethod
    def run_custom_script(cls, path: str):
        print('Running script')

    @classmethod
    def clipboard(cls, mode: str, idx: str):
        print(f'setting clipboard {idx} in {mode}')

    @classmethod
    def foo(cls, i, ii, iii):
        print(f'foo {i}, {ii}, {iii}')
