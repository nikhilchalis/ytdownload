from pytube import YouTube
import os

def download_youtube_video(video_url, save_path="C:/CDocuments/MUDA/"):
    try:
        # Create YouTube object
        yt = YouTube(video_url)
        
        # Get the highest resolution video stream
        stream = yt.streams.get_highest_resolution()
        
        print(f"Downloading: {yt.title}")
        print(f"Resolution: {stream.resolution}")
        print(f"File size: {round(stream.filesize / 1024 / 1024, 2)} MB")

        # Download the video
        stream.download(output_path=save_path)
        
        print("Download completed!")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Get user input
    video_url = input("Enter the YouTube video URL: ").strip()
    save_path = input("Enter the directory to save the video (leave empty for current directory): ").strip()

    if save_path == "":
        save_path = "./"

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Download the video
    download_youtube_video(video_url, save_path)
