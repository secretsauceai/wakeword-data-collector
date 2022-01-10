from functions import show_hint, collect_number_of_recordings, collect_background_noise, collect_wakewords

def collect_wakeword_part_one_cli(slug, onboarding, wakeword):
    '''
    if onboarding:
        show_hint()
    '''
    recordings_count = 16 #collect_number_of_recordings()
    if wakeword:
        collect_background_noise(slug, nr=1)

        collect_wakewords(0, recordings_count, wakeword, slug)

        collect_background_noise(slug, nr=2)

def collect_wakeword_part_two_cli(slug, onboarding, wakeword):
    recordings_count = 32 #collect_number_of_recordings()
    if wakeword:
        collect_background_noise(slug, nr=5)

        collect_wakewords(16, recordings_count, wakeword, slug)

        collect_background_noise(slug, nr=6)

def collect_wakeword_part_three_cli(slug, onboarding, wakeword):
    recordings_count = 44 #collect_number_of_recordings()
    if wakeword:
        collect_background_noise(slug, nr=9)

        collect_wakewords(32, recordings_count, wakeword, slug)

        collect_background_noise(slug, nr=10)
    
