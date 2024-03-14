# Redact PII with Python

Automatically redact PII from audio and video files in minutes with Python.

Companion repo for the blog Automatically redact PII from audio and video with Python.

## To use
1. Install the [AssemblyAI Python SDK](https://github.com/AssemblyAI/assemblyai-python-sdk)
2. Set your AssemblyAI API key as an environment variable (you can get a key [here](https://www.assemblyai.com/dashboard/signup))
```shell
# Mac/Linux:
export ASSEMBLYAI_API_KEY=<YOUR_KEY>

# Windows:
set ASSEMBLYAI_API_KEY=<YOUR_KEY>
```
3. Run `python main.py` to print a redacted transcript and URL for redacted version of a hard-coded audio file
4. (Optional) Install `termcolor` with `pip install termcolor`, and then run `python compare.py` to print out a comparison of the unredacted and redacted transripts.