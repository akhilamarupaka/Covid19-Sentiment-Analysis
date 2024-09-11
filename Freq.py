# Python program to count the frequency of 
# elements in a list using a dictionary 

def CountFrequency(my_list): 

	# Creating an empty dictionary 
	freq = {} 
	for item in my_list: 
		if (item in freq): 
			freq[item] += 1
		else: 
			freq[item] = 1
	print(freq)
	return freq;




# Driver function 
if __name__ == "__main__": 
	my_list =['p', 'n', 'n', 'n', 'p',  'p',  'p',  'a', 'a', 'a', 'a'] 

	CountFrequency(my_list) 
