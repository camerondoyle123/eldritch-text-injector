# eldritch-text-injector

The following repository was born of madness, as H.P. Lovecraft intended. However, I would argue that if he learnt of this piece of software's existence, he would likely be surprised.

Given a a normal string input as found in `files/input.txt` , presented as a single line, a new markdown file will be generated
with non-standard ASCII characters injected into an otherwise unhinged list of statements made by Agile managers (most likely).

The list of Agile commentary can be found in the `files/eldritch.txt` which are ingested via line breaks; that is, if you wish to add to the file just add a line break with the text you want.

Generally, the files are split at into randomly generated chunks which allows the eldritch text to first be injected and then interspered to the original `files/input.txt`.

Finally, the `base-readme.md` file will be concatenated with the generated `eldritch.md` file to generate the page your reading now.

Both the input `input.txt` and `eldritch.txt` files can be modified to your (despondent and broken) heart's content.

Largely inspired by [You Cannot Parse HTML with Regex](https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454)

## Usage

Still using the traditional `setuptools` from base Python, you can install a development version of the package
into your local pip environment.

```
> activate your_venv_here
> python setup.py develop
> python run_text.py
```

If you want to see the compiled examples, simply push them back to your feature branch on this repo.


## Example


Lietuenant! They're breaking through our War**h¹®a - Åt's funny you had to wßrk througÊ your ñunch b¼eak to meet the sprint goàls!** p Shields! We can't hold them! Get a hold of**¹ hope everyone is cëmfortable with their sprinÈ commi¸ments haha**  yourself Guardsmen, they can't enter our fi**I can't believe our velocity is 50%ì** 
