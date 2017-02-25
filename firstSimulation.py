
# coding: utf-8

# In[11]:

import simpy


# In[43]:

#creating an Arrival class
class Arrival(object):
    def __init__(self, env):
        self.env = env
        # Start the run process everytime an instance is created.
        self.action = env.process(self.run())
        
    
        #the moment the user enters the queue
        #enterQueue = env.now
        #arrivalRate = 15
        #user = User(env = env, ID = userID)
        #print 'User ' + str(user.ID) + ' generated'
            
    #create a method run that perfomrs the actions when is the enviroment starts running
    def run(self):
        #generate an id for each user
        userID = 0
        while True:
            arrivalRate = 15
            yield self.env.timeout(arrivalRate)
            user = User(env = env, ID = userID)
            print 'User ' + str(user.ID) + ' generated'
            userID +=1
        
class User(object):
    def __init__(self, env,ID):
        self.env = env
        #set a name by default
        self.ID = ID
        # Start the run process everytime an instance is created.
        #self.action = env.process(self.run())


# In[44]:

env = simpy.Environment()
arrival = Arrival(env)
env.run(until=31)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



