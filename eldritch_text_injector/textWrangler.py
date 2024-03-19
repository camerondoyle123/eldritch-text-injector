import random


class textWrangler:
    """
    define all input and outputs for wrangling here
    """

    def __init__(self, input_txt: str, eldritch_txt: str):
        """
        input_txt: str, path to the file that contains your 'normal' narrative.
        eldritch_txt: str, path to file that contains your voices of madness.
        low_n: int, class variable for later on!
        """
        self.input_txt = input_txt
        self.eldritch_txt = eldritch_txt
        self.low_n = int()

    def return_input_str(self):
        """
        retrieve the input 'normal' text from an input file as defined in the
        Class.
        
        return: string from file
        """
        with open(self.input_txt, "r") as f:
            input_str = f.readlines()

        return input_str

    def return_eldritch_str(self):
        """
        retrieve the input 'Eldritch' text from an input file as defined in the
        Class.
        
        return: list of strings (elements defined by line breaks) from file.
        """
        with open(self.eldritch_txt, "r") as f:
            eldritch_str = f.readlines()

        return eldritch_str

    @staticmethod
    def break_txt(txt, low_n):
        """
        txt: str, input string of characters of some kind
        low_n: int, the minimum number of parts to split the string into.
                    always do plus 5 more parts than whatever the length is(?)

        desc: split an input string (originally, from inside a list)
              into a random number of parts ranging from 2 -> char_len.

        return: a list of strings
        """

        if low_n < 1:
            low_n += 1

        parts = list()
        for t in txt:
            split_n = random.randint(low_n, low_n + 5)
            parts = [t[i : i + split_n] for i in range(0, len(t), split_n)]

        return parts

    @staticmethod
    def return_random_non_ascii():
        """
        Static method with no arguments. Can be called independently of 
        other methods.

        Will cycle through characters (at random, repeating allowed) 163 -> 255 
        in the non-standard ASCII set (i.e. those that are greater than 125, 
        although for my purposes, I've set it to 163 for extra Eldritch-ness).

        """

        non_standard_ascii = " ".join(chr(i) for i in range(162, 254)).split()
        upper = len(non_standard_ascii) - 1
        rand_int = random.randint(0, upper)

        non_standard_char = non_standard_ascii[rand_int]

        return non_standard_char

    def intersperse_lists(self):
        """
        Intersperse arbitrary, differing length lists together.

        In this case, input_list is the original 'normal' text
        that is split into 5 parts.

        eldritch_list however, will cycle through the lines provided
        from the eldritch_input file (i.e. line breaks as string in a list).

        This then returns a list that intersperses the eldritch elements
        between the existing 'normal' list of strings.
        """
        input_list = self.break_txt(self.return_input_str(), self.low_n)
        eldritch_list = self.inject_non_ascii()

        # get subdivision sizes in input_list
        m = len(input_list) // len(eldritch_list)

        # create list of lists (in blocks)
        z = [
            input_list[m * i : m * (i + 1)] + [aux]
            for i, aux in enumerate(eldritch_list)
        ]

        # flatten
        z = [k for sec in z for k in sec]

        return z

    def inject_non_ascii(self):
        """
        Firstly, grab the input_eldritch file as a list of strings 
        (based on line breaks in the input file).

        Then, cycle through and give each character in the list a 
        5% change of having it replaced with a non-standard ASCII character.

        This ignores white space for ease-of-reading later on.

        """
        text = self.return_eldritch_str()
        out_list = list()
        self.low_n = len(text)

        for t in text:
            string_list = list()
            inject_list = [*t]

            for inject in inject_list:

                if random.random() < 0.05:
                    c = self.return_random_non_ascii()
                else:
                    c = inject

                # ignore regular whitespace
                if inject == " ":
                    c = inject

                string_list.append(c)

            out_str = "".join(string_list).rstrip()
            out_list.append("**" + out_str + "** ")

        return out_list

    def write_markdown(self):
        """
        write 'em, Bill!
        """
        str_to_write = self.intersperse_lists()
        with open("./md/eldritch.md", "w") as f:
            f.write("".join(str_to_write))
            f.close()


    def concat_txt_file(self):
        """
        eeewww, I really should fix this...
        """

        # gross, but works
        self.write_markdown()

        # Open the source text files
        file1 = open("./md/base-readme.md", "r")
        file2 = open("./md/eldritch.md", "r")
        
        # Read the contents of the text files
        content1 = file1.read()
        content2 = file2.read()
        
        # Close the source text files
        file1.close()
        file2.close()
        
        # Open the destination file
        destination_file = open("README.md", "w")
        
        # Write the concatenated content to the destination file
        destination_file.write(content1 + content2)
        # Close the destination file
        destination_file.close()
    
        return




