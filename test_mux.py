from app.services.media_muxer import MediaMuxer

mux = MediaMuxer()

print("FFmpeg encontrado:", mux.exists())
print(mux.ffmpeg)