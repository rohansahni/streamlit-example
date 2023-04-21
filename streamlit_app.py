
import streamlit as st
import av
import aiortc
from aiortc.contrib.media import MediaPlayer

def main():
    st.title("WebRTC Demo")

    # Create a WebRTC peer connection
    pc = aiortc.RTCPeerConnection()

    # Add a video track
    video = st.video()
    video_track = pc.addTrack(aiortc.VideoStreamTrack())
    @video.on_close
    def on_close():
        pc.removeTrack(video_track)

    # Add an audio track
    audio_track = pc.addTrack(aiortc.AudioStreamTrack())
    player = MediaPlayer(audio_track)
    player.play()

if __name__ == "__main__":
    main()
