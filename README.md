# Redact PII with Python

Automatically redact PII from audio and video files in minutes with Python.

Companion repo for the blog [Automatically redact PII from audio and video with Python](https://www.assemblyai.com/blog/automatically-redact-pii-audio-video-python/).

Example output (set to redact names and phone numbers):
> Good afternoon, MGK design. Hi. I'm looking to have plans drawn up for an addition in my house. Okay, let me have one of our architects return your call. May I have your name, please? My name is ####. ####. And your last name? My last name is #####. Would you spell that for me, please? # # # # # #. Okay, and your telephone number? Area code? ###-###-#### that's ###-###-#### yes, ma'am. Is there a good time to reach you? That's my cell, so he could catch me anytime on that. Okay, great. I'll have him return your call as soon as possible. Great. Thank you very much. You're welcome. Bye.

## To use
1. Install the [AssemblyAI Python SDK](https://github.com/AssemblyAI/assemblyai-python-sdk) `pip install assemblyai`
2. Set your AssemblyAI API key as an environment variable (you can get a key [here](https://www.assemblyai.com/dashboard/signup))
```shell
# Mac/Linux:
export ASSEMBLYAI_API_KEY=<YOUR_KEY>

# Windows:
set ASSEMBLYAI_API_KEY=<YOUR_KEY>
```
3. Run `python main.py` to print a redacted transcript and URL for redacted version of a hard-coded audio file
4. (Optional) Install `termcolor` with `pip install termcolor`, and then run `python compare.py` to print out a comparison of the unredacted and redacted transripts.
