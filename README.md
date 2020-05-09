## medibot

### pipeline.py

- [ ] remove url and links
- [ ] spellchecker
- [ ] extract gender and age


### Run main.py


```python main.py -file_index=10 -min_length=2 -window=3```

```file_index``` values can be any integer below 88. <br/>

```min_length``` is basically a hack to remove punctuation and single/double length special symbols or string. <br/>

```window``` is the number of tokens around plus the keyword that would be returned. So, if window is 2 then, number of tokens reuturned would be 5 (2 * window + 1). <br/>

You need to install nltk library and uncomment the two lines in the import section of ```pipeline.py``` once its downloaded for the first time.