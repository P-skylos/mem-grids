# what's this for?

This is a small script meant to generate letter grids to help memorize passages of text. A letter grid consists of the first letter of every word in the passage in sequence, this way you can follow along and give yourself a little hint while still working out your recall.

# usage

provide raw text, or an in put path with the `-f` flag to be turned into letters. you can specify an output file with `-o`, toggle punctuation with `-p` and whitespace with `-s`.

# reflection

Well, I'm glad I go around to making this since I've some songs I've been meaning to memorize. But in using it I've found some things I hadn't considered when I set out to make a quick script one afternoon.
- apostrophe's can occur inside words which can cause odd behavior.
- to tell when an apostrophe is an apostrophe and not a single quote would need a lexer like approach rather than my quick n dirty find and replacing.

I also got the chance to learn about the argparse module so that's exciting. If I return to this project it'll probably be a javascript lexer to put on my website.