from experiment import main as experiment
import hashlib

# dummy data for experiment purposes
users = [
    "U001", "U002", "U003", "U004", "U005",
    "U006", "U007", "U008", "U009", "U010",
    "U011", "U012", "U013", "U014", "U015",
    "U016", "U017", "U018", "U019", "U020",
    "U021", "U022", "U023", "U024", "U025",
    "U026", "U027", "U028", "U029", "U030",
    "U031", "U032", "U033", "U034", "U035",
    "U036", "U037", "U038", "U039", "U040",
    "U041", "U042", "U043", "U044", "U045",
    "U046", "U047", "U048", "U049", "U050",
    "U051", "U052", "U053", "U054", "U055",
    "U056", "U057", "U058", "U059", "U060",
    "U061", "U062", "U063", "U064", "U065",
    "U066", "U067", "U068", "U069", "U070",
    "U071", "U072", "U073", "U074", "U075",
    "U076", "U077", "U078", "U079", "U080",
    "U081", "U082", "U083", "U084", "U085",
    "U086", "U087", "U088", "U089", "U090",
    "U091", "U092", "U093", "U094", "U095",
    "U096", "U097", "U098", "U099", "U100"
]

database = []

class Assignment:
    
    def assign(self, user_id, exp):
        if(check_eligibility(user_id, exp.experiment_id) and not check_existing_assinments(user_id, exp.experiment_id)):

            new_val = {}

            new_val["user_id"] = user_id
            new_val["exp_id"] = exp.experiment_id
            
            key = f"{user_id}:{exp.experiment_id}"
            hash_value = hashlib.sha256(key.encode()).hexdigest()
           
            number = int(hash_value, 16)
           
            corrected_num = number%100

            
            if(corrected_num >= 50):
                new_val["variant"] = exp.control
                database.append(new_val)
                return exp.control
            else:
                new_val["variant"] = exp.treatment
                database.append(new_val)
                return exp.treatment


        # If the user already connected before then give its peviously assigned value back
        elif(check_existing_assinments(user_id, exp.experiment_id)):
            for data in database:
                if data["user_id"] == user_id:
                    return data["variant"]
        
def get_bucket(user_id, exp_id):
    key = f"{user_id}:{exp_id}"

    hash_value = hashlib.sha256(key.encode()).hexdigest()

    bucket_no = (int(hash_value, 16))%100
    return bucket_no

# For future eligibility checking
def check_eligibility(user_id, exp_id):
    return True

def check_existing_assinments(user_id, exp_id):
    for dic in database:
        if (dic["user_id"] == user_id and dic["exp_id"] == exp_id):
            return True
    return False

def main():

    exp = experiment()
    assignment = Assignment()
    for user in users:
        assignment.assign(user, exp)

    print(database)
    
main()