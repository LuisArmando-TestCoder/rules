# Natural language to truth tables, for a bullet proof chat gpt logic module

ChatGPT needs real logic, not an emergent one...

```bash
pip install dotenv
pip install openai
cd src
```

create a .env with a openai api key as such

```r
OPENAI_API_KEY=blablabla-this-is-a-palceholder-for-your-openai-api-key
```

plug a string like

```
If desire is the root of suffering, and suffering is the root of greatness, then desire is the root of greatness
```

into the function 

```py
from natural_to_natural_restricted import get_natural_to_natural_restricted

naturalRestrictedSentence = get_natural_to_natural_restricted(natural_sentence)
```

which would be

```t
if (desire_is_the_root_of_all_suffering and suffering_is_the_root_of_all_greatness) then desire_is_the_root_of_all_greatness
```

and then turn that into a truth table

```py
sentence_table = get_sentence_table(naturalRestrictedSentence)

for sentence_row in sentence_table:
    print(sentence_row)
```

which would return the following

```t
Possible: not desire_is_the_root_of_all_suffering and not suffering_is_the_root_of_all_greatness and not desire_is_the_root_of_all_greatness
Possible: not desire_is_the_root_of_all_suffering and not suffering_is_the_root_of_all_greatness and desire_is_the_root_of_all_greatness
Possible: not desire_is_the_root_of_all_suffering and suffering_is_the_root_of_all_greatness and not desire_is_the_root_of_all_greatness
Possible: not desire_is_the_root_of_all_suffering and suffering_is_the_root_of_all_greatness and desire_is_the_root_of_all_greatness
Possible: desire_is_the_root_of_all_suffering and not suffering_is_the_root_of_all_greatness and not desire_is_the_root_of_all_greatness
Possible: desire_is_the_root_of_all_suffering and not suffering_is_the_root_of_all_greatness and desire_is_the_root_of_all_greatness
Contradictory: desire_is_the_root_of_all_suffering and suffering_is_the_root_of_all_greatness and not desire_is_the_root_of_all_greatness
Possible: desire_is_the_root_of_all_suffering and suffering_is_the_root_of_all_greatness and desire_is_the_root_of_all_greatness
```

**This project dives into the realm of logical reasoning and natural language processing. By translating natural language sentences into logical forms, we can achieve more structured and precise reasoning.**