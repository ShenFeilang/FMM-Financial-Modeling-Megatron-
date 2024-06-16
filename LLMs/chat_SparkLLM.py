from langchain_community.chat_models import ChatSparkLLM
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())


def gen_spark_params(model):  # 这里的model指的是
    spark_url_tpl = "wss://spark-api.xf-yun.com/{}/chat"
    model_params_dict = {
        "v1.5": {
            "domain": "general",  # 用于配置大模型版本
            "spark_url": spark_url_tpl.format("v1.1")  # 云端环境的服务地址
        },
        "v2.0": {
            "domain": "generalv2",  # 用于配置大模型版本
            "spark_url": spark_url_tpl.format("v2.1")  # 云端环境的服务地址
        },
        "v3.0": {
            "domain": "generalv3",  # 用于配置大模型版本
            "spark_url": spark_url_tpl.format("v3.1")  # 云端环境的服务地址
        },
        "v3.5": {
            "domain": "generalv3.5",  # 用于配置大模型版本
            "spark_url": spark_url_tpl.format("v3.5")  # 云端环境的服务地址
        }
    }
    return model_params_dict[model]


def get_llm(model, temperature):
    spark_api_url = gen_spark_params(model=model)['spark_url']
    return ChatSparkLLM(spark_api_url=spark_api_url, temperature=temperature, streaming=True)
