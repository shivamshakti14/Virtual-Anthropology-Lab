f1= open('anthropologylink.txt','r')
num=1
num1=1
list11=['Identification of Prehistoric handaxe','Identification of finger prints patterns','Pottery-Virtual Reconstruction of Shapes','Calculation of Indices','Obtain the main line formula','Skeleton - Assembling, Identification & labeling','Blood Group Techniques','Hunting, Fishing, Gathering Tools',"Mendel's Law"]
for ll in f1:
	if 'http' not in ll:
		print 'name of experiment'+ll
'''
    for qq in range(0,9):
    	if list11[qq]==str(ll):
	    	str1=ll
	    	num=1
	    	print 'name of experiment'+ll

'''