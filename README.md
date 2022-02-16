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

After collecting your data, it is highly recommended to run the [Precise Wakeword Model Maker](https://github.com/secretsauceai/precise-wakeword-model-maker).

## General
The Wakeword Data Collector records wave files with a sample rate of `16000` for two main categories of data:
* Wakewords (ie 'hey Jarvis') `audio/wake-word/`
  * Wakeword variations (ie saying 'hey jarvis' further/closer to the mic, faster, or slower) `audio/wake-word/variations`
* Not-wakewords `audio/not-wake-word/`
   * background noise recordings `audio/not-wake-word/background/`
   * syllables (ie 'hey, jar, vis') `audio/not-wake-word/syllables/`
   * combinations of syllable pairs (ie 'hey jar', 'jarvis') `audio/not-wake-word/parts`
   * other longer recordings: recording the TV and a natural conversation `audio/not-wake-word/`
