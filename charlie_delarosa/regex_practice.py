import re
def get_matching_words(regex):
  results = []
  words = [
    "baby",
    "baseball",
    "denver",
    "facetious",
    "issue",
    "mattress",
    "obsessive",
    "paranoia",
    "rabble",
    "union",
    "volleyball",
  ]

  for word in words:
    if re.search(regex, word):
      results.append(word)

  return results

# my_expression = r"ss"
# my_expression = r"b\wb"
# my_expression = r"b\w+b"
# my_expression = r"a\w*e\w*i\w*o\w*u"
# my_expression = r"[aeiou][aeiou]$"
# my_expression = r"^[regularexpression]+$"
# my_expression = r"^[^regex]+$"

# my_expression = r"a\w*b"
# my_expression = r"ab"
# my_expression = r"io"
# my_expression = r"e$"
# my_expression = r"(\w)\1\w*(\w)\2"

print get_matching_words(my_expression)
