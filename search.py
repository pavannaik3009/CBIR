# import the necessary packages
from project.colordescriptor import ColorDescriptor
from project.searcher import Searcher
import argparse
import cv2
# construct the argument parser and parse the arguments
argp = argparse.ArgumentParser()
argp.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
argp.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
argp.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(argp.parse_args())
# initialize the image descriptor
cdvar = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread(args["query"])
features = cdvar.describe(query)
# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)
# display the query
cv2.imshow("Query", query)
# loop over the results
for (score, resultID) in results:
	# load the result image and display it
	result = cv2.imread(args["result_path"] + "/" + resultID)
	cv2.imshow("Result", result)
	cv2.waitKey(0)
