python reconstruct_redecoder.py \
    --source /workspace/chinese-audio-sample/old\ oti.wav \
    --target /workspace/chinese-audio-sample/ML Lecture 1_ Regression - Demo.mp3 \ 
    --codec-ckpt-path /workspace/unofficial_facodec_ckpt/FAcodec/pytorch_model.bin \
    --redecoder-ckpt-path /workspace/unofficial_facodec_ckpt/FAcodec-redecoder/pytorch_model.bin \
    --codec-config-path /workspace/unofficial_facodec_ckpt/FAcodec/config.yml \
    --redecoder-config-path /workspace/unofficial_facodec_ckpt/FAcodec-redecoder/config.yml 