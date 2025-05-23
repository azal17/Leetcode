#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		  result, maxx, minn = arr[0], arr[0], arr[0]
		  
		  for i in range(1, len(arr)):
		      element = arr[i]
		      
		      if element <0:
		          maxx, minn = minn, maxx
		      maxx = max(element, element*maxx)
		      minn = min(element, element*minn)
		      
		      result = max(result, maxx)
		  return result