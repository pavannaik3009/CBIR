# import the necessary packages
import numpy as np
import csv
class Searcher:
	def __init__(self, indexPath):
		# store our index path
		self.indexPath = indexPath
	def search(self, queryFeatures, limit = 10):
		# initialize our dictionary of results
		results = {}

		# open the index file for reading
		with open(self.indexPath) as f:
			# initialize the CSV reader
			my_reader = csv.reader(f)
			# loop over the rows in the index
			for row in my_reader:
				
				features = [float(x) for x in row[1:]]
				d = self.chi2_distance(features, queryFeatures)
				
				results[row[0]] = d
			# close the reader
			f.close()
		
		results = sorted([(v, k) for (k, v) in results.items()])
		
		return results[:limit]

	def chi2_distance(self, histA, histB, eps = 1e-10):
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])
		# return the chi-squared distance
		return d