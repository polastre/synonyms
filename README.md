synonyms
========

A python library for checking if a word has a synonym.

Unlike a lot of the other libraries out there, this one is not tied to
a specific data source.  Instead you supply the data from your favorite
source.

# Use

Load a synonyms object from the factory. Accepts either a string with the
synonym file contents (see below), a file pointer, or a list of lists that
contain the synonyms.

  >>> from synonyms import load
  >>> s = load(open('syn.txt'))
  >>> s.match('United States')
  'usa'
  >>> s.match('United States', all=True)
  ['USA', 'United States', 'us', 'the states']
  >>> 'usa' in s:
  True

# Format

The synonyms file is roughly the same format that Solr uses.

Comments start the line with #

Synonyms are separated by commas.  The first word is considered the master
synonym.

Example:

  # This is a comment
  USA, United States, us, the states
  foo, bar, baz