import os
from mobi import Mobi
def converandadd(book):
    filname=os.path.join(path,book)
    newname=os.path.join(output,os.path.splitext(book)[0]+'.txt')
    #print(filname,'\nj',newname)
    book = Mobi(filname);
    book.parse();
    # this will print, 1 record at a time, the entire contents of the book
    title=book.title().decode('utf-8')
    author=book.author().decode('utf-8')
    cmd='ebook-convert '+filname+ ' ' +newname
    last="\n\n\n'#####BOOK INFO#####\nAuthor:"+author+"\nTitle:"+title
    os.system(cmd)

    with open(newname, "a") as myfile:
        myfile.write(last)
path ='/home/satyam/bookk'
output='/home/satyam/bookk/txtbooks'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        converandadd(file)

# for f in files:
#     print(f)
