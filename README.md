# ChatGLM-6B-int4-qe

## 1. Install

### I. Install requirements.
```shell
conda create -n torch2.0 python=3.9
conda activate torch2.0
pip install transformers==4.26.1 icetk==0.0.5 cpm-kernels==1.0.11 protobuf==3.19.5 gradio==3.22.1 streamlit==1.20.0 streamlit-chat==0.0.2.2
```

### II. Download weights.
```shell
mkdir chatGLM_6B
cd chatGLM_6B

# Huggingface (3G)
sudo apt-get install git-lfs
git init
git lfs install
git clone https://huggingface.co/THUDM/chatglm-6b-int4-qe

# Baidunetdisk (3G)
链接: https://pan.baidu.com/s/1D_-ZHWcyCrkwXus5FmuK1g?pwd=m2si
提取码: m2si 

conda activate stablediffusion
pip install torch==1.12.1+cu113 --extra-index-url https://download.pytorch.org/whl/cu113
pip install transformers==4.19.2 diffusers==0.12.1 invisible-watermark

# -------- tree -h -----------
chatglm-6b-int4-qe/
├── [ 797]  config.json
├── [4.0K]  configuration_chatglm.py
├── [2.6M]  ice_text.model
├── [ 11K]  LICENSE.txt
├── [ 51K]  modeling_chatglm.py
├── [2.3K]  MODEL_LICENSE.txt
├── [2.9G]  pytorch_model.bin
├── [1.1K]  quantization_kernels.c
├── [1.6K]  quantization_kernels_parallel.c
├── [ 28K]  quantization.py
├── [4.6K]  README.md
├── [ 12K]  tokenization_chatglm.py
└── [ 416]  tokenizer_config.json
# ---------------------------
```

## 2. Test: 
### I. txt2img

```shell
python demo.py
python cli_demo.py
python web_demo.py
python web_demo2.py
```


## Plan

- [x] deploy && inference test
- [ ] fine-tune


## Acknowledge
> https://github.com/THUDM/ChatGLM-6B    
> https://huggingface.co/THUDM/chatglm-6b-int4-qe
