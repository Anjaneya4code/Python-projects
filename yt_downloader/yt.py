import yt_dlp


def download_video(url):
    options = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "merge_output_format": "mp4"
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            print("\nFetching video information...")
            ydl.download([url])

        print("\nDownload completed successfully!")

    except Exception as e:
        print("\nDownload failed:")
        print(e)


def main():
    print("==============================")
    print("     YOUTUBE DOWNLOADER")
    print("==============================")

    url = input("\nEnter YouTube URL: ").strip()

    if not url:
        print("Please enter a valid URL.")
        return

    download_video(url)


if __name__ == "__main__":
    main()
