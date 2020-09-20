# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  result = [(i, text[i:]) for i in range(len(text))]
  result.sort(key=lambda x: x[1])
  result = [result[i][0] for i in range(len(text))]
  return result


if __name__ == '__main__':
  text = input()
  print(" ".join(map(str, build_suffix_array(text))))
