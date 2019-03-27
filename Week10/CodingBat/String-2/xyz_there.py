def xyz_there(str):
  	str = '#' + str
  	for i in range(1, len(str) - 2):
    	if str[i:i + 3] == 'xyz' and str[i - 1] != '.':
      		return True
  	return False