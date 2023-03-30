from transformers import AutoTokenizer, AutoModel

# tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
# model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4-qe", trust_remote_code=True).half().cuda()

tokenizer = AutoTokenizer.from_pretrained("./chatGLM_6B_models/chatglm-6b-int4-qe", trust_remote_code=True)
model = AutoModel.from_pretrained("./chatGLM_6B_models/chatglm-6b-int4-qe", trust_remote_code=True).half().cuda()

model = model.eval()

# response, history = model.chat(tokenizer, "你好！", history=[])
# print(f"==> {response}")

prompt = "您好张三女士，我是ABC银行北京营业厅的经理李四，工号是123456，根据监管部门要求，我行将对投资理财类产品销售实施录音录像，您购买的产品是我行代销的EFG公司的某某信托计划，产品的风险等级为R3等级，风险水平为中等风险，您确认吗。确认。......"
response, history = model.chat(tokenizer, prompt, history=[])
print(f"A: {response}")

prompt = "这段话是否包含客户姓名？\
            这段话是否包含销售人员姓名？\
            这段话是否包含销售人员工号？\
            这段话是否包含销售人员所属机构？\
            这段话是否包含销售产品名称？\
            这段话是否包含产品风险提示？\
            这段话是否包含销售禁用词？\
            这段话是否包含保证收益描述？\
            这段话是否包含产品停售描述？\
            这段话是否包含客户否定回复？"
response, history = model.chat(tokenizer, prompt, history)
print(f"A: {response}")

prompt = "请用JSON格式化上述回答"
response, history = model.chat(tokenizer, prompt, history)
print(f"A: {response}")




# A: {
#   "status": "ok",
#   "与客户相关的信息": {
#     "客户姓名": "张三",
#     "销售人员姓名": "李四",
#     "销售人员工号": "123456",
#     "销售人员所属机构": "ABC银行北京营业厅",
#     "销售产品名称": "EFG公司的某某信托计划",
#     "产品风险提示": "产品的风险等级为R3等级，风险水平为中等风险",
#     "销售禁用词": "销售禁止购买此类产品",
#     "保证收益描述": "产品不提供保证收益",
#     "产品停售描述": "该产品已经停售",
#     "客户否定回复": "不确认该信息"
#   }
# }
