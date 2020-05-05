'''
Helper for the installer - receives doulingo username and password, as well as the time, from the user.
Then it replaces the currect places in the XML and the bat can continue to run.
'''
import duolingo
import win32api
import os 


XML_TEMPLATE_PATH = 'DoDuolingo_task_scheduler_template.xml'
OUTPUT_XML_PATH = 'DoDuolingo_task_scheduler.xml'


def receive_params_from_user():
    username = input("Enter your doulingo username: ") 
    password = input("Enter your doulingo password: ") 
    time = input("Enter time to start nagging: ") 
    return (username, password, time)

def validate_duolingo_authentication(username, password):
    try:
        duolingo.Duolingo(username, password)
    except:
        return False
    return True


if __name__ == '__main__':
    (username, password, time) = receive_params_from_user()
    
    print('Trying to connect to duolingo...')

    while not validate_duolingo_authentication(username, password):
        print('Unable to authenticate duolingo. Try again... (Ctrl+C to quit)')
        (username, password, time) = receive_params_from_user()
    
    print('Success!')

    with open(XML_TEMPLATE_PATH, 'r') as xml_template:
        template_data = xml_template.read()

    template_data = template_data.format(username=username, password=password, time=time,
        curr_user=win32api.GetUserNameEx(win32api.NameSamCompatible),
        working_dir=os.path.dirname(os.path.realpath(__file__)))

    with open(OUTPUT_XML_PATH, 'w') as xml_output:
        xml_output.write(template_data)
    

