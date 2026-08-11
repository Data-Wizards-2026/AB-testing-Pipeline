import random as r

class Experiment:
    # experiment_id
    # name
    # description
    # control
    # treatment
    # primary_metric
    # status
    def __init__(self, experiment_id, name, description, control, treatment, primary_metric, status):
        self.experiment_id = experiment_id
        self.name = name
        self.description = description
        self.control = control
        self.treatment = treatment
        self.primary_metric = primary_metric
        self.status = status

    def run_exp(self):
        print()
        print(f"------{self.name}------")
        print(f" >> id: {self.experiment_id}")
        print(f" >> desc: {self.description}")
        print(f" >> version-A: {self.control}")
        print(f" >> version-B: {self.treatment}")
        print(f" >> evaluating: {self.primary_metric}")
        print(f" >> status: {self.status}")
        print()

# Experiment class finish


# For experimental purposes
def random_experiment_generation():
    experiments = [
        {
            "name": "Homepage CTA Test",
            "description": "Test whether changing the homepage CTA improves user engagement.",
            "control": "Current homepage CTA",
            "treatment": "New homepage CTA",
            "primary_metric": "conversion_rate"
        },
    
        {
            "name": "Checkout Flow Test",
            "description": "Test whether simplifying the checkout process increases completed purchases.",
            "control": "Existing checkout flow",
            "treatment": "Simplified checkout flow",
            "primary_metric": "checkout_completion_rate"
        },
    
        {
            "name": "Product Recommendation Test",
            "description": "Test whether personalized recommendations increase product interactions.",
            "control": "Current recommendation system",
            "treatment": "Personalized recommendations",
            "primary_metric": "click_through_rate"
        },
    
        {
            "name": "Search Algorithm Test",
            "description": "Test whether a new search algorithm improves search success rate.",
            "control": "Current search algorithm",
            "treatment": "New search algorithm",
            "primary_metric": "search_success_rate"
        },
    
        {
            "name": "Pricing Page Test",
            "description": "Test whether a redesigned pricing page improves conversions.",
            "control": "Current pricing page",
            "treatment": "Redesigned pricing page",
            "primary_metric": "conversion_rate"
        },
    
        {
            "name": "Email Subject Test",
            "description": "Test whether different email subjects improve email engagement.",
            "control": "Current email subject format",
            "treatment": "Personalized email subjects",
            "primary_metric": "click_through_rate"
        },
    
        {
            "name": "Login Page Test",
            "description": "Test whether a redesigned login page reduces login failures.",
            "control": "Current login page",
            "treatment": "Redesigned login page",
            "primary_metric": "login_success_rate"
        },
    
        {
            "name": "Onboarding Flow Test",
            "description": "Test whether a shorter onboarding process improves user activation.",
            "control": "Existing onboarding flow",
            "treatment": "Shortened onboarding flow",
            "primary_metric": "activation_rate"
        },
    
        {
            "name": "Product Image Test",
            "description": "Test whether different product images improve purchase decisions.",
            "control": "Current product images",
            "treatment": "Alternative product images",
            "primary_metric": "purchase_rate"
        },
    
        {
            "name": "Notification Timing Test",
            "description": "Test whether optimized notification timing affects user engagement.",
            "control": "Current notification schedule",
            "treatment": "Optimized notification timing",
            "primary_metric": "user_engagement"
        }
    ]

    index = r.randint(0, 9)
    
    return experiments[index]["name"], experiments[index]["description"], experiments[index]["control"], experiments[index]["treatment"], experiments[index]["primary_metric"]  

def main():
    experiment_name, description, control, treatment, primary_metric = random_experiment_generation()

    exp = Experiment("EX001", experiment_name, description, control, treatment, primary_metric, "draft")

    exp.run_exp()

    return exp

main()