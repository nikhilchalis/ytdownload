import os
import yt_dlp
import time

def download_video(video_url, save_path="./"):
    # yt-dlp options
    ydl_opts = {
        "format": "bv+ba/best",  # Best video + best audio, fallback to best single file
        "merge_output_format": "mp4",  # Ensure video and audio are merged into mp4
        "outtmpl": f"{save_path}/%(title)s.%(ext)s",  # Save path and file naming
        "progress_hooks": [handle_progress],  # Hook to handle file final path
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def handle_progress(d):
    if d['status'] == 'finished':
        # When the download is finished, update the file's timestamp
        final_file = d['filename']  # The merged final file
        current_time = time.time()  # Get the current time in seconds
        os.utime(final_file, (current_time, current_time))  # Update access and modification time
        print(f"File saved as {final_file}. Modification date updated.")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ").strip()
    save_path = input("Enter the directory to save the video (leave empty for default current folder): ").strip()

    if not save_path:
        save_path = "./"

    download_video(video_url, save_path)
