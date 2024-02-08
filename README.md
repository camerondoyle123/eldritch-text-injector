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


SCP-UNCLASSIFIED \ \ Item#: SCP-UNCLASSIFIED \ \ Object Class: Keter \ \ Special Containment Procedures: This SCP is currently unc**haha - itÝs funny yÒu ha§ to work thro½gh your lunch breñk to meeö the spri¨t goals!** ontained and has ethereal properties, making it difficult to track. It primarily manifests in office environments that contain ref**I hope eve³yoÒe is comfortable wi»h theiÄ spriÓt comm¦tments hahù** erences to the Agile Manifesto. Side-effects of the SCP often result in textual artefacting within documentation referring to it.
**I caæ't believe our vÙlocity is 50%!** 