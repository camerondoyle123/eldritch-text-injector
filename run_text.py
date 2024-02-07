from eldritch_text_injector.textWrangler import textWrangler

text = textWrangler('./files/input.txt', './files/eldritch.txt')

text.write_markdown()


# Open the source text files
file1 = open('base-readme.md', 'r')
file2 = open('eldritch.md', 'r')

# Read the contents of the text files
content1 = file1.read()
content2 = file2.read()

# Close the source text files
file1.close()
file2.close()

# Open the destination file
destination_file = open('README.md', 'w')

# Write the concatenated content to the destination file
destination_file.write(content1 + content2)
# Close the destination file
destination_file.close()
