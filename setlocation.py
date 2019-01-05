import pandas as pd

if __name__ == '__main__':
	df 	=	pd.read_csv('all_stus_in_room.csv')
	df['Row'] = 0
	df['Col'] = 0
	handle = open('reges_of_class.txt')
	lines = handle.readlines()
	reges = [l[:-1] for l in lines]
	rdic, cdic = {}, {}
	reges = [str(reg) for reg in reges]


	row, col = 1,1

	for reg in reges:
		rdic[reg] = row
		cdic[reg] = col
		if row == 6:
			row = 1
			col += 1
		else:
			row += 1

	# for reg in reges:
	# 	print(f'{reg} -- {rdic[reg]} -- {cdic[reg]}')

	df = pd.read_csv('stus_in_room_details.csv')

	def getrow(string):
		return rdic[str(string)]

	def getcol(string):
		return cdic[str(string)]

	df['Row'] = df['RegNo'].apply(getrow)
	df['Col'] = df['RegNo'].apply(getcol)

	df.to_csv('stus_in_room_details.csv')

