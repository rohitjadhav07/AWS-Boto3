import boto3

polly = boto3.client("polly", region_name="ap-south-1")

voices = polly.describe_voices()

print("\nAvailable Voices:\n")

voice_data = []

for i, voice in enumerate(voices["Voices"]):
    name = voice["Id"]
    lang = voice["LanguageName"]
    engines = voice["SupportedEngines"]

    print(f"{i+1}. {name} ({lang}) - Engines: {engines}")

    voice_data.append({
        "id": name,
        "engine": engines[0]
    })

choice = int(input("\nSelect voice number: ")) - 1
selected_voice = voice_data[choice]["id"]
selected_engine = voice_data[choice]["engine"]

text = input("\nEnter text:\n")

response = polly.synthesize_speech(
    Text=text,
    OutputFormat="mp3",
    VoiceId=selected_voice,
    Engine=selected_engine
)

with open("speech_output.mp3", "wb") as f:
    f.write(response["AudioStream"].read())

print("\n✅ Speech generated successfully")
print(f"Voice used: {selected_voice}")
print(f"Engine used: {selected_engine}")