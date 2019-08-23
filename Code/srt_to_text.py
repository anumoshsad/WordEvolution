import pysrt
import glob

for file in glob.glob("../Data/*.srt"):
	text =''
	subs = pysrt.open(file)
	for sub in subs:
		text+=sub.text
	text = text.replace('<i>',' ')
	text = text.replace('</i>',' ')

	text = " ".join(text.split())

	with open("../Data/"+file[:-3], 'w') as text_file:
		text_file.write(text)


