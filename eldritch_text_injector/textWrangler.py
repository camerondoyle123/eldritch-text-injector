import random

class textWrangler:
    """
    define all input and outputs for wrangling here
    """

    def __init__(self, input_txt: str, eldritch_txt: str):
        """
        input_txt: str, path to the file that contains your 'normal' narrative.
        eldritch_txt: str, path to file that contains your voices of madness.
        """
        self.input_txt = input_txt
        self.eldritch_txt = eldritch_txt
        self.input_list = list()
        self.eldritch_list = list()
        self.low_n = int()

    def return_input_str(self):
        with open(self.input_txt, 'r') as f:
            input_str = f.readlines()

        return input_str

    def return_eldritch_str(self):
        with open(self.eldritch_txt, 'r') as f:
            eldritch_str = f.readlines()

        return eldritch_str

    @staticmethod
    def break_txt(txt, low_n):
        """
        split an input string (originally, from inside a list)
        into a random number of parts ranging from 2 -> char_len.
        """

        if low_n < 1:
            low_n += 1

        parts = list()
        for t in txt:
            split_n = random.randint(low_n, low_n+5)
            parts = [t[i:i+split_n] for i in range(0, len(t), split_n)]

        return parts

    @staticmethod
    def return_random_non_ascii():

        non_standard_ascii = ' '.join(chr(i) for i in range(162, 254)).split()
        upper = len(non_standard_ascii)-1
        rand_int = random.randint(0, upper)

        non_standard_char = non_standard_ascii[rand_int]

        return non_standard_char

    
    def intersperse_lists(self):
        """
        intersperse arbitrary, differing length lists together
        """
        input_list = self.break_txt(self.return_input_str(), self.low_n)
        eldritch_list = self.inject_non_ascii()
        
        # get subdivision sizes in input_list
        m = len(input_list) // len(eldritch_list)
        
        # create list of lists (in blocks)
        z = [input_list[m*i:m*(i+1)] + [aux] for i,aux in enumerate(eldritch_list)]
        
        # flatten
        z = [k for sec in z for k in sec]

        return z
        
    def inject_non_ascii(self):
        text = self.return_eldritch_str()
        out_list = list()
        self.low_n = len(text)

        for t in text:
            string_list = list()
            inject_list = [*t]

            for inject in inject_list:

                if random.random() < 0.1:
                    c = self.return_random_non_ascii()
                else:
                    c = inject

                # ignore regular whitespace
                if inject == ' ':
                    c = inject

                string_list.append(c)

            out_str = ''.join(string_list).rstrip()
            out_list.append('**' + out_str + '** ')

        return out_list

    def write_markdown(self):
        str_to_write = self.intersperse_lists()
        with open("eldritch.md", "w") as f:
            f.write(''.join(str_to_write))
            f.close()






