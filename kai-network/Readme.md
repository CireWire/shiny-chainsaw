# Kai Network

Kai Network is a video player application built with Python and Pyglet. It allows you to play videos from a playlist and control playback using keyboard shortcuts.

## Features

- Play videos from a playlist
- Pause and resume playback
- Seek forward and backward in the video
- Adjust volume
- Save and resume playback position
- Play the next and previous videos in the playlist

## Requirements

- Python 3.10
- Pyglet
- Requests
- OpenCV

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/kai-network.git
   ```

2. Navigate to the project directory:

   ```shell
   cd kai-network
   ```

3. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

### Running Locally

1. Update the playlist in the `kai_network.py` file with your desired video URLs.

2. Run the application:

   ```shell
   python kai_network.py
   ```

3. Use the following keyboard shortcuts to control playback:

   - Space: Play/Pause
   - Left Arrow: Seek backward
   - Right Arrow: Seek forward
   - Up Arrow: Increase volume
   - Down Arrow: Decrease volume
   - H: Save playback time
   - R: Resume playback from saved position
   - N: Play next video
   - P: Play previous video

### Running with Docker

1. Build the Docker image:

   ```shell
   docker build -t kai-network .
   ```

2. Run the Docker container:

   ```shell
   docker run -it --rm kai-network
   ```

   **Note:** Running the application in Docker requires an X server to display the video. Make sure you have an X server running or use an X server utility like XQuartz on macOS.

3. Use the same keyboard shortcuts mentioned above to control playback.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).