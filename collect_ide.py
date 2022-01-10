from functions import collect_background_noise, collect_user_data, zipfiles, pyaudio_start, pyaudio_terminate, make_directories
from collect_wakeword_cli import collect_wakeword_part_one_cli, collect_wakeword_part_two_cli, collect_wakeword_part_three_cli
from collect_non_wakeword_cli import collect_non_wakeword_cli
from collect_wakeword_variations_cli import collect_wakeword_variations_cli
from collect_random_cli import collect_random_cli
from collect_all_partial_wakeword_cli import collect_all_partial_wakeword_cli

import os
import time
import contextlib

import shutil

# don't forget to import make_slug_directory from functions when you have it working!

onboarding = True
wakeword = None
name = None
labels = None
cli_choice = None
slug = None
recordings_count = 0
collected_wakewords = 0

make_directories()
pyaudio_start()
wakeword, wakeword_split, name, labels, slug = collect_user_data()
#make_slug_directory(slug)

#with open(os.devnull, 'w') as devnull:
#    with contextlib.redirect_stderr(devnull):
#        pyaudio_start()

# TODO:
# add optional to syllables and paragraph

cli_text = "Please enter your choice\n1. First set of 16 wake word recordings\n2. Wake word syllable and syllable permutation recordings\n3. Non-wake-word recordings (optional)\n4. Second set of 16 wake word recordings\n5. Wake word variations\n6. Third set of 16 wake word recordings\n7. First random conversation recording\n8. Second random conversation recording\n9. First Random TV recording\n10. Second Random TV recording\n11. Zip all collected wave files and exit\n\n"

while True:

    print('To successfully use Wakeword recorder, there are 12 steps required\n')
    cli_choice = str(input(cli_text))

    if cli_choice == '1':
        collect_wakeword_part_one_cli(slug, onboarding, wakeword)
        cli_text = cli_text[:cli_text.find('\n2.')] + ' (done) ' + cli_text[cli_text.find('\n2.'):]
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cli_choice == '2':
        collect_all_partial_wakeword_cli(slug, wakeword_split)
        cli_text = cli_text[:cli_text.find('\n3.')] + ' (done) ' + cli_text[cli_text.find('\n3.'):]
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cli_choice == '3':
        collect_non_wakeword_cli(slug)
        cli_text = cli_text[:cli_text.find('\n4.')] + ' (done) ' + cli_text[cli_text.find('\n4.'):]
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cli_choice == '4':
        collect_wakeword_part_two_cli(slug, onboarding, wakeword)
        cli_text = cli_text[:cli_text.find('\n5.')] + ' (done) ' + cli_text[cli_text.find('\n5.'):]
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cli_choice == '5':
        collect_wakeword_variations_cli(slug, wakeword)
        cli_text = cli_text[:cli_text.find('\n6.')] + ' (done) ' + cli_text[cli_text.find('\n6.'):]
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cli_choice == '6':
        collect_wakeword_part_three_cli(slug, onboarding, wakeword)
        cli_text = cli_text[:cli_text.find('\n7.')] + ' (done) ' + cli_text[cli_text.find('\n7.'):]
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cli_choice == '7':
        collect_random_cli(slug, 'conversation', '01')
        cli_text = cli_text[:cli_text.find('\n8.')] + ' (done) ' + cli_text[cli_text.find('\n8.'):]
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cli_choice == '8':
        collect_random_cli(slug, 'conversation', '02')
        cli_text = cli_text[:cli_text.find('\n9.')] + ' (done) ' + cli_text[cli_text.find('\n9.'):]
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cli_choice == '9':
        collect_random_cli(slug, 'TV', '01')
        cli_text = cli_text[:cli_text.find('\n10.')] + ' (done) ' + cli_text[cli_text.find('\n10.'):]
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cli_choice == '10':
        collect_random_cli(slug, 'TV', '02')
        cli_text = cli_text[:cli_text.find('\n11.')] + ' (done) ' + cli_text[cli_text.find('\n11.'):]
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cli_choice == '11':
        collect_background_noise(slug, nr=13)
        time.sleep(1.0)
        print('Zipping all wave files, please send this zip file to bartmoss.bs@gmail.com or use wake word data prep\nThank you!\n')
        shutil.make_archive(f'{slug}_ww_recordings', 'zip', 'audio/')
        #zipfiles(f'{slug}_ww_recordings.zip')
        time.sleep(2.5)
        pyaudio_terminate()
        exit()
    else:
        print('Invlid number added. Make sure the number is between 1 and 12')
