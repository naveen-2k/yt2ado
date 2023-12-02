from pytube import YouTube

def download_audio(youtube_url, output_path='downloads'):
    try:
       
        yt = YouTube(youtube_url)

       
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

      
        print(f"Downloading audio from {yt.title}...")
        audio_stream.download(output_path)

        print("Download complete!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
   
    youtube_url = "your_video_id_here"

  
    output_path = "downloads"

    # Call the function to download the audio
    download_audio(youtube_url, output_path)
