import sys
import os
Files = os.listdir(os.getcwd() + '/TO BE CONVERTED')

# Change encoding_from and encoding_to parameters as you desired

def correctSubtitleEncoding(filename, newFilename, encoding_from = 'iso-8859-9', encoding_to='UTF-8'):
    with open(os.getcwd() + '/TO BE CONVERTED/' + filename, 'r', encoding=encoding_from) as fr:
        with open(os.getcwd() + '/CONVERTED/' + newFilename, 'w', encoding=encoding_to) as fw:
            for line in fr:
                fw.write(line[:-1]+'\n')

for NameOfFile in Files:
  correctSubtitleEncoding(NameOfFile, NameOfFile.replace('.srt', '_UTF8.srt'))