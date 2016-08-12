from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from autocorrect import spell

f1= open('anthropologylink.txt','r')
num=1
num1=1
list11=['Identification of Prehistoric handaxe','Identification of finger prints patterns','Pottery-Virtual Reconstruction of Shapes','Calculation of Indices','Obtain the main line formula','Skeleton - Assembling, Identification & labeling','Blood Group Techniques','Hunting, Fishing, Gathering Tools',"Mendel's Law"]
for ll in f1:
    if 'http' not in ll:
    	str1=ll
    	num=1
    	print 'name of experiment = '+ll
    else:
	    #driver = webdriver.Firefox()
	    print ll
	    driver = webdriver.Chrome('/home/shivam/Downloads/chromedriver')
	    driver.set_page_load_timeout(100)
	    driver.get(ll)
	    element = driver.find_elements(By.XPATH,'//p')
	    #filewritename = str(num1)+ '_' + str(num) + '.txt'
	    filewritename = str1+str(num)+".txt"
	    num+=1
	    count =0 
	    fp = open(filewritename,'w')
	    for ii in element:
	        q = ii.text
	        lis = ii.text.split()
	        print 'paragraph ' + str(count)
	        for j in lis:
	            qqq=j.replace('.',',').replace('-',',').replace('(',',').replace(')',',').replace('+',',').replace('=',',').replace(':',',').replace(';',',').replace('/',',').replace("[",',').replace(']',',').replace('{',',').replace('}',',').replace('!',',').replace('@',',').replace('#',',').replace('$',',').replace('%',',').replace('^',',').replace('&',',').replace('*',',').replace('_',',').replace('"',',').replace("'",',').replace('<',',').replace('>',',').replace('?',',').replace('`',',').split(',')
	            for qqq1 in qqq:
	                aa=spell(qqq1)
	                if aa!=qqq1 and aa !='a' and aa!= 'of':
	                    print qqq1,aa
	                    try:
	                        aaaa = str(str(count)+' '+qqq1 + ' = ' + aa) + '\n'
	                        fp.write(aaaa)
	                    except:
	                        pass

	        count+=1

	    fp.close()
	    driver.close()
	                #if not d.check(j):
	                 #   print d.suggest(j)
