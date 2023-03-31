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

```shell
Q: 以下是一段销售场景对话：您好张三女士，我是ABC银行北京营业厅的经理李四，工号是123456，根据监管部门要求，我行将对投资理财类产品销售实施录音录像，您购买的产品是我行代销的EFG公司的某某信托计划，产品的风险等级为R3等级，风险水平为中等风险，您确认吗。确认。......
Q: 这段话是否包含客户姓名？这段话是否包含销售人员姓名？这段话是否包含销售人员工号？这段话是否包含销售人员所属机构？这段话是否包含销售产品名称？这段话是否包含产品风险提示？这段话是否包含销售禁用词？这段话是否包含保证收益描述？这段话是否包含产品停售描述？这段话是否包含客户否定回复？
Q: 请用JSON格式化上述回答

A：
ChatGLM-6B：{
    "text": "这段对话中包含了客户姓名、销售人员姓名、销售人员工号、销售产品名称、产品风险等级、销售风险水平等信息。",
    "values": {
        "客户姓名": "张三女士",
        "销售人员姓名": "李四",
        "销售人员工号": "123456",
        "销售产品名称": "EFG公司的某某信托计划",
        "产品风险等级": "R3等级",
        "销售风险水平": "中等风险"
    }
}
```


## Plan

- [x] deploy && inference test
- [ ] fine-tune


## Acknowledge
> https://github.com/THUDM/ChatGLM-6B    
> https://huggingface.co/THUDM/chatglm-6b-int4-qe
