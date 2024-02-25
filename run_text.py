from eldritch_text_injector.textWrangler import textWrangler

text = textWrangler("./files/input.txt", "./files/eldritch.txt")


if __name__ == "__main__":
    text.concat_txt_file()

