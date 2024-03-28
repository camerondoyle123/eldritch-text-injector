# eldritch-text-injector

The following repository was born of madness, as H.P. Lovecraft intended. However, I would argue that if he learnt of this piece of software's existence, he would likely be surprised.

Given a normal string input as found in `files/input.txt` , presented as a single line, a new markdown file will be generated
with non-standard ASCII characters injected into an otherwise unhinged list of statements made by Agile managers (most likely).

The list of Agile commentary can be found in the `files/eldritch.txt` which are ingested via line breaks; that is, if you wish to add to the file just add a line break with the text you want.

Generally, the files are split into randomly generated chunks which allows the eldritch text to first be injected and then interspered to the original `files/input.txt`. Additionally,
there is a `mapping.py` file contained within which has a mapping of diacritic characters with their respective Unicode index representation which take precedence over randomly generated
'eldritch-like' characters.

Finally, the `base-readme.md` file will be concatenated with the generated `eldritch.md` file to generate the page your reading now.

Both the input `input.txt` and `eldritch.txt` files can be modified to your (despondent and broken) heart's content.

Largely inspired by [You Cannot Parse HTML with Regex](https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454)

## Usage

This repo does leverage [Poetry](https://python-poetry.org/) and it is recommended to create a local virutal-environment first, such as `poetry-eldritch`, to then run the following:

```
                  > mkvirtualenv your_venv_here
(your_venv_here)  > poetry run python run_text.py
```

If you want to see the compiled output, simply push them back to your feature branch on this repo.


## Example


SCP-UNCLASSIFIED <br> Item#: SCP-UNCLASSIFIED <br> Object Class: Keter <br> Special Containment Procedures: This SCP is currently u**hÂhÃ - ¦t'š ƒûÑÑ ÿôû hãÐ tÖ óÔ®k th®óügh ýÔµ® £µÑÇh þ®ëÁk tÔ mÊét tíË šÞ®ìñt gÓª£§!** ncontained and has ethereal properties, making it difficult to track. It primarily manifests in office environments that contain re**´ hÖÞé èvè®ÝÕÑé ¦š ¢õmƒÓ®tåß£é wÌth thëî® šÞ®íñt ¢Ômm¦tmÈñtš hÂhå** ferences to the Agile Manifesto. Side-effects of the SCP often result in textual artefacting within documentation referring to it.
**I ©ÄÑôt þÉ£¡ËvÉ Õü® vË£ÔÇìtÿ ¦§ 50%!** 