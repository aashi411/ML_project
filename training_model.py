import pickle
class SalaryModel: 
    def __init__(self):
        self.base = 30000
        self.exp_coeff = 5000
        self.skill_coeff = 2000

    def predict(self, years, skill):
        return self.base + (years* self.exp_coeff)+ (skill*self.self.skill_coeff)
    
model = SalaryModel()

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("model work completed")