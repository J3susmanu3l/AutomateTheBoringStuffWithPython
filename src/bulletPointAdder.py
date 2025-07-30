import pyperclip
text = pyperclip.paste()
text_lines = list(text.split("\n"))
text_lines = list(text_lines)
for c in range(len(text_lines)):
    text_lines[c] = text_lines[c].strip('\r ')
    text_lines[c] = "* " + text_lines[c]
final_text = "\n".join(text_lines)
pyperclip.copy(final_text)



# this it the 
# text to be copied into 
# the clipboard



'''
this is the result of the function I just created. It basically copies again to the
clipboard all the text, but with *s in the fron of each new line
'''
# * this it the
# * text to be copied into
# * the clipboard


