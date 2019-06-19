class A:
	MAX_SIZE = 228

    data_results = []
    title = 'bla bla'
    
    def __init__(self):
    	self.MAX_SIZE = 228
        self.data_results2 = []
    
    def calculate(self, a, b):
        self.data_results.append(a+b)
        self.data_results2.append(a+b)
        return self.data_results[-1]
    

    