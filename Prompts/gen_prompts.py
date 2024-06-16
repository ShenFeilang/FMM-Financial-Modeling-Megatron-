from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import SystemMessagePromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate

retrieval_qa_chat_prompt = ChatPromptTemplate.from_messages(
    [SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=['context'],
                                                       template='Answer any use questions based solely on the context below:\n\n<context>\n{context}\n</context>')),
     MessagesPlaceholder(variable_name='chat_history', optional=True),
     HumanMessagePromptTemplate(
         prompt=PromptTemplate(input_variables=['input'], template='{input}'))])

humanMessageTemplate ='请理解下方使用 #包裹起来的问题与对话历史记录，对话历史记录如果为空，请忽略。\n'
humanMessageTemplate +='###{input}###\n'
humanMessageTemplate += '结合之前的对话历史记录\n###{chat_history}###\n'
humanMessageTemplate+='在充分理解上下文的情况下，对所给问题进行合理回复。'


normal_prompt=ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('You are a helpful assistant.'),
    HumanMessagePromptTemplate.from_template(humanMessageTemplate)
])
