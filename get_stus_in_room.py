#all_students_of_lpu.csv
import pandas as pd

if __name__ == '__main__':
	handle = open('reges_of_class.txt')
	lines = handle.readlines()
	reges = [l[:-1] for l in lines]
	df = pd.DataFrame(reges, columns  = ['RegNo'])
	print(df)
	df.to_csv('all_stus_in_room.csv')
	

