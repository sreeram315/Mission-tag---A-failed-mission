import pandas as pd


if __name__ == '__main__':
	df_stusinroom = pd.read_csv('all_stus_in_room.csv')
	df_unistus	  = pd.read_csv('all_students_of_lpu.csv')
	stus_in_room  = df_stusinroom['RegNo']
	# df_unistus.set_index(['RegNo'], inplace = True)
	reges = list(df_stusinroom['RegNo'])

	# def stu_filter(string):
	# 	if string in reges: return True
	# 	return False	

	# ans = df_unistus[df_unistus['RegNo'] in reges]

	df = df_unistus[df_unistus['RegNo'].isin(reges)]

	# print(df)

	df.to_csv('stus_in_room_details.csv')