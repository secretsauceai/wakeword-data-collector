from functions import collect_random_recording

def collect_random_cli(slug, recording_type, recording_number):
    if recording_type == 'conversation': 
        print("For best results: use this to record a 15 minute nature conversation with you as the primary speaking")
    else:
        print("For best results: record your TV for 15 minutes")
    collect_random_recording(slug, recording_type, recording_number)