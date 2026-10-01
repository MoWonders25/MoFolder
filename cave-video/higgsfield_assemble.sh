#!/bin/bash
set -e
cd /home/user; mkdir -p w; cd w
B=https://d8j0ntlcm91z4.cloudfront.net/user_3K4hocMIWll0AjZb7crtHRLfdYD/hf_20261001_
V=(053504_1d6a7ba4-9169-4d5f-a649-9f05202892b5 053226_15acdf41-c4de-424e-aea9-9e925881459f 053226_796a74b0-cf2d-4f3f-af6f-1c800ef569c9 053226_c00ba4e3-f2ef-431e-9205-bfabf55ae205 053226_c5bde01b-e42b-42df-8fa7-c74cf3fcdcf6 053504_af455abe-8e73-4b90-ac0f-d2d106b942fa 053226_5419b370-9dc1-4a7b-8cad-b235e2d1abe4 053226_491804da-ea81-44e5-972e-e104b992a380 053226_144dd8fe-7ec7-4e81-b6e1-0cded8dffc78 053226_8b1c3262-a031-42e0-a839-8806843103dc 053226_e8239f9b-ef9d-4275-9bfb-214911df8b0d 053226_109bbc18-26cb-4a64-a7aa-ae59f599708a 053320_a083b64f-b264-4111-afe9-7511e5a0b302 053255_2310896e-e946-4a87-b4cb-aefd03989235 053256_c56a5a1f-67c5-4a80-be59-bb8d38066b4d 053256_1a6e6718-d373-477c-9080-02520357b241 053256_f83b4cdb-2525-4c01-9ead-6e3ed5cfa87e 053256_b56a0c56-8046-452d-a74b-9e7452f29839 053256_4f2603da-1b63-47df-9980-c52c694a2ea5 053256_4bbb034c-14c9-40f3-aba4-79d56019bd0b 053256_29aabb31-9d5c-4a81-b114-6c748092213b 053256_792b1141-9b89-4a9e-bd75-acd056f64d6f 053256_1c821472-7972-4d79-8f57-7fdf297f1ce2 053910_326d3387-36d0-420f-979c-58044392595f 053504_6a54d675-f2a6-42f1-877c-3f929c272d41 053504_e7193410-3ce2-4f7b-9f18-3a2e5d839965 053319_a4f10fdd-bd00-41b3-bf90-e0f4575f6efc 053319_bff8ad83-e6ef-44da-b389-4a431ee0b3f8 053505_9247f9f4-fda7-45ab-be3c-7a7ba24863bf 053504_833f940d-4d8d-4495-9e4d-3098453fa0fd)
A=(053414_066870c8-aed3-4af9-925b-43303b3a0621 053414_d66ab5f6-17b2-42b3-a973-6d468bd0e66c 053414_3f14dd9d-c077-44d1-ab9a-6846c6fc6e9b 053414_08f8c408-aed4-445e-9046-bd71073183d8 053450_f5f355d1-cb60-43a9-8362-dd62970db3f9 053414_a79a8cce-e363-4eb7-b440-aae4de4eabb0 053414_a31d93a6-fde7-4418-b51d-3ae6c1340c84 053450_6516f76e-ffd8-474d-855f-52d4d811b3c7 053414_b182f539-7f04-4b27-8dd5-e9aab7ecf88e 053414_b15c88e2-26e1-457c-ab6a-48d4d783a647)
for i in $(seq 0 29); do f=$(printf c%02d.mp4 $i); [ -s $f ] || curl -fsSL --retry 3 -o $f "$B${V[$i]}.mp4"; done
for i in $(seq 0 9); do [ -s a$i.mp3 ] || curl -fsSL --retry 3 -o a$i.mp3 "$B${A[$i]}.mp3"; done
echo downloaded
FPS=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 c00.mp4)
for i in $(seq 0 29); do f=$(printf c%02d.mp4 $i); ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate:format=duration -of csv=p=0 $f | tr '\n' ' '; echo $f; done
: > vl.txt; for i in $(seq 0 29); do printf "file 'c%02d.mp4'\n" $i >> vl.txt; done
ffmpeg -loglevel error -y -f concat -safe 0 -i vl.txt -an -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=$FPS,setsar=1" -t 300 -c:v libx264 -preset veryfast -crf 19 -pix_fmt yuv420p video.mp4
echo video done
ffmpeg -loglevel error -y -f lavfi -i anullsrc=r=44100:cl=stereo -t 0.25 gap.wav
: > al.txt; for i in $(seq 0 9); do ffmpeg -loglevel error -y -i a$i.mp3 -ar 44100 -ac 2 a$i.wav; echo "file 'a$i.wav'" >> al.txt; [ $i -lt 9 ] && echo "file 'gap.wav'" >> al.txt; done
ffmpeg -loglevel error -y -f concat -safe 0 -i al.txt vo.wav
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 vo.wav); T=$(python3 -c "print(round($D/299.5,4))"); echo "vo=$D tempo=$T"
ffmpeg -loglevel error -y -i vo.wav -af "atempo=$T,apad" -t 300 vo_fit.wav
ffmpeg -loglevel error -y -i video.mp4 -i vo_fit.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -t 300 -movflags +faststart final.mp4
ffprobe -v error -show_entries stream=codec_type,width,height:format=duration,size -of compact final.mp4
[ -s final.mp4 ] && curl -sS -o /dev/null -w "upload_http=%{http_code}\n" -X PUT -H "Content-Type: video/mp4" -H "If-None-Match: *" --upload-file final.mp4 "$(cat up.txt)"
echo ALLDONE
