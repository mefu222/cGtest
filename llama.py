import os
import logging
import sys
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

os.environ["OPENAI_API_KEY"]="sk-***"

# ログレベルの設定
logging.basicConfig(stream=sys.stdout, level=logging.INFO, force=True)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# インデックスの作成
documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex(documents)

print(index.query("Nyokkeyとは"))
