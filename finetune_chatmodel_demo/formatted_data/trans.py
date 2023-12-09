import json
with open("/home/ubuntu/ChatGLM3/finetune_chatmodel_demo/formatted_data/Train_JSON.json") as f:
    with open("/home/ubuntu/ChatGLM3/finetune_chatmodel_demo/formatted_data/Train_JSON.jsonl","w") as w:
        data=json.load(f)
        for i in data:
            w.write(json.dumps(i,ensure_ascii=False) + "\n")
