from wakeword_collector.functions import collect_all_partial_wake_word_recording, collect_background_noise, collect_background_noise


def collect_all_partial_wakeword_cli(slug, wakeword_split):
    collect_background_noise(slug, nr=11)
    collect_all_partial_wake_word_recording(slug, wakeword_split)
    collect_background_noise(slug, nr=12)