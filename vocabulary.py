import os.path
import unicodedata
import re
from collections import Counter
import pdb


class Vocabulary:
    single_words = []
    double_words = []

    def build(self, *args):
        content = ""
        files_content = ""
        list_contents = []
        self.single_words = []
        self.double_words = []
        for arg in args:
            if os.path.exists(arg) == False:
                return

            file = open(arg)
            content = file.read().lower()
            list_contents.append(content)
            # remove special characters
            content = re.sub(r"[^\w\s]", " ", content)
            # match all single words
            prog = re.compile(r"\w[\w|\d]*",
                              re.IGNORECASE | re.MULTILINE | re.UNICODE)
            words = prog.findall(content)

            # compose double words vocabulary
            for index in range(len(words)):
                if index > 0:
                    w2 = words[index - 1] + " " + words[index]
                else:
                    w2 = words[index] + " " + words[index + 1]

                if w2 not in self.double_words:
                    self.double_words.append(w2)

        # compose single words vocabulary
        for content in list_contents:
            words = prog.findall(content)
            for word in words:
                if word not in self.single_words:
                    self.single_words.append(word)

        print("Vocabulary")
        print("===== single words ======")
        print("{}".format(self.single_words))
        print("Size: {}".format(len(self.single_words)))
        print("===== double words ======")
        print("{}".format(self.double_words))
        print("Size: {}".format(len(self.double_words)))
        print()

        # find vocabulary occurrencies in files to build your arrays
        for index, content in enumerate(list_contents):
            counters = []
            print("Arrays")
            print("===== file {} =====".format(index + 1))
            for sw in self.single_words:
                counters.append(content.count(sw))
            print("Single words: {}".format(counters))

            counters = []
            for dw in self.double_words:
                counters.append(content.count(dw))
            print("Double words: {}".format(counters))
