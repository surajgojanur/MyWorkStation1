
Title:
Audio Muting Tool using FFmpeg

Description:
This Python script harnesses FFmpeg's capabilities to mute audio within video files swiftly. With a straightforward user interface built on tkinter, it prompts the user to select an input folder containing video files of various formats such as MP4, AVI, MKV, MOV, and WMV. Following the input selection, the user is prompted to designate an output folder where the muted video files will be stored.

The script then employs FFmpeg commands to mute the audio tracks of the selected video files while preserving the video content. Utilizing the -an option, it disables the audio stream and utilizes -c:v copy to maintain the original video codec. This process is executed seamlessly, providing users with muted versions of their video files efficiently without altering the visual content.






