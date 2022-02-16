![Secret Sauce AI](https://github.com/secretsauceai/secret_sauce_ai/blob/main/SSAI_logo_2.3_compressed_cropped.png?raw=true)
# Wakeword Data Collector
![Wake word](https://github.com/secretsauceai/secret_sauce_ai/blob/main/SSAI_wakeword_scene_compressed.png?raw=true)
## Do you want your own personal wake word?
Prototype CLI to record wakewords, non-wakewords, and background noise written in python. Think of it as your wakeword data collection recipe for creating bullet proof wakeword models. 

![wakeword data collector wakeword collection example](https://github.com/secretsauceai/secret_sauce_ai/blob/main/SSAI_ww_collector_01.1.gif)
## Installation
As usual once you have cloned the repo, it is recommended to create and activate python virtual environment.
```console
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Simply run `collect_ide.py` in your console and follow the instructions.
```
python collect_ide.py
```

## Tips to improve your model
* After collecting your data, it is highly recommended to run the [Precise Wakeword Model Maker](https://github.com/secretsauceai/precise-wakeword-model-maker).
* Use several TTS systems to gather more wake word samples.
For example you could use [kukarella](https://www.kukarella.com/). Is there perhaps a better resource?
* To lower the number of 'false wake ups' after you have trained your model with your collected audio and TTS samples, iteratively train over the following audio data sets:

    * [Mycroft noise data](https://github.com/MycroftAI/Precise-Community-Data/tree/master/not-wake-words/noises)
    * [public domain sounds](http://pdsounds.tuxfamily.org/)
    * [OpenPathMusic44V5](https://archive.org/details/OpenPathMusic44V5)
    * [audiocheck.net sweeps and noises](https://www.audiocheck.net/testtones_index.php) 

     If your model uses voices from several people, you might need to add in voice data sets into your iterative training:
    * [Mozilla Common Voice EN](https://commonvoice.mozilla.org/en/datasets) (only need roughly the first 30k not the entire 56GB). 
    * [precise community data not-wake](https://github.com/MycroftAI/Precise-Community-Data/tree/master/not-wake-words)
