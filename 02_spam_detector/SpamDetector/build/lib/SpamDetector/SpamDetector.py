import pickle

class SpamDetector:

	"""SpamDetector Classe

    	Attributes:
    	thresh_spam (float): A float value that define the threshhold for the spam decision, if 0, means that any slight indice of spam id valid, if 1,
    	only cases with strong indice are spam

    	Methods:
    	
    	set_model     : Set the the model for prediction
    	set_thresh_spam: Set the value of the threshold for the spam detector
    	get_thresh_spam: Returns the threshold of the threshold from the spam detector
		prob_spam     : Return the probabilitie of a message be a spam
		is_spam       : Evaluate the spam probabilitie based on the threshold

   	"""
  
  	#Load the model and sets the threshold
	def __init__(self,thresh_spam=0.5):
    	
		self.sms_model = None
		self.thresh_spam = thresh_spam

	#Set the model to predict
	def set_model(self,model):

		self.sms_model = pickle.load(open(model, "rb"))

	#Return the threshhold
	def set_thresh(self,thresh_spam):

		self.thresh_spam = thresh_spam

	#Get the actual threshold
	def get_thresh(self):

		return self.thresh_spam

	#Get the probabilite of being a spam
	def prob_spam(self,text):

		return self.sms_model.predict_proba([text])[0][1]

	#Return if a message is a spam
	def is_spam(self,text):

		prob_spam = self.prob_spam(text)
		
		if (prob_spam>=self.thresh_spam):

			return True

		else:

			return False