# install PyPDF2
# pip3 install PyPDF2

# importing all the required modules
import PyPDF2
import pandas as pd
import os
import io
import re


os.getcwd()

# ------------------------------------------------------------
# creating an object
file = open(
    '/home/rafatieppo/Documents/pessoal/financas/pgto_contas_pessoais/c6_2021_05_boleto.pdf', 'rb')

# creating a pdf reader object
filepdf = PyPDF2.PdfFileReader(file)


page = filepdf.getPage(0)
page_content = page.extractText()
print(page_content)

# reading and line by line in a txt file
content = ""
print(filepdf.numPages)
num_pages = 2

# writing file
qfile = open('./c6_2009_05.txt', 'w')
for i in range(0, num_pages):
    # content += pdf.getPage(i).extractText() + "\n"
    content = filepdf.getPage(0)
    content.extractText()
    # Printing Page Number
    # print("Page No: ", i)
    # Extracting text from page
    # And splitting in blocks by " PAÍS"
    blocks = content.extractText().split(" PAÍS")
    # each Block is splitted by "R$ "
    lsDicts = []
    for j in range(1, len(blocks)):
        b = blocks[j]  # .split("R$ ")r'\W+
        cc = re.split(r',[0..9][0..9]', b)
        for jj in range(len(b) - 1):
            date = b[jj][0:10]
            local = b[jj][10:]
            price = b[jj + 1][0:6]
            price = list(price)
            price[-3] = "."
            price = ("".join(price))
            dictline = {"date": date,
                        "local": local,
                        "price": price}
            lsDicts.append(dictline)

    # Finally the lines are stored into list
    # For iterating over list a loop is used
    for j in range(len(text)):
        # Printing the line
        # Lines are seprated using "\n"
        # print(text[j])
        content = text[j]
        qfile.write(str(content))
        # print(content)
    # For Seprating the Pages
    # print()
# closing the pdf file object
qfile.close()
file.close()

# ------------------------------------------------------------
# reading lines from txt file and append in a list

txt_file = open('./q2009.txt', 'r')
lines = txt_file.readlines()  # leitura de todas as linhas
txt_file.close()

ls_col0 = []
ls_col1 = []
ls_col2 = []
ncount = 0

for i in range(len(lines)):
    if ncount == 0:
        a = lines[i].strip()
        ls_col0.append(a)
        ncount += 1
    elif ncount == 1:
        a = lines[i].strip()
        ls_col1.append(a)
        ncount += 1
    elif ncount == 2:
        a = lines[i].strip()
        ls_col2.append(a)
        ncount = 0
    else:
        pass

df_q2009 = pd.DataFrame({"ISSN": ls_col0,
                         "TITULO": ls_col1,
                        "ESTRATO": ls_col2})
df_q2009.to_csv('./qualis2009geral.csv')

# ------------------------------------------------------------
# for x in txt_file:
#     print(txt_file.readline())
#
#
# yyi = config_file.readlines()[5].split(':')[1]
# yyi = yyi.rstrip('\n')
# yyi = yyi.strip(' ')
# yyi = float(yyi)
# config_file.close()
