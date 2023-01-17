from wakeword_collector.functions import collect_number_of_recordings, collect_background_noise, collect_wakewords, collect_non_wakeword

non_wake_recording_number = None

def collect_non_wakeword_cli(slug):
    collect_non_wakeword(0, slug)
    collect_background_noise(slug, nr=3)
    collect_non_wakeword(1, slug)
    collect_background_noise(slug, nr=4)