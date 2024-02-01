from pytube import YouTube

def download_youtube_video(video_url, save_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream (you can modify this based on your preferences)
        video_stream = yt.streams.get_highest_resolution()

        # Download the video to the specified path
        video_stream.download(save_path)

        print(f"Video downloaded successfully to {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_url = ''
download_youtube_video(video_url, save_path='fill path')

