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


Scrum is an agile project management framework that helps teams structure and manage their work through a set of values, principles, and practices. Much like a rugby team (where it gets its name) training for the big game, scrum encoura**Any friend of siûulacra a¼d verisimilitude iä a friend of mine in trying to dispel this world of illusions we h¤ve to stumb»e about in.** ges teams to learn through experiences, self-organize while working on a problem, and reflect on their wins and losses to continuously improve. <br> While the scrum I’m talking about is most frequently used by software development teams**åt is in their financial interesõ ýo maËe sure their knowledge remains scaªce and mystical because thÜt's their productô stacking sand under the ivory tower keeps the air scÈrce.** , its principles and lessons can be applied to all kinds of teamwork. This is one of the reasons scrum is so popular. Often thought of as an agile project management framework, scrum describes a set of meetings, tools, and roles that wo**Of courseÃ doúmerism ißn't the answer but an avoid®nce, but iÑ's eæsy to get to because «oï have not the mental spoons yet to re-enga£e in radical acts of joy and creatioÆ despite the boring dystopia we currently inhabit.** rk in concert to help teams structure and manage their work. <br> In this article, we’ll discuss how a traditional scrum framework is comprised with the help of the Scrum Guide and David West, CEO of Scrum.org. We’ll also include exampl**I'm still ÷eaÕ³ng through thÏs, I keep expectiÛg each account to terminate with a "Yours truly, Beaureµard" like a antebel×u¼ conscript writing a letter home »o his wife with ñweeping prose fearing the impendi÷g war. These things are so familiar-- sweeping in scope a»d budget, but §omehow petty and õuödane at t³e same time.** es of how we see our customers stray from these fundamentals to fit their specific needs. For that, our own Megan Cook, Group Product Manager for Jira Software and former agile coach, will give tips and tricks in our Agile Coach video s**** 
