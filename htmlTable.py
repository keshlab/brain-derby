import os
import sys
import HTML
import cherrypy

def CountRaters(study): 
		table = {}
		colors = {'0': 'red', '1': 'red', '2': 'orange', '3': 'orange', '4': 'green', '5':'green'}
		projectpath = os.path.join('/users/siddharth/keshlab/brainderby/mnt/QNAP/Datasets', study, 'Processing/Editing/Completed') #projectpath indicates absolute path to Completed folder
		folderpath = os.path.join('/users/siddharth/keshlab/brainderby/mnt/QNAP/Datasets', study, 'Processing/Editing/Raters') # folderpath indicates absolute path to Raters folder 
		for folder in os.listdir(folderpath):
			table[folder] = 0 			# initializes values of brains to zero 
		if len(os.listdir(projectpath)) > 0: 
			for file in os.listdir(projectpath): 
				filepath = os.path.join(projectpath, file)
				infile = open(filepath,'r', encoding = "latin-1")  # opens and reads each text file in log-files
				linelist = infile.readlines()
				lastline = (linelist[len(linelist)-1]) # reads the names that are in the last line 
				for names in table:
					if names == lastline:
						if table[names]:
							table[names] += 1  # if the name in the table matches the name in the text file, increment the brain count 
						else:
							table[names] = 1  # if the name in the table does not match the name in the text file, keep the count the same
		t=HTML.Table(header_row=['Names', 'Study', 'Number of Brains']) 
		for names in table:
			t.rows.append([names, study, table[names]])
			htmlcode=str(t)
				
		print(htmlcode)
	
		
CountRaters('BSNIP2')
CountRaters('BICEPS')
CountRaters('Childrens')
CountRaters('PARDIP') # input the name of the study, and view table of number of brains completed 

