dim=10
epoch=100
#fname="dailystar"
/home/anumoshsad/StarSpace/starspace train -trainFile /home/anumoshsad/WordEvolution/Data/word_list/*.txt -model output_avengers -trainMode 1 -label 'page' -thread 2 -dim $dim -epoch $epoch
